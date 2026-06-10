---
layout: default
lang: zh
title: 故事线
description: 档案回放——逐事件回放灵接记录的故事线。
permalink: /zh/anotherworld/storylines/
---

<style>
.sl-wrap{display:flex;gap:2rem;align-items:flex-start}
.sl-books{flex:0 0 280px;display:flex;flex-direction:column;gap:1rem}
.sl-book{display:flex;gap:1rem;align-items:center;text-align:left;cursor:pointer;
  background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
  padding:1rem;color:var(--fg);font-family:inherit;font-size:1rem;
  transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease}
.sl-book:hover{transform:translateY(-3px);border-color:var(--accent)}
.sl-book.active{border-color:var(--accent);box-shadow:0 0 28px rgba(0,229,255,.12)}
.sl-book-glyph{flex:0 0 auto;width:62px;height:84px;display:flex;align-items:center;justify-content:center;
  font-size:1.9rem;font-family:var(--font-display);color:var(--accent);
  background:linear-gradient(160deg,rgba(0,229,255,.14),rgba(124,77,255,.14));
  border:1px solid var(--accent);border-radius:8px}
.sl-book-meta{display:flex;flex-direction:column;gap:.2rem;min-width:0}
.sl-book-meta strong{font-size:1.02rem;line-height:1.3}
.sl-book-meta em{font-style:normal;color:var(--muted);font-size:.8rem}
.sl-book-status{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.sl-locked{opacity:.4;pointer-events:none}
.sl-stage{flex:1;min-width:0}
.sl-canvas{overflow-x:auto;border:1px solid var(--border);border-radius:var(--radius);
  background:rgba(10,18,32,.5)}
.sl-svg{display:block}
.sl-label{fill:#cdd7ea;font-size:12.5px;font-family:var(--font-body)}
.sl-label-sm{font-size:11px;fill:#8fa0bd}
.sl-branch-label{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;font-family:var(--font-body)}
.sl-n{cursor:pointer;outline:none}
.sl-n:hover .sl-dot,.sl-n:focus .sl-dot{stroke-width:3.5}
.sl-n.active .sl-dot{fill:#fff}
.sl-detail{margin-top:1.25rem;min-height:120px;border:1px solid var(--border);
  border-radius:var(--radius);padding:1.25rem 1.5rem;background:var(--card)}
.sl-detail h3{margin:.4rem 0 .5rem;color:#fff}
.sl-detail p{margin:0;color:var(--fg)}
.sl-detail-meta{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase}
.sl-hint{color:var(--muted);margin:0}
@media(max-width:900px){
  .sl-wrap{flex-direction:column}
  .sl-books{flex:1 1 auto;flex-direction:row;flex-wrap:wrap;width:100%}
  .sl-book{flex:1 1 260px}
}

.sl-views{display:flex;gap:.6rem;margin-bottom:1.5rem}
.sl-view{padding:.5rem 1.3rem;border-radius:999px;border:1px solid var(--border);
  background:var(--card);color:var(--muted);cursor:pointer;font-family:inherit;
  font-size:.92rem;transition:all .25s ease}
.sl-view:hover{border-color:var(--brand);color:var(--fg)}
.sl-view.active{border-color:var(--brand);color:var(--brand);box-shadow:0 0 18px rgba(0,229,255,.15)}
.sg-mount{position:relative;border:1px solid var(--border);border-radius:var(--radius);
  background:rgba(10,18,32,.5);overflow:hidden}
.sg-canvas{display:block;cursor:grab}
.sg-chips{position:absolute;top:.8rem;left:.9rem;z-index:2;display:flex;gap:.5rem;flex-wrap:wrap}
.sg-chip{display:flex;align-items:center;gap:.4rem;padding:.28rem .75rem;border-radius:999px;
  border:1px solid var(--border);background:rgba(15,27,45,.85);color:var(--muted);
  font-size:.75rem;cursor:pointer;font-family:inherit;transition:all .2s ease}
.sg-chip.active{color:var(--fg);border-color:rgba(0,229,255,.35)}
.sg-chip:not(.active){opacity:.4}
.sg-chip-dot{width:9px;height:9px;border-radius:50%;display:inline-block}
.sg-tip{position:absolute;bottom:.7rem;right:.95rem;z-index:2;color:var(--muted);
  font-size:.72rem;opacity:.8;pointer-events:none}
</style>

<header class="hero" style="padding: 5rem 0 3rem;">
  <div class="bg"></div>
  <div class="container">
    <span class="badge">档案回放</span>
    <h1>故事线</h1>
    <p class="lead">
      另一个世界中保存的每一份记录，都可以作为一条线回放。在左侧选择一份档案——
      故事线会从第一个事件生长到最后一个事件，在记录分岔的地方生出分支。
      点击任意节点，阅读那里发生了什么。
    </p>
  </div>
</header>

<section class="section">
  <div class="container">
    <div class="sl-views">
      <button type="button" id="tab-line" class="sl-view active">故事线</button>
      <button type="button" id="tab-graph" class="sl-view">关系图谱</button>
    </div>
    <div id="view-line">
    <div class="sl-wrap">
      <div class="sl-books" id="sl-list" aria-label="档案"></div>
      <div class="sl-stage">
        <div class="sl-canvas" id="sl-canvas"></div>
        <div class="sl-detail" id="sl-detail"></div>
      </div>
    </div>
    </div>
    <div id="view-graph" style="display:none">
      <div id="sg-mount" class="sg-mount">
        <div class="sg-tip">拖拽节点 · 滚轮缩放 · 拖动空白平移</div>
      </div>
      <div class="sl-detail" id="sg-detail"></div>
    </div>
  </div>
</section>

<script src="{{ '/assets/storylines.js' | relative_url }}"></script>
<script>
initStorylines({
  listId: 'sl-list', canvasId: 'sl-canvas', detailId: 'sl-detail',
  hint: '故事线正在生成……点击任意节点查看事件。',
  mainLabel: '主线',
  lockedCard: '更多记录 · 解密中……',
  books: [
    {
      id: 'moon', glyph: '月', accent: '#00e5ff',
      title: '月球暗面',
      subtitle: '档案 I · 第一扇门',
      status: '已出版',
      nodes: [
        { t: '第二次数字矫正', d: '2118 年，十八岁的吉姆·维尔走进灵接舱，进行人生第二次数字矫正。这一次，有什么东西没有按程序进行。' },
        { t: '唯一归来者', d: '吉姆醒来——带着不属于他的记忆。同一批参与者中，安娜·刘易斯与查理·黑尔没有醒来。' },
        { t: '月暗记录会议', d: '灵接科技开始内部追查。卢恩博士第一个意识到：灵接舱连接的，可能不是公司建造的任何东西。' },
        { t: '人类是宿主', d: '带回的记录开始与神话逐条对号。月球的工程真相浮出水面：它不完全是一颗天然卫星。' },
        { t: '数字亚瑟', d: '最早一批上传者之一、斯皮尔的旧友亚瑟·惠勒——他的数字人格已停止生长。数字永生第一次露出它的缺陷。' },
        { t: '罗斯威尔遗产', d: '1947 年的残骸、百年逆向工程、2047 年的技术释放——灵接技术的真正来源终于被揭开。' },
        { t: '死球理论', d: '肖恩·柯宾的危险假说：在地球上死亡，意识会被这颗行星的势阱束缚；而死在一颗"死球"上——它也许能挣脱。' },
        { t: '解构倒计时', d: '艾拉告诉吉姆真相：安娜与查理正被月暗系统判定为异常意识——并被解构。剩下的时间不多了。' },
        { t: 'LUNA-EXIT', d: '斯皮尔的旧梦浮出水面：一个终点不是"保存"而是"迁出"的封存计划。吉姆决定登月——用真正的肉体。' },
        { t: '发射与着陆', d: '穿过不可返回区域，吉姆在月球暗面着陆。没有副本，没有远程连接，没有退路。' },
        { t: '肉体死亡', d: '在月球暗面，吉姆完成肉体死亡，进入真实的泰拉撒记录。第一扇门，从里面被打开了。' },
        { t: '下一本入口', d: '泰拉撒深处，数字吉姆仍然存在。而困着安娜与查理的两片区域，开始微微发亮。' }
      ],
      branches: [
        { from: 1, dir: 'up', label: '数字吉姆的记忆碎片', nodes: [
          { t: '黑水与苏醒', d: '那段借来的记忆，开始于黑水，开始于从黑水中醒来。' },
          { t: '石门之后的战场', d: '石门之后是远古战场——巨鲸形的阴影掠过一具不属于任何已知文明的骨骸。' },
          { t: '稻田与小女孩', d: '沙路尽头的稻田里，一个小女孩直视着吉姆的意识。他后来给她起名：艾拉。' },
          { t: '蓝黑球体与时间井', d: '一颗蓝黑色的球体，和一口时间不走直线的井。' }
        ]},
        { from: 7, dir: 'down', label: '被困者', nodes: [
          { t: '安娜的区域', d: '记录边缘的树林里，有一只能直视意识的猫影。——《灵猫》的入口。' },
          { t: '查理的区域', d: '时间切片中闪过尸山，和一头从天而降的巨鲸。——《巨鲸陨落》的入口。' }
        ]}
      ]
    },
    {
      id: 'whale', glyph: '鲸', accent: '#7c4dff',
      title: '巨鲸陨落',
      subtitle: '档案 II · 法厄同证词',
      status: '筹备中',
      nodes: [
        { t: '尸山之上', d: '查理在一具陌生的身体里醒来，站在尸体堆成的山上，不知道自己是谁，也不知道这里是哪里。' },
        { t: '巨鲸从天而降', d: '天空开始震动。一头燃烧的巨鲸自高空坠落——像星舰，也像一个文明的记忆本身在下坠。' },
        { t: '宿主的名字', d: '这具身体叫洛安：远古战争的一名普通幸存者。查理只能借他的眼睛，看完一个世界的结局。' },
        { t: '谁赢了', d: '五族的残骸铺满战场。所有人都以为战争胜利了——直到有人问出那个问题：赢的，是谁？' },
        { t: '战争的真相', d: '这不是资源战争。地球是正在成形的生命孵化场，而法厄同星，是通往它的战略门槛。' },
        { t: '巨鲸不是武器', d: '巨鲸族是星海的记忆载体——活的文明档案库。坠落从来不是攻击。它是另一回事。' },
        { t: '种子', d: '无法在地球存续的巨鲸族，把自身的一部分记忆、频率与生物蓝图，封进了年轻海洋的生命演化链。' },
        { t: '小行星带的诞生', d: '法厄同开始下沉、碎裂。胜利者们在残骸上争吵，只在一件事上达成一致：没有一族配拥有地球。' },
        { t: '蓝鲸在地球歌唱', d: '亿万年后，那颗种子长成了地球上最大的动物。在借来的意识深处，查理听见了歌声。' },
        { t: '宿主最后的选择', d: '洛安的故事走到尽头。查理终于明白：怕死的人，也可能是最后一个站着的见证者。' },
        { t: '回声归档', d: '记录闭合。醒来之前，查理把这场战争看到了最后——替所有不在场的人。' },
        { t: '尾声：没有完全死去', d: '巨鲸死在星空里，醒在地球的海中。' }
      ],
      branches: [
        { from: 4, dir: 'up', label: '五族的愿望', nodes: [
          { t: '日辉族', d: '想要人类跪拜。' },
          { t: '鳞裔族', d: '想要漫长的地底潜伏。' },
          { t: '节肢族', d: '想要一个没有孤独的世界。' },
          { t: '渊民族', d: '想把记忆交给海。' },
          { t: '震翼族', d: '只想天空还有路。' }
        ]},
        { from: 8, dir: 'down', label: '来自外面的信号', nodes: [
          { t: '吉姆的信号', d: '月暗深处，吉姆的信号穿透了记录。' },
          { t: '星环', d: '另一个吉姆，在记录的另一层，看见了同一道星环。' },
          { t: '查理不想走', d: '救援终于抵达时，查理犹豫了——他还没有看完。' }
        ]}
      ]
    }
  ]
});
</script>

<script src="{{ '/assets/storygraph.js' | relative_url }}"></script>
<script>
var GRAPH = {
  mountId:'sg-mount', detailId:'sg-detail', height:620,
  hint:"点击节点查看说明；悬停可高亮它的所有连接。",
  connLabel:"连接",
  types:{
    book:{label:"书卷",color:'#5ef9ff'},
    character:{label:"人物",color:'#ffb454'},
    event:{label:"事件",color:'#a78bfa'},
    concept:{label:"概念",color:'#4dd0a1'}
  },
  nodes:[
  {
    "id": "b1",
    "label": "月球暗面",
    "type": "book",
    "d": "档案 I · 第一扇门。吉姆的事故、追查与登月。系列的入口。"
  },
  {
    "id": "b2",
    "label": "巨鲸陨落",
    "type": "book",
    "d": "档案 II · 法厄同证词。查理在远古战争中的见证。"
  },
  {
    "id": "jim",
    "label": "吉姆·维尔",
    "type": "character",
    "d": "第一扇门的打开者。第一个完整接触并返回月球暗面的人。"
  },
  {
    "id": "djim",
    "label": "数字吉姆",
    "type": "character",
    "d": "吉姆的数字双生体，留在泰拉撒深处的另一半。主体核问题的入口。"
  },
  {
    "id": "anna",
    "label": "安娜·刘易斯",
    "type": "character",
    "d": "读规则的人。困于非人类意识区域——《灵猫》的入口。"
  },
  {
    "id": "charlie",
    "label": "查理·黑尔",
    "type": "character",
    "d": "最像普通人的见证者。困于法厄同终战的记录之中。"
  },
  {
    "id": "elara",
    "label": "艾拉",
    "type": "character",
    "d": "小女孩形态只是投影。她帮助吉姆——但她的立场是一个未解的问题。"
  },
  {
    "id": "spire",
    "label": "伊莱亚斯·斯皮尔",
    "type": "character",
    "d": "灵接科技创始人。被血色游轮改变的人，「迁出」执念的源头。"
  },
  {
    "id": "lune",
    "label": "阿德里安·卢恩",
    "type": "character",
    "d": "现实侧的伦理见证者。铁律：人不是样本。"
  },
  {
    "id": "arthur",
    "label": "亚瑟·惠勒",
    "type": "character",
    "d": "斯皮尔旧友，最早的上传者之一。他的停滞是主体核假说的关键证据。"
  },
  {
    "id": "corbin",
    "label": "肖恩·柯宾",
    "type": "character",
    "d": "物理学家，死球理论的提出者。"
  },
  {
    "id": "loan",
    "label": "洛安",
    "type": "character",
    "d": "查理在远古战场醒来时所在的身体——一名普通幸存者。"
  },
  {
    "id": "e1947",
    "label": "罗斯威尔坠毁（1947）",
    "type": "event",
    "d": "军方获得意识接口残骸。一切的起点。"
  },
  {
    "id": "e2047",
    "label": "技术释放（2047）",
    "type": "event",
    "d": "百年逆向工程的成果，以「意识接口革命」的形式进入公众世界。"
  },
  {
    "id": "e2053",
    "label": "黑潮（2053）",
    "type": "event",
    "d": "物质文明信仰崩塌，意识产业兴起。"
  },
  {
    "id": "e2118",
    "label": "矫正事故（2118）",
    "type": "event",
    "d": "第二次数字矫正异常。吉姆带回记忆，安娜与查理没有醒来。"
  },
  {
    "id": "ecount",
    "label": "解构倒计时",
    "type": "event",
    "d": "月暗系统将安娜与查理判定为异常意识——并开始解构。"
  },
  {
    "id": "emoon",
    "label": "月面肉体死亡",
    "type": "event",
    "d": "吉姆在月球暗面完成肉体死亡，进入真实的泰拉撒记录。"
  },
  {
    "id": "ewar",
    "label": "法厄同终战",
    "type": "event",
    "d": "围绕地球未来与生命实验权的太阳系战争的最后一战。"
  },
  {
    "id": "efall",
    "label": "巨鲸坠落",
    "type": "event",
    "d": "一头星舰般的巨鲸自天而降，撕裂了法厄同星。"
  },
  {
    "id": "cabin",
    "label": "灵接舱",
    "type": "concept",
    "d": "表面是矫正与数字永生设备，本质是低阶意识接口。"
  },
  {
    "id": "twin",
    "label": "双生模式",
    "type": "concept",
    "d": "肉体与数字生命并行发展，按年龄节点同步。"
  },
  {
    "id": "core",
    "label": "主体核",
    "type": "concept",
    "d": "信息可以复制；主体核只能迁移，永不可复制。"
  },
  {
    "id": "dead",
    "label": "死球理论",
    "type": "concept",
    "d": "「死亡地点决定意识去向」的危险假说。"
  },
  {
    "id": "terasa",
    "label": "泰拉撒记录",
    "type": "concept",
    "d": "月球暗面的古老记录系统，长期归档地球生命的演化。"
  },
  {
    "id": "luna",
    "label": "LUNA-EXIT",
    "type": "concept",
    "d": "斯皮尔的封存计划：终点不是保存，而是迁出。"
  },
  {
    "id": "roswell",
    "label": "罗斯威尔接口",
    "type": "concept",
    "d": "不靠机械驾驶、由意识结构直接耦合的非物质接口。"
  },
  {
    "id": "song",
    "label": "蓝鲸歌声",
    "type": "concept",
    "d": "封进海洋生命链的种子，一段低频的记忆回声。"
  },
  {
    "id": "whalekind",
    "label": "巨鲸族",
    "type": "concept",
    "d": "星海的记忆载体，活的文明档案库。"
  },
  {
    "id": "five",
    "label": "五族",
    "type": "concept",
    "d": "日辉、鳞裔、节肢、渊民、震翼——战争中的五个族群。"
  },
  {
    "id": "incub",
    "label": "地球孵化场",
    "type": "concept",
    "d": "在远古各族眼中，地球是一场正在成形的生命实验。"
  },
  {
    "id": "cat",
    "label": "灵猫文明",
    "type": "concept",
    "d": "动物意识的高阶网络，那里的时间不走直线。（档案 III 伏笔）"
  }
],
  links:[["b1", "jim"], ["b1", "e2118"], ["b1", "elara"], ["b1", "terasa"], ["b1", "emoon"], ["b1", "ecount"], ["b2", "charlie"], ["b2", "ewar"], ["b2", "efall"], ["b2", "loan"], ["b2", "five"], ["jim", "djim"], ["jim", "anna"], ["jim", "charlie"], ["jim", "e2118"], ["jim", "elara"], ["jim", "emoon"], ["jim", "lune"], ["jim", "spire"], ["djim", "terasa"], ["djim", "core"], ["anna", "e2118"], ["anna", "cat"], ["anna", "ecount"], ["charlie", "e2118"], ["charlie", "loan"], ["charlie", "efall"], ["charlie", "ecount"], ["charlie", "song"], ["elara", "terasa"], ["elara", "ecount"], ["spire", "luna"], ["spire", "arthur"], ["spire", "cabin"], ["lune", "cabin"], ["lune", "e2118"], ["arthur", "core"], ["arthur", "cabin"], ["corbin", "dead"], ["dead", "emoon"], ["luna", "emoon"], ["cabin", "twin"], ["cabin", "roswell"], ["twin", "e2118"], ["twin", "core"], ["roswell", "e1947"], ["e1947", "e2047"], ["e2047", "e2053"], ["e2053", "cabin"], ["terasa", "incub"], ["ewar", "five"], ["ewar", "incub"], ["ewar", "efall"], ["whalekind", "efall"], ["whalekind", "song"], ["cat", "terasa"]]
};
var graphInited = false;
function showView(which){
  document.getElementById('view-line').style.display = which==='line' ? '' : 'none';
  document.getElementById('view-graph').style.display = which==='graph' ? '' : 'none';
  document.getElementById('tab-line').classList.toggle('active', which==='line');
  document.getElementById('tab-graph').classList.toggle('active', which==='graph');
  if(which==='graph' && !graphInited){ graphInited = true; initStoryGraph(GRAPH); }
}
document.getElementById('tab-line').addEventListener('click', function(){ showView('line'); });
document.getElementById('tab-graph').addEventListener('click', function(){ showView('graph'); });
</script>
