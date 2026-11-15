from pathlib import Path
import html
import re


ROOT = Path("巨鲸陨落_V1")
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"


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


def page(title, body, nav, lang="zh-CN"):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<main>
{body}
{nav}
</main>
</body>
</html>
"""


CHAPTERS = {
    "01_尸山之上": {
        "zh_title": "01 尸山之上",
        "en_title": "01 On the Mountain of Dead",
        "zh": """# 01 尸山之上

我醒来的时候，脚下是软的。

那不是泥，也不是雪。那东西在靴底下轻微塌陷，带着迟钝的弹性，像一层被热血泡烂的厚布。我低头看了一眼，才发现自己站在尸体上。

尸体堆成了山。

不是人类的尸体。至少不全是。

最靠近我脚边的那具残骸有四条手臂，胸腔裂开，里面没有肋骨，而是一排排像黑色甲片一样叠在一起的结构。更远处有一颗头颅滚在碎石间，复眼已经碎了一半，每一片破裂的晶面里都映着暗红色天空。还有一具身体半埋在灰里，背后残留透明翼骨，薄得像被烧焦的玻璃。风一吹，那些翼骨发出细微的震颤声，仿佛死去很久之后仍在试图飞行。

我想后退。

身体没有动。

或者说，这具身体没有按照我的意思动。

我听见自己在喘息。那声音低沉、粗糙，喉咙里像塞满沙粒。胸口疼得厉害，每一次呼吸都把某种尖锐的东西往肺里推。我抬起手，看到手背上覆盖着暗灰色的细鳞，指节比人类长，指甲像短而钝的爪。

这不是我的手。

我想说话，却只从喉咙里挤出一串陌生音节。它们不像任何我学过的语言，发音位置更深，带着颤动，好像声音不是从声带出来，而是从胸腔某个硬壳里磨出来。

可是我听懂了。

“我们活下来了。”

这句话不是我说的。是这具身体说的。

我不知道“我们”是谁，也不知道这里是哪里。天空压得很低，颜色像被铁锈染过的血。远方有几座倾斜的塔，塔身断裂，内部亮着快要熄灭的蓝光。地面上到处是坑洞、金属碎片和凝固的暗色液体。有些地方还在燃烧，却没有火焰，只有一团团无声发亮的白。

尸山之下，战场一直延伸到地平线。

我看见更多种族。

金发的高大人形倒在一片碎旗旁，皮肤苍白，额骨上嵌着像太阳纹章一样的金属环。几个鳞片覆盖全身的生物抱着破碎容器死在一起，容器里流出的液体已经结成绿色晶体。远处有成片昆虫般的尸体，它们的肢节互相扣着，像死后仍保持队列。更远处，一个水生种族的战士跪在干裂地面上，脖颈两侧的鳃片张开，里面已经没有水，只有灰。

我忽然意识到，这不是一场战斗。

这是战争的尽头。

身旁有人笑了。

那笑声很轻，带着漏风一样的颤音。我转过头，看见一个身形瘦长的生物站在尸山另一侧。他比我高一些，肩背很窄，背后收着两对透明翅膀，翅膀边缘不断细微震动，让他周围的空气泛起水纹般的模糊。

他的脸不像人。眼睛很大，虹膜呈银蓝色，嘴唇薄得几乎看不见。可他看着我的表情，我却莫名读懂了。

疲惫。疼痛。难以置信。

还有一种被压抑到快要崩溃的喜悦。

他向我伸出手，掌心上满是烧伤。

这具身体抬手握住了他。

“结束了。”他说。

我不知道他说的是哪种语言，但意思直接落进我的脑子里。

结束了。

我听见自己笑了起来。

不是我想笑。是身体在笑。笑声一开始很低，后来越来越响，像是从胸腔深处撕出来。旁边那个带翅的朋友也笑。我们站在尸山上，在无数死去种族之间笑得像两个疯子。

那不是快乐。

那是活下来的人在确认自己还没有死。

风从战场尽头吹来，带着灰、血和某种金属烧焦后的甜味。尸山下方，残存的幸存者陆续站起。有的举起断裂武器，有的跪在地上，有的只是抬头看向天空。很快，战场各处传来零散呼喊。那些声音彼此不同，却都带着同一个意思。

胜利。

我们赢了。

这具身体也这么相信。

可在我意识最深处，有一个不属于他的念头轻轻浮起来。

不对。

如果赢了，为什么天空还在变暗？

我抬头。

云层背后，有什么东西正在下降。""",
        "en": """# 01 On the Mountain of Dead

When I woke, the ground beneath my feet was soft.

It was not mud, and it was not snow. It gave way beneath my boots with a slow, obscene elasticity, like thick cloth soaked through with blood. I looked down and realized I was standing on bodies.

Bodies piled into a mountain.

Not human bodies. Not all of them.

Nearest my foot lay a corpse with four arms. Its chest had split open, and inside there were no ribs, only layered black plates. Farther away, a head had rolled between broken stones, half of its compound eye shattered, each cracked facet reflecting the dark red sky. Another body lay half-buried in ash, transparent wing-bones rising from its back, thin as scorched glass. When the wind passed through them, they trembled faintly, as if even death had not fully convinced them to stop flying.

I wanted to step back.

The body did not move.

Or rather, this body did not obey me.

I heard myself breathing. The sound was low and rough, as if my throat were packed with sand. My chest hurt so badly that every breath drove something sharp deeper into my lungs. I lifted a hand and saw dark gray scales across the back of it. The fingers were too long. The nails were blunt little claws.

This was not my hand.

I tried to speak. What came out was a string of unfamiliar sounds, deeper than any language I knew, vibrating as if speech were being ground out of some hard chamber in the chest.

And yet I understood it.

“We survived.”

The sentence was not mine. It belonged to this body.

I did not know who “we” were. I did not know where this was. The sky hung low, rust-red and heavy. In the distance, several towers leaned at impossible angles, their broken interiors glowing with fading blue light. The ground was full of craters, metal fragments, and dark fluids hardened into glass. Some places were still burning without flame, shining white in silence.

Below the mountain of dead, the battlefield reached all the way to the horizon.

I saw more peoples.

Tall golden-haired figures lay beside a torn banner, pale-skinned, their brows set with rings like sun emblems. Scaled beings clutched broken containers, green crystals forming where their contents had spilled. Farther off, insect-like bodies lay in formations, limbs interlocked as if the dead still obeyed command. Beyond them, an aquatic warrior knelt on cracked ground, gill-slits open at the throat, holding no water now, only ash.

This was not a battle.

This was the end of a war.

Someone laughed beside me.

The sound was thin, trembling, almost leaking through him. I turned and saw a slender being on the other side of the corpse-mound. He was taller than I was, narrow through the shoulders, with two pairs of translucent wings folded behind him. Their edges vibrated constantly, blurring the air around him like heat over water.

His face was not human. His eyes were large, silver-blue, and his mouth was almost invisible. But I understood his expression.

Exhaustion. Pain. Disbelief.

And a joy so compressed it was almost breaking him.

He reached out a burned hand.

This body took it.

“It is over,” he said.

I did not know the language, but the meaning landed directly inside me.

It is over.

I heard myself laugh.

Not because I wanted to. The body laughed. Low at first, then louder, torn from somewhere deep in the chest. The winged friend laughed too. We stood on a mountain of dead among the remains of many peoples and laughed like madmen.

It was not happiness.

It was the sound of the living confirming they had not died.

Wind came from the far end of the battlefield, carrying ash, blood, and the sweet stink of burned metal. Below us, survivors began to rise. Some lifted broken weapons. Some fell to their knees. Some only looked up at the sky. Soon scattered cries passed across the field. Different voices, different throats, one meaning.

Victory.

We had won.

This body believed it.

But deep inside me, a thought that did not belong to him rose quietly.

No.

If we had won, why was the sky still getting darker?

I looked up.

Something was descending behind the clouds."""
    },
    "02_巨鲸从天而降": {
        "zh_title": "02 巨鲸从天而降",
        "en_title": "02 The Whale Falls from the Sky",
        "zh": """# 02 巨鲸从天而降

一开始，我以为那是云。

战场上空本来就堆满了灰色云层，像一层层被烧焦的布压在天顶。可是那片阴影比云更重，也更慢。它没有被风推着走，而是从高处一点点压下来，像整个天空终于承受不住自己的重量。

幸存者的呼喊渐渐停了。

没有命令，也没有谁提醒。所有还活着的东西都抬起头，看向同一个方向。连那些仍在执行残余指令的节肢族单位也停了下来，复眼齐齐转向天空。那一瞬间，战场安静得可怕。火光还在燃烧，裂开的塔还在坍塌，可所有声音都像被某种巨大的东西按住。

云层裂开。

我看见了一头鲸。

这是我脑子里唯一能找到的词。

它太大了。

大到无法判断距离，也无法判断速度。它的身体横贯天空，背脊像一条缓慢弯曲的大陆，腹部布满暗蓝色裂纹，裂纹之间有光在流动。它没有鳍，却有类似鳍的巨大膜翼，边缘燃着冷白火焰。无数细小结构附着在它身体表面，像城市、像骨刺、又像一排排沉默的舱室。

那不是动物。

也不是飞船。

它像两者之间某种更古老的东西。

它正在坠落。

带翅的朋友松开了我的手。他向后退了一步，翅膀震动得更快，银蓝色眼睛里第一次出现真正的恐惧。

“它不该落在这里。”他说。

这具身体没有回答。或者说，他也不知道该怎么回答。

我听见战场下方有人跪了下去。日辉族残存的士兵把额头贴向地面，像是在迎接神明。鳞裔族的人则开始疯狂撤向地下通道。节肢族的阵列重新启动，却不是进攻，而是向四面八方散开。渊民族幸存者发出一阵低沉的水声，那声音带着某种悲伤，我听不懂，却几乎立刻想哭。

巨鲸发出了声音。

那不是吼叫。

它低到不像声音，更像整个星球的骨头被缓慢拉动。尸山开始震颤。碎石跳起，金属残片发出共鸣，远处断塔内部的蓝光一盏盏熄灭。我胸口的疼痛突然消失了，取而代之的是一种被掏空的感觉。好像有什么东西穿过这具身体，也穿过我，把两个本不该重叠的意识同时按在原地。

我看见画面。

不是眼睛看见的。

无数星图在黑暗中展开。陌生航线穿过太阳风暴，庞大的鲸群在行星之间缓慢游动。它们身体内部有城市，有记忆，有成千上万种语言被压缩成光。它们不是从某个地方来，也不属于某个族群。它们像在替整个太阳系记住曾经发生过的一切。

然后画面断了。

巨鲸撞入大气低层。

没有爆炸。

真正可怕的是没有爆炸。

它坠落时，战场被一圈无形波纹扫过。波纹经过哪里，声音就从哪里消失。火焰熄灭，旗帜碎成粉，仍站着的尸体被轻轻推倒。那些还在试图逃跑的人没有被烧成灰，也没有被撕碎，只是在波纹穿过身体的一瞬间停住，然后像被抽掉结构一样散开。

我看见一名日辉族士兵张着嘴，前一刻还在祈祷，下一刻整个人化成金色尘埃。节肢族阵列像被风吹散的壳。鳞裔族的地下入口塌陷，黑暗从里面喷出来。渊民族的水声戛然而止。

尸山也开始下沉。

带翅的朋友抓住我，把我向后拖。

“走！”

这一次，我听懂了他的恐惧。

不是怕死。

是怕巨鲸的死亡没有被完成。

远处，巨鲸庞大的身体终于接触地面。大地向下凹陷，像一张被无形手掌按住的皮。裂缝从落点向四周奔跑，穿过战壕、塔群、尸山、平原，一直奔向地平线。

天空亮了一瞬。

我在那一瞬间看见了法厄同。

不是战场，不是城市，不是我们脚下这片尸体堆成的山，而是整颗行星。它像一枚被内部光线照亮的石榴，裂缝已经从核心向外蔓延。

巨鲸没有清理战场。

它在撕裂星球。""",
        "en": """# 02 The Whale Falls from the Sky

At first, I thought it was a cloud.

The sky over the battlefield was already packed with gray layers, like scorched cloth pressed against the heavens. But this shadow was heavier than cloud, and slower. It did not drift with the wind. It descended, little by little, as if the sky could no longer bear its own weight.

The survivors stopped shouting.

No one ordered them. No one warned them. Everything still alive raised its head toward the same point. Even the Chitinous units still following broken commands stopped, their compound eyes turning upward together. For one moment, the battlefield became terribly quiet. Fires still burned. Broken towers still fell. But every sound seemed pinned beneath something vast.

The clouds split open.

I saw a whale.

It was the only word my mind could find.

It was too large.

Too large to judge distance or speed. Its body crossed the sky, its spine like a slow-bending continent, its belly veined with dark blue fissures through which light flowed. It had no fins, but immense membrane-like wings where fins should have been, their edges burning with cold white fire. Countless structures clung to its surface, like cities, like bone-spurs, like silent rows of chambers.

It was not an animal.

It was not a ship.

It was something older between the two.

It was falling.

The winged friend released my hand. He stepped back, his wings vibrating faster, true fear entering his silver-blue eyes for the first time.

“It should not fall here,” he said.

This body did not answer. Perhaps he had no answer.

Below the corpse-mountain, someone knelt. Surviving Sunbright soldiers pressed their brows to the ground as if receiving a god. Scale-Kin began fleeing madly toward underground passages. Chitinous formations restarted, not to attack, but to scatter in every direction. Abyssal survivors released a deep water-sound filled with grief. I did not understand it, and still I almost wept.

The whale made a sound.

It was not a roar.

It was so low it hardly seemed like sound at all, more like the bones of the planet being slowly pulled apart. The corpse-mountain trembled. Stones jumped. Metal fragments resonated. Far away, the blue lights inside broken towers went out one by one. The pain in my chest vanished, replaced by a hollowing sensation. Something passed through this body and through me, pinning two consciousnesses that should never have overlapped into the same place.

I saw images.

Not with the eyes.

Star maps unfolded in darkness. Unknown routes crossed solar storms. Vast herds of whales moved slowly between planets. Inside their bodies were cities, memories, thousands of languages compressed into light. They did not come from one place. They did not belong to one people. They seemed to remember the solar system on behalf of everyone.

Then the images broke.

The whale struck the lower atmosphere.

There was no explosion.

That was the terrifying part. There was no explosion.

As it fell, an invisible ripple swept across the battlefield. Wherever the ripple passed, sound disappeared. Fires went out. Banners became powder. Corpses still standing were gently pushed down. Those still trying to flee were not burned or torn apart. They simply stopped when the ripple crossed them, then scattered as if structure had been removed.

A Sunbright soldier stood with his mouth open in prayer. A moment later, he became golden dust. Chitinous ranks blew apart like empty shells. A Scale-Kin tunnel mouth collapsed, darkness spraying from within. The Abyssal water-song cut off.

The corpse-mountain began to sink.

The winged friend grabbed me and dragged me backward.

“Run!”

This time I understood his fear.

It was not fear of death.

It was fear that the whale's death had not yet been completed.

In the distance, the whale's immense body finally touched the ground. The world dented downward like skin pressed by an invisible palm. Cracks raced outward from the point of impact, through trenches, towers, corpse-heaps, plains, all the way to the horizon.

The sky flashed.

In that flash, I saw Phaeton.

Not the battlefield, not the city, not the corpse-mountain beneath us, but the whole planet. It looked like a pomegranate lit from within, cracks already spreading outward from its core.

The whale was not clearing the battlefield.

It was tearing the planet apart."""
    },
    "03_我不是这具身体": {
        "zh_title": "03 我不是这具身体",
        "en_title": "03 I Am Not This Body",
        "zh": """# 03 我不是这具身体

他拖着我往尸山下跑。

不，准确地说，是他拖着这具身体往下跑，而我被困在身体里面，像被塞进一件不合身的盔甲。每一步都让我头晕。腿部肌肉的发力方式不对，膝盖弯曲的角度不对，脚掌落地时传来的震感也不对。这个身体比人类更低，更贴近地面，奔跑时脊背会本能前倾，手臂几乎要碰到碎石。

我想控制它，却只能影响一点点。

向左。

身体微微偏了一下，避开一截从尸堆里伸出的节肢。

停下。

身体没有停。

那不是我的命令优先级太低，而是另一个意识比我更完整。他恐惧、疼痛、疲惫，却依然知道怎么活下去。相比之下，我像一个刚被扔进驾驶舱的乘客，连仪表盘都看不懂。

带翅的朋友在前面跳下尸堆，翅膀高速震动，短暂托住他的身体。他落地时踉跄了一下，右侧翅膜裂开，透明边缘不断滴落银色液体。

“洛安！”他回头喊。

这具身体猛地一震。

洛安。

原来他叫洛安。

名字出现的瞬间，一小片记忆被撕开。

不是完整人生，只是几个短促片段。昏暗舱室里，有人把一枚灰色识别片按进他的掌心；低矮训练场上，他因为反应太慢被长官踢倒；一片蓝绿色天空下，那个带翅的朋友第一次落在他面前，笑着说他的名字发音像坏掉的石门。

朋友。

他的名字也浮了上来。

瑟恩。

震翼族，低空通讯斥候，临时编入洛安所在的小队。按军规，他们不该成为朋友。按战争逻辑，不同族群之间的信任只是资源不足时的临时妥协。可记忆里的瑟恩总是在笑，笑洛安跑得慢，笑他怕死，笑他把所有逃生路线背得比祷文还熟。

“怕死有什么错？”记忆里的洛安曾经反驳。

“没错。”瑟恩说，“怕死的人通常活得久。”

画面消失。

我被重新拽回正在崩塌的战场。

身后传来低频震动。不是声音，而是从地面深处传来的持续推力。尸山塌陷，碎骨和甲片像潮水一样向下滑。几个幸存者被卷进去，连叫声都没来得及发出。

瑟恩带着洛安冲进一条半塌的战壕。战壕壁上有发光符号，但大部分已经熄灭。空气里到处是灰，吸进去时像吞刀片。洛安的左腿受了伤，跑到一半忽然跪倒。我感觉疼痛从膝盖炸开，眼前一黑。

这一次，我发出了自己的声音。

“疼！”

瑟恩猛地回头。

他看着我，眼神变了。

“你刚才说什么？”

洛安也愣住了。

我能感觉到他的恐惧突然变了方向。之前他怕的是巨鲸、战场、星球破裂。现在，他开始怕自己。

因为刚才那一声，不属于他的语言。

那是中文。

在法厄同终战的战壕里，在无数远古种族尸体之间，我用查理·黑尔的声音喊了一句疼。

“我……”我试图再说话。

喉咙收紧。洛安的意识像本能一样压过来，把我的声音按回深处。

别出声。

这不是语言，却是明确的意志。

他知道我在。

我也终于知道，他不是一段影像，不是供我读取的记忆，不是游戏里的宿主模型。

他是活过的人。

或者，曾经活过的人。

瑟恩扶起洛安，盯着他的眼睛。

“你身上有别的频率。”

洛安没有回答。

因为他不知道答案。

我也不知道。

战壕上方，巨鲸坠落后的第二道波纹扫过。整个世界忽然向右倾斜，像有一只手抓住星球边缘轻轻一掰。远处传来连绵不断的断裂声，低沉、漫长，像大陆骨骼正在一节节折断。

瑟恩咬牙，翅膀再次震动。

“先活下去。”

这一次，我和洛安同时理解了这句话。

不管我是谁，不管他是谁，不管这颗叫法厄同的星球正在发生什么，在所有答案出现之前，我们必须先活下去。""",
        "en": """# 03 I Am Not This Body

He dragged me down the mountain of dead.

No. More precisely, he dragged this body downward, and I was trapped inside it like someone forced into armor that did not fit. Every step made me dizzy. The leg muscles fired wrong. The knees bent at the wrong angle. The soles struck the ground with a shock I did not recognize. This body ran lower than a human body, closer to the ground, spine leaning forward by instinct, arms almost brushing broken stone.

I tried to control it.

Only a little of me got through.

Left.

The body shifted slightly, avoiding a jointed limb jutting from the corpse-pile.

Stop.

The body did not stop.

It was not that my command was weak. It was that another consciousness was more complete. He was afraid, hurt, exhausted, and still he knew how to survive. I was only a passenger thrown into a cockpit whose instruments I could not read.

The winged friend jumped down ahead of us, wings vibrating fast enough to hold him briefly in the air. He stumbled when he landed. The membrane on his right side was torn, its transparent edge dripping silver fluid.

“Lo'an!” he shouted back.

This body jolted.

Lo'an.

So that was his name.

The moment it appeared, a small piece of memory tore open.

Not a life, only fragments. A dim cabin where someone pressed a gray identity chip into his palm. A low training yard where an officer kicked him down for reacting too slowly. A blue-green sky under which the winged friend first landed in front of him and laughed that his name sounded like a broken stone gate.

Friend.

The friend's name surfaced too.

Sern.

Wing-Shiver. Low-altitude communication scout. Temporarily assigned to Lo'an's unit. By regulation, they should not have become friends. By the logic of war, trust between different peoples was only a temporary compromise when resources were short. But in memory, Sern was always laughing: laughing that Lo'an ran slowly, that he feared death, that he memorized escape routes more faithfully than prayers.

“What is wrong with fearing death?” Lo'an had once snapped.

“Nothing,” Sern said. “Those who fear death often live longer.”

The memory vanished.

I was thrown back into the collapsing battlefield.

Behind us came a low vibration. Not sound, but pressure from deep beneath the ground. The corpse-mountain caved in, bones and armor plates sliding like a tide. Several survivors were swallowed without time to scream.

Sern pulled Lo'an into a half-collapsed trench. Faint symbols glowed on its walls, most of them already dead. Ash filled the air. Breathing it felt like swallowing knives. Lo'an's left leg was injured; halfway through the trench he fell to one knee. Pain burst from the joint, and my vision went black.

This time, I made a sound of my own.

“It hurts!”

Sern spun around.

He stared at me, and his expression changed.

“What did you say?”

Lo'an froze too.

I felt his fear shift direction. Until now, he had feared the whale, the battlefield, the breaking planet. Now he had begun to fear himself.

Because the words had not belonged to him.

They had been Chinese.

In a trench during Phaeton's final war, among the corpses of ancient peoples, I had cried out in the voice of Charlie Hale.

“I...” I tried to speak again.

The throat tightened. Lo'an's consciousness surged over me by instinct, pressing my voice back down.

Do not speak.

It was not language, but it was will.

He knew I was there.

And I finally knew that he was not a recording, not a memory prepared for me to read, not a host model in some game.

He was a person who had lived.

Or once lived.

Sern helped Lo'an up, staring into his eyes.

“There is another frequency in you.”

Lo'an did not answer.

He did not know.

Neither did I.

Above the trench, the second ripple from the whale's fall swept past. The world suddenly tilted rightward, as if some hand had gripped the edge of the planet and bent it. From far away came a long chain of cracking sounds, deep and extended, like continental bones breaking one by one.

Sern clenched his teeth. His wings began to vibrate again.

“Survive first.”

This time, Lo'an and I understood together.

Whoever I was, whoever he was, whatever was happening to this planet called Phaeton, before any answers could arrive, we had to survive."""
    },
}


def write_pair(key, data, prev_key=None, next_key=None):
    zh_path = ZH_MD / f"{key}.md"
    en_path = EN_MD / f"{key}.md"
    zh_path.write_text(data["zh"], encoding="utf-8")
    en_path.write_text(data["en"], encoding="utf-8")

    prev_link = f'<a href="{prev_key}.html">上一章</a>' if prev_key else ""
    next_link = f'<a href="{next_key}.html">下一章</a>' if next_key else ""
    nav = f'<nav class="nav"><span>{prev_link}</span><span><a href="../index.html">目录</a></span><span>{next_link}</span></nav>'
    ZH_HTML.joinpath(f"{key}.html").write_text(page(data["zh_title"], md_to_html(data["zh"]), nav, "zh-CN"), encoding="utf-8")

    en_prev = f'<a href="{prev_key}.html">Previous</a>' if prev_key else ""
    en_next = f'<a href="{next_key}.html">Next</a>' if next_key else ""
    en_nav = f'<nav class="nav"><span>{en_prev}</span><span><a href="../index_EN.html">Index</a></span><span>{en_next}</span></nav>'
    EN_HTML.joinpath(f"{key}.html").write_text(page(data["en_title"], md_to_html(data["en"]), en_nav, "en"), encoding="utf-8")


if __name__ == "__main__":
    keys = ["01_尸山之上", "02_巨鲸从天而降", "03_我不是这具身体"]
    all_order = [p.stem for p in sorted(ZH_MD.glob("*.md"))]
    for key in keys:
        idx = all_order.index(key)
        prev_key = all_order[idx - 1] if idx > 0 else None
        next_key = all_order[idx + 1] if idx + 1 < len(all_order) else None
        write_pair(key, CHAPTERS[key], prev_key, next_key)
    print("expanded chapters 01-03")
