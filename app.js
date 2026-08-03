import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

const books = [
  {
    id: "dark-moon",
    glyph: { zh: "月", en: "DM" },
    title: { zh: "月球暗面", en: "Darkside of the Moon" },
    kicker: { zh: "档案 I · 死在月球是知晓地球真相最快的方式", en: "Archive I · Dying on the Moon is the fastest way to know the truth of Earth" },
    status: { zh: "已出版", en: "Published" },
    theme: { zh: "意识迁出 · 死球理论", en: "Consciousness Exodus · Dead Moon Theory" },
    accent: "#2bb8ff",
    cover: { zh: "assets/DM_cn.png", en: "assets/DM_en.png" },
    link: "novels/dark-moon/",
    description: {
      zh: "遍览古代文明，人类像猴子一样几千年没有成长。阿卡西的海洋像雨水一样浇灌在每一位智人的颅顶，没有高一级的文明介入，就算淹死，猴子依然是猴子。",
      en: "Across the sweep of ancient civilizations, humanity has remained like monkeys, unchanged for thousands of years. The ocean of Akasha pours like rain onto the crown of every Homo sapiens; without the intervention of a higher civilization, even if drowned, a monkey remains a monkey.",
    },
  },
  {
    id: "whale-fall",
    glyph: { zh: "鲸", en: "WF" },
    title: { zh: "巨鲸陨落", en: "Whale Fall" },
    kicker: { zh: "档案 II · 法厄同证词", en: "Archive II · Phaethon Testimony" },
    status: { zh: "阅读稿已接入", en: "Reading Draft Added" },
    theme: { zh: "文明遗产 · 鲸歌回声", en: "Civilization Relic · Whale Echo" },
    accent: "#4da3ff",
    cover: { zh: "assets/WF_cn.png", en: "assets/WF_en.png" },
    link: "novels/whale-fall/",
    description: {
      zh: "文明从不只由技术定义。每一代人都会依照自己的审美，为繁荣赋予形状，也为永恒规定尺度。物质的极大丰饶催生了巨构文明，而太阳帝国，则是它最壮丽的象征。它巍峨，恢宏，仿佛足以抵抗时间。我们曾相信它会永垂不朽。后来我们才明白：所谓不朽，往往只是身处盛世之中的人，对时间产生的一种错觉。",
      en: "Civilization is never defined by technology alone. Every generation shapes prosperity according to its own aesthetic and sets its own measure for eternity. Material abundance gave rise to megastructure civilization, and the Solar Empire was its most magnificent embodiment: towering, monumental, seemingly able to withstand time itself. We once believed it would endure forever. Only later did we understand that immortality is often merely an illusion of time, born in those who live at the height of an age.",
    },
  },
  {
    id: "mystic-cat",
    glyph: { zh: "猫", en: "MC" },
    title: { zh: "灵猫", en: "Mystic Cat" },
    kicker: { zh: "档案 III · 安娜的区域", en: "Archive III · Anna's Region" },
    status: { zh: "伏笔开放", en: "Foreshadowed" },
    theme: { zh: "动物意识 · 时间井", en: "Animal Consciousness · Time Well" },
    accent: "#e2a72b",
    cover: { zh: "assets/MC_cn.png", en: "assets/MC_en.png" },
    link: "novels/mystic-cat/",
    description: {
      zh: "安娜被困在非人类意识区域。记录边缘的森林里，有一只能够直视意识的猫影；那里的时间不走直线。",
      en: "Anna is trapped in a non-human consciousness region. At the edge of the archive, a cat-shaped shadow can look directly into the mind.",
    },
  },
  {
    id: "crimson-cruise",
    glyph: { zh: "邮", en: "CC" },
    title: { zh: "血色邮轮", en: "The Crimson Cruise" },
    kicker: { zh: "档案 IV · 海上亡灵", en: "Archive IV · The Sea of the Dead" },
    status: { zh: "预告", en: "Preview" },
    theme: { zh: "邮轮 · 轮回 · 失踪航线", en: "Cruise · Rebirth · Missing Route" },
    accent: "#ff4f9a",
    cover: { zh: "assets/CC_cn.png", en: "assets/CC_en.png" },
    link: "novels/crimson-cruise/",
    description: {
      zh: "一艘驶向未知海域的邮轮，把生者、死者和未完成的记忆带进同一条航线。",
      en: "A cruise ship sails beyond the mapped ocean, carrying the living, the dead, and unfinished memories on the same route.",
    },
  },
  {
    id: "home-soul",
    glyph: { zh: "魂", en: "HS" },
    title: { zh: "灵魂归处", en: "Where Souls Return" },
    kicker: { zh: "档案 V · 归处", en: "Archive V · Return Point" },
    status: { zh: "预留", en: "Reserved" },
    theme: { zh: "归乡 · 意识余辉", en: "Return · Afterglow" },
    accent: "#42d6ff",
    cover: { zh: "assets/WSR_cn.png", en: "assets/WSR_en.png" },
    link: "novels/where-souls-return/",
    description: {
      zh: "当身体和数字人格都不能回答“我是谁”，灵魂也许会寻找第三个归处。",
      en: "When neither body nor digital persona can answer who you are, the soul may search for a third place to return.",
    },
  },
  {
    id: "spacetime-labyrinth",
    glyph: { zh: "迷", en: "SL" },
    title: { zh: "时空迷宫", en: "Spacetime Labyrinth" },
    kicker: { zh: "档案 VI · 时空回环", en: "Archive VI · Spacetime Loop" },
    status: { zh: "预留", en: "Reserved" },
    theme: { zh: "时空 · 迷宫 · 认知回环", en: "Spacetime · Labyrinth · Cognitive Loop" },
    accent: "#7ecbff",
    cover: { zh: "assets/SL_cn.png", en: "assets/SL_en.png" },
    link: "novels/spacetime-labyrinth/",
    description: {
      zh: "一座由时间切片、空间回廊和意识错觉共同构成的迷宫。每一次接近出口，都会把人带回另一个入口。",
      en: "A labyrinth built from time slices, spatial corridors, and perceptual loops. Every exit leads back to another entrance.",
    },
  },
];

const soulVolumeIndex = books.findIndex((book) => book.id === "home-soul");
const soulVolume = soulVolumeIndex >= 0 ? books.splice(soulVolumeIndex, 1)[0] : null;
if (soulVolume) books.push(soulVolume);

const CABIN_COUNT = 6;
const cabinBooks = books.slice(0, CABIN_COUNT);

const reserved = [
  { zh: "数字吉姆", en: "Digital Jim" },
  { zh: "泰拉撒记录", en: "Terasa Records" },
  { zh: "罗斯威尔接口", en: "Roswell Interface" },
  { zh: "主体核", en: "Subject Core" },
];

const uiText = {
  zh: {
    title: "灵接幻想档案",
    htmlLang: "zh-CN",
    navOverview: "档案总览",
    navStory: "故事线",
    brand: "灵接幻想",
    day: "白天",
    night: "夜间",
    enter: "进入小说档案",
    introEyebrow: "另一个世界 · 叙事档案馆",
    introTitle: "灵接幻想",
    introBody:
      "六座灵接舱，六本正在醒来的书。镜头会从中央环形大厅进入每一座舱，展示书卷封面、核心概念与后续阅读入口。",
    archiveEyebrow: "档案索引",
    archiveTitle: "灵接幻想书卷序列",
    archiveLead:
      "已挂入现有封面资源；英文封面暂缺的书卷会先使用中文封面，之后你替换文件即可继续扩展。",
    views: ["书卷总览", "故事线", "关系图谱"],
    graphTip: "拖拽视图 · 悬停高亮 · 点击节点查看说明",
    storyHint: "故事线正在生成……点击任意节点查看事件。",
    graphHint: "点击节点查看说明；悬停可高亮它的所有连接。",
    mainLine: "主线",
    footerCopy: "© 2026 灵接幻想。版权所有。",
    reservedPrefix: "预留舱",
    reservedText: "后续卷宗入口预留。",
  },
  en: {
    title: "Spirit Connect Fantasy Archives",
    htmlLang: "en",
    navOverview: "Archive",
    navStory: "Storylines",
    brand: "SPIRIT CONNECT FANTASY",
    day: "Day",
    night: "Night",
    enter: "Open archive",
    introEyebrow: "Another World · Narrative Archive",
    introTitle: "Spirit Connect Fantasy",
    introBody:
      "Six connection cabins. Six books waking in sequence. The camera moves from the central ring to each cabin, revealing covers, concepts, and reading entry points.",
    archiveEyebrow: "ARCHIVE INDEX",
    archiveTitle: "Spirit Connect Fantasy Book Sequence",
    archiveLead:
      "Current cover assets are wired in. When an English cover is missing, the site falls back to the Chinese cover until you replace it.",
    views: ["Archive", "Story Lines", "Relation Graph"],
    graphTip: "Drag view · Hover to highlight · Click a node",
    storyHint: "The line is drawing... click any node to read the event.",
    graphHint: "Click a node to read about it; hover to light up its connections.",
    mainLine: "Main line",
    footerCopy: "© 2026 Spirit Connect Fantasy. All rights reserved.",
    reservedPrefix: "Reserved Cabin",
    reservedText: "Future volume entry reserved.",
  },
};

const storyBooks = [
  {
    id: "moon",
    glyph: "月",
    accent: "#00e5ff",
    title: { zh: "月球暗面", en: "Darkside of the Moon" },
    subtitle: { zh: "档案 I · 挣脱通往真相的第一道枷锁", en: "Archive I · Break Free from the First Shackle Toward Truth" },
    status: { zh: "已出版", en: "Published" },
    nodes: [
      { zh: ["第二次数字矫正", "2118 年，十八岁的吉姆·维尔走进灵接舱，进行人生第二次数字矫正。这一次，有什么东西没有按程序进行。"], en: ["The Second Correction", "In 2118, Jim Vale enters the connection cabin for his second digital correction. This time, something does not follow the program."] },
      { zh: ["唯一归来者", "吉姆醒来，带着不属于他的记忆。同一批参与者中，安娜·刘易斯与查理·黑尔没有醒来。"], en: ["The Only Returnee", "Jim wakes carrying memories that are not his. Anna Lewis and Charlie Hale do not wake at all."] },
      { zh: ["月暗记录会议", "灵接幻想开始内部追查。卢恩博士第一个意识到：灵接舱连接的，可能不是公司建造的任何东西。"], en: ["The Record Meeting", "Spirit Connect begins its internal investigation. Dr. Lune suspects the cabin may not connect to anything the company built."] },
      { zh: ["人类是宿主", "带回的记录开始与神话逐条对号。月球的工程真相浮出水面：它不完全是一颗天然卫星。"], en: ["Humanity as Host", "The recovered records begin to match myths. The engineering truth of the Moon surfaces: it is not entirely natural."] },
      { zh: ["数字亚瑟", "最早一批上传者之一亚瑟·惠勒已停止生长。数字永生第一次露出它的缺陷。"], en: ["Digital Arthur", "Arthur Wheeler, among the first uploaded, has stopped growing. Digital immortality shows its flaw."] },
      { zh: ["罗斯威尔遗产", "1947 年的残骸、百年逆向工程、2047 年的技术释放，灵接技术的真正来源终于被揭开。"], en: ["The Roswell Legacy", "The 1947 wreckage, a century of reverse engineering, and the 2047 release reveal the origin of connection technology."] },
      { zh: ["死球理论", "肖恩·柯宾的危险假说：死在地球，意识会被势阱束缚；死在死球上，也许能挣脱。"], en: ["Dead Sphere Theory", "Shawn Corbin's dangerous hypothesis: die on Earth and consciousness is bound; die on a dead sphere and it may slip free."] },
      { zh: ["解构倒计时", "艾拉告诉吉姆真相：安娜与查理正被月暗系统判定为异常意识，并被解构。"], en: ["The Countdown", "Elara tells Jim the truth: Anna and Charlie are being read as anomalies and deconstructed."] },
      { zh: ["LUNA-EXIT", "斯皮尔的旧梦浮出水面：终点不是保存，而是迁出。吉姆决定用真正的肉体登月。"], en: ["LUNA-EXIT", "Spire's sealed program surfaces: the endpoint is not preservation, but migration. Jim decides to go to the Moon in the flesh."] },
      { zh: ["发射与着陆", "穿过不可返回区域，吉姆在月球暗面着陆。没有副本，没有远程连接，没有退路。"], en: ["Launch & Landing", "Through the no-return zone, Jim lands on the far side. No copy, no remote link, no way back."] },
      { zh: ["肉体死亡", "吉姆完成肉体死亡，进入真实的泰拉撒记录。第一道枷锁，从里面断开了。"], en: ["Death of the Body", "Jim completes his bodily death and enters the true Terasa Records. The first shackle breaks from within."] },
      { zh: ["下一本入口", "泰拉撒深处，数字吉姆仍然存在。困着安娜与查理的两片区域开始微微发亮。"], en: ["The Next Entrance", "Deep in Terasa, digital Jim still exists. The regions holding Anna and Charlie begin to glow."] },
    ],
    branches: [
      { from: 1, dir: "up", label: { zh: "数字吉姆的记忆碎片", en: "Fragments of Digital Jim" }, nodes: [
        { zh: ["黑水与苏醒", "那段借来的记忆，开始于黑水，开始于从黑水中醒来。"], en: ["Black Water", "The borrowed memory begins in black water, and in waking from it."] },
        { zh: ["石门之后的战场", "石门之后是远古战场，巨鲸形的阴影掠过不属于任何已知文明的骨骸。"], en: ["The Battlefield", "Beyond a stone gate lies an ancient battlefield, with whale-shaped shadows over impossible bones."] },
        { zh: ["稻田与小女孩", "沙路尽头的稻田里，一个小女孩直视着吉姆的意识。他后来给她起名：艾拉。"], en: ["The Rice Field", "At the end of a sand road, a little girl looks straight into Jim's consciousness. He names her Elara."] },
        { zh: ["时间井", "一颗蓝黑色的球体，和一口时间不走直线的井。"], en: ["The Time Well", "A blue-black sphere, and a well in which time is not a line."] },
      ] },
      { from: 7, dir: "down", label: { zh: "被困者", en: "The Trapped" }, nodes: [
        { zh: ["安娜的区域", "记录边缘的树林里，有一只能直视意识的猫影。《灵猫》的入口。"], en: ["Anna's Region", "At the treeline, a cat-shadow can look into a mind. The entrance to Mystic Cat."] },
        { zh: ["查理的区域", "时间切片中闪过尸山，和一头从天而降的巨鲸。《巨鲸陨落》的入口。"], en: ["Charlie’s Region", "A time-slice flashes a mountain of the dead and a whale falling from the sky. The entrance to Whale Fall."] },
      ] },
    ],
  },
  {
    id: "whale",
    glyph: "鲸",
    accent: "#7c4dff",
    title: { zh: "巨鲸陨落", en: "Whale Fall" },
    subtitle: { zh: "档案 II · 法厄同证词", en: "Archive II · Phaethon Testimony" },
    status: { zh: "阅读稿已接入", en: "Reading Draft Added" },
    nodes: [
      { zh: ["尸山之上", "查理在一具陌生的身体里醒来，站在尸体堆成的山上。"], en: ["Mountain of the Dead", "Charlie wakes in a stranger's body, standing on a mountain of corpses."] },
      { zh: ["巨鲸从天而降", "天空开始震动。一头燃烧的巨鲸自高空坠落，像星舰，也像文明的记忆。"], en: ["The Whale Falls", "The sky shudders. A burning whale descends like a starship and a civilization's memory."] },
      { zh: ["宿主的名字", "这具身体叫洛安：远古战争的一名普通幸存者。"], en: ["The Host's Name", "The body is called Loan, an ordinary survivor of an ancient war."] },
      { zh: ["谁赢了", "五族残骸铺满战场。所有人都以为战争胜利了，直到有人问：赢的是谁？"], en: ["Who Won", "The remains of five peoples cover the field. Everyone thinks the war is won until someone asks: by whom?"] },
      { zh: ["战争的真相", "这不是资源战争。地球是正在成形的生命孵化场。"], en: ["Truth of the War", "This is not a resource war. Earth is a forming incubator of life."] },
      { zh: ["巨鲸不是武器", "巨鲸族是星海的记忆载体，活的文明档案库。坠落从来不是攻击。"], en: ["Not a Weapon", "The whale-kind are memory vessels of the star sea. The fall was never an attack."] },
      { zh: ["种子", "巨鲸族把一部分记忆、频率与生物蓝图封进年轻海洋的生命演化链。"], en: ["The Seed", "The whale-kind seal memory, frequency, and biological blueprint into the young ocean."] },
      { zh: ["小行星带的诞生", "法厄同下沉碎裂。胜利者在残骸上争吵，只同意一件事：没有一族配拥有地球。"], en: ["The Belt Is Born", "Phaethon shatters. The victors agree on only one thing: no people deserves Earth."] },
      { zh: ["蓝鲸在地球歌唱", "亿万年后，那颗种子长成了地球上最大的动物。查理听见了歌声。"], en: ["The Blue Whale Sings", "Ages later, the seed has become Earth's largest animal. Charlie hears the song."] },
      { zh: ["宿主最后的选择", "洛安的故事走到尽头。怕死的人，也可能是最后一个站着的见证者。"], en: ["The Host's Choice", "Loan's story reaches its end. The one afraid to die may be the last witness standing."] },
      { zh: ["回声归档", "记录闭合。查理把这场战争看到了最后。"], en: ["Echo Archived", "The record closes. Charlie watches the war through to its end."] },
      { zh: ["没有完全死去", "巨鲸死在星空里，醒在地球的海中。"], en: ["Not Entirely Dead", "The whale died among the stars, and woke in the seas of Earth."] },
    ],
    branches: [
      { from: 4, dir: "up", label: { zh: "五族的愿望", en: "Five Peoples" }, nodes: [
        { zh: ["日辉族", "想要人类跪拜。"], en: ["Sunbright", "Wanted humanity kneeling."] },
        { zh: ["鳞裔族", "想要漫长的地底潜伏。"], en: ["Scale-Kin", "Wanted a long concealment underground."] },
        { zh: ["节肢族", "想要一个没有孤独的世界。"], en: ["Chitinous", "Wanted a world without loneliness."] },
        { zh: ["渊民族", "想把记忆交给海。"], en: ["Abyssals", "Wanted to give memory to the sea."] },
        { zh: ["震翼族", "只想天空还有路。"], en: ["Wing-Shiver", "Only wanted the sky to still have roads."] },
      ] },
      { from: 8, dir: "down", label: { zh: "来自外面的信号", en: "Signals from Outside" }, nodes: [
        { zh: ["吉姆的信号", "月暗深处，吉姆的信号穿透了记录。"], en: ["Jim's Signal", "From the lunar dark, Jim's signal breaks through the record."] },
        { zh: ["星环", "另一个吉姆，在记录的另一层，看见了同一道星环。"], en: ["The Star Ring", "Another Jim, in another layer, sees the same ring of stars."] },
        { zh: ["查理不想走", "救援终于抵达时，查理犹豫了。他还没有看完。"], en: ["Charlie Hesitates", "When rescue arrives, Charlie hesitates. He has not finished watching."] },
      ] },
    ],
  },
];

const graphTypes = {
  book: { zh: "书卷", en: "Books", color: "#5ef9ff" },
  character: { zh: "人物", en: "Characters", color: "#ffb454" },
  event: { zh: "事件", en: "Events", color: "#a78bfa" },
  concept: { zh: "概念", en: "Concepts", color: "#4dd0a1" },
};

const graphNodes = [
  ["b1", "book", "月球暗面", "Darkside of the Moon", "档案 I · 挣脱通往真相的第一道枷锁。系列入口。", "Archive I · Break Free from the First Shackle Toward Truth. The entrance to the series."],
  ["b2", "book", "巨鲸陨落", "Whale Fall", "档案 II · 法厄同证词。查理在远古战争中的见证。", "Archive II · Phaethon Testimony. Charlie's witness of the ancient war."],
  ["jim", "character", "吉姆·维尔", "Jim Vale", "挣脱第一道枷锁的人。", "The one who breaks free from the first shackle."],
  ["djim", "character", "数字吉姆", "Digital Jim", "吉姆的数字双生体，主体核问题的入口。", "Jim's digital twin, entrance to the Subject Core problem."],
  ["anna", "character", "安娜·刘易斯", "Anna Lewis", "困于非人类意识区域，《灵猫》的入口。", "Trapped in non-human consciousness; entrance to Mystic Cat."],
  ["charlie", "character", "查理·黑尔", "Charlie Hale", "困于法厄同终战记录中的普通见证者。", "The ordinary witness trapped in the Phaethon record."],
  ["elara", "character", "艾拉", "Elara", "小女孩形态只是投影，她的立场仍未解。", "The little girl is a projection; her allegiance remains open."],
  ["spire", "character", "伊莱亚斯·斯皮尔", "Elias Spire", "灵接幻想创始人，迁出执念的源头。", "Founder of Spirit Connect and origin of the migration obsession."],
  ["lune", "character", "卢恩博士", "Dr. Lune", "现实侧的伦理见证者。", "The ethical witness on the reality side."],
  ["arthur", "character", "亚瑟·惠勒", "Arthur Wheeler", "最早上传者之一，其停滞是关键证据。", "One of the first uploaded; his stagnation is key evidence."],
  ["corbin", "character", "肖恩·柯宾", "Shawn Corbin", "死球理论提出者。", "Author of the Dead Sphere Theory."],
  ["loan", "character", "洛安", "Loan", "查理在远古战场醒来时所在的身体。", "The host body Charlie wakes in."],
  ["e1947", "event", "罗斯威尔坠毁", "Roswell Crash", "意识接口残骸的起点。", "The beginning of the consciousness-interface wreckage."],
  ["e2047", "event", "技术释放", "The Release", "百年逆向工程进入公众世界。", "A century of reverse engineering enters the public world."],
  ["e2053", "event", "黑潮", "Black Tide", "物质文明信仰崩塌。", "Faith in material civilization collapses."],
  ["e2118", "event", "矫正事故", "Correction Incident", "吉姆返回，安娜与查理没有醒来。", "Jim returns; Anna and Charlie do not wake."],
  ["ecount", "event", "解构倒计时", "Deconstruction Countdown", "异常意识被月暗系统解构。", "Anomalous minds are deconstructed by the lunar system."],
  ["emoon", "event", "月面肉体死亡", "Death on the Moon", "吉姆进入真实泰拉撒记录。", "Jim enters the true Terasa Records."],
  ["ewar", "event", "法厄同终战", "Phaethon War", "围绕地球未来的太阳系终战。", "The final solar-system war over Earth's future."],
  ["efall", "event", "巨鲸坠落", "The Whale Falls", "星舰般的巨鲸撕裂法厄同。", "A starship-like whale tears Phaethon apart."],
  ["cabin", "concept", "灵接舱", "Connection Cabin", "低阶意识接口。", "A low-order consciousness interface."],
  ["twin", "concept", "双生模式", "Twin Mode", "肉体与数字生命并行发展。", "Physical and digital lives develop in parallel."],
  ["core", "concept", "主体核", "Subject Core", "只能迁移，永不可复制。", "Can only migrate; can never be copied."],
  ["dead", "concept", "死球理论", "Dead Sphere Theory", "死亡地点决定意识去向的危险假说。", "The dangerous hypothesis that death location determines consciousness destination."],
  ["terasa", "concept", "泰拉撒记录", "Terasa Records", "月球暗面的古老记录系统。", "The ancient recording system on the lunar far side."],
  ["luna", "concept", "LUNA-EXIT", "LUNA-EXIT", "终点不是保存，而是迁出。", "The endpoint is not preservation, but migration."],
  ["roswell", "concept", "罗斯威尔接口", "Roswell Interface", "意识结构直接耦合的接口。", "An interface coupled directly to consciousness."],
  ["song", "concept", "蓝鲸歌声", "Whale Song", "封进海洋生命链的低频回声。", "A low-frequency echo sealed into ocean life."],
  ["whalekind", "concept", "巨鲸族", "Whale-Kind", "星海的记忆载体。", "Memory vessels of the star sea."],
  ["five", "concept", "五族", "Five Peoples", "远古战争中的五个族群。", "The five peoples of the ancient war."],
  ["incub", "concept", "地球孵化场", "Earth Incubator", "地球作为生命实验场。", "Earth as a life experiment."],
  ["cat", "concept", "灵猫文明", "Spirit-Cat Network", "动物意识的高阶网络。", "A higher network of animal consciousness."],
].map(([id, type, zh, en, zhd, end]) => ({ id, type, label: { zh, en }, d: { zh: zhd, en: end } }));

const graphLinks = [["b1","jim"],["b1","e2118"],["b1","elara"],["b1","terasa"],["b1","emoon"],["b1","ecount"],["b2","charlie"],["b2","ewar"],["b2","efall"],["b2","loan"],["b2","five"],["jim","djim"],["jim","anna"],["jim","charlie"],["jim","e2118"],["jim","elara"],["jim","emoon"],["jim","lune"],["jim","spire"],["djim","terasa"],["djim","core"],["anna","e2118"],["anna","cat"],["anna","ecount"],["charlie","e2118"],["charlie","loan"],["charlie","efall"],["charlie","ecount"],["charlie","song"],["elara","terasa"],["spire","luna"],["spire","arthur"],["spire","cabin"],["lune","cabin"],["arthur","core"],["corbin","dead"],["dead","emoon"],["luna","emoon"],["cabin","twin"],["cabin","roswell"],["twin","e2118"],["twin","core"],["roswell","e1947"],["e1947","e2047"],["e2047","e2053"],["e2053","cabin"],["terasa","incub"],["ewar","five"],["ewar","incub"],["ewar","efall"],["whalekind","efall"],["whalekind","song"],["cat","terasa"]];

const themes = {
  day: {
    bg: "#eee8dc",
    fog: "#f2eee6",
    fogNear: 420,
    fogFar: 1200,
    floor: "#c9c0b0",
    shell: "#b9c0c6",
    pearl: "#8e9aa5",
    glass: "#55b5d7",
    darkGlass: "#263b4d",
    rail: "#66717a",
    hemiSky: "#f8f1e5",
    hemiGround: "#5d6570",
    hemiIntensity: 1.14,
    keyIntensity: 2.72,
    env: 0.3,
    bloom: 0.28,
  },
  night: {
    bg: "#04080f",
    fog: "#07111f",
    fogNear: 80,
    fogFar: 360,
    floor: "#172234",
    shell: "#253348",
    pearl: "#33455f",
    glass: "#42c9ff",
    darkGlass: "#08111e",
    rail: "#6d83a1",
    hemiSky: "#29466f",
    hemiGround: "#03060b",
    hemiIntensity: 0.72,
    keyIntensity: 0.85,
    env: 0.2,
    bloom: 0.85,
  },
};

let language = "zh";
let mode = "day";
let progressTarget = 0;
let progress = 0;
let activeBook = -1;
let pointerX = 0;
let pointerY = 0;
let smoothPointerX = 0;
let smoothPointerY = 0;
let railDragging = false;
let spiritCore = null;

const SECTIONS = 12;
const textureLoader = new THREE.TextureLoader();
const textureCache = new Map();
const canvas = document.getElementById("scene");
const scrollStage = document.getElementById("scroll-stage");
const intro = document.querySelector(".chapter-intro");
const panel = document.querySelector("[data-book-panel]");
const overview = document.querySelector(".overview");
const rail = document.querySelector(".rail");
const railDot = document.getElementById("rail-dot");
const cover = document.getElementById("book-cover");
const glyph = document.getElementById("book-glyph");
const kicker = document.getElementById("book-kicker");
const title = document.getElementById("book-title");
const description = document.getElementById("book-description");
const statusEl = document.getElementById("book-status");
const themeEl = document.getElementById("book-theme");
const link = document.getElementById("book-link");
const archiveList = document.getElementById("archive-list");

const els = {
  navOverview: document.querySelector("[data-i18n='navOverview']"),
  navStory: document.querySelector("[data-i18n='navStory']"),
  brand: document.querySelector("[data-i18n='brand']"),
  introEyebrow: document.querySelector("[data-i18n='introEyebrow']"),
  introTitle: document.querySelector("[data-i18n='introTitle']"),
  introBody: document.querySelector("[data-i18n='introBody']"),
  archiveEyebrow: document.querySelector("[data-i18n='archiveEyebrow']"),
  archiveTitle: document.querySelector("[data-i18n='archiveTitle']"),
  archiveLead: document.querySelector("[data-i18n='archiveLead']"),
  graphTip: document.querySelector("[data-i18n='graphTip']"),
  footerCopy: document.querySelector("[data-i18n='footerCopy']"),
  bookLink: document.querySelector("[data-i18n='enter']"),
  langButtons: [...document.querySelectorAll("[data-lang]")],
  modeButtons: [...document.querySelectorAll("[data-mode]")],
  finalViewButtons: [...document.querySelectorAll("[data-final-view]")],
};

const storyEls = {
  list: document.getElementById("story-book-list"),
  canvas: document.getElementById("storyline-canvas"),
  detail: document.getElementById("storyline-detail"),
  graph: document.getElementById("relation-graph"),
  graphDetail: document.getElementById("graph-detail"),
  graphChips: document.getElementById("graph-chips"),
};

let selectedStoryBook = storyBooks[0];
let selectedGraphNode = null;
let hoveredGraphNode = null;
let graphInitialized = false;
let graphHiddenTypes = {};
let graphCamera = { x: 0, y: 0, k: 1 };
let graphAlpha = 1;
let graphLinksResolved = [];
let graphNeighbors = {};
let graphDraggingNode = null;
let graphPanning = false;
let graphLastPointer = null;
let graphPointerMoved = false;
let storyDragging = false;
let storyPointerStart = null;
let storyPointerMoved = false;
let storySuppressClick = false;
const storyCamera = { x: 0, y: 0, k: 1 };

scrollStage.style.position = "fixed";
scrollStage.style.inset = "0";
scrollStage.style.overflowY = "auto";
scrollStage.style.overflowX = "hidden";
scrollStage.style.overscrollBehavior = "none";
scrollStage.style.zIndex = "2";
scrollStage.querySelector(".scroll-space").style.height = `${SECTIONS * 100}vh`;

const renderer = new THREE.WebGLRenderer({
  canvas,
  antialias: true,
  alpha: false,
  powerPreference: "high-performance",
});
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.08;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(58, window.innerWidth / window.innerHeight, 0.1, 900);
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.035).texture;

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  0.52,
  0.58,
  0.66
);
composer.addPass(bloom);
composer.addPass(new OutputPass());

const hemi = new THREE.HemisphereLight("#ffffff", "#8793a0", 1.35);
scene.add(hemi);

const keyLight = new THREE.DirectionalLight("#ffffff", 3.2);
keyLight.position.set(64, 98, 84);
keyLight.castShadow = true;
keyLight.shadow.mapSize.set(2048, 2048);
keyLight.shadow.camera.left = -190;
keyLight.shadow.camera.right = 190;
keyLight.shadow.camera.top = 190;
keyLight.shadow.camera.bottom = -190;
scene.add(keyLight);

const coolLight = new THREE.PointLight("#40caff", 34, 280, 1.7);
coolLight.position.set(0, 30, 0);
scene.add(coolLight);

const warmLight = new THREE.PointLight("#ffd08a", 12, 190, 2);
warmLight.position.set(-44, 18, 58);
scene.add(warmLight);

const root = new THREE.Group();
scene.add(root);

const mats = {
  floor: new THREE.MeshPhysicalMaterial({ color: "#d6e1ea", roughness: 0.42, metalness: 0.05, clearcoat: 0.28 }),
  white: new THREE.MeshPhysicalMaterial({ color: "#f2f7fb", roughness: 0.3, metalness: 0.08, clearcoat: 0.5, clearcoatRoughness: 0.2 }),
  pearl: new THREE.MeshPhysicalMaterial({ color: "#c3d0dc", roughness: 0.22, metalness: 0.2, clearcoat: 0.8 }),
  glass: new THREE.MeshPhysicalMaterial({ color: "#87d7ff", roughness: 0.05, metalness: 0, transmission: 0.35, transparent: true, opacity: 0.5, clearcoat: 1, side: THREE.DoubleSide }),
  darkGlass: new THREE.MeshPhysicalMaterial({ color: "#18314a", roughness: 0.18, metalness: 0.3, transparent: true, opacity: 0.58, clearcoat: 1 }),
  rail: new THREE.MeshStandardMaterial({ color: "#76899b", roughness: 0.34, metalness: 0.52 }),
  blueGlow: new THREE.MeshStandardMaterial({ color: "#07131d", emissive: "#2bb8ff", emissiveIntensity: 1.55, roughness: 0.4 }),
  goldGlow: new THREE.MeshStandardMaterial({ color: "#1a1206", emissive: "#d79b3a", emissiveIntensity: 0.9, roughness: 0.42 }),
};

const camPositions = buildCameraPositions();
const camTargets = buildCameraTargets();

const posCurve = new THREE.CatmullRomCurve3(camPositions.map((p) => new THREE.Vector3(...p)), false, "centripetal");
const targetCurve = new THREE.CatmullRomCurve3(camTargets.map((p) => new THREE.Vector3(...p)), false, "centripetal");
const camPos = new THREE.Vector3();
const camTarget = new THREE.Vector3();
const clock = new THREE.Clock();

function cabinAngle(index) {
  return (index / CABIN_COUNT) * Math.PI * 2 - Math.PI / 2;
}

function cabinPoint(index, radius = 134, y = 16) {
  const a = cabinAngle(index);
  return new THREE.Vector3(Math.cos(a) * radius, y, Math.sin(a) * radius);
}

function buildCameraPositions() {
  const pts = [
    [0, 122, 340],
    [0, 74, 248],
  ];
  for (let i = 0; i < CABIN_COUNT; i++) {
    const a = cabinAngle(i);
    pts.push([Math.cos(a - 0.28) * 210, 42, Math.sin(a - 0.28) * 210]);
    pts.push([Math.cos(a - 0.08) * 178, 30, Math.sin(a - 0.08) * 178]);
    pts.push([Math.cos(a + 0.14) * 190, 34, Math.sin(a + 0.14) * 190]);
  }
  pts.push([0, 122, 230], [0, 240, 92], [0, 310, 0]);
  return pts;
}

function buildCameraTargets() {
  const pts = [
    [0, 18, 0],
    [0, 16, 0],
  ];
  for (let i = 0; i < CABIN_COUNT; i++) {
    const p = cabinPoint(i, 134, 17);
    const lead = cabinPoint(i, 118, 28);
    pts.push([p.x, p.y, p.z]);
    pts.push([lead.x, lead.y, lead.z]);
    pts.push([p.x, p.y + 8, p.z]);
  }
  pts.push([0, 16, 0], [0, 0, 0], [0, 0, 0]);
  return pts;
}

buildEnvironment();
const capsules = buildCapsules();
const starField = buildParticles();
const sparkleField = buildSparkles();
const bookSprites = buildBookSprites();
wireControls();
const initialLanguage = (() => {
  const requested = new URLSearchParams(window.location.search).get("lang") || localStorage.getItem("spiritConnectLang");
  return requested === "en" || requested === "zh" ? requested : "zh";
})();
applyLanguage(initialLanguage);
applyTheme("night");
onResize();
onScroll();
animate();

function getCover(book) {
  return book.cover[language] || book.cover.zh || book.cover.en;
}

function getTexture(url) {
  if (!textureCache.has(url)) {
    const texture = textureLoader.load(url);
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.anisotropy = 8;
    textureCache.set(url, texture);
  }
  return textureCache.get(url);
}

function buildEnvironment() {
  const floor = new THREE.Mesh(new THREE.CircleGeometry(230, 180), mats.floor);
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  root.add(floor);

  const headRing = new THREE.Mesh(new THREE.TorusGeometry(148, 1.05, 14, 192), mats.blueGlow);
  headRing.rotation.x = Math.PI / 2;
  headRing.position.y = 0.9;
  headRing.scale.set(1, 1, 0.92);
  headRing.castShadow = true;
  headRing.receiveShadow = true;
  root.add(headRing);

  const tailRing = new THREE.Mesh(new THREE.TorusGeometry(118, 0.8, 14, 192), mats.goldGlow);
  tailRing.rotation.x = Math.PI / 2;
  tailRing.position.y = 1.08;
  tailRing.scale.set(1, 1, 0.88);
  tailRing.castShadow = true;
  tailRing.receiveShadow = true;
  root.add(tailRing);

  const dome = new THREE.Mesh(
    new THREE.SphereGeometry(282, 96, 32, 0, Math.PI * 2, 0, Math.PI / 2.18),
    new THREE.MeshPhysicalMaterial({
      color: "#b9d1e4",
      roughness: 0.16,
      metalness: 0.02,
      transparent: true,
      opacity: 0.18,
      side: THREE.DoubleSide,
    })
  );
  dome.name = "dome-shell";
  dome.position.y = -8;
  dome.scale.y = 0.82;
  root.add(dome);

  const core = new THREE.Mesh(new THREE.CylinderGeometry(26, 34, 8, 72), mats.pearl);
  core.position.y = 4;
  core.castShadow = true;
  core.receiveShadow = true;
  root.add(core);

  const coreRing = new THREE.Mesh(new THREE.TorusGeometry(38, 0.8, 12, 140), mats.blueGlow);
  coreRing.rotation.x = Math.PI / 2;
  coreRing.position.y = 9.2;
  root.add(coreRing);

  spiritCore = buildSpiritLogoCore();
  root.add(spiritCore.group);
}

function buildSpiritLogoCore() {
  const group = new THREE.Group();
  group.name = "spirit-logo-core";

  const logoTexture = getTexture("assets/spirit-connect-logo.png");
  const layers = [];
  const layerSettings = [
    { scale: [50, 41], opacity: 0.16, color: "#49d6ff", z: -2.2 },
    { scale: [42, 34], opacity: 0.28, color: "#7fe6ff", z: -1.1 },
    { scale: [34, 28], opacity: 0.96, color: "#eafbff", z: 0 },
  ];

  layerSettings.forEach((setting, index) => {
    const mat = new THREE.SpriteMaterial({
      map: logoTexture,
      color: setting.color,
      transparent: true,
      opacity: setting.opacity,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
    });
    const sprite = new THREE.Sprite(mat);
    sprite.position.set(0, 37, setting.z);
    sprite.scale.set(setting.scale[0], setting.scale[1], 1);
    sprite.userData.baseScale = setting.scale;
    sprite.userData.baseOpacity = setting.opacity;
    sprite.userData.phase = index * 0.7;
    group.add(sprite);
    layers.push(sprite);
  });

  const floorWaves = [];
  for (let i = 0; i < 5; i++) {
    const mat = new THREE.MeshBasicMaterial({
      color: i % 2 ? "#8fefff" : "#27bdff",
      transparent: true,
      opacity: 0.26,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
    });
    const ring = new THREE.Mesh(new THREE.TorusGeometry(25, 0.16, 8, 144), mat);
    ring.rotation.x = Math.PI / 2;
    ring.position.y = 16 + i * 1.2;
    ring.userData.phase = i / 5;
    group.add(ring);
    floorWaves.push(ring);
  }

  const particleCount = 280;
  const pos = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);
  const phases = new Float32Array(particleCount);
  const cyan = new THREE.Color("#6ce8ff");
  const white = new THREE.Color("#ffffff");
  for (let i = 0; i < particleCount; i++) {
    const a = Math.random() * Math.PI * 2;
    const r = 6 + Math.random() * 34;
    const y = 16 + Math.random() * 48;
    const b = i * 3;
    pos[b] = Math.cos(a) * r;
    pos[b + 1] = y;
    pos[b + 2] = Math.sin(a) * r * 0.62;
    const c = cyan.clone().lerp(white, Math.random() * 0.35);
    colors[b] = c.r;
    colors[b + 1] = c.g;
    colors[b + 2] = c.b;
    phases[i] = Math.random() * Math.PI * 2;
  }
  const particleGeo = new THREE.BufferGeometry();
  particleGeo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  particleGeo.setAttribute("color", new THREE.BufferAttribute(colors, 3));
  const particleMat = new THREE.PointsMaterial({
    size: 0.74,
    vertexColors: true,
    transparent: true,
    opacity: 0.46,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
  const particles = new THREE.Points(particleGeo, particleMat);
  particles.userData.base = pos.slice();
  particles.userData.phases = phases;
  group.add(particles);

  return { group, layers, floorWaves, particles };
}

function buildCapsules() {
  const group = new THREE.Group();
  const items = [];
  const podGeo = new THREE.CapsuleGeometry(8, 26, 12, 26);
  const baseGeo = new THREE.BoxGeometry(19, 4, 46);
  const canopyGeo = new THREE.CapsuleGeometry(6.7, 20, 10, 22);

  for (let i = 0; i < CABIN_COUNT; i++) {
    const angle = cabinAngle(i);
    const pod = new THREE.Group();
    const book = cabinBooks[i] || null;
    pod.position.set(Math.cos(angle) * 134, 3.8, Math.sin(angle) * 134);
    pod.rotation.y = -angle + Math.PI / 2;

    const base = new THREE.Mesh(baseGeo, mats.pearl);
    base.position.y = -1.9;
    base.castShadow = true;
    base.receiveShadow = true;
    pod.add(base);

    const body = new THREE.Mesh(podGeo, mats.white);
    body.rotation.x = Math.PI / 2;
    body.scale.set(1.08, 1.0, 0.68);
    body.position.y = 2;
    body.castShadow = true;
    body.receiveShadow = true;
    pod.add(body);

    const canopy = new THREE.Mesh(canopyGeo, book ? mats.glass : mats.darkGlass);
    canopy.rotation.x = Math.PI / 2;
    canopy.scale.set(0.78, 0.82, 0.4);
    canopy.position.set(0, 6.6, -1.6);
    pod.add(canopy);

    const rimMat = book
      ? new THREE.MeshStandardMaterial({ color: "#07131d", emissive: book.accent, emissiveIntensity: 1.2, roughness: 0.4 })
      : mats.rail;
    const rim = new THREE.Mesh(new THREE.TorusGeometry(7.05, 0.32, 10, 84), rimMat);
    rim.rotation.x = Math.PI / 2;
    rim.position.set(0, 6.83, -1.6);
    rim.scale.set(1, 1.58, 1);
    pod.add(rim);

    group.add(pod);
    items.push({ pod, book, rimMat });
  }
  root.add(group);
  return items;
}

function buildParticles() {
  const count = 1000;
  const pos = new Float32Array(count * 3);
  const colors = new Float32Array(count * 3);
  const blue = new THREE.Color("#67d8ff");
  const amber = new THREE.Color("#ffd078");
  for (let i = 0; i < count; i++) {
    const a = Math.random() * Math.PI * 2;
    const r = 36 + Math.random() * 214;
    pos[i * 3] = Math.cos(a) * r;
    pos[i * 3 + 1] = 8 + Math.random() * 150;
    pos[i * 3 + 2] = Math.sin(a) * r;
    const c = blue.clone().lerp(amber, Math.random() * 0.25);
    colors[i * 3] = c.r;
    colors[i * 3 + 1] = c.g;
    colors[i * 3 + 2] = c.b;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  geo.setAttribute("color", new THREE.BufferAttribute(colors, 3));
  const mat = new THREE.PointsMaterial({
    size: 1.05,
    vertexColors: true,
    transparent: true,
    opacity: 0.64,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
  const points = new THREE.Points(geo, mat);
  root.add(points);
  return points;
}

function makeSparkTexture(kind) {
  const c = document.createElement("canvas");
  c.width = 96;
  c.height = 96;
  const ctx = c.getContext("2d");
  ctx.clearRect(0, 0, 96, 96);
  const g = ctx.createRadialGradient(48, 48, 0, 48, 48, 46);
  g.addColorStop(0, "rgba(255,255,255,1)");
  g.addColorStop(0.38, "rgba(120,220,255,.7)");
  g.addColorStop(1, "rgba(120,220,255,0)");
  ctx.fillStyle = g;
  if (kind === "star") {
    ctx.beginPath();
    ctx.moveTo(48, 4);
    ctx.lineTo(58, 38);
    ctx.lineTo(92, 48);
    ctx.lineTo(58, 58);
    ctx.lineTo(48, 92);
    ctx.lineTo(38, 58);
    ctx.lineTo(4, 48);
    ctx.lineTo(38, 38);
    ctx.closePath();
    ctx.fill();
  } else {
    ctx.beginPath();
    ctx.arc(48, 48, kind === "square" ? 18 : 24, 0, Math.PI * 2);
    ctx.fill();
  }
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

function buildSparkles() {
  const group = new THREE.Group();
  const textures = [makeSparkTexture("dot"), makeSparkTexture("star"), makeSparkTexture("square")];
  for (let i = 0; i < 90; i++) {
    const mat = new THREE.SpriteMaterial({
      map: textures[i % textures.length],
      transparent: true,
      opacity: i % 3 === 1 ? 0.38 : 0.28,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: i % 4 === 0 ? "#ffe7a8" : "#95ddff",
    });
    const s = new THREE.Sprite(mat);
    const a = Math.random() * Math.PI * 2;
    const r = 60 + Math.random() * 210;
    s.position.set(Math.cos(a) * r, 20 + Math.random() * 150, Math.sin(a) * r);
    const size = 2.2 + Math.random() * 5.2;
    s.scale.set(size, size, 1);
    s.userData.phase = Math.random() * Math.PI * 2;
    s.userData.baseOpacity = mat.opacity;
    group.add(s);
  }
  root.add(group);
  return group;
}

function buildBookSprites() {
  const group = new THREE.Group();
  const items = cabinBooks.map((book, i) => {
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({
      map: getTexture(getCover(book)),
      transparent: true,
      opacity: 0.78,
      depthWrite: false,
    }));
    const angle = cabinAngle(i);
    sprite.position.set(Math.cos(angle) * 122, 38, Math.sin(angle) * 122);
    sprite.scale.set(18, 27, 1);
    sprite.visible = true;
    sprite.userData.base = sprite.position.clone();
    group.add(sprite);
    return sprite;
  });
  root.add(group);
  return items;
}

function makeTextSprite(text, color) {
  const c = document.createElement("canvas");
  c.width = 256;
  c.height = 256;
  const ctx = c.getContext("2d");
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.fillStyle = color;
  ctx.font = '800 54px "Microsoft YaHei", sans-serif';
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.shadowColor = "rgba(0,0,0,.35)";
  ctx.shadowBlur = 10;
  ctx.fillText(text, 128, 130);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  return new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false }));
}

function wireControls() {
  els.langButtons.forEach((btn) => btn.addEventListener("click", () => applyLanguage(btn.dataset.lang)));
  els.modeButtons.forEach((btn) => btn.addEventListener("click", () => applyTheme(btn.dataset.mode)));
  wireStoryPan();
  els.finalViewButtons.forEach((btn) => {
    btn.addEventListener("click", () => showFinalView(btn.dataset.finalView));
  });
  els.navOverview.addEventListener("click", (ev) => {
    ev.preventDefault();
    jumpToFinal("archive");
  });
  els.navStory.addEventListener("click", (ev) => {
    ev.preventDefault();
    jumpToFinal("storyline");
  });
}

function applyLanguage(next) {
  language = next;
  localStorage.setItem("spiritConnectLang", language);
  const copy = uiText[language];
  document.title = copy.title;
  document.documentElement.lang = copy.htmlLang;
  document.body.dataset.lang = language;
  els.navOverview.textContent = copy.navOverview;
  els.navStory.textContent = copy.navStory;
  els.brand.textContent = copy.brand;
  els.introEyebrow.textContent = copy.introEyebrow;
  els.introTitle.textContent = copy.introTitle;
  if (els.introBody) els.introBody.textContent = copy.introBody;
  els.archiveEyebrow.textContent = copy.archiveEyebrow;
  els.archiveTitle.textContent = copy.archiveTitle;
  els.archiveLead.textContent = copy.archiveLead;
  els.graphTip.textContent = copy.graphTip;
  els.footerCopy.textContent = copy.footerCopy;
  els.bookLink.textContent = copy.enter;
  els.finalViewButtons.forEach((btn, i) => {
    btn.textContent = copy.views[i];
  });
  els.langButtons.forEach((btn) => btn.classList.toggle("is-active", btn.dataset.lang === language));
  els.modeButtons.forEach((btn) => {
    btn.textContent = btn.dataset.mode === "day" ? copy.day : copy.night;
  });
  bookSprites?.forEach((sprite, i) => {
    sprite.material.map = getTexture(getCover(cabinBooks[i]));
    sprite.material.needsUpdate = true;
  });
  buildArchive();
  buildStoryline();
  setupGraph();
  drawRelationGraph();
  setActiveBook(activeBook < 0 ? 0 : activeBook, true);
}

function bookLinkFor(linkTarget) {
  return `${linkTarget}${linkTarget.includes("?") ? "&" : "?"}lang=${language}`;
}

function applyTheme(next) {
  mode = next;
  const t = themes[mode];
  document.body.dataset.theme = mode;
  scene.background = new THREE.Color(t.bg);
  scene.fog = new THREE.Fog(t.fog, t.fogNear, t.fogFar);
  scene.environmentIntensity = t.env;
  renderer.toneMappingExposure = mode === "day" ? 1.0 : 0.92;
  hemi.color.set(t.hemiSky);
  hemi.groundColor.set(t.hemiGround);
  hemi.intensity = t.hemiIntensity;
  keyLight.intensity = t.keyIntensity;
  bloom.strength = t.bloom;
  mats.floor.color.set(t.floor);
  mats.white.color.set(t.shell);
  mats.pearl.color.set(t.pearl);
  mats.glass.color.set(t.glass);
  mats.darkGlass.color.set(t.darkGlass);
  mats.rail.color.set(t.rail);
  els.modeButtons.forEach((btn) => btn.classList.toggle("is-active", btn.dataset.mode === mode));
}

function buildArchive() {
  const copy = uiText[language];
  const items = [
    ...books.map((book) => ({
      title: book.title[language] || book.title.zh,
      text: `${book.kicker[language] || book.kicker.zh}。${book.theme[language] || book.theme.zh}。${(book.description[language] || book.description.zh).slice(0, 86)}...`,
      empty: false,
      cover: getCover(book),
      link: bookLinkFor(book.link),
    })),
    ...reserved.map((name, i) => ({
      title: `${copy.reservedPrefix} ${String(i + books.length + 1).padStart(2, "0")}`,
      text: `${name[language] || name.zh} · ${copy.reservedText}`,
      empty: true,
    })),
  ];

  archiveList.innerHTML = items
    .map(
      (item) => `
        <${item.link ? `a href="${item.link}"` : "article"} class="archive-card ${item.empty ? "is-empty" : ""}">
          ${item.cover ? `<span class="archive-thumb" style="background-image:url('${item.cover}')"></span>` : ""}
          <strong>${item.title}</strong>
          <p>${item.text}</p>
          ${item.link ? `<span class="archive-card-link">${copy.enter}</span>` : ""}
        </${item.link ? "a" : "article"}>
      `
    )
    .join("");
}

function showFinalView(view) {
  els.finalViewButtons.forEach((btn) => btn.classList.toggle("is-active", btn.dataset.finalView === view));
  document.querySelectorAll(".final-view").forEach((el) => el.classList.remove("is-active"));
  document.getElementById(`final-${view}`).classList.add("is-active");
  if (view === "storyline") buildStoryline();
  if (view === "graph") {
    setupGraph();
    drawRelationGraph();
  }
}

function jumpToFinal(view) {
  showFinalView(view);
  scrollStage.scrollTop = scrollStage.scrollHeight - scrollStage.clientHeight;
  onScroll();
}

function storyNodeText(node) {
  const pair = node[language] || node.zh || node.en;
  return { t: pair[0], d: pair[1] };
}

function getStoryCover(book) {
  const source = book.id === "moon" ? books[0] : book.id === "whale" ? books[1] : books.find((item) => item.title.zh === book.title.zh);
  return source ? getCover(source) : "";
}

function buildStoryline() {
  if (!storyEls.list || !storyEls.canvas) return;
  const copy = uiText[language];
  storyEls.list.innerHTML = "";
  storyBooks.forEach((book) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `story-book ${book === selectedStoryBook ? "is-active" : ""}`;
    button.style.color = book.accent;
    const storyCover = getStoryCover(book);
    button.innerHTML = `
      <span class="story-book-cover" style="background-image:url('${storyCover}')"></span>
      <span><strong>${book.title[language] || book.title.zh}</strong><span>${book.subtitle[language] || book.subtitle.zh} · ${book.status[language] || book.status.zh}</span></span>
    `;
    button.addEventListener("click", () => {
      selectedStoryBook = book;
      buildStoryline();
    });
    storyEls.list.appendChild(button);
  });

  const book = selectedStoryBook;
  const nodes = book.nodes.map(storyNodeText);
  const branchData = (book.branches || []).map((branch) => ({
    ...branch,
    labelText: branch.label[language] || branch.label.zh,
    nodes: branch.nodes.map(storyNodeText),
  }));
  const n = nodes.length;
  const SP = 112;
  const X0 = 80;
  const Y = 252;
  const H = 500;
  let lastX = X0 + (n - 1) * SP;
  branchData.forEach((branch) => {
    const bx = X0 + branch.from * SP + 52 + (branch.nodes.length - 1) * 96;
    if (bx > lastX) lastX = bx;
  });
  const W = lastX + 140;
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", `0 0 ${W} ${H}`);
  svg.setAttribute("width", W);
  svg.setAttribute("height", H);
  svg.setAttribute("class", "story-svg");
  storyEls.canvas.innerHTML = "";
  storyEls.canvas.appendChild(svg);
  applyStoryTransform();

  const defs = document.createElementNS(ns, "defs");
  defs.innerHTML = `<filter id="storyGlow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>`;
  svg.appendChild(defs);

  const add = (tag, attrs, parent = svg) => {
    const el = document.createElementNS(ns, tag);
    Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, v));
    parent.appendChild(el);
    return el;
  };

  add("path", {
    d: `M ${X0} ${Y} L ${X0 + (n - 1) * SP} ${Y}`,
    stroke: book.accent,
    "stroke-width": 2.8,
    fill: "none",
    filter: "url(#storyGlow)",
    "stroke-linecap": "round",
  });

  nodes.forEach((node, i) => {
    const x = X0 + i * SP;
    const group = add("g", { class: "story-node", tabindex: "0" });
    const above = i % 2 === 0;
    add("circle", { cx: x, cy: Y, r: 18, fill: "transparent" }, group);
    add("circle", { cx: x, cy: Y, r: 6, fill: "#0f1b2d", stroke: book.accent, "stroke-width": 2, class: "story-dot", filter: "url(#storyGlow)" }, group);
    const text = add("text", { x, y: above ? Y - 22 : Y + 36, "text-anchor": "middle", class: "story-label" }, group);
    text.textContent = node.t;
    group.addEventListener("click", (ev) => {
      if (storySuppressClick) {
        ev.preventDefault();
        return;
      }
      showStoryDetail(book, node, copy.mainLine, group, svg);
    });
  });

  branchData.forEach((branch) => {
    const sx = X0 + branch.from * SP;
    const dir = branch.dir === "up" ? -1 : 1;
    const by = Y + dir * 86;
    const endX = sx + 52 + (branch.nodes.length - 1) * 96;
    add("path", {
      d: `M ${sx} ${Y} L ${sx + 52} ${by} L ${endX} ${by}`,
      stroke: book.accent,
      "stroke-width": 1.7,
      fill: "none",
      opacity: 0.76,
      "stroke-linecap": "round",
    });
    const label = add("text", { x: endX + 14, y: by + 4, fill: book.accent, class: "story-branch-label" });
    label.textContent = branch.labelText;
    branch.nodes.forEach((node, j) => {
      const x = sx + 52 + j * 96;
      const group = add("g", { class: "story-node", tabindex: "0" });
      add("circle", { cx: x, cy: by, r: 14, fill: "transparent" }, group);
      add("circle", { cx: x, cy: by, r: 4.7, fill: "#0f1b2d", stroke: book.accent, "stroke-width": 1.6, class: "story-dot" }, group);
      const text = add("text", { x, y: dir < 0 ? by - 14 : by + 24, "text-anchor": "middle", class: "story-label story-label-small" }, group);
      text.textContent = node.t;
      group.addEventListener("click", (ev) => {
        if (storySuppressClick) {
          ev.preventDefault();
          return;
        }
        showStoryDetail(book, node, branch.labelText, group, svg);
      });
    });
  });

  storyEls.detail.innerHTML = `<p>${copy.storyHint}</p>`;
}

function wireStoryPan() {
  if (!storyEls.canvas || storyEls.canvas.dataset.panWired) return;
  storyEls.canvas.dataset.panWired = "true";
  storyEls.canvas.addEventListener("pointerdown", onStoryPointerDown);
  storyEls.canvas.addEventListener("pointermove", onStoryPointerMove);
  storyEls.canvas.addEventListener("pointerup", onStoryPointerUp);
  storyEls.canvas.addEventListener("pointercancel", onStoryPointerUp);
  storyEls.canvas.addEventListener("wheel", onStoryWheel, { passive: false });
}

function onStoryPointerDown(ev) {
  if (ev.button !== undefined && ev.button !== 0) return;
  storyDragging = true;
  storyPointerMoved = false;
  storyPointerStart = {
    x: ev.clientX,
    y: ev.clientY,
    cameraX: storyCamera.x,
    cameraY: storyCamera.y,
  };
  storyEls.canvas.setPointerCapture?.(ev.pointerId);
  storyEls.canvas.classList.add("is-dragging");
}

function onStoryPointerMove(ev) {
  if (!storyDragging || !storyPointerStart) return;
  const dx = ev.clientX - storyPointerStart.x;
  const dy = ev.clientY - storyPointerStart.y;
  if (Math.hypot(dx, dy) > 4) storyPointerMoved = true;
  if (!storyPointerMoved) return;
  ev.preventDefault();
  ev.stopPropagation();
  storyCamera.x = storyPointerStart.cameraX + dx;
  storyCamera.y = storyPointerStart.cameraY + dy;
  applyStoryTransform();
}

function onStoryPointerUp(ev) {
  if (!storyDragging) return;
  storyDragging = false;
  storyPointerStart = null;
  storyEls.canvas.releasePointerCapture?.(ev.pointerId);
  storyEls.canvas.classList.remove("is-dragging");
  if (storyPointerMoved) {
    storySuppressClick = true;
    window.setTimeout(() => {
      storySuppressClick = false;
    }, 0);
  }
}

function onStoryWheel(ev) {
  ev.preventDefault();
  ev.stopPropagation();
  const rect = storyEls.canvas.getBoundingClientRect();
  const px = ev.clientX - rect.left;
  const py = ev.clientY - rect.top;
  const worldX = (px - storyCamera.x) / storyCamera.k;
  const worldY = (py - storyCamera.y) / storyCamera.k;
  const nextK = clamp(storyCamera.k * (ev.deltaY < 0 ? 1.12 : 0.9), 0.55, 2.8);
  storyCamera.k = nextK;
  storyCamera.x = px - worldX * nextK;
  storyCamera.y = py - worldY * nextK;
  applyStoryTransform();
}

function applyStoryTransform() {
  const svg = storyEls.canvas?.querySelector(".story-svg");
  if (!svg) return;
  svg.style.transform = `translate(${storyCamera.x}px, ${storyCamera.y}px) scale(${storyCamera.k})`;
}

function showStoryDetail(book, node, context, group, svg) {
  svg.querySelectorAll(".story-node.is-active").forEach((el) => el.classList.remove("is-active"));
  group.classList.add("is-active");
  storyEls.detail.innerHTML = `
    <span class="story-detail-meta" style="color:${book.accent}">${book.title[language] || book.title.zh} · ${context}</span>
    <h3>${node.t}</h3>
    <p>${node.d}</p>
  `;
}

function setupGraph() {
  if (!storyEls.graph || graphInitialized) {
    refreshGraphChips();
    return;
  }
  graphInitialized = true;
  const golden = Math.PI * (3 - Math.sqrt(5));
  graphNodes.forEach((node, i) => {
    const r = 60 + Math.sqrt(i) * 14;
    const a = i * golden;
    node.x = Math.cos(a) * r;
    node.y = Math.sin(a) * r;
    node.vx = 0;
    node.vy = 0;
    node.fixed = false;
    node.r = node.type === "book" ? 15 : node.type === "character" ? 9.5 : 7.5;
  });
  const byId = Object.fromEntries(graphNodes.map((node) => [node.id, node]));
  graphLinksResolved = graphLinks.map(([a, b]) => ({ a: byId[a], b: byId[b] })).filter((link) => link.a && link.b);
  graphNeighbors = Object.fromEntries(graphNodes.map((node) => [node.id, {}]));
  graphLinksResolved.forEach((link) => {
    graphNeighbors[link.a.id][link.b.id] = true;
    graphNeighbors[link.b.id][link.a.id] = true;
  });
  graphNodes.forEach((node) => {
    node.r += Math.min(4, Object.keys(graphNeighbors[node.id]).length * 0.35);
  });
  graphAlpha = 1;
  for (let i = 0; i < 220; i++) stepGraphPhysics();
  graphAlpha = 0.4;
  storyEls.graph.addEventListener("pointerdown", onGraphPointerDown);
  storyEls.graph.addEventListener("pointermove", onGraphPointerMove);
  storyEls.graph.addEventListener("pointercancel", onGraphPointerUp);
  storyEls.graph.addEventListener("mouseleave", () => {
    if (graphDraggingNode || graphPanning) return;
    hoveredGraphNode = null;
    drawRelationGraph();
  });
  window.addEventListener("pointerup", onGraphPointerUp);
  storyEls.graph.addEventListener("click", onGraphClick);
  storyEls.graph.addEventListener("wheel", (ev) => {
    if (overview.classList.contains("is-visible") && overview.scrollTop <= 1 && ev.deltaY < 0) {
      ev.preventDefault();
      ev.stopPropagation();
      const factor = ev.deltaMode === 1 ? 33 : ev.deltaMode === 2 ? window.innerHeight : 1;
      scrollStage.scrollTop += ev.deltaY * factor;
      onScroll();
      return;
    }
    ev.preventDefault();
    ev.stopPropagation();
    const rect = storyEls.graph.getBoundingClientRect();
    const before = graphScreenToWorld(ev.clientX - rect.left, ev.clientY - rect.top, rect);
    graphCamera.k = clamp(graphCamera.k * (ev.deltaY < 0 ? 1.12 : 0.9), 0.55, 2.8);
    const after = graphScreenToWorld(ev.clientX - rect.left, ev.clientY - rect.top, rect);
    graphCamera.x += before.x - after.x;
    graphCamera.y += before.y - after.y;
    drawRelationGraph();
  }, { passive: false });
  refreshGraphChips();
}

function refreshGraphChips() {
  if (!storyEls.graphChips) return;
  storyEls.graphChips.innerHTML = "";
  Object.entries(graphTypes).forEach(([type, meta]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `graph-chip ${graphHiddenTypes[type] ? "" : "is-active"}`;
    button.innerHTML = `<span class="graph-chip-dot" style="background:${meta.color}"></span>${meta[language]}`;
    button.addEventListener("click", () => {
      graphHiddenTypes[type] = !graphHiddenTypes[type];
      reheatGraph();
      refreshGraphChips();
      drawRelationGraph();
    });
    storyEls.graphChips.appendChild(button);
  });
}

function visibleGraphNode(node) {
  return !graphHiddenTypes[node.type];
}

function graphDegree(node) {
  return Object.keys(graphNeighbors[node.id] || {}).length;
}

function reheatGraph() {
  graphAlpha = Math.max(graphAlpha, 0.6);
}

function stepGraphPhysics() {
  for (let i = 0; i < graphNodes.length; i++) {
    const a = graphNodes[i];
    if (!visibleGraphNode(a)) continue;
    for (let j = i + 1; j < graphNodes.length; j++) {
      const b = graphNodes[j];
      if (!visibleGraphNode(b)) continue;
      let dx = a.x - b.x;
      let dy = a.y - b.y;
      const d2 = dx * dx + dy * dy + 0.01;
      if (d2 > 90000) continue;
      const d = Math.sqrt(d2);
      const f = 1300 / d2;
      dx /= d;
      dy /= d;
      a.vx += dx * f;
      a.vy += dy * f;
      b.vx -= dx * f;
      b.vy -= dy * f;
    }
  }

  graphLinksResolved.forEach((link) => {
    if (!visibleGraphNode(link.a) || !visibleGraphNode(link.b)) return;
    let dx = link.b.x - link.a.x;
    let dy = link.b.y - link.a.y;
    const d = Math.sqrt(dx * dx + dy * dy) + 0.01;
    const target = 95 + (link.a.r + link.b.r) * 1.6;
    const f = (d - target) * 0.012;
    dx /= d;
    dy /= d;
    const spring = dx * f * d * 0.02 + dx * f;
    const springY = dy * f * d * 0.02 + dy * f;
    link.a.vx += spring;
    link.a.vy += springY;
    link.b.vx -= spring;
    link.b.vy -= springY;
  });

  graphNodes.forEach((node) => {
    if (!visibleGraphNode(node)) return;
    node.vx -= node.x * 0.004;
    node.vy -= node.y * 0.004;
    if (!node.fixed) {
      node.vx *= 0.86;
      node.vy *= 0.86;
      node.x += node.vx * graphAlpha;
      node.y += node.vy * graphAlpha;
    } else {
      node.vx = 0;
      node.vy = 0;
    }
  });
  graphAlpha = Math.max(0.06, graphAlpha * 0.985);
}

function graphToScreen(node, rect) {
  return {
    x: rect.width / 2 + (node.x - graphCamera.x) * graphCamera.k,
    y: rect.height / 2 + (node.y - graphCamera.y) * graphCamera.k,
  };
}

function graphScreenToWorld(x, y, rect) {
  return {
    x: (x - rect.width / 2) / graphCamera.k + graphCamera.x,
    y: (y - rect.height / 2) / graphCamera.k + graphCamera.y,
  };
}

function pickGraphNode(ev) {
  const rect = storyEls.graph.getBoundingClientRect();
  const world = graphScreenToWorld(ev.clientX - rect.left, ev.clientY - rect.top, rect);
  let best = null;
  let bestD = Infinity;
  graphNodes.forEach((node) => {
    if (!visibleGraphNode(node)) return;
    const dx = node.x - world.x;
    const dy = node.y - world.y;
    const d = dx * dx + dy * dy;
    const hit = node.r + 6;
    if (d < hit * hit && d < bestD) {
      best = node;
      bestD = d;
    }
  });
  return best;
}

function onGraphPointerDown(ev) {
  if (ev.button !== undefined && ev.button !== 0) return;
  ev.preventDefault();
  ev.stopPropagation();
  graphPointerMoved = false;
  graphLastPointer = { x: ev.clientX, y: ev.clientY };
  const picked = pickGraphNode(ev);
  if (picked) {
    graphDraggingNode = picked;
    picked.fixed = true;
    hoveredGraphNode = picked;
  } else {
    graphPanning = true;
    hoveredGraphNode = null;
  }
  storyEls.graph.setPointerCapture?.(ev.pointerId);
  storyEls.graph.style.cursor = "grabbing";
  drawRelationGraph();
}

function onGraphPointerMove(ev) {
  const rect = storyEls.graph.getBoundingClientRect();
  if (graphLastPointer) {
    const dx = ev.clientX - graphLastPointer.x;
    const dy = ev.clientY - graphLastPointer.y;
    if (Math.hypot(dx, dy) > 3) graphPointerMoved = true;

    if (graphDraggingNode) {
      ev.preventDefault();
      ev.stopPropagation();
      const p = graphScreenToWorld(ev.clientX - rect.left, ev.clientY - rect.top, rect);
      graphDraggingNode.x = p.x;
      graphDraggingNode.y = p.y;
      reheatGraph();
      graphLastPointer = { x: ev.clientX, y: ev.clientY };
      drawRelationGraph();
      return;
    }

    if (graphPanning) {
      ev.preventDefault();
      ev.stopPropagation();
      graphCamera.x -= dx / graphCamera.k;
      graphCamera.y -= dy / graphCamera.k;
      graphLastPointer = { x: ev.clientX, y: ev.clientY };
      drawRelationGraph();
      return;
    }
  }

  hoveredGraphNode = pickGraphNode(ev);
  storyEls.graph.style.cursor = hoveredGraphNode ? "grab" : "grab";
  drawRelationGraph();
}

function onGraphPointerUp(ev) {
  if (!graphDraggingNode && !graphPanning) return;
  if (graphDraggingNode) {
    if (!graphPointerMoved) selectGraphNode(graphDraggingNode);
    graphDraggingNode.fixed = false;
    reheatGraph();
  }
  graphDraggingNode = null;
  graphPanning = false;
  graphLastPointer = null;
  storyEls.graph.releasePointerCapture?.(ev.pointerId);
  storyEls.graph.style.cursor = hoveredGraphNode ? "grab" : "grab";
  drawRelationGraph();
}

function onGraphClick(ev) {
  if (graphPointerMoved) {
    graphPointerMoved = false;
    return;
  }
  const picked = pickGraphNode(ev);
  if (!picked) return;
  selectGraphNode(picked);
  return;
  selectedGraphNode = pickGraphNode(ev);
  if (!selectedGraphNode) return;
  const meta = graphTypes[selectedGraphNode.type];
  const count = graphLinks.filter(([a, b]) => a === selectedGraphNode.id || b === selectedGraphNode.id).length;
  storyEls.graphDetail.innerHTML = `
    <span class="story-detail-meta" style="color:${meta.color}">${meta[language]} · ${count}</span>
    <h3>${selectedGraphNode.label[language]}</h3>
    <p>${selectedGraphNode.d[language]}</p>
  `;
  drawRelationGraph();
}

function selectGraphNode(node) {
  selectedGraphNode = node;
  const meta = graphTypes[node.type];
  const count = graphDegree(node);
  storyEls.graphDetail.innerHTML = `
    <span class="story-detail-meta" style="color:${meta.color}">${meta[language]} · ${count}</span>
    <h3>${node.label[language]}</h3>
    <p>${node.d[language]}</p>
  `;
  drawRelationGraph();
}

function drawRelationGraph() {
  if (!storyEls.graph) return;
  const canvas = storyEls.graph;
  const rect = canvas.getBoundingClientRect();
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  if (canvas.width !== Math.floor(rect.width * dpr) || canvas.height !== Math.floor(rect.height * dpr)) {
    canvas.width = Math.floor(rect.width * dpr);
    canvas.height = Math.floor(rect.height * dpr);
  }
  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, rect.width, rect.height);
  const focus = hoveredGraphNode || selectedGraphNode;
  const linked = new Set();
  if (focus) {
    linked.add(focus.id);
    Object.keys(graphNeighbors[focus.id] || {}).forEach((id) => linked.add(id));
  }

  graphLinksResolved.forEach(({ a, b }) => {
    if (!a || !b || !visibleGraphNode(a) || !visibleGraphNode(b)) return;
    const pa = graphToScreen(a, rect);
    const pb = graphToScreen(b, rect);
    const hot = focus && (a.id === focus.id || b.id === focus.id);
    ctx.strokeStyle = hot ? "rgba(94,249,255,.9)" : focus ? "rgba(160,180,210,.08)" : "rgba(160,180,210,.24)";
    ctx.lineWidth = hot ? 1.7 : 1;
    ctx.beginPath();
    ctx.moveTo(pa.x, pa.y);
    ctx.lineTo(pb.x, pb.y);
    ctx.stroke();
  });

  graphNodes.forEach((node) => {
    if (!visibleGraphNode(node)) return;
    const p = graphToScreen(node, rect);
    const meta = graphTypes[node.type];
    const hot = !focus || linked.has(node.id);
    const r = node.r * graphCamera.k;
    ctx.globalAlpha = hot ? 1 : 0.14;
    ctx.shadowColor = meta.color;
    ctx.shadowBlur = node === focus || node === selectedGraphNode ? 22 : 10;
    ctx.fillStyle = meta.color;
    ctx.beginPath();
    ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
    if (node === selectedGraphNode) {
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(p.x, p.y, r + 4, 0, Math.PI * 2);
      ctx.stroke();
    }
    ctx.globalAlpha = hot ? 0.9 : 0.12;
    ctx.fillStyle = mode === "night" ? "#dbe7f6" : "#eef7ff";
    ctx.font = `${node.type === "book" ? 13 : 11}px "Microsoft YaHei", sans-serif`;
    ctx.textAlign = "center";
    ctx.fillText(node.label[language], p.x, p.y + r + 14);
    ctx.globalAlpha = 1;
  });

  if (!selectedGraphNode) {
    storyEls.graphDetail.innerHTML = `<p>${uiText[language].graphHint}</p>`;
  }
}

function setActiveBook(index, force = false) {
  if (index === activeBook && !force) return;
  activeBook = index;
  if (index < 0 || !cabinBooks[index]) return;
  const book = cabinBooks[index];
  glyph.textContent = book.glyph[language] || book.glyph.zh;
  kicker.textContent = book.kicker[language] || book.kicker.zh;
  title.textContent = book.title[language] || book.title.zh;
  description.textContent = book.description[language] || book.description.zh;
  statusEl.textContent = book.status[language] || book.status.zh;
  themeEl.textContent = book.theme[language] || book.theme.zh;
  link.href = bookLinkFor(book.link);
  cover.style.setProperty("--cover-image", `url('${getCover(book)}')`);
  cover.style.borderColor = book.accent;
}

function fadeWindow(p, start, end) {
  const fade = Math.min(0.035, (end - start) * 0.32);
  if (p < start || p > end) return 0;
  if (p < start + fade) return (p - start) / fade;
  if (p > end - fade) return (end - p) / fade;
  return 1;
}

function updateDom(p) {
  railDot.style.top = `${p * 100}%`;
  const introOpacity = p <= 0.105 ? 1 - p / 0.105 : 0;
  intro.classList.toggle("is-visible", introOpacity > 0.02);
  intro.style.opacity = introOpacity.toFixed(3);
  const panelOpacity = fadeWindow(p, 0.11, 0.78);
  panel.classList.toggle("is-visible", panelOpacity > 0.02);
  panel.style.opacity = panelOpacity.toFixed(3);
  panel.style.transform = `translate(-50%, ${-42 + (1 - panelOpacity) * 4}%)`;
  const overviewVisible = p >= 0.82;
  overview.classList.toggle("is-visible", overviewVisible);
  overview.style.opacity = overviewVisible ? "1" : "0";
  overview.style.visibility = overviewVisible ? "visible" : "hidden";
  overview.style.transform = overviewVisible ? "translateY(0)" : "translateY(18px)";

  if (p >= 0.11 && p < 0.78) {
    const local = (p - 0.11) / 0.67;
    setActiveBook(clamp(Math.floor(local * cabinBooks.length), 0, cabinBooks.length - 1));
  } else if (p < 0.16) {
    setActiveBook(-1);
  }
}

function updateScene(dt, elapsed) {
  const t = clamp(progress / 0.86);
  posCurve.getPoint(t, camPos);
  targetCurve.getPoint(t, camTarget);
  smoothPointerX += (pointerX - smoothPointerX) * Math.min(1, dt * 3);
  smoothPointerY += (pointerY - smoothPointerY) * Math.min(1, dt * 3);
  camera.position.copy(camPos);
  camera.lookAt(camTarget);
  camera.translateX(smoothPointerX * 2.2);
  camera.translateY(-smoothPointerY * 1.1);

  root.rotation.y = Math.sin(elapsed * 0.08) * 0.012;
  starField.rotation.y += dt * 0.012;
  starField.material.opacity = mode === "night" ? 0.64 : 0.2;
  sparkleField.rotation.y -= dt * 0.008;
  sparkleField.children.forEach((sprite, i) => {
    const nightBoost = mode === "night" ? 1 : 0.28;
    sprite.material.opacity = sprite.userData.baseOpacity * nightBoost * (0.72 + 0.28 * Math.sin(elapsed * 1.4 + sprite.userData.phase + i));
  });
  coolLight.intensity = (mode === "day" ? 30 : 42) + Math.sin(elapsed * 1.2) * 4;
  warmLight.intensity = mode === "day" ? 12 : 18;
  capsules.forEach((item, i) => {
    const isActive = activeBook === i;
    const pulse = (Math.sin(elapsed * 2.1 + i) + 1) / 2;
    item.pod.position.y = 3.8 + Math.sin(elapsed * 0.7 + i) * 0.25;
    item.pod.scale.setScalar(isActive ? 1.065 : 1);
    if (item.rimMat.emissive) {
      item.rimMat.emissiveIntensity = isActive ? 2.35 + pulse * 0.65 : 0.9 + pulse * 0.18;
    }
  });
  bookSprites.forEach((sprite, i) => {
    const active = activeBook === i && progress > 0.12 && progress < 0.78;
    sprite.visible = true;
    sprite.material.opacity += ((active ? 1 : 0.62) - sprite.material.opacity) * Math.min(1, dt * 4.5);
    const base = sprite.userData.base;
    sprite.position.x = base.x;
    sprite.position.z = base.z;
    sprite.position.y = base.y + Math.sin(elapsed * 1.2 + i) * 0.8 + (active ? 9 + Math.sin(elapsed * 2.4) * 1.5 : 0);
    const targetScale = active ? 1.48 : 1;
    const currentScale = sprite.scale.x / 18;
    const nextScale = currentScale + (targetScale - currentScale) * Math.min(1, dt * 4.5);
    sprite.scale.set(18 * nextScale, 27 * nextScale, 1);
    sprite.lookAt(camera.position);
  });
  updateSpiritCore(dt, elapsed);
}

function updateSpiritCore(dt, elapsed) {
  if (!spiritCore) return;

  const nightBoost = mode === "night" ? 1 : 0.62;
  const pulse = 0.5 + 0.5 * Math.sin(elapsed * 1.65);
  spiritCore.group.rotation.y += dt * 0.09;

  spiritCore.layers.forEach((sprite) => {
    const shimmer = 1 + Math.sin(elapsed * 1.4 + sprite.userData.phase) * 0.035;
    sprite.scale.set(
      sprite.userData.baseScale[0] * shimmer,
      sprite.userData.baseScale[1] * shimmer,
      1
    );
    sprite.material.opacity = sprite.userData.baseOpacity * nightBoost * (0.86 + pulse * 0.14);
  });

  spiritCore.floorWaves.forEach((ring, i) => {
    const phase = (elapsed * 0.28 + ring.userData.phase) % 1;
    const scale = 0.56 + phase * 1.72;
    ring.scale.set(scale, scale, scale);
    ring.position.y = 15.5 + phase * 11.5;
    ring.material.opacity = (mode === "night" ? 0.34 : 0.18) * (1 - phase);
    ring.rotation.z += dt * (0.12 + i * 0.025);
  });

  const attr = spiritCore.particles.geometry.getAttribute("position");
  const base = spiritCore.particles.userData.base;
  const phases = spiritCore.particles.userData.phases;
  for (let i = 0; i < phases.length; i++) {
    const b = i * 3;
    const phase = elapsed * 1.15 + phases[i];
    const radial = 1 + Math.sin(phase * 0.7) * 0.028;
    attr.array[b] = base[b] * radial;
    attr.array[b + 1] = base[b + 1] + Math.sin(phase) * 1.15;
    attr.array[b + 2] = base[b + 2] * radial + Math.cos(phase * 0.83) * 0.7;
  }
  attr.needsUpdate = true;
  spiritCore.particles.material.opacity = (mode === "night" ? 0.5 : 0.26) * (0.78 + pulse * 0.22);
}

function clamp(n, min = 0, max = 1) {
  return Math.min(max, Math.max(min, n));
}

function onScroll() {
  const max = scrollStage.scrollHeight - scrollStage.clientHeight;
  progressTarget = max > 0 ? scrollStage.scrollTop / max : 0;
  if (progressTarget > 0.985) {
    progress = progressTarget;
    updateDom(progress);
  }
}

function onWheel(ev) {
  if (ev.ctrlKey) return;
  if (ev.target?.closest?.(".graph-wrap")) return;
  if (ev.target?.closest?.(".overview")) return;
  ev.preventDefault();
  const factor = ev.deltaMode === 1 ? 33 : ev.deltaMode === 2 ? window.innerHeight : 1;
  scrollStage.scrollTop += ev.deltaY * factor;
  onScroll();
}

function onOverviewWheel(ev) {
  if (!overview.classList.contains("is-visible")) return;
  const factor = ev.deltaMode === 1 ? 33 : ev.deltaMode === 2 ? window.innerHeight : 1;
  const atTop = overview.scrollTop <= 1;
  if (ev.deltaY < 0 && atTop) {
    ev.preventDefault();
    scrollStage.scrollTop += ev.deltaY * factor;
    onScroll();
  }
}

function setScrollFromRail(clientY) {
  const rect = rail.getBoundingClientRect();
  const ratio = clamp((clientY - rect.top) / rect.height);
  const max = scrollStage.scrollHeight - scrollStage.clientHeight;
  scrollStage.scrollTop = ratio * max;
  progressTarget = ratio;
  progress = ratio;
  updateDom(progress);
}

function onRailPointerDown(ev) {
  ev.preventDefault();
  ev.stopPropagation();
  railDragging = true;
  rail.classList.add("is-dragging");
  rail.setPointerCapture?.(ev.pointerId);
  setScrollFromRail(ev.clientY);
}

function onRailPointerMove(ev) {
  if (!railDragging) return;
  ev.preventDefault();
  setScrollFromRail(ev.clientY);
}

function onRailPointerUp(ev) {
  if (!railDragging) return;
  railDragging = false;
  rail.classList.remove("is-dragging");
  rail.releasePointerCapture?.(ev.pointerId);
}

function onResize() {
  const w = window.innerWidth;
  const h = window.innerHeight;
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(w, h);
  composer.setSize(w, h);
  bloom.setSize(w, h);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  drawRelationGraph();
}

window.addEventListener("wheel", onWheel, { passive: false });
window.addEventListener("resize", onResize);
window.addEventListener("pointermove", (ev) => {
  pointerX = (ev.clientX / window.innerWidth - 0.5) * 2;
  pointerY = (ev.clientY / window.innerHeight - 0.5) * 2;
});
scrollStage.addEventListener("scroll", onScroll, { passive: true });
overview.addEventListener("wheel", onOverviewWheel, { passive: false });
rail.addEventListener("pointerdown", onRailPointerDown);
rail.addEventListener("pointermove", onRailPointerMove);
rail.addEventListener("pointerup", onRailPointerUp);
rail.addEventListener("pointercancel", onRailPointerUp);

function animate() {
  const dt = Math.min(clock.getDelta(), 0.05);
  const elapsed = clock.elapsedTime;
  onScroll();
  progress += (progressTarget - progress) * Math.min(1, dt * 1.75);
  updateDom(progress);
  updateScene(dt, elapsed);
  if (document.getElementById("final-graph")?.classList.contains("is-active")) {
    if (graphAlpha > 0.061 || graphDraggingNode) stepGraphPhysics();
    drawRelationGraph();
  }
  composer.render();
  requestAnimationFrame(animate);
}
