from pathlib import Path
import html
import re


ROOT = Path("巨鲸陨落_V1")
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"
ASSETS = ROOT / "assets"


CSS = """
:root {
  color-scheme: light;
  --ink: #202124;
  --muted: #5f6368;
  --line: #dadce0;
  --paper: #ffffff;
  --soft: #f6f7f8;
  --accent: #345c72;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--soft);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Segoe UI", sans-serif;
  line-height: 1.75;
}
main {
  max-width: 880px;
  margin: 0 auto;
  padding: 48px 28px 72px;
  background: var(--paper);
  min-height: 100vh;
}
h1, h2, h3 {
  line-height: 1.35;
  color: #111;
  font-weight: 650;
}
h1 { font-size: 2.1rem; margin: 0 0 16px; }
h2 { font-size: 1.45rem; margin: 34px 0 10px; border-top: 1px solid var(--line); padding-top: 20px; }
h3 { font-size: 1.15rem; margin: 24px 0 8px; color: var(--accent); }
p { margin: 0 0 14px; }
ul, ol { margin: 0 0 18px 1.2rem; padding: 0; }
li { margin: 4px 0; }
a { color: #1a5f7a; text-decoration: none; }
a:hover { text-decoration: underline; }
.meta {
  color: var(--muted);
  font-size: 0.95rem;
  border-left: 4px solid var(--accent);
  padding: 8px 0 8px 14px;
  margin: 18px 0 26px;
}
.nav {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  margin-top: 42px;
  padding-top: 20px;
  border-top: 1px solid var(--line);
  color: var(--muted);
}
blockquote {
  margin: 20px 0;
  padding: 10px 18px;
  background: #f3f6f8;
  border-left: 4px solid var(--accent);
}
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  background: #f1f3f4;
  padding: 1px 4px;
  border-radius: 4px;
}
table { border-collapse: collapse; width: 100%; margin: 20px 0; }
td, th { border: 1px solid var(--line); padding: 8px 10px; vertical-align: top; }
th { background: #f1f3f4; text-align: left; }
"""


CHAPTERS = [
    ("00", "书名页与写作说明", "Title Page and Writing Notes", "frontmatter",
     "建立《巨鲸陨落》V1 的写作目标、章节文件规则、双语阅读方式。", "Set up the V1 writing target, chapter-file rules, and bilingual reading mode.",
     "这不是最终定稿，而是一套可以逐章扩写的工程版。每个章节文件都保留剧情功能、文明背景插入点和正文种子，后续扩写时以自然发生为原则，避免人物为了讲设定而停下来。"),
    ("01", "尸山之上", "On the Mountain of Dead", "act1",
     "查理附身醒来，站在法厄同终战后的尸山上，保留梦境原始震撼。", "Charlie wakes inside another body on the corpse mountain after the final battle of Phaeton.",
     "开篇不解释身份和战争原因，只写疼痛、陌生身体、异族残骸、身旁的朋友，以及那种以为自己胜利了的荒凉狂喜。查理要先不知道自己是查理，只在身体深处感到一种不属于宿主的恐惧。"),
    ("02", "巨鲸从天而降", "The Whale Falls from the Sky", "act1",
     "巨鲸坠落清空战场，读者第一次意识到这不是普通战争。", "The falling whale clears the battlefield and reveals the scale of the war.",
     "巨鲸不是怪物，而像一座燃烧的生物星舰。它落下时，战场不是爆炸式毁灭，而是被某种低频震荡抹平。宿主和朋友以为这是胜利的标志，但查理感到那声音像悲伤。"),
    ("03", "我不是这具身体", "I Am Not This Body", "act1",
     "查理意识到自己附身在远古幸存者体内。", "Charlie realizes he is inhabiting an ancient survivor's body.",
     "用感官错位推动情节：手指数量、呼吸方式、血液颜色、语言不是中文却能理解。查理的意识像水泡一样浮在宿主记忆里，不能完全控制身体，只能跟着对方活下去。"),
    ("04", "震翼族朋友", "The Wing-Shiver Friend", "act1",
     "介绍身边异族战友，建立跨族情感锚点。", "Introduce the alien comrade who becomes Charlie's emotional anchor.",
     "朋友暂定来自震翼族，翅膀像蜻蜓但不是昆虫，靠高速震动进行短距飞行和频率通讯。他不负责讲设定，而是负责把查理从尸山上拖下来。"),
    ("05", "法厄同的天空裂开", "The Sky of Phaeton Splits", "act1",
     "巨鲸陨落后，法厄同星开始破裂。", "After the whale's fall, Phaeton begins to fracture.",
     "天空出现不是云层裂缝，而是轨道穹顶、磁场和大气同时崩坏的视觉。尸体浮起，远方陆架断开。查理第一次听到法厄同这个名字。"),
    ("06", "逃离胜利", "Fleeing the Victory", "act1",
     "宿主和朋友逃离战场，胜利被重新染上不祥。", "The host and his friend flee the battlefield, and victory turns ominous.",
     "这一章要让读者感到：庆祝胜利的人其实正在逃命。不要解释巨鲸，只让幸存者反复说一句类似‘它不该落在这里’的话。"),
    ("07", "宿主的名字", "The Host's Name", "act2",
     "查理从残余记忆里知道宿主身份。", "Charlie learns the host's identity through memory fragments.",
     "宿主可暂名为洛安，低阶斥候或战地搬运员，不是英雄。他能活下来不是因为强大，而是因为怕死、敏锐、愿意跟着朋友跑。查理在他身上看见自己。"),
    ("08", "五族残骸", "The Remains of Five Peoples", "act2",
     "通过战场遗骸介绍各族外观，不做长篇百科。", "Introduce the factions through battlefield remains rather than exposition.",
     "尸体中有日辉族的金色骨饰、鳞裔族的冷硬鳞甲、节肢族的碎裂复眼、渊民族的干涸鳃膜、震翼族的透明翼骨。每个细节都是查理看见的，不是作者讲出来的。"),
    ("09", "日辉族的律令", "The Decrees of the Sunbright", "act2",
     "进入第一段文明背景：日辉族代表秩序与天神原型。", "First civilization background insert: the Sunbright as order and godlike archetype.",
     "通过遗留战令和宿主记忆介绍日辉族。他们相信地球未来需要被秩序化，生命必须有阶层、律法、建筑和统一意识组织。不要把他们写成纯反派。"),
    ("10", "鳞裔族的地底库", "The Scale-Kin Vaults", "act2",
     "介绍鳞裔族与基因保存、地下设施、长期潜伏。", "Introduce the Scale-Kin and their vaults of genetic preservation.",
     "洛安和朋友进入地下避难通道，发现鳞裔族的冷藏库。里面保存的不是武器，而是种子、胚胎、基因图谱。查理意识到这场战争和未来生命有关。"),
    ("11", "节肢族不会哀悼", "The Chitinous Do Not Mourn", "act2",
     "介绍节肢族集群意识和战争效率。", "Introduce the Chitinous and their collective war logic.",
     "节肢族的残部仍在执行失效命令。一个个体死去时，其他个体没有哀悼，只是调整队列。查理既害怕这种冷酷，也感到它们像一台受伤的整体。"),
    ("12", "渊民的水声", "The Abyssal Water-Song", "act2",
     "介绍渊民族和地球海洋生命记忆。", "Introduce the Abyssal people and their link to oceanic life.",
     "逃亡者经过破裂水穹，听到渊民族用水声传递信息。这里第一次埋蓝鲸歌声的低频前奏，但查理还不懂，只觉得像很远的哭声。"),
    ("13", "震翼族的频率", "The Frequency of the Wing-Shiver", "act2",
     "让震翼族朋友成为信息与情感桥梁。", "Use the Wing-Shiver friend as the emotional and informational bridge.",
     "朋友用翅振把信息传给查理的宿主。查理不是听懂语言，而是被频率触碰到情绪：恐惧、忠诚、失去家园。文明背景通过朋友的伤口显出来。"),
    ("14", "谁赢了", "Who Won", "act2",
     "开始质疑开篇胜利。", "Begin questioning the opening victory.",
     "幸存者之间争论谁赢了。日辉族说秩序胜利，鳞裔族说保存胜利，节肢族说目标未完成，渊民族说海会记住一切。查理发现没人真的知道战争结果。"),
    ("15", "地球不是战场", "Earth Was Not the Battlefield", "act3",
     "揭示地球是争夺目标，不是战争地点。", "Reveal Earth as the contested prize rather than the battlefield.",
     "法厄同位于火星与木星之间，是通往地球实验场的门槛。谁控制法厄同，谁就能决定地球生命的未来改造路径。"),
    ("16", "第五行星", "The Fifth Planet", "act3",
     "明确法厄同星和小行星带的小说设定。", "Define Phaeton and its link to the asteroid belt within the novel.",
     "这一章可以由宿主记忆、碎裂地图和查理的现代知识叠加完成。现代查理意识到：这颗星后来不存在了，它的残骸就是火星与木星之间的小行星带。"),
    ("17", "生命孵化场", "The Cradle-Lab", "act3",
     "解释地球被视为生命孵化场。", "Explain Earth as a cradle-lab for future life.",
     "不要写成会议说明。让查理看到地球投影：还未完全属于任何一族，海洋、陆地、大气和意识频率都在被观察。各族都想留下自己的版本。"),
    ("18", "日辉族想要人类跪拜", "The Sunbright Wanted Kneeling Humans", "act3",
     "日辉族对地球未来的方案。", "The Sunbright proposal for Earth's future.",
     "他们不一定邪恶，但他们相信秩序高于自由。未来人类在他们设想中会拥有建筑、法律、王权和对天神的记忆。"),
    ("19", "鳞裔族想要漫长潜伏", "The Scale-Kin Wanted Patience", "act3",
     "鳞裔族对地球未来的方案。", "The Scale-Kin proposal for Earth's future.",
     "他们希望把地球变成长期基因库，文明可以沉入地下，等待周期更替。这里可连接后世蜥蜴人、地下文明传说。"),
    ("20", "节肢族想要没有孤独的世界", "The Chitinous Wanted a World Without Loneliness", "act3",
     "节肢族方案不只是效率，也包含免除个体孤独的诱惑。", "The Chitinous proposal contains not only efficiency but the temptation of freedom from loneliness.",
     "给节肢族一点悲悯：它们不理解个体痛苦，因为它们从不孤独。它们想给地球一种集群意识未来，却会抹去个人。"),
    ("21", "渊民族想把记忆交给海", "The Abyssals Wanted the Sea to Remember", "act3",
     "渊民族与海洋、记忆、蓝鲸种子相关。", "The Abyssals link ocean, memory, and the future whale seed.",
     "渊民族认为海比陆地诚实。它们不想统治地球，只想让地球海洋保留远古文明的声音。蓝鲸种子的承接人可从这里出现。"),
    ("22", "震翼族只想天空还有路", "The Wing-Shiver Wanted the Sky to Stay Open", "act3",
     "震翼族不是主要争夺者，却是道路、通讯和自由的守护者。", "The Wing-Shiver are not dominant claimants but guardians of routes and communication.",
     "朋友的族群不想拥有地球，只想保持通道开放。这样他和查理/宿主的友谊会更自然：他们都不是宏大计划的主人，只是被卷进去的人。"),
    ("23", "巨鲸不是武器", "The Whale Was Not a Weapon", "act4",
     "第一次真正解释巨鲸族。", "Reveal that the whale people are not weapons.",
     "查理从残留频率里看到巨鲸内部：不是胃和骨骼，而是记忆星图、意识舱室、文明档案。巨鲸像生物飞船，也像活着的图书馆。"),
    ("24", "星海的记忆载体", "Carriers of Star-Sea Memory", "act4",
     "巨鲸族作为文明级意识载体。", "The whale people as civilization-scale carriers of memory.",
     "每头巨鲸承载一个族群、一段航线或一场文明失败。它们在太阳系内不是霸主，而是见证者。它们最大的力量是不让任何一族单独改写历史。"),
    ("25", "它为什么坠落", "Why It Fell", "act4",
     "提出巨鲸陨落的真正动机。", "Present the true motive of the whale's fall.",
     "巨鲸选择坠落不是为了帮助某一方赢，而是为了终结所有族群独占地球的可能。它以自身为代价，把战争变成没有胜利者的结局。"),
    ("26", "洛安第一次想逃", "Lo'an Wanted to Run", "act4",
     "宿主的普通人本质显现。", "The host's ordinary nature emerges.",
     "宿主洛安不想承担历史，他只想活着。查理在他身上看见自己，也第一次不再羞耻于怕死。怕死不等于懦弱，它证明你还知道生命有重量。"),
    ("27", "朋友没有跟上", "The Friend Fell Behind", "act4",
     "异族朋友牺牲或失散，情感推进。", "The alien friend is lost or separated, pushing the emotional arc.",
     "不要为了煽情牺牲他。让他的选择自然发生：为了打开频率通道、保护种子或拖住残余部队，他停下了。查理/洛安必须继续走。"),
    ("28", "种子", "The Seed", "act4",
     "巨鲸种子出现。", "The whale seed appears.",
     "种子不是一颗物理种子，而是一段生物蓝图、意识频率和低维记忆压缩体。它需要被带往地球海洋，不能被任何一族独占。"),
    ("29", "渊民的容器", "The Abyssal Vessel", "act4",
     "渊民族提供保存巨鲸种子的方式。", "The Abyssals provide a way to preserve the whale seed.",
     "渊民族用水声和生物容器保存种子。这里要把蓝鲸连接写得含蓄：不是直接说将来会有蓝鲸，而是说它会在地球海洋里等待足够长的时间。"),
    ("30", "法厄同开始下沉", "Phaeton Begins to Sink", "act4",
     "行星破裂进入不可逆阶段。", "Phaeton's fracture becomes irreversible.",
     "陆地像船一样倾斜，天空中轨道碎片落下，远方城市从地平线翻起。这里要写出星球级灾难，不只是战场灾难。"),
    ("31", "胜利者的争吵", "The Winners Argue", "act5",
     "各族残余争夺巨鲸种子，胜利反转开始。", "The surviving factions fight over the whale seed, beginning the reversal of victory.",
     "战争结束后仍有人想抢种子。查理看到所谓文明的高贵在失败面前剥落。幸存者必须决定：把种子交给谁，或者不交给任何一族。"),
    ("32", "没有一族配拥有地球", "No People Deserved Earth Alone", "act5",
     "核心主题落地：任何单一族群都不该独占地球。", "Core theme: no single people should own Earth.",
     "洛安、震翼族朋友的残留讯息、渊民族容器共同推动决定：地球不能成为某一族的未来，而只能成为混合之后的新开始。"),
    ("33", "通往地球的残舟", "The Broken Vessel to Earth", "act5",
     "幸存者带种子离开法厄同。", "Survivors carry the seed away from Phaeton.",
     "他们搭乘的不该是宏伟飞船，而是残破逃生舟。这样巨鲸种子去地球不是胜利者凯旋，而是失败者护送最后一点温柔。"),
    ("34", "小行星带的诞生", "Birth of the Asteroid Belt", "act5",
     "法厄同破碎成为小行星带的神话真相。", "Phaeton breaks into the asteroid belt.",
     "从逃生舟回望，法厄同被撕成无数碎片。现代查理的意识叠加进来，意识到人类后来会把这里叫小行星带。"),
    ("35", "地球的海", "Earth's Sea", "act5",
     "巨鲸种子抵达早期地球海洋。", "The whale seed reaches Earth's early ocean.",
     "这章要安静。没有大战，只有海。渊民族容器释放种子，巨鲸频率沉入早期生命链。主题句可在这里出现：巨鲸死在星空里，醒在地球的海中。"),
    ("36", "蓝鲸尚未诞生", "The Blue Whale Was Not Born Yet", "act5",
     "明确蓝鲸不是外星巨鲸直接变成，而是低维种子漫长演化结果。", "Clarify that blue whales are not direct alien whales but long-evolved low-dimensional seeds.",
     "写一段跨越时间的蒙太奇：海洋生命演化，哺乳动物回到海中，歌声越来越低。不要违背现实感，要像神话藏在演化里面。"),
    ("37", "查理听见歌声", "Charlie Hears the Song", "act5",
     "查理通过蓝鲸歌声理解巨鲸没有完全死。", "Charlie understands through whale song that the giant whales did not fully die.",
     "现代查理意识在记录里听见蓝鲸低频。那声音与法厄同终战中巨鲸临终频率相同。他不是用脑子理解，而是先哭了。"),
    ("38", "宿主最后的选择", "The Host's Last Choice", "act5",
     "洛安完成自己的命运，查理尊重这个普通人。", "Lo'an completes his fate, and Charlie honors an ordinary man.",
     "洛安不必成为伟人。他只要做一件小事：把种子交出去、守住朋友的托付、或者承认没有人赢了。这就是普通幸存者的重量。"),
    ("39", "吉姆的信号", "Jim's Signal", "bridge",
     "连接回《月球暗面》结尾，吉姆和数字吉姆开始触碰查理区域。", "Connect back to the end of Moon-Dark as Jim and digital Jim touch Charlie's region.",
     "查理第一次感觉到外部有人在喊他。不要让救援太快成功，信号像远处穿过水的光。"),
    ("40", "数字吉姆看见星环", "Digital Jim Sees the Ring", "bridge",
     "从救援侧短暂切视角，确认巨鲸战场区域。", "Briefly shift to the rescue side to confirm the whale battlefield region.",
     "可以用很短章节写数字吉姆判断：这里不是月暗记录表层，而是太阳系战争深层切片。吉姆意识到查理不是梦见战争，而是被战争记忆选中。"),
    ("41", "查理不想走", "Charlie Does Not Want to Leave", "bridge",
     "查理因同情宿主和朋友，不愿立刻脱离。", "Charlie hesitates to leave because of the host and his friend.",
     "成长点：查理不再只是想醒来逃走。他想确认洛安、朋友和巨鲸种子的意义没有被白白消耗。"),
    ("42", "尸山重新出现", "The Corpse Mountain Returns", "bridge",
     "开篇场景回返，意义反转。", "Return to the opening image with reversed meaning.",
     "查理再次站上尸山，但这次他知道那不是胜利纪念碑，而是所有族群失败的证据。身旁朋友的影像或频率残留再次出现。"),
    ("43", "所谓胜利", "The So-Called Victory", "bridge",
     "主题章：胜利其实是共同失败。", "Theme chapter: victory was collective failure.",
     "把开篇庆祝胜利彻底翻转。查理明白他们庆祝的不是赢，而是终于活过一个无人真正赢下的时刻。"),
    ("44", "人类的混合遗产", "Humanity's Mixed Inheritance", "bridge",
     "查理带回地球人来源关键结论。", "Charlie carries back the key truth about humanity's mixed inheritance.",
     "不是某一族创造人类，而是法厄同终战后多族遗产被迫混合，经过地球漫长演化与后续月暗系统干预，才出现人类。"),
    ("45", "给安娜留下的问题", "The Question Left for Anna", "bridge",
     "不抢《灵猫》，但留下动物灵文明连接。", "Leave a question for Anna without taking over the Lingmao book.",
     "查理在蓝鲸歌声里察觉不止巨鲸种子，还有动物意识网络的暗线。他不知道那是什么，只知道安娜可能会懂。"),
    ("46", "回声归档", "Archiving the Echo", "bridge",
     "查理区域开始稳定，月暗守卫或泰拉撒系统反应。", "Charlie's region stabilizes, and the system responds.",
     "系统试图把查理经历归档。吉姆和数字吉姆要在归档前把查理的主体核拉出来。这里是救援动作高潮。"),
    ("47", "醒来之前", "Before Waking", "bridge",
     "查理与宿主告别。", "Charlie says farewell to the host.",
     "宿主洛安未必以人形出现，也可以是一段身体记忆。查理感谢他让自己知道怕死也可以完成使命。"),
    ("48", "蓝鲸在地球歌唱", "Blue Whales Sing on Earth", "ending",
     "查理醒来或即将醒来，蓝鲸歌声成为本书情感落点。", "Charlie wakes or nearly wakes, with blue whale song as the emotional landing point.",
     "结尾不要大喊真相。让查理听见现代地球海洋中的蓝鲸歌声，低声说：它们还在。"),
    ("49", "尾声：没有完全死去", "Epilogue: Not Fully Dead", "ending",
     "收束第二本，接回系列主线并预告《灵猫》。", "Close book two, reconnect to the series, and foreshadow Lingmao.",
     "吉姆接收到查理带回的记忆：法厄同、小行星带、巨鲸种子、人类混合遗产。最后镜头转向安娜的区域：一只黑猫听见蓝鲸低频，抬头。"),
]


def slug(item):
    number, zh_title, *_ = item
    safe = re.sub(r"[\\/:*?\"<>| ]+", "_", zh_title)
    return f"{number}_{safe}"


def md_to_html(text):
    lines = text.splitlines()
    out = []
    in_ul = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            continue
        if stripped.startswith("# "):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append(f"<h1>{html.escape(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append(f"<h2>{html.escape(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append(f"<h3>{html.escape(stripped[4:])}</h3>")
        elif stripped.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{html.escape(stripped[2:])}</li>")
        elif stripped.startswith("> "):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append(f"<blockquote><p>{html.escape(stripped[2:])}</p></blockquote>")
        else:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            out.append(f"<p>{html.escape(stripped)}</p>")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


def page(title, body, rel_css="../assets/style.css", nav=""):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{rel_css}">
</head>
<body>
<main>
{body}
{nav}
</main>
</body>
</html>
"""


def zh_chapter(item):
    number, zh_title, en_title, act, zh_goal, en_goal, seed = item
    return f"""# {number} {zh_title}

## 章节定位

- 所属部分：{act}
- 目标字数：1500-2000 中文字
- 本章功能：{zh_goal}

## 正文种子

{seed}

## 写作要点

- 让事件自然发生，先写人物的身体反应和选择，再把文明背景藏进场景。
- 尽量避免让角色停下来讲百科；背景信息优先通过遗迹、伤口、战令、歌声、逃亡路线和错误理解显现。
- 查理的核心气质是怕死、嘴碎、普通，但关键时刻会跟上。他不是突然变成英雄，而是慢慢学会见证。

## 文明背景插入点

本章只插入必要背景，不提前解释全局真相。读者应该和查理一样先迷失，再逐步理解法厄同终战、巨鲸族和地球来源。
"""


def en_chapter(item):
    number, zh_title, en_title, act, zh_goal, en_goal, seed = item
    return f"""# {number} {en_title}

## Chapter Position

- Part: {act}
- Target length: 1,500-2,000 Chinese characters in the source draft
- Function: {en_goal}

## Draft Seed

This chapter should follow the Chinese version's story beat: {seed}

## Writing Notes

- Let plot arise from action, bodily sensation, memory fragments, and choice before explaining civilization lore.
- Avoid encyclopedia-style exposition. Background should surface through ruins, wounds, orders, songs, escape routes, and misinterpretation.
- Charlie's core nature is ordinary, frightened, verbally defensive, but loyal at the decisive moment. His growth is not becoming a mythic hero; it is learning that an ordinary survivor can carry historical truth.

## Civilization Insert

Use only the background required by this chapter. The reader should remain as disoriented as Charlie at first, then slowly understand Phaeton's final war, the whale people, and the origin of Earth's inheritance.
"""


def index_md(language="zh"):
    if language == "zh":
        lines = ["# 巨鲸陨落 V1", "", "《灵接科技》第二本章节工程版。", "", "## 章节目录"]
        for item in CHAPTERS:
            lines.append(f"- [{item[0]} {item[1]}](zh_md/{slug(item)}.md) / [HTML](zh_html/{slug(item)}.html)")
        lines.append("")
        lines.append("## 版本说明")
        lines.append("")
        lines.append("这一版先建立 50 个小章节的独立文件、阅读 HTML、双语对应和剧情功能。后续扩写时，每章目标控制在 1500-2000 中文字，最终形成约 10 万字 V1 正文。")
    else:
        lines = ["# The Fall of the Giant Whale V1", "", "Book two of Spirit Connect, chapter-engineering edition.", "", "## Chapter Index"]
        for item in CHAPTERS:
            lines.append(f"- [{item[0]} {item[2]}](en_md/{slug(item)}.md) / [HTML](en_html/{slug(item)}.html)")
        lines.append("")
        lines.append("## Version Notes")
        lines.append("")
        lines.append("This version first establishes 50 separate chapter files, reading HTML pages, bilingual counterparts, and story functions. Later passes should expand each chapter to roughly 1,500-2,000 Chinese characters, forming an approximately 100,000-character V1 manuscript.")
    return "\n".join(lines) + "\n"


def write_all():
    for folder in [ZH_MD, EN_MD, ZH_HTML, EN_HTML, ASSETS]:
        folder.mkdir(parents=True, exist_ok=True)
    (ASSETS / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")

    for idx, item in enumerate(CHAPTERS):
        name = slug(item)
        zh = zh_chapter(item)
        en = en_chapter(item)
        (ZH_MD / f"{name}.md").write_text(zh, encoding="utf-8")
        (EN_MD / f"{name}.md").write_text(en, encoding="utf-8")
        prev_link = ""
        next_link = ""
        if idx > 0:
            prev_name = slug(CHAPTERS[idx - 1])
            prev_link = f'<a href="{prev_name}.html">上一章</a>'
        if idx + 1 < len(CHAPTERS):
            next_name = slug(CHAPTERS[idx + 1])
            next_link = f'<a href="{next_name}.html">下一章</a>'
        nav = f'<nav class="nav"><span>{prev_link}</span><span><a href="../index.html">目录</a></span><span>{next_link}</span></nav>'
        (ZH_HTML / f"{name}.html").write_text(page(item[1], md_to_html(zh), nav=nav), encoding="utf-8")

        en_prev = ""
        en_next = ""
        if idx > 0:
            en_prev = f'<a href="{slug(CHAPTERS[idx - 1])}.html">Previous</a>'
        if idx + 1 < len(CHAPTERS):
            en_next = f'<a href="{slug(CHAPTERS[idx + 1])}.html">Next</a>'
        en_nav = f'<nav class="nav"><span>{en_prev}</span><span><a href="../index_EN.html">Index</a></span><span>{en_next}</span></nav>'
        (EN_HTML / f"{name}.html").write_text(page(item[2], md_to_html(en), nav=en_nav), encoding="utf-8")

    zh_index = index_md("zh")
    en_index = index_md("en")
    (ROOT / "index.md").write_text(zh_index, encoding="utf-8")
    (ROOT / "index_EN.md").write_text(en_index, encoding="utf-8")
    (ROOT / "index.html").write_text(page("巨鲸陨落 V1", md_to_html(zh_index), rel_css="assets/style.css"), encoding="utf-8")
    (ROOT / "index_EN.html").write_text(page("The Fall of the Giant Whale V1", md_to_html(en_index), rel_css="assets/style.css"), encoding="utf-8")

    readme = """# 巨鲸陨落_V1

这是《灵接科技》第二本《巨鲸陨落》的 V1 章节工程目录。

- `zh_md/`：中文章节 Markdown。
- `zh_html/`：中文阅读 HTML。
- `en_md/`：英文章节 Markdown。
- `en_html/`：英文阅读 HTML。
- `index.html`：中文阅读目录。
- `index_EN.html`：英文阅读目录。

当前版本先建立 50 个小章节的完整骨架和写作种子。下一步应从 `01_尸山之上` 开始逐章扩写到 1500-2000 中文字。
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    write_all()
    print(ROOT.resolve())
