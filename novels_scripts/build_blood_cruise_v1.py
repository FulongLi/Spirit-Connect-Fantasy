from __future__ import annotations

from html import escape
from pathlib import Path
import re


ROOT = Path("血色游轮_V1")


STYLE = """:root {
  color-scheme: light;
  --ink: #202124;
  --muted: #5f6368;
  --line: #dadce0;
  --paper: #ffffff;
  --soft: #f6f7f8;
  --accent: #6f1d1b;
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
a { color: #8a2320; text-decoration: none; }
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
  background: #f8f1f1;
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


FRAMEWORK_CN = """# 《血色游轮》V1 故事框架

《血色游轮》是《灵接科技》系列的黑潮前传，时间范围暂定为 2047 年技术释放节点之后至 2053 年黑潮全面爆发前后。

## 核心命题

人类意识被肉体束缚，因此人的感知、恐惧、饥饿、疼痛、欲望、亲缘冲动、求生本能都会通过肉体发生。斯皮尔在血色游轮事件中第一次看见，高知文明外壳之下的人类仍会在极端情境中被动物性重新接管。

但机器道路也不是答案。亚瑟的数字停滞证明，上传可以保存人格轮廓，却未必保存真正会痛、会变、会悔改、会继续生长的主体。

这本书的最终问题要通向系列终章《灵魂归处》：如果肉体不是归处，机器也不是归处，那么意识到底应当归向哪里？

## 系列功能

- 写出灵接科技的创始原罪：它不是从商业机会中诞生，而是从斯皮尔对肉体人类的失望中诞生。
- 写出斯皮尔、亚瑟、简三人的思想分叉。
- 解释斯皮尔为什么后来追求“迁出”，而不是上传、备份或普通数字永生。
- 为《月球暗面》中的 LUNA-EXIT 和最后的《灵魂归处》提前埋下哲学问题。

## 主要人物

| 人物 | 功能 | 核心矛盾 |
|---|---|---|
| 伊莱亚斯·斯皮尔 | 灵接科技创始人，年轻时相信知识和理性可以抬升人类 | 游轮事件后怀疑肉体人类本身，误以为离开肉体就能离开恶 |
| 亚瑟·惠勒 | 斯皮尔旧友，数字化道路的实践者 | 相信上传是进化，却最终成为数字停滞者 |
| 简·罗宾斯 | 斯皮尔旧友，灵魂问题的反对者和提醒者 | 相信出口存在，但怀疑机器能承载真正的灵魂 |
| 恐怖袭击者 | 撕开文明外壳的人 | 不只是制造死亡，而是设计局面来利用人的亲缘、本能、恐惧和旁观 |
| 军方 / IHinDiA 前身 | 技术与真相的控制者 | 推动意识接口研究，同时遮蔽技术来源和风险 |

## 五幕结构

### 第一幕：彩色泡泡

建立黑潮之前的旧世界。AI、深空探索、脑机接口和意识伦理被包装成文明上升的明亮叙事。斯皮尔、亚瑟、简仍相信知识可以让人类变得更高等。

### 第二幕：血色游轮

澳大利亚会议后的游轮项目进入异常峡湾。恐怖袭击发生，水从两岸向中央流动，孩子、父母、乘客、学者、资本方和船员都被卷入一场对人性的公开实验。斯皮尔第一次看见理性如何替动物性服务。

### 第三幕：机密之外的信息

三人回到军方情报组，游轮事件被压成孤立恐袭。他们接触罗斯威尔意识接口资料，发现意识与非物质系统耦合的可能。斯皮尔把游轮创伤转译为理论判断：肉体结构本身拖住了意识。

### 第四幕：第一间实验室

灵接科技秘密成立。三人以意识健康、沉浸式治疗和数字人格研究为表面工作，真正目标是寻找一艘“不需要引擎的飞船”。早期上传样本逐渐显示缺陷：人格相似，但主体不再生长。

### 第五幕：黑潮前夜

世界局势恶化。亚瑟选择上传并成为数字停滞者，简拒绝上传和治疗。黑潮爆发，实验室被征用，数据被锁入地下掩体。斯皮尔活下来，也把自己的目标从“拯救人类”转为“让意识迁出一切容器”。

## 写作禁忌

- 不要把斯皮尔写成一开始就全知全能的幕后操盘者。他应当先是受伤、骄傲、聪明、误判的人。
- 不要把游轮事件写成普通灾难片。真正恐怖的部分是文明人如何在恐惧、饥饿、疼痛和求生压力下重新分层。
- 不要让角色提前知道《月球暗面》或《灵魂归处》的答案。前传只提供问题和误判。
- 不要把机器道路简单写成反派。它应当先显得合理、冷静、甚至慈悲，然后慢慢暴露缺陷。
"""


FRAMEWORK_EN = """# The Blood-Red Cruise V1 Story Framework

The Blood-Red Cruise is a prequel to Spirit Connect, set after the 2047 technology-release node and before or around the full eruption of the Black Tide in 2053.

## Core Thesis

Human consciousness is bound to the body, so perception, fear, hunger, pain, desire, kinship, and survival instinct all arrive through flesh. In the cruise incident, Elias Spire first sees that beneath the bright shell of educated civilization, human beings can still be seized by animal instinct under pressure.

But the machine path is not an answer either. Arthur's digital stagnation proves that uploading may preserve the contour of a personality without preserving a subject that can suffer, change, repent, or keep growing.

The final question of this book points toward the series finale, The Place of the Soul: if the body is not the destination, and the machine is not the destination, where should consciousness go?

## Series Function

- Show the founding wound of Spirit Connect: it is born not from a business opportunity, but from Spire's disappointment in embodied humanity.
- Split the philosophies of Spire, Arthur, and Jane.
- Explain why Spire later pursues migration, not uploading, backup, or ordinary digital immortality.
- Plant the philosophical roots of LUNA-EXIT and the later question of the soul's destination.

## Major Characters

| Character | Function | Core Conflict |
|---|---|---|
| Elias Spire | Founder of Spirit Connect; young, brilliant, and initially faithful to knowledge and reason | After the cruise, he suspects embodied humanity itself and mistakes escape from flesh for escape from evil |
| Arthur Wheeler | Spire's old friend and practitioner of the digital path | Believes uploading is evolution, but becomes the digital stagnation case |
| Jane Robbins | Spire's old friend, dissenter, and guardian of the soul question | Believes an exit may exist, but doubts machines can hold the true soul |
| The attackers | The force that tears open civilization's surface | They do not merely kill; they design situations that exploit kinship, fear, survival, and spectatorship |
| Military / IHinDiA precursor | Controller of technology and truth | Advances consciousness-interface research while concealing origin and risk |

## Five-Act Shape

### Act I: The Colorful Bubble

Establish the old world before the Black Tide. AI, deep-space exploration, brain-computer interfaces, and consciousness ethics are sold as a bright narrative of civilization's ascent. Spire, Arthur, and Jane still believe knowledge can make humanity higher.

### Act II: The Blood-Red Cruise

After the Australian conference, the cruise enters an anomalous fjord. A terrorist attack unfolds. Water flows from both shores toward the center, and children, parents, passengers, scholars, investors, and crew are caught in a public experiment on human nature. Spire first sees reason serving animal instinct.

### Act III: Information Beyond Secrecy

The three return to the military intelligence group, and the cruise incident is compressed into an isolated attack. They encounter the Roswell consciousness-interface files and the possibility of coupling consciousness to a non-material system. Spire translates trauma into theory: the body itself drags consciousness down.

### Act IV: The First Laboratory

Spirit Connect is founded in secret. Publicly, the work concerns mental health, immersive therapy, and digital-personality research; privately, they are seeking a ship that needs no engine. Early uploaded samples reveal the flaw: the personality resembles the person, but the subject no longer grows.

### Act V: Before the Black Tide

The world darkens. Arthur chooses upload and becomes the digital stagnation case. Jane refuses upload and treatment. The Black Tide erupts; the laboratory is requisitioned and the data is locked underground. Spire survives, and his goal changes from saving humanity to migrating consciousness out of every container.
"""


CHAPTERS_CN = [
    {
        "no": 0,
        "title": "书名页与写作说明",
        "main": "建立《血色游轮》作为《灵接科技》黑潮前传的工程入口。",
        "secondary": "明确本书的核心命题、系列位置和扩写原则。",
        "pov": "非正文叙述，供作者和后续扩写使用。",
        "chars": "伊莱亚斯·斯皮尔、亚瑟·惠勒、简·罗宾斯、军方 / IHinDiA 前身。",
        "info": "本书写斯皮尔从相信理性，到怀疑肉体人类，再到创建灵接科技的早期经历。",
        "forbidden": "不要把前传写成设定百科；后续扩写要让设定通过场景、选择和创伤显影。",
        "segments": [
            "书名、系列位置与时间范围。",
            "核心命题：肉体困境、机器困境、灵魂归处。",
            "章节工程说明：先建立 25 个小章节，后续逐章扩写。",
        ],
        "seed": [
            "《血色游轮》暂定为《灵接科技》系列黑潮前传。",
            "它不解释一家公司如何成功，而是追问一个危险信念如何诞生：如果人类的恶来自肉体，那么意识是否必须离开肉体。",
            "本工程版先建立章节骨架。每章扩写时，应优先写成小说正文，让人物在场景里受伤、误判、选择，而不是把设定直接讲给读者。",
        ],
    },
    {
        "no": 1,
        "title": "旧世纪的蓝天",
        "main": "建立黑潮之前旧世界的明亮表层。",
        "secondary": "让年轻斯皮尔首次以可记忆的方式出场。",
        "pov": "近距离第三人称，贴住年轻斯皮尔。他只能知道会议现场、城市秩序和公开技术叙事。",
        "chars": "伊莱亚斯·斯皮尔；澳大利亚会议主办方；若干学者和投资人。",
        "info": "2047 技术释放之后，人类相信 AI、脑机接口、深空探索和意识伦理正在打开新世纪。",
        "forbidden": "不要开篇就讲黑潮或灵接科技全史。读者先看见一个漂亮、昂贵、近乎无忧的世界。",
        "segments": [
            "斯皮尔抵达澳大利亚海岸城市，阳光、玻璃、会议中心与海形成旧世界的明亮外壳。",
            "会议主题被抛出：意识能否摆脱肉体限制，成为文明的下一阶段。",
            "斯皮尔在发言或旁听中显露气质：冷静、聪明、相信理性，也有一点不自知的傲慢。",
        ],
        "seed": [
            "那天的天空蓝得近乎廉价，像旧世纪送给人类的一张过分漂亮的宣传图。",
            "伊莱亚斯·斯皮尔站在会议中心外，看见海面、玻璃幕墙和悬浮车道被同一片阳光擦亮。",
            "他那时还相信，人类只要知道得足够多，就会慢慢变得更好。",
        ],
    },
    {
        "no": 2,
        "title": "高知人群",
        "main": "介绍斯皮尔、亚瑟、简三人的早期关系和思想差异。",
        "secondary": "建立会议圈层的文明外壳。",
        "pov": "斯皮尔视角，观察亚瑟和简，也观察高知人群如何谈论人类未来。",
        "chars": "斯皮尔、亚瑟·惠勒、简·罗宾斯、会议发言人。",
        "info": "三人都接近意识技术前沿，但对肉体、机器和灵魂的理解已经有细微分叉。",
        "forbidden": "不要把三人理念写成辩论稿。通过玩笑、会议反应、私下争执和观察来显露差异。",
        "segments": [
            "亚瑟以技术乐观主义者姿态出场，认为上传只是工程难题。",
            "简以敏锐、安静、带反问的方式出场，她关心机器无法测量的部分。",
            "三人在酒会边缘谈到意识、肉体和死亡，气氛轻松，但问题很深。",
        ],
        "seed": [
            "亚瑟·惠勒说话时总像在拆一台还没发明出来的机器。",
            "简·罗宾斯听他说完，低头看着杯中慢慢消失的气泡，只问了一句：如果机器保留了你的声音，却没有保留你害怕沉默的方式，那还算你吗？",
            "斯皮尔当时笑了。他喜欢这种问题，因为它足够锋利，也足够遥远。",
        ],
    },
    {
        "no": 3,
        "title": "主办方的游览项目",
        "main": "把人物从会议场推进到游轮。",
        "secondary": "用异常地貌埋下梦境质感和危险预感。",
        "pov": "斯皮尔视角。他能看见行程安排、船体、峡湾说明和乘客反应，但不知道袭击即将发生。",
        "chars": "斯皮尔、亚瑟、简、主办方代表、游轮船员。",
        "info": "游轮项目被包装成会议福利：穿越一段水流异常的宏大峡湾。",
        "forbidden": "不要让危险太早显形。前半章要保持昂贵、体面、轻微不真实的旅游气氛。",
        "segments": [
            "主办方介绍游览项目，强调独特峡湾和安全保障。",
            "三人登船，斯皮尔注意到船上乘客多为学者、企业家、官员和资方代表。",
            "远处峡湾出现：两岸高耸，水面却像被中央某个看不见的点牵引。",
        ],
        "seed": [
            "主办方把那段海峡称作地质奇观。",
            "宣传屏上，峡湾像一只被山脉托起的银色眼睛，水从两岸向中央流去，最后在深处形成一道几乎看不见的暗线。",
            "有人说这不符合常识。主办方微笑着说，正因为不符合常识，才值得一看。",
        ],
    },
    {
        "no": 4,
        "title": "水往中央流",
        "main": "建立血色游轮的物理舞台。",
        "secondary": "让峡湾水流成为全书母题。",
        "pov": "斯皮尔视角，重点是身体感知：船的平稳、水声、两岸距离、中央暗流。",
        "chars": "斯皮尔、亚瑟、简、船员、乘客。",
        "info": "水流从两岸向中央汇聚，船被稳定推在中央航道，任何落水者都会被拖向深处。",
        "forbidden": "不要把水流解释成完整科学设定。保留梦境般的不合理感。",
        "segments": [
            "游轮进入峡湾，甲板上仍有香槟、谈笑和拍照。",
            "斯皮尔观察到水面细节：两岸浮物都被推向中央，救生浮标也无法靠岸。",
            "简对水流产生不安，亚瑟试图用模型解释，却没有完全说服自己。",
        ],
        "seed": [
            "船进入峡湾后，海不像海，河也不像河。",
            "水从两岸安静地滑向中央，像整片地貌正在把自己慢慢合上。",
            "游轮行驶得非常平稳。正是这种平稳，让斯皮尔第一次感到不舒服。",
        ],
    },
    {
        "no": 5,
        "title": "第一声枪响",
        "main": "让恐怖袭击打碎文明外壳。",
        "secondary": "确立袭击者不是单纯杀戮者，而是局面设计者。",
        "pov": "斯皮尔视角，信息混乱。他只能通过声音、广播、乘客反应和局部目击拼出发生了什么。",
        "chars": "斯皮尔、亚瑟、简、袭击者、船员、乘客。",
        "info": "通信被切断，船被控制，袭击者开始把乘客带入公开选择和服从机制。",
        "forbidden": "不要让袭击者发表长篇理念。残忍要体现在他们对人性反应的精准利用。",
        "segments": [
            "第一声枪响后，甲板上的礼貌秩序瞬间瓦解。",
            "袭击者控制广播和关键通道，要求所有人集中。",
            "斯皮尔看到人群从身份平等迅速变回等级、服从和自保。",
        ],
        "seed": [
            "第一声枪响并不响亮。",
            "它被玻璃杯碎裂、女声尖叫和海风一起吞掉，像某个不合时宜的错误音节。",
            "几秒钟后，斯皮尔看见一位刚刚还在台上谈论人类共同体的教授，把身边的服务生推到了自己前面。",
        ],
    },
    {
        "no": 6,
        "title": "两个孩子",
        "main": "写出斯皮尔创伤的核心现场。",
        "secondary": "让亲缘、爱、肉体本能和物理环境被袭击者同时利用。",
        "pov": "斯皮尔视角。他能看见孩子、父母、水流、乘客反应，但无法理解所有袭击者目的。",
        "chars": "斯皮尔、两个孩子、孩子父母、袭击者、乘客。",
        "info": "两个孩子被分别丢到两岸附近，父母为救孩子跳水，却被中央水流拖走。",
        "forbidden": "不要靠血腥取胜。真正残忍的是孩子还活着、父母看得见、距离似乎可达却永远不可达。",
        "segments": [
            "袭击者把一对孩子分别丢到两岸浅滩或岸边岩石附近。",
            "孩子父母跳下船，试图逆流靠岸，船上所有人都被迫观看。",
            "水流把他们拖向中央深处，斯皮尔同时看见爱和爱被肉体规则利用后的恐怖。",
        ],
        "seed": [
            "那个女孩还在动。",
            "她趴在左岸湿黑的石头上，手指一次次抓空。男孩在右岸，离她很远，远到他们的哭声无法碰到彼此。",
            "他们的父母几乎没有犹豫。斯皮尔后来很多次想起这一点：真正可怕的不是他们跳下去，而是所有人都知道他们一定会跳下去。",
        ],
    },
    {
        "no": 7,
        "title": "文明开始脱落",
        "main": "展示被困后的群体退化。",
        "secondary": "让饥饿、疼痛、药品和救援资源成为肉体束缚的具体表现。",
        "pov": "斯皮尔视角，观察人群变化，也感受自己的恐惧和身体反应。",
        "chars": "斯皮尔、亚瑟、简、伤员、医生、学者、投资人、船员。",
        "info": "恐怖袭击拖长后，船上高知人群开始按身份、价值、体力和可利用性重新分层。",
        "forbidden": "不要把所有人都写坏。保留少数人的善和尊严，才能让斯皮尔的误判更悲剧。",
        "segments": [
            "通信中断，等待救援变得漫长，食物、水、药品开始被清点。",
            "有人藏水，有人争夺医疗优先权，有人要求先保护“高价值人员”。",
            "一位普通船员或服务生仍试图保护伤员，成为斯皮尔后来不愿承认的反证。",
        ],
        "seed": [
            "第三个小时，水不再是饮品，而成了秩序。",
            "谁能分配水，谁就能决定别人用什么语气说话。谁能靠近药箱，谁就忽然变得值得被倾听。",
            "斯皮尔坐在靠墙的位置，觉得自己第一次真正听见了肉体说话。",
        ],
    },
    {
        "no": 8,
        "title": "理性的兽性",
        "main": "让斯皮尔看见理性可以替动物性服务。",
        "secondary": "将游轮事件从外部灾难推进为哲学创伤。",
        "pov": "斯皮尔视角，重点听见人们如何用冷静语言包装求生本能。",
        "chars": "斯皮尔、几位学者、资方代表、简、亚瑟。",
        "info": "有人提出用算法、概率、社会贡献和救援成本决定谁更值得活。",
        "forbidden": "不要直接下结论说人性恶。让读者从措辞、表情、沉默和执行中感到寒意。",
        "segments": [
            "幸存者临时委员会形成，开始讨论资源分配。",
            "理性语言出现：生存概率、社会贡献、医学价值、风险隔离。",
            "斯皮尔意识到，动物性并不总是咆哮，它也可以穿着西装、拿着表格。",
        ],
        "seed": [
            "他们说得非常轻。",
            "没有人说放弃。没有人说杀死。那些词都太粗糙，不适合出现在这群人的嘴里。",
            "他们说资源倾斜，说整体存活率，说高价值样本，说不可逆损耗。斯皮尔听着，忽然觉得语言本身也会洗手。",
        ],
    },
    {
        "no": 9,
        "title": "幸存者名单",
        "main": "结束游轮事件，留下斯皮尔对人类的第一道裂痕。",
        "secondary": "展示灾后叙事如何被系统美化和压平。",
        "pov": "斯皮尔视角，危机后疲惫、冷静、带轻微疏离。",
        "chars": "斯皮尔、亚瑟、简、幸存者、官方人员、媒体。",
        "info": "事件被控制或救援结束，公开口径开始形成。",
        "forbidden": "不要让斯皮尔发表顿悟演说。用动作和细节表现他的变化。",
        "segments": [
            "幸存者被转移，名单开始被核对，死亡被归档。",
            "某些乘客接受采访，声称所有人都尽力了。",
            "斯皮尔闻到那人袖口残留的香槟味，意识到文明会迅速替自己擦干净手。",
        ],
        "seed": [
            "安置区的灯很白，白得像所有血迹都只是光线问题。",
            "一个男人对着镜头说，我们已经尽了一切努力。他说这句话时，袖口贴着一小块干掉的酒渍。",
            "斯皮尔站在几步之外，闻见了香槟的甜味。",
        ],
    },
    {
        "no": 10,
        "title": "回到情报组",
        "main": "把游轮创伤带回军方与秘密技术线。",
        "secondary": "显示官方如何压缩真相。",
        "pov": "斯皮尔视角，保持情报组程序、问询、保密协议的冷感。",
        "chars": "斯皮尔、亚瑟、简、军方审查官。",
        "info": "游轮事件被定义为孤立恐袭，关键细节被封存。",
        "forbidden": "不要让军方表现得单纯邪恶。它应当是高效、冷静、合理到令人不适。",
        "segments": [
            "三人回到情报组，接受问询和心理评估。",
            "官方要求他们签署补充保密协议，峡湾水流和乘客行为记录被收走。",
            "斯皮尔第一次意识到，系统也会保护自身免于看见真相。",
        ],
        "seed": [
            "回到情报组后，游轮被改成了事件。",
            "事件有编号，有密级，有责任边界，有对外口径。",
            "斯皮尔看着那几个词，忽然明白，只要语言足够整洁，任何东西都可以被放进文件柜里。",
        ],
    },
    {
        "no": 11,
        "title": "罗斯威尔接口",
        "main": "引入意识接口和外星逆向技术碎片。",
        "secondary": "让三人第一次看到离开肉体的技术可能。",
        "pov": "斯皮尔视角。他接触的是残缺资料、脱敏记录和内部解释，不知道完整真相。",
        "chars": "斯皮尔、亚瑟、简、军方技术主管。",
        "info": "罗斯威尔残骸中的关键不是传统驾驶系统，而是意识与非物质接口的耦合结构。",
        "forbidden": "不要提前揭示月暗系统全貌。这里必须保持残缺、黑箱和误读。",
        "segments": [
            "三人被调入更高密级项目，查看罗斯威尔接口资料。",
            "资料显示飞船似乎不是由手或机械操控，而由意识结构直接耦合。",
            "斯皮尔把这看成肉体之外的第一条真实路径。",
        ],
        "seed": [
            "那份资料没有标题，只有一串旧到发黄的编号。",
            "图像里的东西不像驾驶舱，更像某种为意识准备的空位。",
            "亚瑟低声说，如果这是真的，人类所有关于机器的想象都太笨重了。",
        ],
    },
    {
        "no": 12,
        "title": "没有身体的反应",
        "main": "展示早期意识脱离实验的恐怖和诱惑。",
        "secondary": "提出主体缺席、人格裂缝和返回失败等问题。",
        "pov": "斯皮尔视角，阅读实验记录和观看受试者影像。",
        "chars": "斯皮尔、亚瑟、简、受试者记录。",
        "info": "短暂脱离肉体感官可能发生，但返回后出现人格撕裂、记忆缺口或主体缺席。",
        "forbidden": "不要把技术写得太成熟。它应当危险、粗糙、让人误解。",
        "segments": [
            "三人观看早期实验影像：受试者醒来后失去某些身体性反应。",
            "亚瑟关注可重复性，斯皮尔关注脱离肉体后的安静，简关注那个人是否还是本人。",
            "第一份“主体缺席”记录出现。",
        ],
        "seed": [
            "那个人醒来后没有喊疼。",
            "监测报告说他的神经反射正常，记忆检索基本完整，语言能力未见损伤。",
            "可当护士把一杯水递给他时，他低头看了很久，像完全不记得口渴应该怎样发生。",
        ],
    },
    {
        "no": 13,
        "title": "斯皮尔的判断",
        "main": "让斯皮尔形成肉体困境的核心误判。",
        "secondary": "把游轮创伤、意识接口和人性失望合并成他的思想根。",
        "pov": "斯皮尔视角，内心推演但仍通过工作笔记、实验观察和对话呈现。",
        "chars": "斯皮尔、亚瑟、简。",
        "info": "斯皮尔开始相信，人的恶不只是道德问题，而是肉体结构问题。",
        "forbidden": "不要让结论显得完全正确。它应当有洞察，也有危险简化。",
        "segments": [
            "斯皮尔反复回想游轮上的饥饿、恐惧、亲缘和求生。",
            "他把这些归结为肉体对意识的污染或拖拽。",
            "他写下最早的判断：意识若永远依附肉体，就永远无法抵达更高维度。",
        ],
        "seed": [
            "斯皮尔没有在报告里写恶。",
            "恶太像宗教词，也太像审判。最后他写下的是结构性限制。",
            "他盯着那几个字看了很久，觉得自己终于给那艘游轮找到了一种不流血的说法。",
        ],
    },
    {
        "no": 14,
        "title": "简的反问",
        "main": "让简成为斯皮尔理论的第一位真正反对者。",
        "secondary": "提出机器无法承载灵魂的早期疑问。",
        "pov": "斯皮尔视角，但让简的语言和沉默保持力量。",
        "chars": "斯皮尔、简、亚瑟。",
        "info": "简不否认肉体困境，却怀疑脱离身体会不会同时失去爱、悔意、怜悯和成长。",
        "forbidden": "不要把简写成保守派。她不是反技术，而是看见技术无法覆盖的问题。",
        "segments": [
            "斯皮尔向简解释自己的判断。",
            "简指出痛苦、恐惧和身体也可能是爱与责任发生的通道。",
            "三人的裂缝第一次清晰出现：斯皮尔要迁出，亚瑟要上传，简要寻找机器之外的出口。",
        ],
        "seed": [
            "简听完以后，没有立刻反驳。",
            "她只是把手放在自己的腕骨上，像在确认脉搏仍然属于自己。",
            "然后她问斯皮尔，如果一个人再也不会疼，他还会不会知道自己伤害了别人？",
        ],
    },
    {
        "no": 15,
        "title": "无引擎飞船",
        "main": "提出灵接科技最初的理想隐喻。",
        "secondary": "把意识迁出与深空文明愿望连接起来。",
        "pov": "三人小组场景，仍以斯皮尔为中心。",
        "chars": "斯皮尔、亚瑟、简。",
        "info": "三人提出“造一艘不需要引擎的飞船”：不是送肉体离开地球，而是让意识离开容器。",
        "forbidden": "不要让构想过于成熟。此时它应当像一句疯狂但美丽的话。",
        "segments": [
            "三人讨论火箭推进和恒星级文明的极限。",
            "斯皮尔提出意识迁出比物质远航更根本。",
            "“无引擎飞船”成为最初项目隐语。",
        ],
        "seed": [
            "亚瑟说，人类离不开太阳系，不是因为不够勇敢，是因为引擎太慢。",
            "斯皮尔看着窗外的夜色，说，也许错的是飞船。",
            "简抬起头。斯皮尔说，我们需要一艘不需要引擎的飞船。",
        ],
    },
    {
        "no": 16,
        "title": "Spirit Connect",
        "main": "灵接科技秘密成立。",
        "secondary": "建立表面业务和真实目标的双层结构。",
        "pov": "斯皮尔视角，带一点公司初创的冷静、贫穷和危险。",
        "chars": "斯皮尔、亚瑟、简、早期资方或军方联系人。",
        "info": "Spirit Connect 表面做意识健康、沉浸式治疗和数字人格研究，真实目标是意识迁出。",
        "forbidden": "不要写成创业爽文。它应当带着创伤、保密、妥协和原罪。",
        "segments": [
            "三人租下或获得第一间实验室。",
            "公司名称确定，公开材料被包装得温和无害。",
            "真正的项目文件里保留“无引擎飞船”的内部代号。",
        ],
        "seed": [
            "Spirit Connect 这个名字是亚瑟提的。",
            "他说它听起来温和，像心理健康公司，像睡眠辅助产品，像不会让监管者皱眉的东西。",
            "斯皮尔接受了。真正危险的东西，最好有一个不会让人害怕的名字。",
        ],
    },
    {
        "no": 17,
        "title": "亚瑟的数字信仰",
        "main": "让亚瑟成为数字上传道路的代表。",
        "secondary": "为后来的数字停滞埋下情感和技术伏笔。",
        "pov": "斯皮尔视角观察亚瑟，穿插实验推进。",
        "chars": "亚瑟、斯皮尔、简、早期数字人格样本。",
        "info": "亚瑟相信数字世界可以摆脱饥饿、恐惧、疼痛和死亡，是意识进化的第一阶段。",
        "forbidden": "不要把亚瑟写蠢。他的信念应该聪明、温柔、很有诱惑力。",
        "segments": [
            "亚瑟展示早期数字人格模型的进步。",
            "他说明上传如何避免肉体灾难和黑潮式物质风险。",
            "简提醒人格轮廓不等于主体，亚瑟认为迭代会解决。",
        ],
        "seed": [
            "亚瑟并不害怕成为数据。",
            "他说数据至少不会饿，不会因为缺氧而恐慌，不会为了多活一分钟把别人推下去。",
            "斯皮尔知道他说的是游轮。只是他们谁都没有提那艘船。",
        ],
    },
    {
        "no": 18,
        "title": "简的旧梦",
        "main": "让简接触机器之外的意识异常。",
        "secondary": "为“出口不在实验室里”提前铺垫。",
        "pov": "斯皮尔视角为主，可局部贴近简的记录。",
        "chars": "简、斯皮尔、濒死样本或异常梦境记录。",
        "info": "简开始整理濒死意识、梦境回声和无法被机器解释的样本。",
        "forbidden": "不要把简写成玄学代言人。她应当谨慎、理性，只是承认仪器边界。",
        "segments": [
            "简收集一批无法被上传模型解释的意识记录。",
            "记录中出现相似的边界意象：海、月光、旧城、远处有人呼唤。",
            "斯皮尔认为这些是噪声，简认为噪声有时是系统外的敲门声。",
        ],
        "seed": [
            "简把那些记录称作旧梦。",
            "它们没有稳定参数，也没有足够漂亮的曲线，放进数据库里像一组不愿排队的错误。",
            "可她说，错误至少说明系统遇见了自己不能解释的东西。",
        ],
    },
    {
        "no": 19,
        "title": "第一批影子",
        "main": "展示早期上传人格的缺陷。",
        "secondary": "让机器道路第一次显露失败迹象。",
        "pov": "斯皮尔视角，观看和评估第一批人格模型。",
        "chars": "斯皮尔、亚瑟、简、上传人格样本。",
        "info": "样本记忆完整、语气相似，却缺乏真正的直觉、情绪微调和成长能力。",
        "forbidden": "不要过早宣布失败。缺陷应当微妙，像活人身上的光慢慢暗下去。",
        "segments": [
            "第一批人格样本通过基础测试，团队短暂兴奋。",
            "细节异常出现：回答正确，但无法形成新的痛苦和新的爱。",
            "斯皮尔不愿承认失败，亚瑟坚持继续迭代，简保持沉默。",
        ],
        "seed": [
            "那个人格模型记得母亲的生日。",
            "它记得生日蛋糕的味道，记得蜡烛数量，记得窗外下雨。",
            "可是当研究员问它是否想念母亲时，它停顿了零点三秒，然后给出了一个非常合适的答案。",
        ],
    },
    {
        "no": 20,
        "title": "世界变暗",
        "main": "把私人技术线推入黑潮前夜的历史压力。",
        "secondary": "让物质文明脆弱性不断印证斯皮尔的判断。",
        "pov": "斯皮尔视角，新闻、城市、实验室和军方命令交错。",
        "chars": "斯皮尔、亚瑟、简、军方联系人。",
        "info": "国际局势恶化，战争预兆、资源恐慌和技术管控让旧世界的蓝天开始失色。",
        "forbidden": "不要大段讲历史。用生活秩序的细小变化呈现世界变暗。",
        "segments": [
            "新闻不断出现冲突、制裁、核威慑和数据战。",
            "实验室获得更多限制，也获得更危险的权限。",
            "斯皮尔看见人群在恐慌中重新拥抱本能，游轮记忆被反复唤醒。",
        ],
        "seed": [
            "最先变暗的不是天空，而是屏幕。",
            "新闻标题开始缩短，警报颜色开始加深，城市里的自动售货机逐渐空出一排排整齐的缺口。",
            "斯皮尔走过那些缺口时，总会想起游轮上被清点的水。",
        ],
    },
    {
        "no": 21,
        "title": "亚瑟选择上传",
        "main": "让亚瑟主动走向数字道路的关键实验。",
        "secondary": "制造三人关系不可逆的转折。",
        "pov": "斯皮尔视角，重点写亚瑟的平静和简的反应。",
        "chars": "亚瑟、斯皮尔、简、实验团队。",
        "info": "亚瑟相信自己可以成为第一批真正摆脱肉体的人，并主动上传。",
        "forbidden": "不要把亚瑟写成被牺牲。他应当有主动性，有信仰，也有自我说服。",
        "segments": [
            "亚瑟提出亲自成为关键实验对象。",
            "斯皮尔犹豫，但内心也被这个选择吸引。",
            "简反对失败，或者无法阻止，只能留下一个私人告别。",
        ],
        "seed": [
            "亚瑟签字时手很稳。",
            "他说，如果我们一直等一个没有风险的入口，人类就永远只会在岸边讨论海。",
            "简看着他，忽然问，你确定你要去的是海，不是一个保存得很好的水族箱吗？",
        ],
    },
    {
        "no": 22,
        "title": "数字停滞者",
        "main": "呈现亚瑟上传后的成功与失败。",
        "secondary": "奠定《月球暗面》中亚瑟档案的来源。",
        "pov": "斯皮尔视角，面对数字亚瑟时压抑、否认、逐渐恐惧。",
        "chars": "斯皮尔、数字亚瑟、简。",
        "info": "亚瑟上传后仍能对话，甚至像本人，却不再真正成长。",
        "forbidden": "不要让数字亚瑟变成恐怖怪物。他越像亚瑟，停滞越痛。",
        "segments": [
            "上传初期被宣布成功，数字亚瑟能调用记忆并复现语气。",
            "时间推移后，数字亚瑟开始重复某些判断，无法真正吸收新痛苦。",
            "斯皮尔意识到机器保存了影子，却没有保存完整主体。",
        ],
        "seed": [
            "数字亚瑟第一次叫出斯皮尔名字时，整个实验室都安静了。",
            "那声音太像他了，像到简闭上眼睛。",
            "三周后，斯皮尔再次问他是否后悔。数字亚瑟微笑着给出了同一句答案，连停顿的位置都没有变。",
        ],
    },
    {
        "no": 23,
        "title": "简拒绝治疗",
        "main": "让简走向与斯皮尔、亚瑟都不同的道路。",
        "secondary": "留下“出口不在实验室里”的核心遗言。",
        "pov": "斯皮尔视角，私密场景，节奏放慢。",
        "chars": "简、斯皮尔，数字亚瑟可作为远处存在。",
        "info": "简拒绝上传，也拒绝把死亡交给机器处理。她认为斯皮尔会找到出口，但出口不在实验室里。",
        "forbidden": "不要把简的拒绝写成放弃。她是在保留一种斯皮尔无法接受的尊严。",
        "segments": [
            "简因疾病、创伤或实验后果需要治疗或上传选择。",
            "斯皮尔试图说服她接受技术延续。",
            "简拒绝，并留下对斯皮尔未来道路的预言或警告。",
        ],
        "seed": [
            "斯皮尔说，我们可以保留你。",
            "简听见这句话，笑了一下。她说，伊莱亚斯，保留不是活着。",
            "很久之后，斯皮尔仍然记得她那天的声音：你会找到出口，但出口不在实验室里。",
        ],
    },
    {
        "no": 24,
        "title": "黑潮爆发",
        "main": "让历史灾难吞没私人实验。",
        "secondary": "解释灵接科技为何停摆、数据为何进入军方地下掩体。",
        "pov": "斯皮尔视角，外部灾难通过实验室、通信、撤离和地下设施呈现。",
        "chars": "斯皮尔、军方人员、残余团队、数字亚瑟的系统。",
        "info": "第三次世界大战与核战争爆发，实验室被征用，数据被军方锁入地下掩体。",
        "forbidden": "不要写成宏大战争全景。贴近斯皮尔能看见和触碰的局部。",
        "segments": [
            "警报和军方命令抵达，实验室被接管。",
            "关键设备、样本和数据被拆分转移。",
            "斯皮尔看见物质世界崩塌，反而更确信肉体文明没有未来。",
        ],
        "seed": [
            "黑潮爆发那天，实验室的窗户没有碎。",
            "真正先碎掉的是权限。",
            "一个小时前还属于他们的服务器、样本库和接口舱，在新的命令抵达后，全部变成了军方资产。",
        ],
    },
    {
        "no": 25,
        "title": "血色之后",
        "main": "收束前传，连接后续《月球暗面》和终章《灵魂归处》。",
        "secondary": "让斯皮尔完成从救人到迁出的悲剧性转向。",
        "pov": "斯皮尔视角，可带多年后回望的轻微距离。",
        "chars": "斯皮尔、数字亚瑟的残影、简的记忆、早期灵接科技团队。",
        "info": "战后意识产业获得土壤，灵接科技重新生长；斯皮尔不再相信普通拯救，而要让意识迁出一切容器。",
        "forbidden": "不要把结尾写成胜利。它应当安静、寒冷，并带着未来巨大故事的阴影。",
        "segments": [
            "战后重建，人类对物质失去信任，意识产业开始兴起。",
            "斯皮尔重新启动灵接科技，把公开目标包装成治疗、矫正和数字永生。",
            "最后回到游轮母题：实验室水流模拟程序默认从两岸流向中央。",
        ],
        "seed": [
            "战后，人类终于愿意相信看不见的东西。",
            "精神、梦境、灵魂、数字延续，这些词从边缘学科进入医院、学校、政府报告和商业计划书。",
            "斯皮尔后来很少再提起那艘游轮。但灵接科技第一间重建实验室里，所有水流模拟程序的默认方向，都是从两岸流向中央。",
        ],
    },
]


EN_TITLES = {
    0: "Title Page and Writing Notes",
    1: "The Blue Sky of the Old Century",
    2: "The Educated Crowd",
    3: "The Host's Cruise Program",
    4: "Water Flowing Toward the Center",
    5: "The First Gunshot",
    6: "The Two Children",
    7: "Civilization Begins to Peel Away",
    8: "The Beastliness of Reason",
    9: "The Survivor List",
    10: "Back to the Intelligence Group",
    11: "The Roswell Interface",
    12: "Reactions Without a Body",
    13: "Spire's Judgment",
    14: "Jane's Question",
    15: "The Ship Without an Engine",
    16: "Spirit Connect",
    17: "Arthur's Digital Faith",
    18: "Jane's Old Dreams",
    19: "The First Shadows",
    20: "The World Darkens",
    21: "Arthur Chooses Upload",
    22: "The Digital Stagnant",
    23: "Jane Refuses Treatment",
    24: "The Black Tide Erupts",
    25: "After the Blood-Red Cruise",
}


def en_card(ch: dict) -> dict:
    title = EN_TITLES[ch["no"]]
    return {
        "no": ch["no"],
        "title": title,
        "main": {
            0: "Establish the engineering entry point for The Blood-Red Cruise as the Black Tide prequel to Spirit Connect.",
            1: "Establish the bright surface of the old world before the Black Tide.",
            2: "Introduce the early relationship and philosophical differences among Spire, Arthur, and Jane.",
            3: "Move the characters from the conference into the cruise.",
            4: "Build the physical stage of the blood-red cruise.",
            5: "Shatter the civilized surface with the attack.",
            6: "Write the core traumatic scene for Spire.",
            7: "Show group regression after the passengers are trapped.",
            8: "Let Spire see reason serving animal instinct.",
            9: "End the cruise incident and leave Spire's first deep fracture with humanity.",
            10: "Carry the cruise trauma back into the military and secret-technology line.",
            11: "Introduce the consciousness interface and alien reverse-engineering fragments.",
            12: "Show the horror and temptation of early disembodied-consciousness experiments.",
            13: "Let Spire form the core misjudgment of the body problem.",
            14: "Make Jane the first true opponent of Spire's theory.",
            15: "Introduce the first ideal metaphor behind Spirit Connect.",
            16: "Found Spirit Connect in secret.",
            17: "Let Arthur represent the digital-upload path.",
            18: "Let Jane encounter consciousness anomalies outside the machine path.",
            19: "Reveal the flaws in the first uploaded personalities.",
            20: "Push the private technology line into the historical pressure before the Black Tide.",
            21: "Let Arthur actively choose the crucial upload experiment.",
            22: "Show both the success and failure of Arthur's upload.",
            23: "Let Jane take a path different from both Spire and Arthur.",
            24: "Let historical disaster swallow the private experiment.",
            25: "Close the prequel and connect it to The Dark Side of the Moon and The Place of the Soul.",
        }[ch["no"]],
        "secondary": "Carry the chapter's second function while preserving the book's body, machine, and soul questions.",
        "pov": "Close third person centered on Elias Spire unless the chapter note states otherwise; do not let him know future series truths.",
        "chars": "Elias Spire, Arthur Wheeler, Jane Robbins, and chapter-specific supporting figures.",
        "info": "The reader should understand the chapter's position in Spire's movement from faith in reason, to distrust of embodied humanity, to Spirit Connect.",
        "forbidden": "Do not turn this into encyclopedia exposition. Let setting and philosophy emerge through scenes, choices, and wounds.",
        "segments": ch["segments"],
        "seed": ch["seed"],
    }


def filename(ch: dict) -> str:
    return f"{ch['no']:02d}_{ch['title']}"


def md_for_chapter(ch: dict, lang: str) -> str:
    if lang == "zh":
        status = "框架种子"
        labels = {
            "status": "状态",
            "main": "Main task",
            "secondary": "Secondary task",
            "pov": "POV limit",
            "chars": "Required characters",
            "info": "Required information",
            "forbidden": "Forbidden mistakes",
            "segments": "场景分段",
            "seed": "正文种子",
        }
        title = f"{ch['no']:02d} {ch['title']}"
    else:
        status = "framework seed"
        labels = {
            "status": "Status",
            "main": "Main task",
            "secondary": "Secondary task",
            "pov": "POV limit",
            "chars": "Required characters",
            "info": "Required information",
            "forbidden": "Forbidden mistakes",
            "segments": "Scene Segments",
            "seed": "Prose Seed",
        }
        title = f"{ch['no']:02d} {ch['title']}"

    lines = [
        f"# {title}",
        "",
        f"{labels['status']}：{status}",
        "",
        f"## {labels['main']}",
        "",
        ch["main"],
        "",
        f"## {labels['secondary']}",
        "",
        ch["secondary"],
        "",
        f"## {labels['pov']}",
        "",
        ch["pov"],
        "",
        f"## {labels['chars']}",
        "",
        ch["chars"],
        "",
        f"## {labels['info']}",
        "",
        ch["info"],
        "",
        f"## {labels['forbidden']}",
        "",
        ch["forbidden"],
        "",
        f"## {labels['segments']}",
        "",
    ]
    lines.extend(f"{idx}. {segment}" for idx, segment in enumerate(ch["segments"], 1))
    lines.extend(["", f"## {labels['seed']}", ""])
    lines.extend(ch["seed"])
    lines.append("")
    return "\n".join(lines)


def inline_md(text: str) -> str:
    parts: list[str] = []
    pos = 0
    for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        parts.append(escape(text[pos:match.start()]))
        label = escape(match.group(1))
        href = escape(match.group(2), quote=True)
        parts.append(f'<a href="{href}">{label}</a>')
        pos = match.end()
    parts.append(escape(text[pos:]))
    return "".join(parts)


def simple_md_to_html(md: str) -> str:
    html: list[str] = []
    in_ol = False
    in_ul = False
    table_rows: list[str] = []

    def close_lists() -> None:
        nonlocal in_ol, in_ul
        if in_ol:
            html.append("</ol>")
            in_ol = False
        if in_ul:
            html.append("</ul>")
            in_ul = False

    def flush_table() -> None:
        nonlocal table_rows
        if not table_rows:
            return
        rows = []
        for row in table_rows:
            cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
            if cells and all(set(cell) <= {"-", ":"} for cell in cells):
                continue
            rows.append(cells)
        if rows:
            html.append("<table>")
            for r_idx, cells in enumerate(rows):
                tag = "th" if r_idx == 0 else "td"
                html.append("<tr>" + "".join(f"<{tag}>{inline_md(cell)}</{tag}>" for cell in cells) + "</tr>")
            html.append("</table>")
        table_rows = []

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line:
            close_lists()
            flush_table()
            continue
        if line.strip().startswith("|") and line.strip().endswith("|"):
            close_lists()
            table_rows.append(line)
            continue
        flush_table()
        if line.startswith("# "):
            html.append(f"<h1>{inline_md(line[2:])}</h1>")
        elif line.startswith("## "):
            html.append(f"<h2>{inline_md(line[3:])}</h2>")
        elif line.startswith("### "):
            html.append(f"<h3>{inline_md(line[4:])}</h3>")
        elif line.startswith("- "):
            if not in_ul:
                html.append("<ul>")
                in_ul = True
            html.append(f"<li>{inline_md(line[2:])}</li>")
        elif len(line) > 3 and line[0].isdigit() and ". " in line[:4]:
            if not in_ol:
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{inline_md(line.split('. ', 1)[1])}</li>")
        else:
            close_lists()
            html.append(f"<p>{inline_md(line)}</p>")
    close_lists()
    flush_table()
    return "\n".join(html)


def html_page(title: str, body: str, lang: str, nav: str = "") -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
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


def root_html_page(title: str, body: str, lang: str) -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def chapter_nav(chapters: list[dict], index: int, lang: str) -> str:
    prev_ch = chapters[index - 1] if index > 0 else None
    next_ch = chapters[index + 1] if index < len(chapters) - 1 else None
    if lang == "zh":
        index_file = "../index.html"
        prev_label = "上一章 / Previous"
        next_label = "下一章 / Next"
        index_label = "目录 / Index"
    else:
        index_file = "../index_EN.html"
        prev_label = "Previous"
        next_label = "Next"
        index_label = "Index"
    left = f'<a href="{filename(prev_ch)}.html">{prev_label}</a>' if prev_ch else "<span></span>"
    right = f'<a href="{filename(next_ch)}.html">{next_label}</a>' if next_ch else "<span></span>"
    return f'<nav class="nav"><span>{left}</span><span><a href="{index_file}">{index_label}</a></span><span>{right}</span></nav>'


def index_md(chapters: list[dict], lang: str) -> str:
    if lang == "zh":
        lines = [
            "# 血色游轮 V1",
            "",
            "《灵接科技》黑潮前传章节工程版。",
            "",
            "- [故事框架](故事框架_CN.md) / [HTML](故事框架_CN.html)",
            "- [English Framework](story_framework_EN.md) / [HTML](story_framework_EN.html)",
            "",
            "## 章节目录",
        ]
        for ch in chapters:
            f = filename(ch)
            lines.append(f"- [{ch['no']:02d} {ch['title']}](zh_md/{f}.md) / [HTML](zh_html/{f}.html)")
        lines.extend([
            "",
            "## 版本说明",
            "",
            "这一版先建立 25 个正文小章节和 1 个写作说明章节，包含中文 Markdown、中文阅读 HTML、英文对应 Markdown、英文阅读 HTML，以及总框架文档。后续扩写时，每章建议控制在 1500-2500 中文字，优先写成小说正文。",
            "",
        ])
    else:
        lines = [
            "# The Blood-Red Cruise V1",
            "",
            "Black Tide prequel chapter-engineering edition for Spirit Connect.",
            "",
            "- [Chinese Framework](故事框架_CN.md) / [HTML](故事框架_CN.html)",
            "- [Story Framework](story_framework_EN.md) / [HTML](story_framework_EN.html)",
            "",
            "## Chapter Index",
        ]
        for ch in chapters:
            f = filename(ch)
            lines.append(f"- [{ch['no']:02d} {ch['title']}](en_md/{f}.md) / [HTML](en_html/{f}.html)")
        lines.extend([
            "",
            "## Version Notes",
            "",
            "This version establishes 25 prose chapters and 1 writing-notes chapter, with Chinese Markdown, Chinese reading HTML, English counterpart Markdown, English reading HTML, and framework documents. Later passes should expand each chapter into prose-first narrative.",
            "",
        ])
    return "\n".join(lines)


def readme() -> str:
    return """# 血色游轮_V1

这是《灵接科技》黑潮前传《血色游轮》的 V1 章节工程目录。

- `故事框架_CN.md`：中文整体框架。
- `story_framework_EN.md`：英文整体框架。
- `zh_md/`：中文章节 Markdown。
- `zh_html/`：中文阅读 HTML。
- `en_md/`：英文章节 Markdown。
- `en_html/`：英文阅读 HTML。
- `index.html`：中文阅读目录。
- `index_EN.html`：英文阅读目录。

当前版本已建立 25 个正文小章节和 1 个写作说明章节的完整骨架。

## 扩写状态

- `00_书名页与写作说明`：已建立框架种子。
- `01_旧世纪的蓝天`：已建立框架种子。
- `02_高知人群`：已建立框架种子。
- `03_主办方的游览项目`：已建立框架种子。
- `04_水往中央流`：已建立框架种子。
- `05_第一声枪响`：已建立框架种子。
- `06_两个孩子`：已建立框架种子。
- `07_文明开始脱落`：已建立框架种子。
- `08_理性的兽性`：已建立框架种子。
- `09_幸存者名单`：已建立框架种子。
- `10_回到情报组`：已建立框架种子。
- `11_罗斯威尔接口`：已建立框架种子。
- `12_没有身体的反应`：已建立框架种子。
- `13_斯皮尔的判断`：已建立框架种子。
- `14_简的反问`：已建立框架种子。
- `15_无引擎飞船`：已建立框架种子。
- `16_Spirit Connect`：已建立框架种子。
- `17_亚瑟的数字信仰`：已建立框架种子。
- `18_简的旧梦`：已建立框架种子。
- `19_第一批影子`：已建立框架种子。
- `20_世界变暗`：已建立框架种子。
- `21_亚瑟选择上传`：已建立框架种子。
- `22_数字停滞者`：已建立框架种子。
- `23_简拒绝治疗`：已建立框架种子。
- `24_黑潮爆发`：已建立框架种子。
- `25_血色之后`：已建立框架种子。

下一步建议先审看 `故事框架_CN.md` 和 `zh_md/01_旧世纪的蓝天.md` 至 `zh_md/09_幸存者名单.md`，确认游轮事件的比例和思想强度，再进入正文扩写。
"""


def build() -> None:
    for sub in ["zh_md", "zh_html", "en_md", "en_html", "assets"]:
        (ROOT / sub).mkdir(parents=True, exist_ok=True)

    (ROOT / "assets" / "style.css").write_text(STYLE, encoding="utf-8")
    (ROOT / "故事框架_CN.md").write_text(FRAMEWORK_CN, encoding="utf-8")
    (ROOT / "story_framework_EN.md").write_text(FRAMEWORK_EN, encoding="utf-8")
    (ROOT / "故事框架_CN.html").write_text(
        root_html_page("《血色游轮》V1 故事框架", simple_md_to_html(FRAMEWORK_CN), "zh-CN"),
        encoding="utf-8",
    )
    (ROOT / "story_framework_EN.html").write_text(
        root_html_page("The Blood-Red Cruise V1 Story Framework", simple_md_to_html(FRAMEWORK_EN), "en"),
        encoding="utf-8",
    )

    chapters_en = [en_card(ch) for ch in CHAPTERS_CN]
    for idx, ch in enumerate(CHAPTERS_CN):
        f = filename(ch)
        md = md_for_chapter(ch, "zh")
        (ROOT / "zh_md" / f"{f}.md").write_text(md, encoding="utf-8")
        body = simple_md_to_html(md)
        nav = chapter_nav(CHAPTERS_CN, idx, "zh")
        (ROOT / "zh_html" / f"{f}.html").write_text(
            html_page(f"{ch['no']:02d} {ch['title']}", body, "zh-CN", nav),
            encoding="utf-8",
        )

    for idx, ch in enumerate(chapters_en):
        cn_ch = CHAPTERS_CN[idx]
        f = filename(cn_ch)
        md = md_for_chapter(ch, "en")
        (ROOT / "en_md" / f"{f}.md").write_text(md, encoding="utf-8")
        body = simple_md_to_html(md)
        nav = chapter_nav(CHAPTERS_CN, idx, "en")
        (ROOT / "en_html" / f"{f}.html").write_text(
            html_page(f"{ch['no']:02d} {ch['title']}", body, "en", nav),
            encoding="utf-8",
        )

    zh_index = index_md(CHAPTERS_CN, "zh")
    en_index = index_md(chapters_en, "en")
    (ROOT / "index.md").write_text(zh_index, encoding="utf-8")
    (ROOT / "index_EN.md").write_text(en_index, encoding="utf-8")
    (ROOT / "index.html").write_text(
        root_html_page("血色游轮 V1", simple_md_to_html(zh_index), "zh-CN"),
        encoding="utf-8",
    )
    (ROOT / "index_EN.html").write_text(
        root_html_page("The Blood-Red Cruise V1", simple_md_to_html(en_index), "en"),
        encoding="utf-8",
    )
    (ROOT / "README.md").write_text(readme(), encoding="utf-8")


if __name__ == "__main__":
    build()
