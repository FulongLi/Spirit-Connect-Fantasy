#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"


STYLE = """:root {
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
  max-width: 900px;
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
    {
        "n": 0,
        "zh": "书名页与写作说明",
        "en": "Title Page and Writing Notes",
        "source": "工程说明",
        "function": "建立《月球暗面》V2 框架工程的使用方式，说明当前文件是结构卡，不是正文重写。",
        "task": "保护 V1 第一、第二章的原声；后续只在三至七章做结构性增强。",
        "notes": ["中文是主创作视图。", "英文是跨对话参考视图。", "HTML 是给作者阅读的入口。"],
        "protect": "不引入旧误改 V2 的二十章正文，不改变当前 V2 正文目录。",
    },
    {
        "n": 1,
        "zh": "作者序",
        "en": "Author's Note",
        "source": "V2/md/01_作者序.md",
        "function": "保留作者对创作动机、宇宙观和系列气质的开场说明。",
        "task": "只做排版和必要错字清理，不改作者自述的温度。",
        "notes": ["让读者知道这不是单本技术设定小说，而是系列入口。", "语气应比正文更接近作者本人。"],
        "protect": "不把作者序改成市场文案或世界观百科。",
    },
    {
        "n": 2,
        "zh": "前言：吉姆的自述",
        "en": "Prologue: Jim's Statement",
        "source": "V2/md/02_前言.md",
        "function": "用吉姆的声音提出真相、沉默、谎言和宇宙叙事的问题。",
        "task": "统一吉姆·维尔的名字，保留哲思感和不稳定的信息噪声。",
        "notes": ["这里应像一道门缝，而不是完整说明书。", "错误代码和乱码感可以保留，作为意识溢出的质地。"],
        "protect": "不提前解释月暗系统、泰拉撒记录或最终选择。",
    },
    {
        "n": 3,
        "zh": "黑水与苏醒",
        "en": "Black Water and Awakening",
        "source": "V2/md/03_第一章_月暗之旅.md",
        "function": "保留第一章原声入口：身体不适、黑水记忆、从矫正事故中醒来。",
        "task": "建立吉姆的第一人称观察方式：怕、恶心、好奇、忍不住分析。",
        "notes": ["这是作者口吻锚点之一。", "可以轻分段，不重写叙述。"],
        "protect": "不把黑水体验改成清晰任务开场。",
    },
    {
        "n": 4,
        "zh": "石门之后的战场",
        "en": "The Battlefield Beyond the Gate",
        "source": "V2/md/03_第一章_月暗之旅.md",
        "function": "让吉姆第一次进入月暗空间，接触石门、古战场和巨鲸/异族战争残影。",
        "task": "强化梦境考古感，保留“看见但不理解”的状态。",
        "notes": ["巨鲸、异族残骸只作为未来《巨鲸陨落》的黑影。", "读者应先被画面击中，而不是先听解释。"],
        "protect": "不解释法厄同终战，不把巨鲸变成明确设定说明。",
    },
    {
        "n": 5,
        "zh": "沙路、稻田与小女孩",
        "en": "The Sand Road, Rice Field, and Little Girl",
        "source": "V2/md/03_第一章_月暗之旅.md",
        "function": "让月暗从废墟恐惧转为稻田、生活痕迹和小女孩的不可解释性。",
        "task": "让小女孩帮助吉姆，但暂不命名为艾拉。",
        "notes": ["她可以像儿童，也可以不像人类儿童。", "她的善意要带一点上位系统的冷感。"],
        "protect": "不让她提前成为说明一切的向导。",
    },
    {
        "n": 6,
        "zh": "蓝黑球体与时间井",
        "en": "The Blue-Black Sphere and the Time Well",
        "source": "V2/md/03_第一章_月暗之旅.md",
        "function": "完成第一章的月暗体验闭环：白视界、黑视界、泰拉撒外缘、时间井返回。",
        "task": "保留信息洪流和梦境式跳转，让吉姆带回未知信息结构。",
        "notes": ["这里是全书最重要的神秘感来源。", "可作为后续所有设定的感性源头。"],
        "protect": "不解释泰拉撒的完整机制。",
    },
    {
        "n": 7,
        "zh": "新世纪与双生",
        "en": "The New Century and the Dual-Born",
        "source": "V2/md/04_第二章_新世纪.md",
        "function": "保留第二章原声：吉姆解释新世纪、双生模式和数字矫正。",
        "task": "统一吉姆·维尔、查理·黑尔等名字，保护吉姆解释世界的口吻。",
        "notes": ["这是作者口吻锚点之二。", "社会设定应从吉姆嘴里出来，而不是百科条。"],
        "protect": "不重排第二章叙事顺序。",
    },
    {
        "n": 8,
        "zh": "第二次数字矫正",
        "en": "The Second Digital Correction",
        "source": "V2/md/04_第二章_新世纪.md",
        "function": "让吉姆、安娜、查理一起进入十八岁矫正，事故开始。",
        "task": "明确主角团关系：吉姆好奇，安娜读规则，查理怕死但跟上。",
        "notes": ["不要把三人写成同一种聪明人。", "设备流程要服务紧张感。"],
        "protect": "不让卢恩博士提前知道全部真相。",
    },
    {
        "n": 9,
        "zh": "数字吉姆的空房间",
        "en": "Digital Jim's Empty Room",
        "source": "V2/md/04_第二章_新世纪.md",
        "function": "让吉姆发现数字世界中的异常和数字自我的威胁。",
        "task": "数字吉姆不做简单反派，而是吉姆自我分裂的第一道阴影。",
        "notes": ["空房间比解释更有效。", "危险来自相似，而不是陌生。"],
        "protect": "不把数字吉姆的动机一次说透。",
    },
    {
        "n": 10,
        "zh": "唯一归来者",
        "en": "The Only Returnee",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "吉姆醒来，其他人未醒；他从幸存者变成样本和门。",
        "task": "把会议邀请建立在现实压力上，而不是剧情便利。",
        "notes": ["保留吉姆头痛、恶心、被注视的距离感。", "小女孩的脸仍然模糊。"],
        "protect": "不让吉姆立刻接受自己是关键。",
    },
    {
        "n": 11,
        "zh": "月暗记录会议",
        "en": "The Lunar Record Meeting",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "灵接科技高层、贾雷德和斯皮尔听取吉姆带回的信息。",
        "task": "让信息释放由会议质疑、投影异常和人物反应推动。",
        "notes": ["斯皮尔与吉姆的亲切感只保留一次强烈感受。", "贾雷德负责把神话和记录对号。"],
        "protect": "不让吉姆像全知讲师。",
    },
    {
        "n": 12,
        "zh": "生命起源的外壳",
        "en": "The Shell of Life's Origin",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "先用人类能理解的化学起源作外壳，再露出蓝黑参数异常。",
        "task": "让读者感觉：教科书解释不够用了。",
        "notes": ["这是发现链第一扣。", "投影异常比长篇解释更有压力。"],
        "protect": "不把生命起源写成科普讲章。",
    },
    {
        "n": 13,
        "zh": "人类是宿主",
        "en": "Humanity as Host",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "揭示人类肉体作为意识载体的设定，并轻埋巨鲸线。",
        "task": "保留鲸类曾被尝试的线索，但只作为黑影。",
        "notes": ["巨鲸形阴影出现但不解释。", "人类不是被创造，而是被改向。"],
        "protect": "不把外星介入写成普通阴谋论。",
    },
    {
        "n": 14,
        "zh": "神话开始对号",
        "en": "Myths Begin to Align",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "贾雷德把古文明神话作为人类内部记忆系统来解释。",
        "task": "让神话不是旁征博引，而是现场压力的一部分。",
        "notes": ["苏美尔、华夏、玛雅、埃及等作为对应结构。", "每个例子要指向同一个问题：人类为何是宿主。"],
        "protect": "不堆文明名录。",
    },
    {
        "n": 15,
        "zh": "月球的工程真相",
        "en": "The Engineered Truth of the Moon",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "把月球从自然卫星改写为撞击灾难后的工程平台。",
        "task": "让月球成为救援和监视系统的关键接口。",
        "notes": ["彗星、巨峰、碎片清理、同步卫星是核心。", "视觉上要壮阔，但不要像论文。"],
        "protect": "不急着证明科学正确，只要在故事内部有压迫感。",
    },
    {
        "n": 16,
        "zh": "海底基地与监视系统",
        "en": "The Undersea Base and Surveillance System",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "把北太平洋海底基地、月暗节点和安娜/查理昏迷联系起来。",
        "task": "让卢恩追问现实后果：这和救人有什么关系。",
        "notes": ["会议必须回到安娜、查理为什么醒不过来。", "月球不是背景，是接口。"],
        "protect": "不让远古设定脱离当前危机。",
    },
    {
        "n": 17,
        "zh": "数字亚瑟",
        "en": "Digital Arthur",
        "source": "V2/md/05_第三章_月暗记录.md",
        "function": "用亚瑟·惠勒的数字停滞证明数字永生不是答案。",
        "task": "建立斯皮尔的迁出执念，但保持危险与悲伤并存。",
        "notes": ["亚瑟不是工具人，是失败永生的活证据。", "斯皮尔不应只像反派，也像被困住的人。"],
        "protect": "不把斯皮尔的计划说成已经完全正确。",
    },
    {
        "n": 18,
        "zh": "童年的另一个世界",
        "en": "Childhood in Another World",
        "source": "V2/md/06_第四章_另一个世界.md",
        "function": "通过三人第一次游戏体验建立主角团性格功能。",
        "task": "保留吉姆非必要介入、安娜读规则、查理怕死但跟上。",
        "notes": ["这一段目前很好，是后续修订的保护区。", "游戏不是说明书，是三人关系的显影液。"],
        "protect": "不删三人吵闹、吐槽和童年感。",
    },
    {
        "n": 19,
        "zh": "隐藏任务",
        "en": "The Hidden Quest",
        "source": "V2/md/06_第四章_另一个世界.md",
        "function": "用救女人和孩子的背景事件，预示吉姆的命运倾向。",
        "task": "让系统第一次记录他们的异常行为模式。",
        "notes": ["这不是普通游戏彩蛋，而是命运性格的早期证据。", "查理嘴上怕，身体会跟。"],
        "protect": "不把隐藏任务写成单纯爽点。",
    },
    {
        "n": 20,
        "zh": "月暗副本",
        "en": "The Moon-Dark Instance",
        "source": "V2/md/06_第四章_另一个世界.md",
        "function": "把月暗区域数字化为《另一个世界》的副本，但强调它只是影子。",
        "task": "保留报告形式，同时穿插吉姆的接收感和卢恩的不确定。",
        "notes": ["游戏副本不能等同真实入口。", "报告里要有质疑，而不是卢恩讲完全部真相。"],
        "protect": "不让项目座谈会变成产品说明书。",
    },
    {
        "n": 21,
        "zh": "克罗斯与肖恩",
        "en": "Cross and Shawn",
        "source": "V2/md/07_第五章_半纪往事.md",
        "function": "引入老一代研究者，为黑潮、罗斯威尔和死球理论提供证词。",
        "task": "让克罗斯稳、肖恩敏感、卢恩焦虑，各自立场清楚。",
        "notes": ["第五章后续最需要节奏整理。", "老一代只知道自己研究和经历过的部分。"],
        "protect": "不把他们写成设定播报员。",
    },
    {
        "n": 22,
        "zh": "黑潮以后",
        "en": "After the Black Tide",
        "source": "V2/md/07_第五章_半纪往事.md",
        "function": "说明黑潮如何让人类从物质信仰转向意识、精神和数字延续。",
        "task": "让历史背景服务灵接科技崛起，而不是泛泛谈文明。",
        "notes": ["黑潮是价值观断裂，不只是灾难史。", "克罗斯的幸存者气质要压住讲述。"],
        "protect": "不写成历史课。",
    },
    {
        "n": 23,
        "zh": "罗斯威尔遗产",
        "en": "The Roswell Inheritance",
        "source": "V2/md/07_第五章_半纪往事.md",
        "function": "揭示意识接口逆向工程和 IHinDiA 的真实起源。",
        "task": "把军方、资本、国际组织之间的权力关系讲清楚。",
        "notes": ["1947 是坠毁，2047 是技术释放。", "外星接口不是万能科技，只是错误打开的门。"],
        "protect": "不让阴谋线抢走吉姆救友主线。",
    },
    {
        "n": 24,
        "zh": "死球理论",
        "en": "The Dead-World Theory",
        "source": "V2/md/07_第五章_半纪往事.md",
        "function": "提出死球、地球势阱、月球死亡出口的理论基础。",
        "task": "为第六章“死在月球”做逻辑铺垫。",
        "notes": ["这是高风险设定，必须写成不安的工程结论。", "肖恩要清楚知道这句话不能公开。"],
        "protect": "不把死亡写成口号或浪漫化选择。",
    },
    {
        "n": 25,
        "zh": "再见小女孩",
        "en": "The Little Girl Returns",
        "source": "V2/md/08_第六章_无尽的等待.md",
        "function": "吉姆多次尝试后重新接通小女孩，得知安娜和查理被解构。",
        "task": "让联系窗口短、危险、被监管。",
        "notes": ["小女孩前期仍称小女孩，不急着命名艾拉。", "她能帮，但不能随意违抗上位协议。"],
        "protect": "不让她变成万能救援者。",
    },
    {
        "n": 26,
        "zh": "解构倒计时",
        "en": "The Countdown to Deconstruction",
        "source": "V2/md/08_第六章_无尽的等待.md",
        "function": "确认安娜、查理和其他人的意识正在被月球系统归档/解构。",
        "task": "把危机从沉睡状态升级为不可逆倒计时。",
        "notes": ["解构要冷静、恐怖，不靠血腥。", "植物人风险要落到现实身体。"],
        "protect": "不把被困者写成抽象样本。",
    },
    {
        "n": 27,
        "zh": "三天失败",
        "en": "Three Days of Failure",
        "source": "V2/md/08_第六章_无尽的等待.md",
        "function": "卢恩尝试所有地球侧办法失败，迫使月球方案成为唯一可行动答案。",
        "task": "让卢恩成为阻止者、验证者和见证者。",
        "notes": ["重连失败、数字备份失败、轨道切断失败。", "肖恩模型提供理论压力。"],
        "protect": "不让去月球像突然决定。",
    },
    {
        "n": 28,
        "zh": "斯皮尔的旧梦",
        "en": "Spire's Old Dream",
        "source": "V2/md/08_第六章_无尽的等待.md",
        "function": "斯皮尔向卢恩说明灵接科技的初衷、亚瑟失败和迁出执念。",
        "task": "让斯皮尔的危险来自长期等待，而不是单纯邪恶。",
        "notes": ["他想自由，但可能会把别人推向不可逆实验。", "卢恩应保持伦理抵抗。"],
        "protect": "不把斯皮尔写成全知导师。",
    },
    {
        "n": 29,
        "zh": "LUNA-EXIT",
        "en": "LUNA-EXIT",
        "source": "V2/md/08_第六章_无尽的等待.md",
        "function": "把登月、非地球死亡区和意识迁出计划正式连成项目。",
        "task": "让计划可执行，但伦理上令人发冷。",
        "notes": ["医学评估、心理稳定、舱体过渡、信息记录是现实层支撑。", "卢恩不是批准者，是见证选择的人。"],
        "protect": "不把项目写成成功确定的救世工程。",
    },
    {
        "n": 30,
        "zh": "不可返回区域",
        "en": "The No-Return Zone",
        "source": "V2/md/09_第七章_接近真相.md",
        "function": "吉姆面对单程登月选择，卢恩保留冻结权限。",
        "task": "让吉姆说出私人理由：不是文明口号，是去找朋友。",
        "notes": ["安娜读不完的规则、查理黑暗中的低频声，作为私人的召唤。", "卢恩要确认他不是被恐惧推着走。"],
        "protect": "不把吉姆写成无惧牺牲的英雄模板。",
    },
    {
        "n": 31,
        "zh": "发射",
        "en": "Launch",
        "source": "V2/md/09_第七章_接近真相.md",
        "function": "执行非常规单人登月任务，现实侧完成最后确认。",
        "task": "低仪式感处理，让冷静工程感反衬死亡选择。",
        "notes": ["SpaceX 只负责工程，不负责解释目的。", "最后撤回权在吉姆自己手里。"],
        "protect": "不写成宏大宣传片。",
    },
    {
        "n": 32,
        "zh": "月球暗面着陆",
        "en": "Landing on the Dark Side",
        "source": "V2/md/09_第七章_接近真相.md",
        "function": "吉姆物理抵达月球暗面，地球光消失。",
        "task": "让读者感到他第一次真正离开地球势阱。",
        "notes": ["黑暗、无导航、内部模型、预设路径。", "卢恩最后一句“我们在这里”保留人类联系。"],
        "protect": "不提前把月暗文明实体化。",
    },
    {
        "n": 33,
        "zh": "肉体死亡",
        "en": "Bodily Death",
        "source": "V2/md/09_第七章_接近真相.md",
        "function": "吉姆关闭意识支持系统，肉体死亡，主体核脱离束缚。",
        "task": "写得安静、具体、不可逆，不煽情。",
        "notes": ["死亡不是壮举表演，而是边界感消失。", "小女孩不拉走他，只让固定点消失。"],
        "protect": "不浪漫化自毁，不写成简单献祭。",
    },
    {
        "n": 34,
        "zh": "泰拉撒第一层门",
        "en": "The First Gate of Terasha",
        "source": "V2/md/09_第七章_接近真相.md",
        "function": "吉姆进入泰拉撒记录，感知被困意识和巨鲸暗影，但只打开第一层门。",
        "task": "保留续作入口，不做完整揭秘。",
        "notes": ["巨鲸暗影与查理线轻轻连接。", "安娜、查理和其他人仍需后续救援/分书展开。"],
        "protect": "不让结尾宣告人类文明已经胜利。",
    },
    {
        "n": 35,
        "zh": "下一本入口",
        "en": "The Door to the Next Book",
        "source": "系列框架",
        "function": "收束《月球暗面》，把读者引向《巨鲸陨落》《灵猫》《时间之井》。",
        "task": "说明下一步不是解释全部宇宙，而是分别救回查理、安娜，并面对数字吉姆。",
        "notes": ["查理入口：巨鲸暗影和低频海声。", "安娜入口：规则、黑猫森林、非人类意识。", "数字吉姆入口：时间井和主体核问题。"],
        "protect": "不在第一本尾声抢走后续三本的主题。",
    },
]


def en_task(text: str) -> str:
    mapping = {
        "工程说明": "Project note",
        "系列框架": "Series framework",
        "建立《月球暗面》V2 框架工程的使用方式，说明当前文件是结构卡，不是正文重写。": "Establish how to use the Moon Dark Side V2 framework project. These files are structure cards, not a prose rewrite.",
        "保护 V1 第一、第二章的原声；后续只在三至七章做结构性增强。": "Protect the original voice of V1 Chapters 1 and 2; later structural work should focus on Chapters 3-7.",
    }
    return mapping.get(text, text)


EN_CARDS = {
    0: {
        "function": "Explain how to use the Moon Dark Side V2 framework layer. These are structure cards, not a prose rewrite.",
        "task": "Protect the original voice of V1 Chapters 1 and 2, and use later cards to guide structural strengthening from Chapters 3-7.",
        "protect": "Do not import the discarded full-rewrite V2 or replace the current V2 prose directory.",
        "notes": ["Chinese is the primary creative layer.", "English is the cross-thread reference layer.", "HTML is the reading layer for review."],
    },
    1: {
        "function": "Keep the author's opening note about creative motive, cosmic scale, and series tone.",
        "task": "Only clean formatting or obvious errors; preserve the personal temperature of the note.",
        "protect": "Do not turn the author's note into marketing copy or a worldbuilding encyclopedia.",
        "notes": ["Let readers feel that this is a series gateway, not a single technical premise.", "The voice should stay close to the author rather than the fictional narrator."],
    },
    2: {
        "function": "Use Jim's voice to raise the questions of truth, silence, lies, and cosmic narrative.",
        "task": "Unify Jim Vale's name while preserving the philosophical and unstable information-noise texture.",
        "protect": "Do not explain the lunar system, Terasha records, or the final choice too early.",
        "notes": ["This should feel like a crack in a door, not a full manual.", "The error-code texture can remain as consciousness overflow."],
    },
    3: {
        "function": "Preserve the original Chapter 1 entry: bodily discomfort, black-water memory, and waking from the correction accident.",
        "task": "Establish Jim's first-person mode: fear, nausea, curiosity, and compulsive analysis.",
        "protect": "Do not turn the black-water experience into a clean mission opening.",
        "notes": ["This is one of the author's voice anchors.", "Light paragraphing is allowed; narrative rewriting is not."],
    },
    4: {
        "function": "Let Jim enter the moon-dark space and encounter the stone gate, ancient battlefield, and whale/alien war shadows.",
        "task": "Strengthen the dream-archaeology quality while preserving the state of seeing without understanding.",
        "protect": "Do not explain the Phaeton final war or define the whale image yet.",
        "notes": ["Whale and alien remains should foreshadow Giant Whale Fall only as shadows.", "The image should hit readers before explanation arrives."],
    },
    5: {
        "function": "Shift the moon-dark experience from ruin and fear into rice fields, traces of life, and the unexplained little girl.",
        "task": "Let the little girl help Jim without naming her Elara too early.",
        "protect": "Do not make her an all-explaining guide.",
        "notes": ["She may look like a child without being humanly childlike.", "Her kindness should carry a cold upper-system edge."],
    },
    6: {
        "function": "Close the first chapter's lunar experience through the white view, black view, outer Terasha layer, and Time Well return.",
        "task": "Preserve the information flood and dreamlike jump structure; Jim returns with an unknown information pattern.",
        "protect": "Do not explain Terasha's full mechanism.",
        "notes": ["This is the main source of mystery for the book.", "It should become the sensory origin of later exposition."],
    },
    7: {
        "function": "Preserve Chapter 2's original explanation of the new century, dual-born model, and digital correction.",
        "task": "Unify names such as Jim Vale and Charlie Hale while protecting Jim's explanatory voice.",
        "protect": "Do not reorder the second chapter's narrative logic.",
        "notes": ["This is the second major voice anchor.", "The social setting should come through Jim, not encyclopedia entries."],
    },
    8: {
        "function": "Bring Jim, Anna, and Charlie into the age-eighteen correction together and start the accident.",
        "task": "Clarify the trio dynamic: Jim intervenes, Anna reads rules, Charlie fears death but follows.",
        "protect": "Do not let Dr. Lune know the whole truth too early.",
        "notes": ["Do not write the trio as the same kind of smart person.", "The device procedure should serve tension."],
    },
    9: {
        "function": "Let Jim discover the anomaly in the digital world and the threat of his digital self.",
        "task": "Digital Jim should be the first shadow of Jim's self-division, not a simple villain.",
        "protect": "Do not fully explain Digital Jim's motive yet.",
        "notes": ["The empty room is more effective than explanation.", "The danger comes from similarity, not strangeness."],
    },
    10: {
        "function": "Jim wakes while others remain unconscious; he becomes survivor, specimen, and door.",
        "task": "Make the meeting invitation grow from real pressure rather than plot convenience.",
        "protect": "Do not let Jim instantly accept that he is the key.",
        "notes": ["Keep Jim's headache, nausea, and sense of being watched.", "The little girl's face should remain blurred."],
    },
    11: {
        "function": "Spirit Connect leadership, Jared, and Spire hear Jim's moon-dark information.",
        "task": "Let revelations emerge through meeting pressure, projection anomalies, and character reactions.",
        "protect": "Do not make Jim sound like an omniscient lecturer.",
        "notes": ["Keep only one strong moment of familiarity between Jim and Spire.", "Jared's job is to align myth with record."],
    },
    12: {
        "function": "Use humanly understandable chemistry as the shell of life's origin, then let blue-black anomalies break through.",
        "task": "Make readers feel that textbook explanation is no longer enough.",
        "protect": "Do not write life's origin as a science lecture.",
        "notes": ["This is the first link in the discovery chain.", "Projection anomalies should create pressure more than explanation does."],
    },
    13: {
        "function": "Reveal humanity as a consciousness host structure and lightly plant the whale line.",
        "task": "Keep the whale experiment clue as a shadow only.",
        "protect": "Do not reduce alien intervention to ordinary conspiracy.",
        "notes": ["The whale-shaped shadow appears but is not explained.", "Humanity is not created from nothing; evolution is redirected."],
    },
    14: {
        "function": "Jared interprets ancient myths as an internal human memory system.",
        "task": "Make mythic alignment part of the meeting pressure, not decorative citation.",
        "protect": "Do not stack civilization names for their own sake.",
        "notes": ["Sumerian, Chinese, Maya, Egyptian, and other examples should point to one shared structure.", "Every example should serve the question of humanity as host."],
    },
    15: {
        "function": "Rewrite the Moon from natural satellite into engineered platform after a collision catastrophe.",
        "task": "Make the Moon essential to rescue and surveillance.",
        "protect": "Do not try to prove real-world science; make the story logic feel pressurized.",
        "notes": ["Comet, giant peak, debris clearing, and synchronous satellite are the core beats.", "The vision should be vast without becoming an academic paper."],
    },
    16: {
        "function": "Connect the North Pacific undersea base, lunar node, and Anna/Charlie coma crisis.",
        "task": "Let Lune force the question: what does this have to do with saving them?",
        "protect": "Do not let ancient lore drift away from the present crisis.",
        "notes": ["The meeting must return to why Anna and Charlie cannot wake.", "The Moon is not background; it is an interface."],
    },
    17: {
        "function": "Use Arthur Wheeler's digital stagnation to show that digital immortality is not the answer.",
        "task": "Build Spire's migration obsession while keeping danger and grief together.",
        "protect": "Do not present Spire's plan as already proven correct.",
        "notes": ["Arthur is not a tool; he is living evidence of failed immortality.", "Spire should feel both dangerous and trapped."],
    },
    18: {
        "function": "Use the trio's first game experience to establish their functions as a group.",
        "task": "Preserve Jim's unnecessary intervention, Anna's rule-reading, and Charlie's fearful loyalty.",
        "protect": "Do not remove the trio's noise, teasing, and childhood texture.",
        "notes": ["This section is currently a protection zone.", "The game is not a manual; it reveals relationship."],
    },
    19: {
        "function": "Use the hidden rescue quest to foreshadow Jim's fate-driven tendency.",
        "task": "Let the system first record the trio's abnormal behavior pattern.",
        "protect": "Do not make the hidden quest a simple reward beat.",
        "notes": ["This is early evidence of character fate.", "Charlie complains, fears, and still follows."],
    },
    20: {
        "function": "Digitize the moon-dark region into Another World while stressing that it is only a shadow.",
        "task": "Keep the report form but add Jim's reception and Lune's uncertainty.",
        "protect": "Do not let the development meeting become a product manual.",
        "notes": ["The game instance is not the real gate.", "The report needs questions, not just Lune explaining everything."],
    },
    21: {
        "function": "Introduce older researchers who can testify about the Black Tide, Roswell, and dead-world theory.",
        "task": "Make Cross steady, Shawn sensitive, and Lune anxious, with clear positions.",
        "protect": "Do not turn them into lore broadcasters.",
        "notes": ["Chapter 5 needs the most pacing work later.", "Older researchers only know what they experienced or studied."],
    },
    22: {
        "function": "Explain how the Black Tide redirected humanity from material faith toward consciousness and digital continuation.",
        "task": "Make history serve Spirit Connect's rise rather than generic civilization commentary.",
        "protect": "Do not write this as a history class.",
        "notes": ["The Black Tide is a value rupture, not only disaster history.", "Cross's survivor texture should weigh down the exposition."],
    },
    23: {
        "function": "Reveal consciousness-interface reverse engineering and IHinDiA's real origin.",
        "task": "Clarify the power relation between military, capital, and international governance.",
        "protect": "Do not let the conspiracy line overtake Jim's rescue story.",
        "notes": ["1947 is the crash; 2047 is technology release.", "The alien interface is not a universal technology; it is a wrongly opened door."],
    },
    24: {
        "function": "Introduce dead worlds, Earth's consciousness well, and lunar death as theoretical escape.",
        "task": "Prepare the logic for Chapter 6's death-on-the-Moon conclusion.",
        "protect": "Do not make death a slogan or romantic choice.",
        "notes": ["This is a high-risk idea and should feel like an unsettling engineering conclusion.", "Shawn must know this cannot be said publicly."],
    },
    25: {
        "function": "After repeated attempts, Jim reconnects with the little girl and learns Anna and Charlie are being deconstructed.",
        "task": "Make the contact window brief, dangerous, and monitored.",
        "protect": "Do not make the little girl an all-purpose rescuer.",
        "notes": ["She can remain 'the little girl' for now; Elara need not appear too early.", "She can help, but cannot casually defy higher protocol."],
    },
    26: {
        "function": "Confirm that Anna, Charlie, and the others are being archived or deconstructed by the lunar system.",
        "task": "Escalate coma into an irreversible countdown.",
        "protect": "Do not turn trapped people into abstract samples.",
        "notes": ["Deconstruction should be calm and terrifying, not bloody.", "The vegetative-state risk must return to real bodies."],
    },
    27: {
        "function": "Lune exhausts Earth-side solutions, forcing the lunar route to become the only actionable answer.",
        "task": "Make Lune the blocker, verifier, and witness.",
        "protect": "Do not make going to the Moon feel like a sudden choice.",
        "notes": ["Reconnect fails; digital backup fails; orbital cutoff fails.", "Shawn's model supplies theoretical pressure."],
    },
    28: {
        "function": "Spire tells Lune about Spirit Connect's origin, Arthur's failure, and the migration obsession.",
        "task": "Make Spire dangerous because he has waited too long, not because he is simply evil.",
        "protect": "Do not write Spire as an omniscient mentor.",
        "notes": ["He wants freedom but may push others into irreversible experiment.", "Lune should keep ethical resistance."],
    },
    29: {
        "function": "Link lunar travel, non-Earth death, and consciousness migration into an executable project.",
        "task": "Make the plan technically actionable but ethically cold.",
        "protect": "Do not make the project feel like a guaranteed salvation machine.",
        "notes": ["Medical assessment, psychological stability, transfer hardware, and information recording support the realism layer.", "Lune is not the approver; he is the witness."],
    },
    30: {
        "function": "Jim faces the one-way lunar choice while Lune keeps the power to freeze permissions.",
        "task": "Make Jim give private reasons: he goes to find friends, not to serve a civilization slogan.",
        "protect": "Do not write Jim as a fearless heroic template.",
        "notes": ["Anna's unreadable rule and Charlie's low-frequency darkness are personal calls.", "Lune must verify Jim is not being driven only by fear."],
    },
    31: {
        "function": "Execute the unconventional single-person lunar mission and complete final checks on the real-world side.",
        "task": "Use low ceremony so cold engineering contrasts with the death-choice.",
        "protect": "Do not make the launch read like a promotional spectacle.",
        "notes": ["SpaceX handles engineering but not meaning.", "The final withdrawal right remains with Jim."],
    },
    32: {
        "function": "Jim physically reaches the Moon's dark side as Earthlight disappears.",
        "task": "Let readers feel that he has truly left Earth's consciousness well.",
        "protect": "Do not materialize the lunar civilization too early.",
        "notes": ["Darkness, no external beacons, internal models, and preset paths matter.", "Lune's final 'we are here' preserves human connection."],
    },
    33: {
        "function": "Jim shuts down consciousness support, dies bodily, and the subject-core loosens from the body.",
        "task": "Write the scene quietly, concretely, and irreversibly.",
        "protect": "Do not romanticize self-destruction or frame it as simple sacrifice.",
        "notes": ["Death is not a heroic performance; it is the loss of boundary.", "The little girl does not drag him away; she lets the fixed point vanish."],
    },
    34: {
        "function": "Jim enters Terasha records, senses trapped consciousnesses and the whale shadow, but only opens the first gate.",
        "task": "Keep sequel entrances alive and avoid full revelation.",
        "protect": "Do not let the ending declare human civilization victorious.",
        "notes": ["The whale shadow lightly links to Charlie's book.", "Anna, Charlie, and others still require later rescue or book-level arcs."],
    },
    35: {
        "function": "Close Moon Dark Side and point toward Giant Whale Fall, Spirit Cat, and The Time Well.",
        "task": "Clarify that the next move is not explaining the universe, but rescuing Charlie, rescuing Anna, and facing Digital Jim.",
        "protect": "Do not let Book 1's ending steal the themes of later books.",
        "notes": ["Charlie entrance: whale shadow and low oceanic frequency.", "Anna entrance: rules, black-cat forest, nonhuman consciousness.", "Digital Jim entrance: Time Well and subject-core problem."],
    },
}


def md_escape(text: str) -> str:
    return text.replace("\n", " ").strip()


def chapter_filename(n: int, title: str) -> str:
    return f"{n:02d}_{title}.md"


def html_filename(md_name: str) -> str:
    return md_name[:-3] + ".html"


def zh_card(ch: dict) -> str:
    notes = "\n".join(f"- {item}" for item in ch["notes"])
    return f"""# {ch['n']:02d} {ch['zh']}

## 章节定位

- 所属来源：{ch['source']}
- 本章功能：{ch['function']}
- 主要任务：{ch['task']}
- 保护边界：{ch['protect']}

## 正文种子

这一章不是独立定稿，而是《月球暗面》V2 的结构卡。后续如果进入正文修订，应优先从当前 V2 的中文 Markdown 母本取材，并保护作者原有梦境感、哲思感和第一人称口吻。

## 写作要点

{notes}

## 禁止误改

- 不套用此前作废 V2 的整本重写内容。
- 不为了结构清晰而抹平吉姆的困惑、旁枝想法和身体感受。
- 不提前解释角色在当前场景中无法知道的真相。
"""


def en_card(ch: dict) -> str:
    e = EN_CARDS[ch["n"]]
    notes = "\n".join(f"- {item}" for item in e["notes"])
    return f"""# {ch['n']:02d} {ch['en']}

## Chapter Position

- Source layer: {ch['source']}
- Function: {e['function']}
- Main task: {e['task']}
- Protection boundary: {e['protect']}

## Draft Seed

This is not final prose. It is a structural card for Moon Dark Side V2. Future prose revision should draw from the current Chinese Markdown source and preserve the author's dreamlike, philosophical, first-person texture.

## Writing Notes

{notes}

## Forbidden Mistakes

- Do not reuse the discarded full-rewrite V2 as the active source.
- Do not flatten Jim's confusion, digressions, bodily sensations, or original voice for the sake of neat structure.
- Do not reveal truths the viewpoint character cannot know in the scene.
"""


def inline_markdown(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def markdown_to_html(md: str, title: str, lang: str, css_href: str = "../assets/style.css") -> str:
    blocks = []
    in_list = False
    for raw in md.splitlines():
        line = raw.strip()
        if not line:
            if in_list:
                blocks.append("</ul>")
                in_list = False
            continue
        if line.startswith("#"):
            if in_list:
                blocks.append("</ul>")
                in_list = False
            level = min(len(line) - len(line.lstrip("#")), 3)
            blocks.append(f"<h{level}>{inline_markdown(line[level:].strip())}</h{level}>")
        elif line.startswith("- "):
            if not in_list:
                blocks.append("<ul>")
                in_list = True
            blocks.append(f"<li>{inline_markdown(line[2:].strip())}</li>")
        else:
            if in_list:
                blocks.append("</ul>")
                in_list = False
            blocks.append(f"<p>{inline_markdown(line)}</p>")
    if in_list:
        blocks.append("</ul>")
    body = "\n".join(blocks)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{html.escape(css_href)}">
</head>
<body>
  <main>
{body}
  </main>
</body>
</html>
"""


def write_indices() -> None:
    zh_lines = [
        "# 月球暗面 V2 结构框架",
        "",
        "《灵接科技》第一本结构工程版。当前层级参考《巨鲸陨落_V1》的工程格式：中文 Markdown、中文 HTML、英文 Markdown、英文 HTML 分开维护。",
        "",
        "注意：这套 `zh_md/en_md` 是章节框架卡，不是正文重写。当前正文母本仍在 `md/` 与 `html/`。",
        "",
        "## 章节目录",
    ]
    en_lines = [
        "# Moon Dark Side V2 Structural Framework",
        "",
        "Structural engineering layer for the first book of Spirit Connect. It mirrors the project format used by Giant Whale Fall V1: Chinese Markdown, Chinese HTML, English Markdown, and English HTML are maintained separately.",
        "",
        "Note: `zh_md/en_md` contain chapter structure cards, not a prose rewrite. The current prose source remains in `md/` and `html/`.",
        "",
        "## Chapter Index",
    ]
    for ch in CHAPTERS:
        zh_name = chapter_filename(ch["n"], ch["zh"])
        en_name = chapter_filename(ch["n"], ch["zh"])
        zh_lines.append(f"- [{ch['n']:02d} {ch['zh']}](zh_md/{zh_name}) / [HTML](zh_html/{html_filename(zh_name)})")
        en_lines.append(f"- [{ch['n']:02d} {ch['en']}](en_md/{en_name}) / [HTML](en_html/{html_filename(en_name)})")
    zh_lines.extend([
        "",
        "## 使用方式",
        "",
        "- 先看本目录确认整体结构。",
        "- 需要讨论某一章时，优先打开对应 `zh_md` 框架卡。",
        "- 进入正文修订时，再回到 `md/` 里的当前 V2 正文母本。",
    ])
    en_lines.extend([
        "",
        "## How to Use",
        "",
        "- Read this index first to review the overall structure.",
        "- When discussing a chapter, open the corresponding `zh_md` structure card first.",
        "- When prose revision begins, return to the current V2 prose source in `md/`.",
    ])
    (ROOT / "index.md").write_text("\n".join(zh_lines) + "\n", encoding="utf-8")
    (ROOT / "index_EN.md").write_text("\n".join(en_lines) + "\n", encoding="utf-8")
    (ROOT / "index.html").write_text(markdown_to_html("\n".join(zh_lines), "月球暗面 V2 结构框架", "zh-CN", "assets/style.css"), encoding="utf-8")
    (ROOT / "index_EN.html").write_text(markdown_to_html("\n".join(en_lines), "Moon Dark Side V2 Structural Framework", "en", "assets/style.css"), encoding="utf-8")


def write_readme() -> None:
    readme = """# 月球暗面_V2

这是《灵接科技》第一本《月球暗面》的 V2 工程目录。

- `md/`：当前 V2 中文正文母本，延续 V1 原始章节，不作为本轮框架重拆对象。
- `html/`：当前 V2 中文正文阅读 HTML。
- `zh_md/`：参考《巨鲸陨落_V1》格式生成的中文章节框架卡。
- `zh_html/`：中文章节框架卡阅读 HTML。
- `en_md/`：英文对应章节框架卡，用于跨对话参考。
- `en_html/`：英文对应章节框架卡阅读 HTML。
- `index.html`：中文框架阅读目录。
- `index_EN.html`：英文框架阅读目录。
- `V2重启修订框架_CN.md` / `V2_restart_revision_framework_EN.md`：本轮 V2 的保护规则与修订路线。

当前原则：

- 第一章《月暗之旅》和第二章《新世纪》是作者原声锚点，原则上不做内容重写。
- 新增 `zh_md/en_md` 是结构卡，不替代正文。
- 后续如果采用此框架，应先由作者确认，再逐章把正文从 `md/` 迁移或扩写到新结构中。
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    for path in [ASSETS, ZH_MD, EN_MD, ZH_HTML, EN_HTML]:
        path.mkdir(exist_ok=True)
    (ASSETS / "style.css").write_text(STYLE, encoding="utf-8")

    for ch in CHAPTERS:
        zh_name = chapter_filename(ch["n"], ch["zh"])
        en_name = chapter_filename(ch["n"], ch["zh"])
        zh_md = zh_card(ch)
        en_md = en_card(ch)
        (ZH_MD / zh_name).write_text(zh_md, encoding="utf-8")
        (EN_MD / en_name).write_text(en_md, encoding="utf-8")
        (ZH_HTML / html_filename(zh_name)).write_text(markdown_to_html(zh_md, f"{ch['n']:02d} {ch['zh']}", "zh-CN"), encoding="utf-8")
        (EN_HTML / html_filename(en_name)).write_text(markdown_to_html(en_md, f"{ch['n']:02d} {ch['en']}", "en"), encoding="utf-8")

    write_indices()
    write_readme()


if __name__ == "__main__":
    main()
