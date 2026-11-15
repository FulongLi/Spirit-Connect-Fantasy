from pathlib import Path
import html


ROOT = Path("巨鲸陨落_V1")
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"


def md_to_html(text):
    out = []
    in_ul = False
    for line in text.splitlines():
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


def page(title, body, nav, lang):
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
    "04_震翼族朋友": {
        "zh_title": "04 震翼族朋友",
        "en_title": "04 The Wing-Shiver Friend",
        "zh": """# 04 震翼族朋友

瑟恩没有再问我刚才说了什么。

他显然想问。那双银蓝色眼睛在我脸上停了半秒，又迅速移向战壕尽头。巨鲸坠落后的低频仍在地底扩散，像一头看不见的兽在星球骨骼里翻身。战壕壁上的符号一枚接一枚熄灭，黑暗追着我们向前爬。

“还能跑吗？”瑟恩问。

这句话是问洛安的。

洛安咬着牙点头。

我能感觉到他在撒谎。左腿膝盖以下几乎没有知觉，伤口处的疼痛被巨鲸低频震得麻木，只剩一阵阵冷。他不敢低头看，因为他知道自己一旦确认伤势，就会跑不动。

瑟恩也知道。

他没有拆穿，只把一只手臂绕到洛安背后，另一只手抓住战壕壁上凸出的金属筋。背后两对透明翅膀忽然展开，翅膜上有数十条极细的银线亮起。

我原以为翅膀只是用来飞的。

下一秒，空气开始震动。

不是普通振翅，而是某种极高频率的切割。瑟恩周围的灰尘被震成一圈细雾，洛安胸腔里某个结构随之共鸣。我听不见全部声音，却能感到一串讯息贴着皮肤传进来。

左侧塌方。  
右侧有热源。  
前方三十七步，旧补给沟。  
别回头。

这不是语言。

是频率。

震翼族就是这样通讯的。这个念头从洛安记忆里浮起。战场上，瑟恩的族人不需要喊叫，不需要旗帜，也不需要通讯器。只要翅膀还在，他们就能用震动把方位、情绪和警告送进同伴骨头里。很多族群害怕他们，因为你不知道一个震翼族在沉默时，是否正在向远处传递整支军队的位置。

可瑟恩现在传给我的不是军情。

是逃命路线。

他拖着洛安冲出战壕。外面已经不是刚才的战场。巨鲸落点方向升起一圈灰白色的墙，那墙不是烟尘，更像被磨碎的地壳与大气混在一起形成的潮。潮面所到之处，金属塔倒下，尸体被卷走，活着的东西变成没有声音的影子。

瑟恩带着洛安贴地奔跑。每隔几步，他的翅膀就短促一振，把两人的身体向前推一段。那不是飞行，更像在濒死星球表面借空气弹跳。洛安的身体被拖得几乎散架，我在里面被颠得想吐，可胃的位置也不对，恶心只变成一阵胸腔抽搐。

“你刚才的声音，”瑟恩终于说，“不是洛安。”

洛安没有回答。

我也不敢出声。

“别怕。”瑟恩说，“我见过频率寄生，也见过临死前的记忆重叠。你不是最奇怪的那个。”

他试图开玩笑，声音却抖得厉害。

洛安在意识深处缩了一下。这个反应很小，却被我感觉到了。他害怕瑟恩知道，也害怕瑟恩不知道。

我忽然意识到，洛安并不是一个孤独的容器。他有朋友，有羞耻，有不想被看穿的脆弱。他不是为了承载查理·黑尔而存在的人。

瑟恩突然停下。

前方的地面裂开，战壕尽头被一道新生深沟切断。沟底没有黑暗，而是翻滚的红光，像星球内部被掀开。对面是一条倾斜的补给沟，距离不算远，但洛安现在的腿不可能跳过去。

瑟恩看了看裂沟，又看了看洛安。

“抱紧我。”

洛安本能后退。

记忆里，震翼族不喜欢负重飞行。翅膀一旦在重压下撕裂，他们很可能再也无法通讯，也无法回到空中。对震翼族来说，翅膀不是工具，是族群、语言和尊严。

“瑟恩，你的翼膜已经裂了。”

洛安终于开口。

瑟恩咧了咧嘴。那个表情不像笑，更像把恐惧压进牙缝。

“所以要快。”

他抓住洛安，四翼同时展开。翅膜边缘的银线全亮起来，震动声刺进骨头。我们冲向裂沟。

半空中，我看见远处的巨鲸残影仍在下沉。

它太大了，像一段文明的夜晚正在落向地面。

然后瑟恩的翅膀猛地一抖，右侧裂开的翼膜被风撕开更大一片。银色液体飞散，落在洛安脸上，烫得像火。

我们没有飞到对面。

我们撞了过去。

洛安的肩膀重重砸在补给沟边缘，半个身体悬空。瑟恩摔在另一侧，翅膀压在碎石下，疼得发出一声短促的嘶鸣。

我想喊他的名字。

这一次，洛安先喊了出来。

“瑟恩！”""",
        "en": """# 04 The Wing-Shiver Friend

Sern did not ask again what I had just said.

He clearly wanted to. His silver-blue eyes rested on my face for half a second, then snapped toward the end of the trench. The low frequency from the whale's fall was still spreading underground, like an unseen beast turning in the planet's bones. Symbols on the trench walls died one by one, darkness crawling after us.

“Can you run?” Sern asked.

The question was for Lo'an.

Lo'an nodded through clenched teeth.

I could feel the lie. Below the left knee there was almost no sensation. The wound had been numbed by the whale's vibration, leaving only waves of cold. He did not dare look down. If he confirmed the damage, he would stop moving.

Sern knew it too.

He did not expose the lie. He hooked one arm around Lo'an's back and gripped a metal rib in the trench wall with the other. Two pairs of transparent wings unfolded behind him. Dozens of hair-thin silver lines lit within the membranes.

I had thought wings were for flying.

Then the air began to vibrate.

Not ordinary wingbeats. A high-frequency cutting motion. Dust around Sern became a ring of fine mist, and something in Lo'an's chest resonated with it. I could not hear the whole signal, but I felt it enter through skin and bone.

Left side collapse.  
Heat source to the right.  
Old supply ditch thirty-seven steps ahead.  
Do not look back.

This was not language.

It was frequency.

That was how the Wing-Shiver spoke. The knowledge rose from Lo'an's memory. On the battlefield, Sern's people did not need shouting, flags, or devices. As long as their wings remained, they could send direction, emotion, and warning into the bones of their allies. Many peoples feared them, because when a Wing-Shiver was silent, you never knew whether he was transmitting the position of an entire army.

But Sern was not sending battle orders now.

He was sending an escape route.

He dragged Lo'an out of the trench. The world outside was no longer the battlefield from before. In the direction of the whale's impact, a gray-white wall had risen. It was not smoke. It looked like crushed crust and atmosphere ground together into a tide. Wherever the tide passed, towers fell, corpses vanished, and living things became soundless silhouettes.

Sern ran low, dragging Lo'an close to the ground. Every few steps his wings snapped once, pushing both bodies forward. It was not flight. It was like skipping across the skin of a dying planet. Lo'an's body felt as if it would come apart, and I was shaken inside him until I wanted to vomit. But the stomach was wrong too; nausea became only a convulsion in the chest.

“That voice,” Sern said at last, “was not Lo'an.”

Lo'an did not answer.

Neither did I.

“Do not be afraid,” Sern said. “I have seen frequency parasitism. I have seen memory overlap before death. You are not the strangest thing today.”

He was trying to joke. His voice trembled anyway.

Deep inside, Lo'an flinched. The reaction was tiny, but I felt it. He was afraid Sern knew, and afraid Sern did not know.

Lo'an was not an empty vessel. He had a friend. Shame. Vulnerability he did not want seen. He had not existed merely to carry Charlie Hale.

Sern stopped suddenly.

The ground ahead had split open, cutting off the end of the trench. Below the fissure was not darkness but rolling red light, as if the planet's interior had been uncovered. Across the gap lay a slanted supply ditch. It was not far, but Lo'an's injured leg could never jump it.

Sern looked at the gap, then at Lo'an.

“Hold on to me.”

Lo'an instinctively stepped back.

In memory, Wing-Shiver did not like burdened flight. If the wings tore under weight, they might never communicate again, never return to air. For them, wings were not tools. They were people, language, dignity.

“Sern, your membrane is torn.”

Lo'an finally spoke.

Sern bared his teeth. It was not a smile so much as fear crushed between them.

“Then we go fast.”

He seized Lo'an. All four wings opened. Silver lines blazed along their edges, and the vibration stabbed into bone. We hurled ourselves toward the fissure.

In midair, I saw the whale's immense shadow still sinking in the distance.

It was too large, like a civilization's night falling toward the ground.

Then Sern's wings shuddered. The tear in the right membrane ripped wider. Silver fluid scattered across Lo'an's face, hot as fire.

We did not fly across.

We crashed.

Lo'an's shoulder struck the supply ditch rim, half his body hanging over empty red light. Sern fell to the other side, wings pinned beneath stone, releasing a short hiss of pain.

I wanted to shout his name.

This time, Lo'an shouted first.

“Sern!”"""
    },
    "05_法厄同的天空裂开": {
        "zh_title": "05 法厄同的天空裂开",
        "en_title": "05 The Sky of Phaeton Splits",
        "zh": """# 05 法厄同的天空裂开

洛安爬上补给沟时，半边身体都在发抖。

瑟恩比他先站起来，却没有立刻收起翅膀。那两对透明翅膜垂在背后，右侧撕裂处从根部一直延伸到边缘，银色液体顺着膜纹往下滴。他看了一眼，没有说什么，只用左手把裂开的翼膜折回身后。

这个动作让洛安的记忆刺痛了一下。

震翼族不在外族面前折翼。

除非他们知道，自己已经没有力气遮掩。

补给沟比战壕更窄，两侧堆满破损箱体。许多箱子已经裂开，里面不是弹药，而是透明片、灰色管束和一排排小型封存罐。洛安认得其中一部分，那是战地用的神经贴片和短程识别核。更多东西他不认得，查理也不认得。它们躺在那里，像一场战争仓促留下的内脏。

头顶忽然亮了一下。

不是闪电。

整片天空像被从外面划开一道口子。

我抬头，看见云层之后有更高的结构正在崩解。那不是自然天空，而像一层看不见的穹顶被巨鲸坠落震出了裂缝。裂缝边缘流动着暗紫色光，光里夹杂无数细小符号，像某种维持行星大气和轨道防线的系统正在失效。

“穹场裂了。”瑟恩说。

洛安的心脏猛地收紧。

穹场。

这个词带出一串残缺记忆：法厄同外层曾有多重轨道护幕，用来抵御木星引力扰动、太阳风暴和外轨道打击。对洛安这种低阶人员来说，穹场不是技术，而是常识。它就像天空一样在那里，从出生到战争末期都在那里。

现在天空裂开了。

补给沟外的战场开始出现更诡异的变化。先是尸体浮起。不是全部，只是某些较轻的残骸和碎甲片，像被失控重力短暂遗忘。接着，远处一座倾斜塔楼突然向上拉伸，像被看不见的线提了一下，随即从中段折断。折断部分没有落下，而是缓慢飘向天空裂缝。

“别看。”瑟恩推了洛安一下。

可是我控制不住。

我看见更远处的地平线正在弯曲。不是因为热浪，也不是视觉错觉。整块陆架像被人从下面抬起，边缘缓慢翻卷，露出底部红黑色的岩层。巨大的裂缝穿过平原，把城市残骸、战壕和尸堆切成两半。

一颗星球正在失去“地面”这个概念。

“法厄同撑不住了。”瑟恩低声说。

法厄同。

这个名字第一次清晰落进我的意识。

不是城市名，不是战场名。

是这颗星球。

我的现代记忆轻轻动了一下。我不是天文学家，但也知道火星和木星之间有一条小行星带。有人曾经提出过假说，说那里原本也许有一颗消失的行星。名字好像就叫法厄同。

这不可能。

我在心里说。

可脚下的星球正在碎裂，巨鲸仍在远方下沉，洛安的记忆告诉我：这里就是法厄同。

瑟恩从一个破损箱体里翻出两枚灰色贴片，把其中一枚按在洛安颈侧。贴片刺入皮肤，释放出一阵冰冷。洛安的左腿疼痛被短暂压低，呼吸也稳定了一点。

“你还有几步能跑？”瑟恩问。

洛安说：“够到下一个避难点。”

“你每次说够，意思都是不够。”

“那你每次问，也不是因为想听真话。”

瑟恩怔了一下，随即笑了。那笑声很短，却让这具身体里某个绷紧的地方松了一点。

他们太熟了。

熟到在星球裂开时，仍能用这种方式确认彼此还活着。

补给沟尽头传来一阵金属摩擦声。几个节肢族残余单位从灰雾里爬出，复眼碎裂，肢节残缺，却仍按照某种命令向前移动。它们没有看洛安和瑟恩，只是朝着巨鲸坠落方向爬去。

“它们还在回收战场数据。”瑟恩说。

“现在回收有什么用？”洛安问。

瑟恩看向天空裂缝。

“也许对它们来说，星球碎了也只是战损。”

一阵更强的震动打断了他们。

补给沟上方的岩层开始塌落。瑟恩抓起洛安，两人冲向沟底更深处。身后，天空裂缝投下暗紫色光，把他们的影子拉得很长。

那影子一会儿像两个逃兵。

一会儿像两个幸存者。

而在更高处，法厄同的天空继续裂开。""",
        "en": """# 05 The Sky of Phaeton Splits

Lo'an was shaking through half his body by the time he climbed into the supply ditch.

Sern stood first, but he did not fold his wings immediately. The two pairs hung behind him, the right membrane torn from root to edge, silver fluid dripping along its veins. He glanced at it and said nothing, only used his left hand to fold the damaged wing back.

The motion made Lo'an's memory ache.

Wing-Shiver did not fold broken wings in front of outsiders.

Unless they no longer had strength to hide the break.

The supply ditch was narrower than the trench, its sides piled with damaged crates. Many had split open. Inside were not munitions, but transparent wafers, gray cable-bundles, and rows of small preservation canisters. Lo'an recognized some of them: neural patches and short-range identity cores. The rest meant nothing to him, and nothing to Charlie. They lay scattered like the hastily abandoned organs of a war.

The sky flashed.

Not lightning.

It was as if the whole sky had been cut open from outside.

I looked up and saw a higher structure breaking behind the clouds. This was not natural sky. It was an invisible dome cracking under the whale's fall. Dark violet light flowed along the edges of the fissure, full of tiny symbols, as though the system maintaining atmosphere and orbital defense had begun to fail.

“The vault-field is splitting,” Sern said.

Lo'an's heart tightened.

Vault-field.

The word dragged up broken memory: Phaeton's outer layers had once carried several orbital veils, shielding the planet from Jupiter's tidal disturbance, solar storms, and attacks from high orbit. For someone like Lo'an, the vault-field was not technology. It was common sense. It had been there like the sky, from birth to the end of war.

Now the sky was splitting.

Outside the ditch, the battlefield began changing in stranger ways. First, corpses lifted. Not all of them, only lighter bodies and fragments of armor, as if malfunctioning gravity had forgotten them for a moment. Then a leaning tower in the distance stretched upward, pulled by an invisible thread, before snapping in the middle. The broken half did not fall. It drifted toward the crack in the sky.

“Do not look,” Sern said, shoving Lo'an forward.

But I could not stop.

I saw the horizon bending. Not from heat, not from illusion. An entire shelf of land was rising from below, its edge slowly curling, exposing red-black strata underneath. A giant fissure crossed the plain, cutting through ruined cities, trenches, and corpse-fields.

A planet was losing the meaning of ground.

“Phaeton will not hold,” Sern said softly.

Phaeton.

The name landed clearly in me for the first time.

Not a city. Not a battlefield.

The planet.

Something stirred in my modern memory. I was no astronomer, but I knew there was an asteroid belt between Mars and Jupiter. Some old hypothesis had imagined a missing planet there. Its name, maybe, had been Phaeton.

Impossible.

I thought it.

But the planet beneath my feet was breaking, the whale still sank in the distance, and Lo'an's memory told me: this was Phaeton.

Sern dug two gray patches from a broken crate and pressed one against Lo'an's neck. The patch bit through skin, releasing a cold wave. Pain in Lo'an's left leg lowered briefly, and his breathing steadied.

“How many more steps can you run?” Sern asked.

“Enough to reach the next shelter.”

“When you say enough, you mean not enough.”

“When you ask, it is not because you want the truth.”

Sern froze for a fraction of a second, then laughed. It was short, but something tight inside this body loosened.

They knew each other too well.

Well enough that even while a planet split open, they could still confirm each other was alive this way.

At the end of the ditch came the scrape of metal. Several damaged Chitinous units crawled from the gray haze, compound eyes cracked, limbs broken, still moving under some command. They did not look at Lo'an or Sern. They crawled toward the whale's impact.

“Still recovering battlefield data,” Sern said.

“What use is data now?” Lo'an asked.

Sern looked toward the fissured sky.

“Perhaps to them, a broken planet is only a combat loss.”

A stronger tremor cut him off.

Rock above the supply ditch began to fall. Sern seized Lo'an, and they ran deeper into the ditch. Behind them, dark violet light from the split sky stretched their shadows long.

For one moment those shadows looked like deserters.

For another, survivors.

High above them, Phaeton's sky continued to split."""
    },
    "06_逃离胜利": {
        "zh_title": "06 逃离胜利",
        "en_title": "06 Fleeing the Victory",
        "zh": """# 06 逃离胜利

补给沟尽头是一扇半埋在岩层里的门。

门原本应该很厚，表面有三层锁环和一排身份识别槽。现在它歪斜着，左下角被炸开，边缘凝着黑色玻璃。洛安看到它时，身体里本能升起一点希望。

避难点。

不是正式避难所，只是战场补给线上的临时藏身处。按规定，它能容纳二十个标准体型单位，维持六个小时的空气和基础屏蔽。对正在碎裂的法厄同来说，六个小时听起来像一种奢侈。

瑟恩把识别片插进门边残缺的槽里。

没有反应。

他低声骂了一句。那句骂人的话带着很细的翅振，我没有完全听懂，但大概和“愿你的祖先都在逆风里产卵”有关。

洛安用肩膀撞了一下门。

门没动。

他又撞。伤口里的冷麻被撞散，疼痛重新冲上来。第三次时，瑟恩按住他。

“让开。”

“你的翅膀不能再震了。”

“那你想用脸把门磨开？”

洛安没有力气反驳。

瑟恩把两只手贴在门缝上，背后的翅膀没有完全展开，只轻轻抖动。震动一开始很弱，像指尖敲在玻璃上。接着频率升高，门缝里的黑色玻璃出现细小裂纹。那些裂纹顺着锁环蔓延，发出刺耳的细响。

我在洛安身体里感到那股震动。它不是力量，而是耐心。像用一根细针挑开一块石头内部最脆弱的纹理。

门终于向内塌了一小段。

瑟恩立刻停下，脸色变得更灰。他的右侧翅膜又裂开一点，银色液体落在地上，像几颗很亮的星。

洛安钻进去，把门从里面推开。

避难点里已经有人。

准确地说，是已经有很多尸体。

狭窄空间被挤得几乎没有落脚处。几个日辉族士兵靠墙坐着，金色头发被灰粘成一缕一缕，额头上的太阳环黯淡无光。一个鳞裔族女人半跪在地上，怀里抱着一只碎裂的封存罐，身体僵硬，像死前仍在护着它。角落里有两名节肢族个体，肢节互相交叠，复眼关闭，像两台终于断电的机器。

空气里没有腐臭。

死亡太新鲜，还没来得及腐烂。

瑟恩看了一圈，轻声说：“他们以为这里安全。”

洛安没有说话。

刚才战场上还有人在喊胜利。这里的人也许也喊过。他们可能冲进避难点，关上门，以为自己活下来了。然后巨鲸的第一道波纹穿过岩层，空气还在，身体还在，个体结构却被抽走。

胜利像一个玩笑。

一个很残忍的玩笑。

洛安把一具日辉族尸体轻轻挪开，腾出一小块地方。瑟恩靠墙坐下，翅膀贴着墙面，疼得闭上眼。洛安检查避难点控制板，发现空气系统还能用，屏蔽层只剩一半。

“够多久？”瑟恩问。

洛安看着跳动的残缺符号。

“不知道。”

“那就是不够。”

“你能不能别总把我的话翻译得这么准确？”

瑟恩笑了一下。

外面传来远远的呼喊。

洛安僵住。那不是敌人，是幸存者。很多个声音，混乱，恐惧，正在朝这边靠近。

“开门吗？”我在心里问。

这句话没有出口，但洛安感觉到了。

他也在问自己。

避难点只能容纳二十个单位。里面已经塞满尸体。空气系统残缺，屏蔽层不稳。再让别人进来，所有人都可能死得更快。

瑟恩睁开眼。

“别想太久。”他说。

“你知道我在想什么？”

“你每次想当好人，脸都很蠢。”

洛安低头看着地上的尸体。然后他拖起一具节肢族残骸，把它挪到门边，又把几具已经没有结构反应的尸体推向角落。

“只让活的进来。”洛安说。

瑟恩叹了口气。

“你迟早死在这种决定上。”

“那你可以别帮。”

瑟恩撑着墙站起，翅膀微微震动，把门缝里的碎玻璃震落。

“少废话，开门。”

洛安拉开门。

外面的幸存者跌了进来。日辉族、渊民族、鳞裔族，还有一个失去半边身体的震翼族幼兵。他们满身灰尘，眼睛里还残留着胜利口号破碎后的茫然。

有人哭着说：“我们赢了，对吗？”

没人回答。

门重新合上时，外面的天空又亮了一次。

这一次，避难点里的所有人都明白，他们正在逃离的不是失败。

而是胜利。""",
        "en": """# 06 Fleeing the Victory

At the end of the supply ditch was a door half-buried in stone.

It had once been thick, with three locking rings and a row of identity slots. Now it leaned sideways, its lower-left corner blasted open and sealed with black glass. When Lo'an saw it, a small instinctive hope rose in him.

Shelter.

Not an official refuge, only a temporary node along the battlefield supply line. By regulation, it could hold twenty standard bodies and maintain six hours of air and basic shielding. On a breaking Phaeton, six hours sounded luxurious.

Sern inserted an identity chip into the damaged slot.

Nothing happened.

He cursed softly. The curse carried a thin wing vibration I did not fully understand, but it seemed to involve someone's ancestors laying eggs in a headwind.

Lo'an rammed the door with his shoulder.

It did not move.

He rammed it again. The cold numbness in his wound broke apart, pain flooding back. On the third attempt, Sern stopped him.

“Move.”

“Your wings cannot vibrate again.”

“Would you rather polish it open with your face?”

Lo'an had no strength to answer.

Sern placed both hands against the seam. His wings did not fully open. They only trembled. At first the vibration was faint, like fingertips tapping glass. Then the frequency climbed. Tiny cracks appeared in the black glass inside the seam and spread along the locking rings with a thin, piercing sound.

Inside Lo'an's body, I felt that vibration. It was not force. It was patience. Like a needle finding the weakest grain inside stone.

The door finally collapsed inward a little.

Sern stopped at once, his face grayer. The right wing membrane tore a little farther, silver fluid dropping to the floor like bright stars.

Lo'an crawled in and shoved the door open from inside.

The shelter already had people in it.

More precisely, it had bodies.

The narrow space was almost full. Several Sunbright soldiers sat against the wall, golden hair clumped with ash, sun-rings on their brows dim. A Scale-Kin woman knelt with a shattered preservation canister in her arms, body stiff, still guarding it in death. Two Chitinous individuals lay in a corner, limbs interlocked, compound eyes closed, like machines finally powered down.

There was no stench.

Death was too fresh to rot.

Sern looked around and said softly, “They thought this was safe.”

Lo'an did not answer.

Out on the battlefield, people had still been shouting victory. Perhaps these people had shouted too. Perhaps they had rushed inside, shut the door, believed they had survived. Then the whale's first ripple had passed through stone. Air remained. Bodies remained. But individual structure had been removed.

Victory was a joke.

A cruel one.

Lo'an moved a Sunbright corpse aside to clear a small space. Sern sat against the wall, wings pressed flat, eyes closed in pain. Lo'an checked the control board. The air system still functioned. The shielding was half gone.

“How long?” Sern asked.

Lo'an looked at the broken symbols.

“I do not know.”

“Then not long enough.”

“Can you stop translating my words so accurately?”

Sern laughed once.

From outside came distant shouting.

Lo'an froze. Not enemies. Survivors. Many voices, chaotic and afraid, coming closer.

Do we open it? I asked inside.

The words did not leave the mouth, but Lo'an felt them.

He was asking himself the same thing.

The shelter could hold twenty. It was full of dead. The air system was damaged. The shield unstable. Letting more in could kill everyone faster.

Sern opened his eyes.

“Do not think too long.”

“You know what I am thinking?”

“Every time you want to be decent, your face becomes stupid.”

Lo'an looked down at the bodies. Then he dragged a Chitinous corpse toward the door and pushed several bodies with no remaining structure response into the corner.

“Only the living enter,” Lo'an said.

Sern sighed.

“You will die from decisions like this.”

“You do not have to help.”

Sern used the wall to stand. His wings vibrated faintly, shaking glass from the door seam.

“Stop talking. Open it.”

Lo'an pulled the door.

Survivors fell in. Sunbright, Abyssal, Scale-Kin, and a young Wing-Shiver missing half his body. They were covered in ash, their eyes still full of the confusion left after a victory cry breaks.

Someone sobbed, “We won, didn't we?”

No one answered.

When the door closed again, the sky outside flashed once more.

This time everyone in the shelter understood that what they were fleeing was not defeat.

It was victory."""
    },
    "07_宿主的名字": {
        "zh_title": "07 宿主的名字",
        "en_title": "07 The Host's Name",
        "zh": """# 07 宿主的名字

避难点里挤进了十三个活着的东西。

我之所以用“东西”，不是因为他们不值得被称作人，而是因为我一时找不到更合适的词。这里没有一个种族和我完全相似。即便最接近人类外形的日辉族，也高得过分，骨架修长，额头上的金属环像从颅骨里长出来。渊民族靠在角落里，用湿布包住自己的鳃片，每隔一会儿就发出痛苦的抽气声。鳞裔族女人把碎裂封存罐抱得更紧，仿佛那里面还有比她自己更重要的生命。

洛安坐在门边，左腿伸直，手里握着一把只剩半截的短刃。

那把刀不是为了战斗。

是为了如果门外有什么东西闯进来，他至少能让自己看上去还在守门。

我越来越能分清洛安和自己。

他的恐惧很具体：空气够不够，瑟恩的翅膀还能不能震，左腿会不会坏死，门外的裂缝什么时候追到这里。我的恐惧更不合时宜：我是谁，我为什么在这里，我的身体是不是还躺在灵接舱里，吉姆和安娜有没有醒来。

有时候两个恐惧会重叠。

比如“我会不会死”。

这个问题我们都很关心。

瑟恩坐在洛安对面，正在用牙齿撕开一段灰色绷带。他的手抖得厉害，几次没能把绷带绕到翅根。洛安看不下去，把短刃放到一边，挪过去帮他。

“别碰右翼。”瑟恩说。

“我不碰你就会流干。”

“震翼族不会流干。”

“你们只是嘴硬到死前最后一刻。”

瑟恩露出一点笑意。

洛安的手比我想象中稳。他先把裂开的翼膜边缘轻轻抬起，再把绷带沿着银线纹路固定。每碰一下，瑟恩的肩背就抽动一下，却没有喊疼。

这段动作带出另一片记忆。

洛安小时候住在法厄同南半球的矿雾区。那里没有真正的蓝天，只有穹场过滤后的淡绿色光。父亲是补给线维修员，母亲在地下水室工作。他不是士兵家庭出身，也没有高贵血统。战争扩大后，他被征召进后勤斥候队，因为他方向感好，记忆路线快，最重要的是，他很会躲。

长官曾经当众羞辱他。

“你跑得比谁都快。”

洛安回答：“活着送到补给，算任务完成吗？”

所有人都笑。

瑟恩也笑，但笑完之后，他把一份备用路线图塞给洛安。

“你说得对。”瑟恩说，“死掉的勇敢没有运输价值。”

那是他们成为朋友的开始。

记忆里的洛安不是英雄。他怕高，怕火，怕节肢族阵列靠近时那种整齐的脚步声。他在第一次上战场前吐了三次，还把自己的识别片弄丢过。瑟恩笑了他整整半个月。

可也是洛安在第三次轨道轰炸后，背着一个昏迷的震翼族幼兵穿过废管道，绕开日辉族封锁，把人送回临时医站。

他不是不怕。

他只是怕归怕，脚还会继续走。

这个事实让我很难受。

因为我突然明白，洛安和查理·黑尔之间的距离并没有我希望的那么远。

我也怕死。

我也总是嘴上说不想掺和。

可真到那一步，我大概也会跟着吉姆和安娜跑进麻烦里。不是因为勇敢，而是因为朋友在里面。

“你又走神了。”瑟恩说。

洛安抬头。

“没有。”

“你有。你的眼睛刚才像坏掉的回收屏，一会儿亮，一会儿暗。”

洛安没有说话。

瑟恩压低声音：“那个频率还在？”

洛安的手停住。

我感觉到他想否认。

但避难点太小，外面的星球正在裂开，谎言在这种地方显得很浪费空气。

“在。”洛安说。

瑟恩看着他。

“它想伤害你吗？”

洛安没有立刻回答。

我也屏住了某种不存在的呼吸。

最后，洛安说：“它很害怕。”

这句话让我愣住。

瑟恩也愣住，然后轻轻笑了。

“那就让它排队。这里每个活着的都很害怕。”

洛安低下头，继续给他的翅膀缠绷带。

在这一刻，我第一次不再只是附身者。

我像一个被允许暂时坐在旁边的人，听见两个远古幸存者在世界崩塌时，用玩笑给恐惧留出一点活路。""",
        "en": """# 07 The Host's Name

Thirteen living things had crowded into the shelter.

I use “things” not because they did not deserve to be called people, but because I had no better word. None of them fully resembled me. Even the Sunbright, closest to human shape, were too tall, too long-boned, their metal brow-rings seeming to grow from the skull. Abyssals leaned in a corner with wet cloth wrapped over their gill-slits, drawing painful breaths. The Scale-Kin woman held her broken preservation canister tighter, as if it contained a life more important than her own.

Lo'an sat by the door, left leg stretched out, holding a short blade broken in half.

The blade was not for fighting.

It was so that if something came through the door, he could at least look as though he were still guarding it.

I was learning to tell Lo'an from myself.

His fears were specific: whether the air would last, whether Sern's wings could vibrate again, whether the left leg would rot, when the cracks outside would reach the door. My fears were badly timed: who I was, why I was here, whether my body still lay in a Spirit Link pod, whether Jim and Anna had woken.

Sometimes the fears overlapped.

Would I die?

Both of us cared about that one.

Sern sat opposite Lo'an, tearing at a strip of gray bandage with his teeth. His hands shook so badly that he failed several times to wrap it around the wing-root. Lo'an finally put down the broken blade and moved over.

“Do not touch the right wing,” Sern said.

“If I do not, you will bleed dry.”

“Wing-Shiver do not bleed dry.”

“You are just stubborn until the last second before death.”

Sern almost smiled.

Lo'an's hands were steadier than I expected. He lifted the torn membrane edge gently, then fixed the bandage along the silver vein-lines. Each touch made Sern's shoulders jerk, but he did not cry out.

The motion opened another memory.

Lo'an had grown up in the mining fog zone of Phaeton's southern hemisphere. There had been no true blue sky there, only pale green light filtered through the vault-field. His father repaired supply lines. His mother worked in the underground water rooms. He was not from a soldier family, and he had no noble blood. When the war expanded, he was drafted into a logistics scout unit because he had a good sense of direction, memorized routes quickly, and above all, knew how to hide.

An officer once humiliated him in front of everyone.

“You run faster than anyone.”

Lo'an answered, “If the supplies arrive alive, does the task count as complete?”

Everyone laughed.

Sern laughed too, but afterward he slipped Lo'an a spare route map.

“You are right,” Sern said. “Dead bravery has no transport value.”

That was the beginning of their friendship.

Lo'an was no hero. He feared heights, fire, and the synchronized footfalls of Chitinous ranks. Before his first battlefield deployment, he vomited three times and lost his identity chip. Sern mocked him for half a month.

But after the third orbital bombardment, it was Lo'an who carried an unconscious Wing-Shiver youngling through waste pipes, around a Sunbright blockade, and back to a field station.

He was not unafraid.

He was afraid, and his feet kept moving.

The fact hurt.

Because I suddenly understood that Lo'an and Charlie Hale were not as far apart as I wanted.

I was afraid of dying too.

I always said I did not want to get involved.

But when the moment came, I would probably run after Jim and Anna into trouble. Not because I was brave. Because my friends were inside.

“You drifted again,” Sern said.

Lo'an looked up.

“No.”

“Yes. Your eyes looked like a broken recovery screen. Bright, dark, bright.”

Lo'an said nothing.

Sern lowered his voice. “That frequency is still there?”

Lo'an's hand stopped.

I felt him want to deny it.

But the shelter was small, the planet outside was breaking, and lies seemed a waste of air in such a place.

“It is,” Lo'an said.

Sern watched him.

“Does it want to harm you?”

Lo'an did not answer at once.

I held a breath I did not have.

At last, Lo'an said, “It is afraid.”

I froze.

Sern froze too, then laughed softly.

“Then make it queue. Everyone alive in here is afraid.”

Lo'an lowered his head and continued binding the wing.

For the first time, I was not only an intruder.

I was someone permitted to sit nearby for a while, listening as two ancient survivors made room for fear with jokes while the world collapsed."""
    },
    "08_五族残骸": {
        "zh_title": "08 五族残骸",
        "en_title": "08 The Remains of Five Peoples",
        "zh": """# 08 五族残骸

避难点的空气系统撑了不到二十分钟。

不是完全坏掉，而是开始间歇性抽风。每一次抽风，墙缝里都会喷出带灰的冷气，把地上的尘和死者身上的碎屑吹起来。活着的人咳嗽，死去的人沉默。那种沉默比咳嗽更重。

洛安和瑟恩不得不清理出一条通向后门的路。

所谓后门，是避难点最里面的一块维修板。板后可能连着旧管道，也可能只连着塌方。没有人知道。可前门外的裂缝正在逼近，空气也撑不了多久，不知道的路总比确定的死路好。

清路意味着搬开尸体。

这件事比想象中更难。

日辉族士兵很重。他们骨架修长，死后身体仍保持某种仪式感，像连倒下都要符合规训。洛安拖动其中一具时，尸体额头上的金属环刮过地面，发出清脆声响。金属环上刻着细密线条，中心是太阳形符号。

一段记忆从洛安脑中浮起：日辉族军官在战前宣读律令，声音通过扩音塔传遍阵地。他们说法厄同必须被统一，地球必须被交给拥有秩序的族群，否则未来生命只会在混乱中互相吞噬。

洛安当时站在队列末尾，只记得那军官的头发在灯下亮得刺眼。

现在，那种亮埋在灰里。

鳞裔族女人更难搬。

不是因为重，而是因为她死死抱着那只封存罐。洛安试图把罐子拿出来，尸体僵硬的手指却扣得极紧。瑟恩看了一眼，说：“别动她的东西。”

“我们需要挪开她。”

“那就连东西一起挪。”

洛安照做。

封存罐裂缝里有绿色微光，像某种还没完全死去的东西。鳞裔族的鳞片不是蜥蜴那样粗糙，而是冷硬、细密，边缘有金属质感。她脖颈处挂着一枚黑色小牌，上面没有名字，只有一串周期编号。

洛安认得这种编号。

长期库。

鳞裔族不相信短暂胜利。他们保存基因、保存胚胎、保存失败后的下一次机会。战争对他们来说不是一代人的事，而是可以拖进地下、拖进睡眠、拖进漫长周期里的事。

角落里的节肢族个体最轻，也最难让人下手。

它们像昆虫，却又明显不是昆虫。外骨骼呈暗褐色，胸部嵌着战术节点，复眼关闭后像两块碎裂黑镜。洛安搬起其中一具时，另一具的肢节突然动了一下。

避难点里所有人都僵住。

那具节肢族没有复活。只是某个残留指令让它的前肢抬起，轻轻碰了碰同伴的胸部节点。动作很小，像在确认连接是否还在。

然后它彻底不动了。

查理，也就是我，在那一瞬间忽然不那么害怕它们了。

如果一个集群意识的个体在死后仍试图确认同伴，那它们真的没有感情吗？还是我们只是听不懂它们表达感情的方式？

渊民族幸存者主动站起来，帮忙挪开自己族人的尸体。

那具渊民族战士死在门边，鳃片干裂，皮肤从蓝灰变成近乎白色。幸存者跪在他身旁，用随身水囊里最后一点水抹过死者额头。水一接触皮肤，便发出极低的声音。

不是滴水声。

像歌。

避难点里没人说话。

那声音很短，却让我想起巨鲸坠落前的低频。不同的是，巨鲸的声音像星球骨骼被拉动，而这声音像海在很远的地方记住了一个名字。

“渊民会把死者交给水。”洛安的记忆告诉我，“如果没有水，就交给声音。”

最后是震翼族幼兵。

他还活着，但失去了半边翅膀和一条腿。瑟恩靠过去时，幼兵睁开眼，银蓝色虹膜已经开始浑浊。他用极弱的翅振说了些什么。

瑟恩的脸色变了。

洛安听不懂全部，只捕捉到几个频率：

上层通道。  
仍有人。  
不要让日辉族拿到种子。

种子。

这个词像一枚小石子落进我意识里。

洛安也听见了，但他不知道意思。瑟恩显然知道一点，却没有立刻解释。他只把幼兵的手放回胸前，低声说：“收到。”

幼兵的翅膀停止震动。

维修板终于被清出来。

洛安回头看了一眼避难点。短短二十分钟里，这里像一座被压缩的太阳系坟场。日辉族、鳞裔族、节肢族、渊民族、震翼族，所有刚才还在战场上互相杀戮的族群，现在被迫挤在同一个快要失效的盒子里。

死亡把他们混在一起。

而活着的人不得不从他们中间爬出去。

瑟恩撬开维修板，一股冷风从后面涌出。

不是新鲜空气。

是通向更深处的灰。

洛安握紧短刃，钻了进去。

我跟着他，穿过五族残骸之间最后一点狭窄的空隙。""",
        "en": """# 08 The Remains of Five Peoples

The shelter's air system lasted less than twenty minutes.

It did not fail completely. It began to cough. Each time it did, cold air full of ash sprayed from the wall seams, lifting dust and fragments from the dead. The living coughed. The dead were silent. Their silence weighed more than the coughing.

Lo'an and Sern had to clear a path to the rear exit.

The “rear exit” was a maintenance panel at the back of the shelter. Behind it might be an old pipeway, or only collapse. No one knew. But the fissures outside were coming closer, and the air would not last. An unknown path was better than a certain dead end.

Clearing the path meant moving bodies.

It was harder than expected.

Sunbright soldiers were heavy. Their frames were long, and even in death their bodies held a kind of ceremony, as if falling down had to obey discipline. When Lo'an dragged one aside, the metal ring on its brow scraped the floor with a clear sound. Fine lines covered the ring. At the center was a sun-shaped mark.

A memory rose from Lo'an: a Sunbright officer reciting decrees before battle, his voice carried across the line by amplification towers. Phaeton must be unified, he had said. Earth must be entrusted to the people of order, or future life would devour itself in chaos.

Lo'an had stood at the end of the formation, remembering only how painfully bright the officer's hair looked under the lamps.

Now that brightness lay buried in ash.

The Scale-Kin woman was harder to move.

Not because she was heavy, but because she held the preservation canister so tightly. Lo'an tried to pull it free, but her rigid fingers would not release. Sern looked once and said, “Do not take her thing.”

“We need to move her.”

“Then move both.”

Lo'an did.

Green light glowed faintly from the cracked canister, like something not fully dead. The Scale-Kin's scales were not rough like a lizard's, but fine, cold, and hard, with metallic edges. Around her neck hung a small black tag. No name. Only a cycle number.

Lo'an recognized such numbers.

Long vault.

The Scale-Kin did not believe in brief victory. They preserved genes, embryos, and the next chance after failure. To them, war was not the work of one generation. It could be dragged underground, into sleep, into long cycles.

The Chitinous bodies in the corner were the lightest and the hardest to touch.

They looked insectile, but were clearly not insects. Their exoskeletons were dark brown, their chests fitted with tactical nodes, their closed compound eyes like cracked black mirrors. When Lo'an lifted one, the other's limbs suddenly moved.

Everyone in the shelter froze.

The Chitinous had not revived. Some residual instruction raised its forelimb and touched the tactical node on its companion's chest. A tiny motion, like checking whether connection remained.

Then it went still.

Charlie, meaning me, became a little less afraid of them in that moment.

If an individual of a collective mind still tried after death to confirm a companion, did they truly have no feeling? Or did we simply not understand the way they expressed it?

An Abyssal survivor stood and helped move one of his own dead.

The dead Abyssal warrior lay near the door, gill-slits cracked dry, skin faded from blue-gray to almost white. The survivor knelt beside him and used the last water in a pouch to wipe the dead one's brow. When the water touched skin, it made a very low sound.

Not a drip.

A song.

No one in the shelter spoke.

The sound was brief, but it reminded me of the whale's low frequency before falling. Different, though. The whale had sounded like planetary bones being pulled. This sounded like the sea, far away, remembering a name.

A memory from Lo'an told me: Abyssals gave their dead to water. If there was no water, they gave them to sound.

Last came the young Wing-Shiver.

He was alive, but missing half a wing and one leg. When Sern came near, the youngling opened his eyes, their silver-blue already clouding. He sent something with a faint wing vibration.

Sern's face changed.

Lo'an could not catch all of it, only several frequencies:

Upper passage.  
Still survivors.  
Do not let the Sunbright take the seed.

Seed.

The word dropped like a small stone into my consciousness.

Lo'an heard it too, but did not know its meaning. Sern clearly knew something, but did not explain. He only placed the youngling's hand back on his chest and whispered, “Received.”

The youngling's wings stopped vibrating.

At last, the maintenance panel was cleared.

Lo'an looked back at the shelter. In twenty minutes, it had become a compressed graveyard of the solar system. Sunbright, Scale-Kin, Chitinous, Abyssal, Wing-Shiver. Peoples who had been killing one another outside were now forced into the same failing box.

Death had mixed them together.

The living had to crawl out through them.

Sern pried open the maintenance panel. Cold wind poured from behind it.

Not fresh air.

Ash leading deeper.

Lo'an tightened his grip on the broken blade and crawled in.

I followed him through the last narrow gap between the remains of five peoples."""
    },
}


def write_pair(key, data, prev_key=None, next_key=None):
    (ZH_MD / f"{key}.md").write_text(data["zh"], encoding="utf-8")
    (EN_MD / f"{key}.md").write_text(data["en"], encoding="utf-8")

    prev_link = f'<a href="{prev_key}.html">上一章</a>' if prev_key else ""
    next_link = f'<a href="{next_key}.html">下一章</a>' if next_key else ""
    nav = f'<nav class="nav"><span>{prev_link}</span><span><a href="../index.html">目录</a></span><span>{next_link}</span></nav>'
    (ZH_HTML / f"{key}.html").write_text(page(data["zh_title"], md_to_html(data["zh"]), nav, "zh-CN"), encoding="utf-8")

    en_prev = f'<a href="{prev_key}.html">Previous</a>' if prev_key else ""
    en_next = f'<a href="{next_key}.html">Next</a>' if next_key else ""
    en_nav = f'<nav class="nav"><span>{en_prev}</span><span><a href="../index_EN.html">Index</a></span><span>{en_next}</span></nav>'
    (EN_HTML / f"{key}.html").write_text(page(data["en_title"], md_to_html(data["en"]), en_nav, "en"), encoding="utf-8")


if __name__ == "__main__":
    keys = list(CHAPTERS.keys())
    all_order = [p.stem for p in sorted(ZH_MD.glob("*.md"))]
    for key in keys:
        idx = all_order.index(key)
        prev_key = all_order[idx - 1] if idx > 0 else None
        next_key = all_order[idx + 1] if idx + 1 < len(all_order) else None
        write_pair(key, CHAPTERS[key], prev_key, next_key)
    print("expanded chapters 04-08")
