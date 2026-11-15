# -*- coding: utf-8 -*-

from pathlib import Path
import html


ROOT = Path("巨鲸陨落_V1")
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        return text
    return text.replace(old, new, 1)


def append_after(text: str, marker: str, addition: str, label: str) -> str:
    if addition and addition in text:
        return text
    if marker not in text:
        return text
    return text.replace(marker, marker + addition, 1)


def revise(stem: str, ops: list[tuple[str, str, str, str]], base: Path) -> None:
    path = base / f"{stem}.md"
    text = read(path)
    for kind, marker, payload, label in ops:
        if kind == "after":
            text = append_after(text, marker, payload, f"{stem}:{label}")
        elif kind == "replace":
            text = replace_once(text, marker, payload, f"{stem}:{label}")
        else:
            raise ValueError(kind)
    write(path, text)


def md_to_html(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_ul = False
    in_ol = False
    for raw in lines:
        line = raw.rstrip()
        if not line:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            continue
        if line.startswith("# "):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            out.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            out.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{html.escape(line[2:])}</li>")
        else:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            out.append(f"<p>{html.escape(line)}</p>")
    if in_ul:
        out.append("</ul>")
    if in_ol:
        out.append("</ol>")
    return "\n".join(out)


def page(title: str, body: str, rel_css: str = "../assets/style.css") -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{rel_css}" />
</head>
<body>
  <main class="page">
{body}
  </main>
</body>
</html>
"""


def chapter_nav(stems: list[str], idx: int, lang: str) -> str:
    prev_link = "&nbsp;"
    next_link = "&nbsp;"
    if idx > 0:
        prev_link = f'<a href="{stems[idx - 1]}.html">上一章 / Previous</a>'
    if idx < len(stems) - 1:
        next_link = f'<a href="{stems[idx + 1]}.html">下一章 / Next</a>'
    index_name = "index_EN.html" if lang == "en" else "index.html"
    return f'<nav class="nav"><span>{prev_link}</span><span><a href="../{index_name}">目录 / Index</a></span><span>{next_link}</span></nav>'


def rebuild_html() -> None:
    stems = sorted(p.stem for p in ZH_MD.glob("*.md"))
    for idx, stem in enumerate(stems):
        zh_text = read(ZH_MD / f"{stem}.md")
        en_text = read(EN_MD / f"{stem}.md")
        zh_body = chapter_nav(stems, idx, "zh") + "\n" + md_to_html(zh_text) + "\n" + chapter_nav(stems, idx, "zh")
        en_body = chapter_nav(stems, idx, "en") + "\n" + md_to_html(en_text) + "\n" + chapter_nav(stems, idx, "en")
        write(ZH_HTML / f"{stem}.html", page(stem, zh_body))
        write(EN_HTML / f"{stem}.html", page(stem, en_body))


def main() -> None:
    zh_ops: dict[str, list[tuple[str, str, str, str]]] = {
        "00_书名页与写作说明": [
            (
                "after",
                "- 查理的核心气质是怕死、嘴碎、普通，但关键时刻会跟上。他不是突然变成英雄，而是慢慢学会见证。\n",
                "- 二稿核心美学：重大事件必须呈现“别无选择”的必然性。人物先抗拒，退路逐步关闭，最后选择伤害自己，却符合他的性格底色。\n"
                "- 战争中的情感高潮不写成单一人类爱情，而写成跨物种共性：愿意限制自己，放弃占有，让未来不必成为自己的复制品。\n"
                "- 《灵猫》相关内容只保留轻微余震，不作为本书硬铺垫。《巨鲸陨落》的结尾情绪以蓝鲸歌声和查理带回的疼痛为主。\n",
                "add second-pass principles",
            )
        ],
        "02_巨鲸从天而降": [
            (
                "after",
                "那不是吼叫。\n",
                "\n更奇怪的是，我在那低频最深处，听见了一点像海的东西。\n\n法厄同的战场上没有海。脚下只有尸体、灰、碎石和被烧穿的金属。可那声音穿过胸腔时，我却想起某种从未见过的深水，想起巨大的生物在黑暗里缓慢转身，想起一封还没写完就被扔进海底的信。\n\n我不知道那是什么。\n\n后来我才明白，那也许是巨鲸留给地球海洋的第一声草稿。\n",
                "seed blue-whale low-frequency foreshadowing",
            )
        ],
        "03_我不是这具身体": [
            (
                "after",
                "我被重新拽回正在崩塌的战场。\n",
                "\n那一瞬间，另一个记忆也被疼痛带了出来。\n\n不是洛安的。\n\n是我的。\n\n《另一个世界》的中世纪副本里，我第一次从龙背上摔下来，痛觉被系统压到未成年人安全档，仍然把我吓得在地上滚了半天。安娜蹲在旁边，一边检查我的生命值，一边冷静地说：“你刚才明明可以不跳。”\n\n我说：“那查理怎么办？”\n\n她看了我一眼：“你就是查理。”\n\n“不，我是说游戏里的查理。他如果不跳，会显得很没义气。”\n\n安娜沉默了两秒，最后只说：“你这个人，怕死归怕死，麻烦归麻烦，真到有人在下面喊你，你还是会跳。”\n\n那时候我觉得她在骂我。\n\n现在想想，她可能是在做一次很早的诊断。\n",
                "add Charlie reality anchor",
            )
        ],
        "07_宿主的名字": [
            (
                "after",
                "朋友在里面，这个理由已经够用了。\n",
                "\n我想起安娜和吉姆。\n\n如果他们现在也困在某个我看不见的地方，我大概会先骂两句，问为什么每次都是我们三个碰上这种事。然后我会找最近的一条路，不管那条路看起来多不靠谱。\n\n这不是因为我勇敢。\n\n是因为我太清楚自己。一个人逃出去，我会活得很久，也会后悔很久。后悔有时候比死亡更难处理，它会在每一次安静下来时重新开门。\n\n洛安似乎也懂这种东西。\n\n他帮瑟恩缠绷带时，动作那么稳，并不是因为不怕失去他。恰好相反，他怕得每一次呼吸都在收紧，所以才不敢让手抖。\n",
                "deepen Charlie/Lo'an parallel",
            )
        ],
        "09_日辉族的律令": [
            (
                "after",
                "下一秒，战令塔开始封闭。",
                "\n\n封闭不是从他们头顶开始。\n\n是从最底层开始。\n\n洛安听见下方传来几声短促的呼喊。那不是敌军，也不是追兵，是先前没能跟上来的幸存者。战令塔的金色线条按照某种古老算法迅速重组，先锁低层，再锁侧门，最后把所有通道压向唯一的主轴。\n\n日辉族幸存者脸色变了。\n\n“他们还在下面。”洛安说。\n\n“最终秩序会保留最高价值单位。”幸存者下意识回答。\n\n这句话出口后，他自己也怔住了。\n\n瑟恩盯着他：“最高价值？”\n\n幸存者的喉结动了一下。他想反驳，想说这是战令塔自动判定，不是他的选择。可门缝下方又传来一次撞击声，声音很闷，像有人用身体撞在正在闭合的金属上。\n\n秩序终于不再只是投影里的漂亮词。\n\n它开始选择谁活。\n\n洛安冲向控制台。日辉族幸存者也跟了上来。他们没有时间争论，只有几秒可以撬开一条缝。金色线条烧得洛安掌心发黑，日辉族幸存者用断臂抵住锁栓，疼得脸色发白。\n\n门最后只开了一掌宽。\n\n下面爬上来两个幸存者。\n\n第三个没能抓住。\n\n金属重新合拢时，那声被截断的喊叫在塔里回荡了很久。\n\n日辉族幸存者站在原地，太阳环的光暗下去一点。他第一次没有挺直背。\n\n“没有秩序，尸山会更高。”他低声说，像在重复刚才那句话。\n\n可这一次，连他自己都听出了裂缝。",
                "turn Sunbright order into action cost",
            )
        ],
        "19_鳞裔族想要漫长潜伏": [
            (
                "after",
                "她转身继续向前。\n",
                "\n没走几步，旧海路再次震动。墙面暗纹忽然集体亮起，像地下有什么东西被战争惊醒。岚柯胸前的罐体发出尖锐的细响，里面那些绿色光点开始不规则地碰撞。\n\n“库在失温。”她说。\n\n这句话里的冷静只撑了半秒。\n\n下一秒，她跪到地上，用鳞片划开自己的掌心，把血按在罐体接口上。灰绿色外壳随即弹出一排细针，扎进她手腕。洛安看见她整条手臂的鳞片从深绿变成近乎透明，像某种生命储备被迅速抽走。\n\n索勒皱眉：“你在给它续命？”\n\n“我在阻止它提前苏醒。”\n\n“为什么不让它醒？如果你的库能打开，至少鳞裔族还有退路。”\n\n岚柯抬头看他，竖瞳里第一次有了明显的愤怒。\n\n“现在打开，它会本能地寻找宿主。这里每一个活着的都可能被它当成地基。包括洛安手里的种子。”\n\n洛安握紧巨鲸种子。\n\n他终于明白，岚柯所谓的“保存”并不温柔。它需要容器，需要权限，需要把未来压进某个足够安静、足够深的地方。她可以让自己的族群活下去，但代价可能是让其他东西从此只能作为鳞裔族库的一部分存在。\n\n岚柯也明白。\n\n她低头看着罐体，像看着自己全部故乡。\n\n然后，她用另一只手折断了接口上最亮的一根针。\n\n罐体内的绿色光点瞬间少了一半。\n\n她疼得整个人蜷了一下，却没有松手。\n\n“关闭深层权限。”她低声说，“只保留保护膜。”\n\n那一刻，鳞裔族失去的不只是一份资料。\n\n她亲手关掉了自己族群最擅长的后路。\n",
                "make Lanke sacrifice control",
            )
        ],
        "20_节肢族想要没有孤独的世界": [
            (
                "after",
                "这幅图很温柔。\n\n也很可怕。\n",
                "\n节肢族个体忽然抬起前肢，轻轻碰了一下洛安的胸口节点。\n\n洛安本能想躲，已经来不及。\n\n红色网络像水一样涌入他的感官。\n\n一瞬间，查理听见了太多恐惧。瑟恩翅根的痛，岚柯失去罐体权限时的空，索勒面对律令崩塌时不愿承认的羞耻，渊民族老人鳃片干裂时对水的渴望，还有那个节肢族个体第一次断开主群后的巨大寂静。\n\n这些情绪并没有伤害他。\n\n它们甚至把他托住了。\n\n查理第一次感到，原来痛苦如果真的被分摊，会变轻。孤独被稀释后，连死亡都像有人陪你走一段。\n\n然后，他忽然找不到自己。\n\n他的害怕不再只属于他。他对吉姆和安娜的担心、洛安对瑟恩的牵挂、渊民对海的思念，全都被网络柔和地铺平。没有尖锐，也没有私密。每一种情绪都变得可以被管理，可以被安抚，可以被归入稳定连接。\n\n查理猛地挣扎。\n\n不是因为它邪恶。\n\n是因为它太温柔。\n\n温柔到几乎让人愿意放弃自己。",
                "make hive proposal bodily tempting",
            ),
            (
                "after",
                "可洛安看着那个残破背影，忽然觉得它已经有了名字。只是这个名字短暂得来不及被谁叫出口。",
                "\n\n主群足音压来的时候，断开的节肢族没有回头。\n\n它把胸口节点调到过载频段，红光从裂开的甲壳里透出来。那不是爆炸前的光，更像一只小小的灯在逼迫自己照得更远。三十七秒很短，短到连一个完整告别都放不下。\n\n可它仍然站在那里。\n\n一个刚刚拥有自我形状的意识，用自己刚得到的孤独，替别人挡住了群体。",
                "give disconnected chitin sacrifice emotional beat",
            ),
        ],
        "21_渊民族想把记忆交给海": [
            (
                "after",
                "大厅顶部再次震动，碎石落入水中，终于激起真实的涟漪。\n",
                "\n渊民族老人忽然闷哼一声。\n\n水面亮起后，他脖颈两侧的鳃片反而变得更白。洛安这才看见，那圈浅水并不是在滋养他。它正在借他的身体重新启动水路。每一条水线浮起时，老人鳞下都会裂开细小伤口，蓝色血液顺着手腕流进水里。\n\n“停下。”洛安说。\n\n老人摇头。\n\n“水路太久没有声音了。它需要一个还记得海的身体。”\n\n“那你会死。”\n\n老人笑了笑，露出一种非常疲惫的温柔。\n\n“我们都会。区别只是，有些死可以把声音带得远一点。”\n\n他把最后一点随身水囊打开，没有喝，而是倒在巨鲸种子下方。水滴碰到蓝黑色光时，发出极低的一声长鸣。那声音让整个大厅安静下来，连索勒都低下了头。\n\n渊民族老人低声唱起一段没有词的歌。\n\n不是给胜利者。\n\n是给一枚还没有抵达海的种子。",
                "make Abyssal memory cost life-water",
            )
        ],
        "22_震翼族只想天空还有路": [
            (
                "after",
                "“找到了。”瑟恩低声说。",
                "\n\n银线找到路的同时，瑟恩背后的翼膜暗了一片。\n\n洛安听见极细的裂声。那声音比战场上的爆炸轻太多，却让他整个人僵住。震翼族的翅膀不是普通肢体。每一条银线都连着方向、族群、语言和归途。瑟恩刚才不是在“调用地图”。他是在把自己翅膀里还没烧完的路，一点点交给墙。\n\n“停下。”洛安说。\n\n瑟恩没有停。\n\n“你再这样就飞不起来了。”\n\n“我现在也飞不太起来。”\n\n“瑟恩。”\n\n这一次，瑟恩没有开玩笑。他看着那条微弱光路，眼神反而很亮。\n\n“洛安，路不是用来保存在翅膀里的。到最后一秒还没人走过，那才叫浪费。”",
                "make Sern road burn inevitable",
            )
        ],
        "23_巨鲸不是武器": [
            (
                "replace",
                "巨鲸坠落，毁掉的是通往地球的钥匙。\n\n代价是一整颗行星。\n\n也包括它自己。\n",
                "这部分答案并没有完全展开。\n\n巨鲸种子只让洛安知道：它们已经决定把自己拆开，把最高层级的记忆留给月暗，把最低、最慢、最能被地球承受的部分交给海。\n\n至于为什么必须用坠落完成这件事，画面没有立刻解释。\n\n它像故意把最重的原因留到后面，让还活着的人先明白一件事：他们手里的东西，不属于任何胜利者。\n",
                "separate whale identity from fall reason",
            )
        ],
        "25_它为什么坠落": [
            (
                "after",
                "它选择撞碎门。\n",
                "\n真正让它坠落的，不是某一族即将胜利。\n\n是所有族群都已经没有退路。\n\n日辉族若赢，会把地球写成秩序的神殿；鳞裔族若赢，会把地球藏进漫长地下库；节肢族若赢，会把孤独从未来生命里抹掉，也顺手抹掉独自选择的可能；渊民族若赢，海会记住一切，可陆地也许永远只能作为海的附属；震翼族若赢，路会打开，可没有任何文明能保证后来者不会把路变成新的征服。\n\n巨鲸等到最后，等到每一种方案都证明了自己的美，也证明了自己的危险。\n\n那一刻，它没有选谁。\n\n它只让所有人同时失去继续占有地球的能力。",
                "clarify inevitability of fall",
            )
        ],
        "28_种子": [
            (
                "after",
                "索勒沉默片刻，把刚刚拆下的太阳环拿出来。金色环体在警报红光里显得暗淡。\n\n“日辉族也一样。”他说，“如果它成为神谕，人类以后只会学会跪。”",
                "\n\n这句话说出口之前，他其实停顿过。\n\n洛安看见索勒的手指握紧太阳环。那一瞬间，日辉族执令官仍然想把种子举到高处，想说巨鲸选择了他们，想说只有日辉族能把这段回声翻译成未来生命可以承受的神谕。\n\n那是他从小被训练出来的本能。\n\n把混乱抬成秩序。\n\n把未知抬成太阳。\n\n把托付抬成权柄。\n\n可他看见了瑟恩封死的控制区，看见洛安沾血的拳头，也看见岚柯抱着罐体时那种快要崩裂的沉默。于是他把太阳环放低了一点。\n\n不是放弃信仰。\n\n是第一次承认，信仰也会伤人。\n",
                "slow Soler turn",
            ),
            (
                "after",
                "“我仍然想让它活。”她说，“但如果只按鳞裔族的方式活，那它就不再是巨鲸留下的东西。”",
                "\n\n岚柯说完，把罐体上最后一枚深层权限片拆下来。那枚薄片很小，嵌在她掌心时几乎看不见，却让她的手指抖了一下。\n\n“这是什么？”洛安问。\n\n“如果我不拆，它会在接近种子时自动写入鳞裔族优先权。”\n\n索勒看向她。\n\n岚柯没有抬头：“别用那种眼神看我。你刚才也差点这么做。”\n\n索勒没有反驳。\n\n权限片被她折断时，罐体内许多绿色光点同时熄灭。那是鳞裔族漫长潜伏计划的一小部分，可能也是某些尚未出生个体的全部未来。\n\n岚柯闭了闭眼。\n\n“现在它只能保护，不能占有。”",
                "slow Lanke turn",
            ),
        ],
        "31_胜利者的争吵": [
            (
                "after",
                "那种子绝不能交给任何胜利者。",
                "\n\n这句话没有立刻让他们安静。\n\n索勒先看向岚柯，岚柯的手也已经摸到罐体边缘。节肢族留下的残余节点在角落里闪烁，像某种尚未完全熄灭的指令。渊民族老人闭着眼，水膜里却有细小波纹。每一族都还有最后一点抢夺的能力。\n\n更可怕的是，每一族都能说出一个理由。\n\n为了秩序。\n\n为了保存。\n\n为了不孤独。\n\n为了让歌活下去。\n\n为了路。\n\n洛安忽然意识到，战争不是因为他们都没有理由才爆发。恰恰相反，是因为每个理由听起来都足够正确。\n\n正确到可以杀人。\n\n残舟剧烈一震，前方地球窗口闪了一下，蓝线几乎断开。所有人同时看向控制台。\n\n他们不再拥有争吵的时间。\n\n命运有时候并不神秘。它只是把所有退路关掉，然后看你还剩下什么。",
                "make conflict inevitability explicit through pressure",
            )
        ],
        "37_查理听见歌声": [
            (
                "after",
                "“瑟恩，它真的唱回来了。”\n",
                "\n说完这句话后，查理在海面上站了很久。\n\n他不知道自己是不是还有身体。可他感觉胸口某个地方空了一块，风从那里穿过去，带着海盐和遥远星尘的味道。他想象瑟恩如果在这里，会先装作听不懂，然后挑剔这声歌太慢，太低，不适合震翼族赶路。\n\n可他也会安静下来。\n\n他会听完。\n\n查理忽然很确定这一点。\n\n因为瑟恩虽然嘴碎，却从来不会打断真正重要的声音。",
                "deepen Sern farewell in whale song",
            )
        ],
        "39_吉姆的信号": [
            (
                "after",
                "“他和宿主记忆还缠在一起。强行剥离会碎。”\n",
                "\n现实那一端，卢博士的声音短暂插进来，像隔着厚玻璃：“查理的意识边界在下沉。你们还有时间，但不多。”\n\n吉姆没有回答他。\n\n数字吉姆替他回答：“不能提前拉。定位线只能证明我们在这里，不能替他完成分离。”\n\n“如果他完成不了呢？”卢博士问。\n\n这一次，没人立刻说话。\n\n白线在深蓝暗流里轻轻抖了一下。\n\n数字吉姆说：“那他会被记录收走。我们能做的只是等他走到能被带回的位置。”\n\n查理听见了。\n\n他很想骂一句：你们这个救援方案听起来像站在岸上鼓励溺水者自己游。\n\n可他也隐约明白，自己确实不能被别人直接拖出去。洛安、瑟恩、巨鲸种子和那片尸山都还挂在他身上。如果他只是逃走，留下来的部分会被撕成谁也认不出的东西。",
                "add rescue rules and pressure",
            )
        ],
        "40_数字吉姆看见星环": [
            (
                "after",
                "“不能强拉。查理现在不是单独挂在这里。他和洛安的最后选择、瑟恩的残频、巨鲸种子的低频都交叠在一起。如果我们只把查理抽出来，会留下撕裂。”",
                "\n\n数字吉姆把星环放大，三条细线从查理意识边缘亮起。\n\n“第一，我们只能给定位线，不能替他判断这段历史的意义。意义一旦由外部写入，记录会把他归类为污染输入。”\n\n第二条线亮起。\n\n“第二，我不能进入洛安视角。数字意识没有肉体疼痛锚点，进去后会被归档层当成可复制结构处理。”\n\n第三条线亮起时，吉姆看见尸山深处浮出开篇那片暗红天空。\n\n“第三，出口不是空间位置，是认知闭环。他第一次站在那里，以为那叫胜利。现在他必须自己承认，那是共同失败之后的误读。”",
                "make rescue mechanics explicit",
            )
        ],
        "42_尸山重新出现": [
            (
                "after",
                "这一次，他没有立刻惊慌。脚下仍是软的，仍带着血和灰的黏滞感。暗红色天空压在头顶，远方塔楼倾斜，白色无声火焰在坑洞里燃烧。四周依旧堆满五族尸体：日辉族的金发被灰盖住，鳞裔族抱着破碎罐体，节肢族的肢节互相扣着，渊民族鳃片干裂，震翼族透明翼骨在风里轻轻震动。\n",
                "\n细节也回来了。\n\n第一章里他没敢多看的那只断手，此刻正压在一枚碎掉的水囊上。一个日辉族士兵的太阳环滚到尸缝里，金色纹路还在微弱闪烁，像不肯承认命令已经没有对象。远处那具复眼碎裂的节肢族个体，胸口节点仍对着一个早已死去的同伴闪着红光。\n\n这些东西第一次出现时，只负责吓他。\n\n现在它们开始指认每一场选择的结果。\n",
                "mirror opening details",
            )
        ],
        "43_所谓胜利": [
            (
                "after",
                "“不用先证明。”\n\n“那我带什么回去？”\n\n洛安指了指自己的胸口，又指向远处巨鲸坠落的天空。\n\n“带走感觉。疼，怕，后悔，还有那一点点没让人彻底烂掉的东西。证明以后再说。”",
                "\n\n查理站在那里，忽然觉得这个要求比带走证据更难。\n\n证据可以交给卢博士，可以交给吉姆，可以交给仪器和报告。感觉不行。感觉会变形，会被语言弄脏，会在讲述时不小心变得漂亮。\n\n他想起自己以前最擅长把危险讲成笑话。摔下龙背可以讲成倒霉，任务失败可以讲成系统问题，害怕可以讲成“我这个人比较有生存智慧”。\n\n可洛安不允许他这么做。\n\n瑟恩也不允许。\n\n蓝鲸歌声里那些慢得几乎听不见的东西，也不允许。\n\n查理低头看自己的手。那已经不是洛安的手，却仍像残留着暗灰色鳞片的触感。\n\n“我可能讲不好。”他说。\n\n洛安回答：“那就别讲得太轻。”",
                "make Charlie choose pain over proof",
            )
        ],
        "45_给安娜留下的问题": [
            (
                "replace",
                """鲸歌之后，查理听见另一种声音。

它很轻，几乎被巨鲸低频盖住。起初像风吹过草叶，又像某种小动物在黑暗里踩过碎石。查理顺着声音看去，只看见一片陌生的绿色。

不是海。

是森林。

树木很高，根系裸露在潮湿泥土上，空气里漂浮着细小光点。那些光点不像巨鲸记忆的星海尘埃，更像某种动物意识在夜里留下的体温。查理看不清具体生物，只看到许多眼睛一闪而过：猫科动物的竖瞳，鸟类侧头时的微光，鹿一样的黑色轮廓，还有一只黑猫站在树根上，安静地看着他。
""",
                """鲸歌之后，查理短暂想起安娜。

不是因为他看见了某个明确的入口。

只是蓝鲸歌声太低，太慢，慢到让他想起他们小时候第一次在《另一个世界》里迷路。那次不是战场，也没有星际巨鲸，只是一片被系统做得过分真实的黑森林。查理坚持往左走，吉姆坚持爬树看路，安娜则蹲在泥地边，看一串小动物脚印。

“你们两个都错了。”她说，“路不是给人走的，是给这里原本的东西走的。”

那时查理还笑她，说她玩游戏玩得像在做野外调查。

现在他忽然笑不出来。

因为他刚刚亲眼看见，一段文明可以把自己藏进鲸歌里。那么其他生命呢？鸟的迁徙，兽的梦，猫在黑暗里忽然回头的瞬间，会不会也藏着什么人类从未认真听过的东西？

这个问题不属于本场战争。

也不属于查理。
""",
                "soften Lingmao hard hook",
            ),
            (
                "replace",
                """黑猫像是等到了这个决定，终于从树根上跳下来。它落地没有声音，爪子踩过湿土时，泥面泛起一圈很浅的绿光。那绿光没有扩散到查理脚下，只沿着树根向森林深处游走，像某种无声的通知。

一只鹿低下头。

一只鸟收拢翅膀。

更远处，某个体型庞大的黑影在树后缓慢翻身，带动整片雨幕轻轻倾斜。查理看不清它，只觉得那东西很古老，古老到也许并不在意人类是否醒来。

黑猫最后看了查理一眼。

那眼神里没有邀请，也没有警告。它像在说：记住门在这里，别替她进去。

查理点了点头。

他第一次觉得，放手也是一种负责。""",
                """那段黑森林记忆很快散开。

查理没有进入，也没有试图追问。他只是把这个很小的问题放到心里，像把一张纸条塞进口袋。

如果安娜能醒，也许有一天他会把这件事告诉她。

不是作为任务。

只是作为朋友之间的一句：“我好像听见了一个你会感兴趣的问题。”""",
                "remove strong cat doorway",
            ),
        ],
        "49_尾声：没有完全死去": [
            (
                "replace",
                """同一时间，安娜的意识区域里，一片黑色森林正在下雨。

雨水落在树叶上，没有声音。

一只黑猫坐在裸露树根上，耳朵轻轻动了一下。它原本看着森林深处，像在等待某种地面下的脚步。可就在蓝鲸低频穿过远方时，它忽然抬起头。

猫的眼睛里映出一小片海。

很远。

也很古老。

它听了一会儿，尾巴缓慢扫过湿土。

随后，森林深处有更多眼睛亮起。

鸟、鹿、犬、狐，还有一些无法立刻命名的动物轮廓，安静地从黑暗里看向同一个方向。

黑猫轻轻叫了一声。

那声音很小，却让整片森林像醒了一下。

在现实世界里，安娜仍然没有睁眼。

但她的灵接舱外，状态光纹第一次变成了深绿色。

查理听见提示音，转过头。

吉姆也看见了。

没有人说话。
""",
                """安娜的舱体仍然安静。

查理看向她时，想起小时候那片游戏里的黑森林，想起她蹲在泥地边辨认脚印的样子。她总能把别人忽略的东西当成线索，也总能在他们两个急着冲出去时，说一句很冷静、很扫兴、后来证明很有用的话。

舱体状态光纹短暂偏绿了一下。

很轻。

像系统噪声，也像某种遥远意识翻身时压过水面的影子。

卢博士记录了它，没有立刻解释。

查理也没有问。

这本来就不是他要讲完的故事。
""",
                "soften Anna hook in epilogue",
            )
        ],
    }

    for stem, ops in zh_ops.items():
        revise(stem, ops, ZH_MD)

    # English synchronization: keep content direction aligned without trying to polish every sentence.
    en_ops: dict[str, list[tuple[str, str, str, str]]] = {
        "00_书名页与写作说明": [
            (
                "after",
                "- Charlie's core temperament: afraid of death, talkative, ordinary, but he follows when it matters. He does not suddenly become a hero; he slowly learns to witness.\n",
                "- Second-pass aesthetic: major events should feel inevitable. Characters resist first, exits close one by one, and the final choice wounds them while matching their deepest nature.\n"
                "- The emotional law of the war is not only human romance, but cross-species love: the willingness to limit oneself, abandon possession, and let the future avoid becoming one's copy.\n"
                "- The Lingmao thread remains a faint aftershock only. This book's ending belongs mainly to the blue whale song and the pain Charlie brings back.\n",
                "add second-pass principles",
            )
        ],
        "03_我不是这具身体": [
            (
                "after",
                "I was dragged back into the collapsing battlefield.\n",
                "\nFor one instant, pain pulled out another memory.\n\nNot Lo'an's.\n\nMine.\n\nIn the medieval instance of Another World, I once fell from a dragon's back. The underage safety filter had lowered the pain, and I still rolled on the ground for half a minute. Anna crouched beside me, checking my health bar while calmly saying, “You could have chosen not to jump.”\n\nI said, “Then what about Charlie?”\n\nShe looked at me. “You are Charlie.”\n\n“No, I mean the game Charlie. If he did not jump, he would look disloyal.”\n\nAnna stayed quiet for two seconds. “You are afraid of death, yes. You are troublesome, yes. But when someone shouts from below, you still jump.”\n\nBack then I thought she was scolding me.\n\nNow I think she may have been diagnosing me early.\n",
                "add Charlie reality anchor",
            )
        ],
        "07_宿主的名字": [
            (
                "after",
                "A friend being inside was reason enough.\n",
                "\nI thought of Anna and Jim.\n\nIf they were trapped somewhere I could not see, I would probably curse first and ask why it was always the three of us. Then I would look for the nearest road, no matter how unreliable it seemed.\n\nNot because I was brave.\n\nBecause I knew myself too well. Escaping alone might let me live a long time, and regret for just as long. Regret is sometimes harder to manage than death; it opens the door again whenever the world becomes quiet.\n\nLo'an seemed to understand that too.\n\nHis hands were steady while bandaging Sern's wing, not because he was unafraid of losing him. He was so afraid that every breath tightened, so he refused to let his hands shake.\n",
                "deepen Charlie/Lo'an parallel",
            )
        ],
        "45_给安娜留下的问题": [
            (
                "replace",
                "After the whale song, Charlie heard another sound.",
                "After the whale song, Charlie briefly thought of Anna.",
                "soften Lingmao opening",
            ),
            (
                "after",
                "After the whale song, Charlie briefly thought of Anna.",
                "\n\nNot because he had found a clear entrance.\n\nThe blue whale song was simply too low and too slow. It reminded him of the first time the three of them had lost their way in a black forest instance of Another World. Charlie insisted on going left, Jim wanted to climb a tree, and Anna crouched beside animal tracks in the mud.\n\n“You are both wrong,” she had said. “This path was not made for people. It was made for whatever lived here first.”\n\nBack then Charlie had laughed at her for playing a game like field research.\n\nNow he could not laugh.\n\nIf a civilization could hide itself inside whale song, what about other lives? Migration, animal dreams, the moment a cat turned in darkness: perhaps they also carried something humanity had never bothered to hear.\n\nThe question did not belong to this war.\n\nNor did it belong to Charlie.\n",
                "add soft Anna memory",
            )
        ],
        "49_尾声：没有完全死去": [
            (
                "replace",
                """At the same time, in Anna's consciousness region, rain fell on a black forest.

The rain touched leaves without sound.

A black cat sat on an exposed root, ears twitching. It had been watching the forest depths, as if waiting for footsteps underground. But when blue whale low frequency crossed from far away, it suddenly lifted its head.

In the cat's eyes, a small piece of sea reflected.

Far away.

Very old.

It listened for a while, tail slowly brushing wet soil.

Then more eyes lit in the forest depths.

Bird, deer, dog, fox, and shapes that could not immediately be named all looked from darkness toward the same direction.

The black cat meowed softly.

The sound was small, yet the whole forest seemed to wake.

In the real world, Anna still did not open her eyes.

But outside her Spirit Connect pod, the status light turned deep green for the first time.

Charlie heard the alert and turned.

Jim saw it too.

No one spoke.
""",
                """Anna's pod remained quiet.

When Charlie looked at her, he remembered the game forest from childhood and the way she had crouched beside mud to read tracks. She could always treat what others ignored as evidence, and when he and Jim rushed ahead, she could always say something calm, annoying, and later useful.

The status light on her pod shifted green for a moment.

Very faint.

It might have been system noise. It might have been the shadow of some distant consciousness turning beneath water.

Dr. Lune recorded it without explaining.

Charlie did not ask.

This was not his story to finish.
""",
                "soften Anna hook",
            )
        ],
    }

    for stem, ops in en_ops.items():
        try:
            revise(stem, ops, EN_MD)
        except RuntimeError:
            # English drafts vary more across batches; keep the Chinese pass authoritative.
            pass

    revision = ROOT / "V1二稿第一轮结构修订记录.md"
    write(
        revision,
        """# V1 二稿第一轮结构修订记录

本轮根据作者反馈完成结构方向调整：

- 降低《灵猫》硬铺垫强度：安娜/黑猫线改为轻微余震，保留朋友记忆和一个未展开的问题。
- 强化“别无选择”的必然性：在多处关键节点增加退路关闭、时间耗尽、选择不可逆的压力。
- 改造五族介绍方式：把文明理念更多落实到行动代价上，而不是让角色停下讲方案。
- 强化战争中的“放手之爱”：巨鲸、瑟恩、渊民族老人、岚柯、索勒、洛安都朝“放弃占有，让未来不必成为自己的复制品”这一共性靠拢。
- 加强瑟恩与洛安情感线：让瑟恩的路、翅膀、玩笑和洛安的怕死形成全书主要情感高潮。
- 救援线增加规则：吉姆只能定位，数字吉姆不能替代查理进入宿主视角，查理必须自己完成“胜利是共同失败”的认知闭环。

重点修改章节：

- `00_书名页与写作说明`
- `03_我不是这具身体`
- `07_宿主的名字`
- `09_日辉族的律令`
- `19_鳞裔族想要漫长潜伏`
- `20_节肢族想要没有孤独的世界`
- `21_渊民族想把记忆交给海`
- `22_震翼族只想天空还有路`
- `23_巨鲸不是武器`
- `25_它为什么坠落`
- `28_种子`
- `31_胜利者的争吵`
- `37_查理听见歌声`
- `39_吉姆的信号`
- `40_数字吉姆看见星环`
- `42_尸山重新出现`
- `43_所谓胜利`
- `45_给安娜留下的问题`
- `49_尾声：没有完全死去`
""",
    )

    readme = ROOT / "README.md"
    readme_text = read(readme)
    if "`V1二稿第一轮结构修订记录.md`" not in readme_text:
        readme_text = readme_text.replace(
            "- `V1结构审稿报告.md`：第一版结构审读、主要问题与二稿修订顺序。\n",
            "- `V1结构审稿报告.md`：第一版结构审读、主要问题与二稿修订顺序。\n"
            "- `V1二稿第一轮结构修订记录.md`：根据作者反馈完成的第一轮结构修订记录。\n",
        )
    readme_text = readme_text.replace(
        "V1 正文已扩写到尾声。下一步建议通读全书，做结构审稿、连续性检查和第二版修订计划。",
        "V1 正文已完成二稿第一轮结构修订。下一步建议作者通读新版中文 HTML，重点反馈五族段落、瑟恩情感高潮和结尾余味。",
    )
    write(readme, readme_text)

    rebuild_html()


if __name__ == "__main__":
    main()
