from pathlib import Path
import html

ROOT = Path("巨鲸陨落_V1")
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"


ZH = {
    "44_人类的混合遗产": """# 44 人类的混合遗产

白线带着查理上升。

尸山、巨鲸阴影和法厄同碎环在下方逐渐收缩，像被卷进一枚透明的核。查理以为自己会直接回到灵接舱，或者至少回到吉姆伸手的那片黑白记录层。

可中途，他被一片更细碎的光拦住了。

那些光点像尘埃，漂浮在无边暗处。每一个光点里都有一小段画面：日辉族建塔，鳞裔族封存胚胎，节肢族群体同步，渊民族把声音交给水，震翼族在高空标记航线，巨鲸种子沉入海底。

它们没有排成一条直线。

它们互相穿过，互相污染，互相改变。

查理忽然明白，这里不是单一族群留下的血统谱。

又一个旧句式差点冒出来，他把它按住。

这里更像一片被战争打碎后的沉积层。每一族都以为自己能决定地球未来，结果法厄同崩裂后，所有方案都变成碎片，被时间、海洋、月球暗面的记录系统和后来的干预一点点搅在一起。

人类并非某一族的作品。

这个念头出现时，查理没有感到骄傲，反倒有点发冷。

因为这意味着人类身上那些互相矛盾的东西，并不只是偶然。仰望天空和挖向地下，渴望群体又害怕失去自己，想把记忆交给海，又不断修路离开故乡。这些冲突像古老碎片，一直留在人类的神话、身体和意识结构里。

吉姆的声音从白线另一端传来：“查理，别试图全记。抓住最稳定的结论。”

“我在看。”查理回答。

他说出这句话时，自己都愣了一下。

他真的能回答了。

光点继续流动。

他看见远古地球上，一些后来会被称为“神”的影子降落在不同文明的记忆里。它们有时像日辉族，有时像鳞裔族，有时像渊民在洪水神话里的残响，有时又像震翼族留下的飞行者传说。人类把看不懂的东西叫作神，把无法解释的介入叫作造物。

可真相更乱。

更不体面。

也更像生命本身。

“不是一族创造。”查理慢慢说，“是很多失败遗产被迫混在一起。后来又经过地球自己的演化，经过月暗系统的筛选和记录，才慢慢变成了我们。”

白线另一端安静了一瞬。

数字吉姆的声音响起：“保留这个句子。它足够短。”

“短得不像真相。”查理说。

“真相太长时，先带回骨架。”

查理看着那些光点。

他知道自己带不走全部。带不走每一名死者，每一段航路，每一次争吵，也带不走洛安身体里所有疼痛。可他至少能带走一个方向：人类不是谁的奖品，也不是谁的纯血延续。

人类是混合后的新问题。

也许这才可怕。

也许这才自由。

这个结论落进他心里时，并没有变成某种伟大的光。它更像一块沉到胃里的石头，让他想起自己小时候在《另一个世界》里第一次看见不同种族角色混住的城市。那时候他只觉得设定很酷，酒馆里有兽人、精灵、矮人，大家吵吵闹闹，偶尔还会因为一句任务奖励分配不均打起来。现在他才意识到，人类现实里的混合远比游戏里沉重。这里没有设计师提前调好的平衡表，也没有系统保证每一种遗产都会被公平保留。

有些遗产变成了天赋。

有些遗产变成了病。

有些遗产变成了无法解释的梦，藏在孩子第一次仰望星空时的恐惧里，藏在成年人听见海啸新闻时忽然涌起的熟悉感里，藏在人类明明知道自己渺小，却仍然一次次建塔、造船、发射探测器的冲动里。

查理忽然很想把这些告诉以前那个只会开玩笑的自己。

如果那时有人告诉他，你的身体和意识里住着一场太阳系战争的余波，他大概会先问，这个设定能不能做成游戏。

现在他问不出来了。

因为他知道，每一个酷炫设定背后，都可能有人真的死过。

而且死亡并没有自动变得高贵。

有些死得仓促，有些死得狼狈，有些甚至没人看见。被历史选中的，从来只有极少数画面。剩下的，都像尘埃一样落进记录的缝隙里，等某个倒霉的后来者经过时，忽然粘在他的意识上。

查理觉得自己就是那个后来者。

白线再次收紧，光点逐渐远去。查理在离开前，听见很低的一声鲸歌，从所有碎片下方传来。

像在确认，他没有听错。""",

    "45_给安娜留下的问题": """# 45 给安娜留下的问题

鲸歌之后，查理听见另一种声音。

它很轻，几乎被巨鲸低频盖住。起初像风吹过草叶，又像某种小动物在黑暗里踩过碎石。查理顺着声音看去，只看见一片陌生的绿色。

不是海。

是森林。

树木很高，根系裸露在潮湿泥土上，空气里漂浮着细小光点。那些光点不像巨鲸记忆的星海尘埃，更像某种动物意识在夜里留下的体温。查理看不清具体生物，只看到许多眼睛一闪而过：猫科动物的竖瞳，鸟类侧头时的微光，鹿一样的黑色轮廓，还有一只黑猫站在树根上，安静地看着他。

查理心里一紧。

“吉姆？”他试着喊。

没有回应。

黑猫没有靠近，只抬起头，像在听远处海底的鲸歌。那歌声传到森林里时，已经变得很淡，可森林里的光点竟然一起亮了一下。

查理不懂。

他见过五族战争，见过巨鲸种子，见过蓝鲸歌声如何从星海遗产变成地球生命的自然回响。可眼前这片森林不属于法厄同，也不像月暗记录里的战争切片。

这里更柔软，也更危险。

这里没有武器，危险感却从那些沉默目光里慢慢渗出来。那些动物没有说话，却像在共享某种比语言更早的理解。查理忽然想到安娜。她并不像猫，可如果有人能站在这片复杂、安静、规则不明的森林里不慌，也许会是她。

她会先观察。

会记下每一只动物出现的位置。

会问：它们是在听鲸歌，还是在回应鲸歌？

黑猫眨了一下眼。

查理觉得它好像听见了自己的想法。

他下意识往后退了半步，脚底却没有踩到地面。这里的森林不像普通空间，更像一层被动物意识共同维持的梦。树根下有细小的白骨，也有刚刚发芽的嫩叶。腐烂和新生挤在同一寸泥土里，毫不避讳地贴在一起。查理看见一只灰色鸟落在骨头上，低头啄了一下，抬头时眼睛里闪过非常短促的蓝光。

那蓝光让他想起巨鲸种子的低频。

海洋和森林之间，好像有一条极细的线。

线的那一端，是庞大生命把记忆交给歌声；这一端，则像是无数动物把经验交给本能、气味、迁徙和梦。查理没有能力解释这些，他只知道这里跟安娜有关。安娜总能在别人看热闹的时候，看见规则边缘的缺口。她会知道这片森林里哪些东西是诱饵，哪些东西是求救，哪些东西只是某种古老生命在睡梦里翻身。

下一秒，森林深处传来一声极轻的猫叫。

那声音穿过查理意识时，留下一个奇怪的问题：如果巨鲸的回声能藏进海洋生命，那么其他动物的意识里，是否也藏着某种更古老的灵文明？

这个问题太大。

也太不像查理能回答的问题。

“这个留给安娜。”他几乎立刻想。

白线轻轻震动，像吉姆在另一端接收到了他的念头。

数字吉姆的声音很远：“不要进入。那不是查理区域。”

查理立刻后退。

这一回他退得很自觉，甚至有点熟练。经历了法厄同之后，他已经对“不属于自己的记录”有了足够敬畏。黑猫仍站在树根上，尾巴轻轻扫过湿土。

它没有阻止。

也没有告别。

查理被白线拉离森林前，看见黑猫再次抬头，望向看不见的海。

很远很远的地方，蓝鲸还在唱。

森林里的动物意识像夜色下的水面，微微起伏。

查理把这个画面塞进自己能带走的最后一点空间里。

给安娜。

他不知道她会不会醒。

可如果她醒来，这个问题应该属于她。

黑猫像是等到了这个决定，终于从树根上跳下来。它落地没有声音，爪子踩过湿土时，泥面泛起一圈很浅的绿光。那绿光没有扩散到查理脚下，只沿着树根向森林深处游走，像某种无声的通知。

一只鹿低下头。

一只鸟收拢翅膀。

更远处，某个体型庞大的黑影在树后缓慢翻身，带动整片雨幕轻轻倾斜。查理看不清它，只觉得那东西很古老，古老到也许并不在意人类是否醒来。

黑猫最后看了查理一眼。

那眼神里没有邀请，也没有警告。它像在说：记住门在这里，别替她进去。

查理点了点头。

他第一次觉得，放手也是一种负责。""",

    "46_回声归档": """# 46 回声归档

白线忽然收紧。

查理还没来得及从黑猫的目光里回过神，周围空间便开始折叠。鲸歌、森林、尸山、小行星带和灵接舱白光同时向中心塌缩，像有人终于按下了归档按钮。

数字吉姆的声音第一次变得急促：“归档开始了。”

吉姆问：“什么意思？”

“查理区域正在被泰拉撒记录收回。它会把可保存信息压成回声，把主体核剥离出来。如果我们慢了，他会成为记录的一部分。”

查理听见“成为记录的一部分”时，心里猛地一沉。

他已经见过太多被保存的东西。

保存听起来温柔，可如果被保存的是自己，那就不一定了。他不想变成一段供后来者访问的战争切片，不想永远站在尸山上，一遍遍理解所谓胜利。

“那你们快点啊！”他终于喊出来。

吉姆的声音从白线另一端传来：“抓紧。”

“我抓着呢！”

“再抓紧一点。”

“你这话听起来一点技术含量都没有！”

“我负责没技术含量的部分。”

在这种时候还能吵两句，查理忽然觉得自己确实快回来了。

可归档没有给他们太多时间。

白线开始发热。

那种热并不烫皮肤，因为查理此刻已经没有稳定皮肤。它更像一根被过度拉紧的神经，所有细小颤动都直接传到他的“我”里。吉姆那边似乎也不好受，白线时明时暗，有几次差点被归档层吞掉。查理甚至能听见数字吉姆在更深处快速计算的余音，像无数玻璃片互相摩擦。

“如果断了会怎样？”查理问。

“别问。”吉姆说。

“这通常不是好答案。”

“所以别问。”

查理闭嘴了。

他忽然很清楚，自己其实仍然怕。怕被留下，怕醒不过来，怕回去以后没人相信，也怕回去以后所有人都信了。可这一次，害怕没有把他往后拖。它像一块很重的铁，被他抱在怀里一起往前跑。

周围的画面一层层剥落。洛安的残舟先变成一小段低频，随后被吸入暗处；瑟恩的银蓝翅光化成一条细线；渊民族老人的水膜变成透明环；法厄同碎片压缩成一串轨道参数；蓝鲸歌声也开始变成可索引的声谱。

每一样东西都在变干净。

太干净了。

查理忽然产生一种强烈的反感。

他以前很喜欢清晰的东西。游戏任务要有明确目标，地图最好能标注路线，任务奖励要写在说明里。可这一刻他看见战争被清理成档案，看见痛苦被压成数据，才突然明白，太清楚的记录也会骗人。它让后来的人以为一切都有结论，以为死亡只是某个历史节点的代价，以为幸存者只要留下名字，就算被记住了。

可洛安不是一行名字。

瑟恩也不是一条牺牲记录。

他们会开玩笑，会后悔，会在逃跑时骂人，会在真的怕到不行的时候还装作没事。查理甚至记得瑟恩翅膀震动时带起的细小痛感，记得洛安的喉咙在缺水时像被砂纸磨过。这些东西没有宏大意义，却比宏大意义更难伪造。

查理拼命抓住那些还带着疼痛的部分：洛安手指裂开的血，瑟恩笑起来时那点欠揍的弧度，老人倒下时轻得吓人的身体，岚柯丢掉罐体后贴紧的鳞片，索勒烧掉太阳环时暗下去的金色。

“这些不能全被洗掉。”查理说。

数字吉姆回答：“你带不走全部。”

“那我带走会疼的部分。”

白线猛地一亮。

吉姆低声说：“就是现在。”

查理感觉自己被两股力量同时拉扯。一边是泰拉撒记录的归档层，冷静、庞大、耐心，像海水要把一切磨成可保存的形状；另一边是吉姆的白线，不算稳定，却有人类手掌的温度。

数字吉姆在更深处切开一道缝。

“主体核通过。”

查理听不懂这句话具体意味着什么。

他只觉得自己突然被撕出水面。

所有画面向后退去，鲸歌被拉成长长一线，尸山坍缩成灰点，黑猫的眼睛在最后一秒亮了一下。然后，洛安的声音从很远的地方传来：

“跑得认真点。”

查理抓着白线，冲进白光。""",

    "47_醒来之前": """# 47 醒来之前

醒来之前，查理又回到了一具身体里。

这一次没有战场。

也没有完整的人形。

他只感觉到一只手。暗灰色细鳞覆盖在手背上，指节修长，指尖有干涸的血。那是洛安的手。它悬在黑暗里，没有手臂，没有胸口，也没有脸，像整个宿主最后只留下这一点身体记忆。

查理伸出自己的手。

两只手隔着一层很薄的光。

“你还在吗？”查理问。

没有语言回答。

那只手只是轻轻动了一下。

于是查理感到很多东西一起涌上来：第一次在尸山上醒来时的喘息，补给沟里的灰，瑟恩拽他逃跑时手掌的力道，抱住水膜容器时胸口的冷，按下日志系统时伤口被识别的刺痛。

洛安没有以灵魂或英雄的姿态出现。

他以身体记忆告别。

这反而更像他。

查理忽然很想哭，但他已经哭过太多次，眼泪在这里显得不够用。

“谢谢。”他说。

那只手停了一下。

查理知道洛安会不喜欢这个词。

于是他改口：“好吧，不谢。你跑得很认真。”

手指轻轻蜷了一下，像在笑。

查理也笑了。

他终于明白，洛安给他的并不是勇敢。勇敢这个词太干净，太容易被后来者拿去做雕像。洛安给他的，是另一种更普通的东西：害怕时仍然知道什么不能丢，想逃时仍然记得朋友把路交给了自己。

这种东西不漂亮。

却能把种子送到海里。

那只手又动了一下。

这一次，查理看见了几段更碎的东西。

不是战争，也不是巨鲸。是一间低矮的舱室，洛安小时候把耳朵贴在薄薄的舱壁上，听外面水循环管道的低鸣；是某个黄昏，他和瑟恩趴在维修架下偷吃补给糖，被巡检员发现后一起装作无辜；是很久以前，法厄同的天空还没有完全变成战争颜色时，有一小段蓝紫色晚霞落在金属屋顶上。

这些记忆太小了。

小到战争档案可能永远不会保存。

可查理忽然觉得，它们比任何战略会议都更重要。因为洛安不是从尸山上长出来的人。他也曾经只是一个偷吃糖的孩子，一个会把管道低鸣误认为远方海声的孩子。后来历史把他推到出口前，他才变成了查理认识的那个幸存者。

“我会尽量记住你不是一开始就这么苦。”查理说。

那只手停住。

然后，指尖轻轻碰了一下光膜。

像一次很短的握手。

查理忽然想起自己在现实里说过很多次“我怕死”。那时候他说得很轻松，像一句能让气氛变好的玩笑。他会在安娜认真分析风险时举手，说自己负责活着回去；会在吉姆想往危险区域冲时抱怨，说下次能不能先写个遗书模板；会在《另一个世界》里打不过怪物时第一个喊撤退。

现在他发现，怕死这件事并没有让他显得渺小。

真正怕死的人，才会知道每一次留下来都要付出什么。洛安不是不怕。他只是怕到最后，仍然把手伸向了需要按下去的开关。瑟恩也不是天生适合牺牲。他只是明白，如果那一秒没人去接上航路，所有人都会白死。

查理想把这点带回去。

带给吉姆，也带给安娜。

如果有一天他们也站在类似的选择前，至少不要把“勇敢”想得太轻。

黑暗开始变亮。

远处传来吉姆的声音，越来越清晰。还有卢博士的声音，混着设备提示、液体排空和某种急促脚步声。现实正在靠近，带着消毒水、金属和人类身体那种沉重的呼吸。

查理看着洛安留下的那只手。

“我会记住疼的部分。”他说。

手背上的鳞片一点点散开，变成灰色光尘。

最后一刻，查理听见一声很轻的震翼频率。它像瑟恩的笑，也像远处蓝鲸歌声里的某一个低音。

然后，黑暗彻底裂开。

查理向上浮去。""",

    "48_蓝鲸在地球歌唱": """# 48 蓝鲸在地球歌唱

查理醒来时，第一件事是呛咳。

空气冲进肺里，像一把粗糙的刷子从里面刮过去。他整个人蜷起来，手指抓住舱体边缘，指节白得发青。有人在喊他的名字，有人按住他的肩膀，还有仪器发出一连串过度兴奋的提示音。

“查理，听得见吗？”

是卢博士。

查理想回答，却先吐出一口混着黏液的水。喉咙火辣辣地疼，眼睛也睁不开。他觉得自己的身体陌生得要命，太轻，也太窄，没有暗灰色鳞片，没有洛安那种更深的胸腔共鸣。

然后他哭了。

不是在记录里那种没有眼睛的哭。

这一次，眼泪真的从他脸上滚下来，混进舱体残留液里。他哭得很难看，咳嗽、喘气、发抖，像一个刚从很深很深的水里被拖上岸的人。

卢博士的声音低下来：“慢一点，别急。你回来了。”

查理抓住他的袖口。

“蓝鲸。”他说。

卢博士愣了一下：“什么？”

“找蓝鲸的声音。”

没人立刻理解。

吉姆站在不远处，脸色苍白得像也刚经历了一场长途迁移。他看着查理的眼睛，忽然转头对控制台旁的助手说：“调海洋声学数据库。蓝鲸低频。现在。”

几秒钟后，实验室的扬声器里传来一段很低的声音。

长，慢，穿过空气时几乎不像声音，更像某种让胸腔跟着震动的压力。

查理闭上眼。

他没有解释。

也解释不了。

那声音一响，灵接舱、实验室、医生、警报全都退远了。海水重新在意识深处展开，法厄同的碎环在更远处安静旋转。瑟恩的翅膀，洛安的手，渊民族老人的水膜，巨鲸坠落时压下来的阴影，全都在那段低频里轻轻碰了一下。

它们还在。

不是完整地活着。

可它们没有完全死去。

查理把额头抵在舱壁边缘，眼泪还在往下掉。他忽然想起梦最开始的那个画面：自己站在尸山上，身边有一个朋友，远处有人庆祝胜利。那时候他以为自己只是梦见了一场过于壮烈的战争。现在他终于知道，那种“胜利”为什么从一开始就让人不舒服。

因为真正的胜利者没有站在尸山上。

真正留下来的，是海里一段缓慢到几乎没人愿意认真听完的歌。

他想笑一下，结果又咳了起来。卢博士递来一块吸水巾，动作很轻。这个平时总能把情绪压在专业表情后面的人，此刻眼眶也有点发红。他没有问查理看见了什么，没有催促他组织语言，只把声谱图放大，让那条低频曲线在屏幕上慢慢滑动。

查理觉得，这大概就是人类很奇怪的地方。

他们可以把一场远古战争压进数据库，也可以因为一段鲸歌安静下来。

控制室外，有人轻轻吸了一口气。

那声音很小，却让查理意识到，听见蓝鲸歌声的不止他一个。几名原本只负责监测数据的研究员站在玻璃后面，脸上的表情从工作状态里松动出来。有个人摘下了耳机，像是忽然忘了自己该记录哪一项指标。另一个年轻助手低头看着屏幕，手指悬在确认键上迟迟没有按下。

他们也许听不懂法厄同。

听不懂洛安。

听不懂巨鲸种子穿过地球窗口时留下的真正含义。

可他们能听见一种巨大的孤独，正从海洋最深处慢慢经过人类的实验室。

这已经够了。

查理睁开眼，声音很哑：“它们还在。”

这一次，没有人打断他。

卢博士看着声谱图，又看向吉姆。

吉姆没有说话。他只是慢慢坐到查理身边，像终于确认自己真的把人拉回来了一点。

查理靠在舱壁上，听完那整段蓝鲸歌声。

歌声结束后，实验室安静了几秒。

查理抬头，看向仍在沉睡舱里的安娜。

“她那边……”他声音很轻，“可能不是战争。”

吉姆顺着他的视线看过去。

安娜的舱体表面，状态光纹极轻地闪了一下。

像一只在黑暗里睁开的眼。""",

    "49_尾声：没有完全死去": """# 49 尾声：没有完全死去

查理醒来后的第三小时，吉姆终于收到了那段记忆。

不是完整影像。

查理带回来的东西更像一团被水泡过的线。它里面有法厄同裂解时的白光，有小行星带最初形成的轨道，有巨鲸种子穿过地球窗口时留下的低频，还有洛安最后烧掉坐标后的那句日志：

我们没有赢。

种子已经不属于任何一族。

别追。

吉姆听完很久没有说话。

卢博士站在旁边，手里拿着平板，却忘了记录。屏幕上的声谱还停留在蓝鲸歌声那一段，低频曲线像一条缓慢起伏的海底山脉。

“所以人类……”卢博士开口，又停住。

查理靠在病床上，脸色很差，精神却异常清醒。

“不是谁单独造出来的。”他说，“至少从我看到的东西来看，不是。我们更像很多失败方案混在一起后，经过地球自己漫长演化，又被后来的月暗系统和别的干预筛过一遍，才长成现在这样。”

他说完，自己苦笑了一下。

“这句话听起来像疯话。”

吉姆摇头：“我们现在这里，疯话已经不够用了。”

查理闭上眼。

他太累了。

可只要一闭眼，他就又看见尸山。看见瑟恩指着战场说，别把这里写得太漂亮。看见洛安说，会怕死的人，讲死亡的时候不会太轻。

于是他又睁开眼。

“吉姆。”他说，“如果你们要把这段记忆给别人看，别只给结论。”

“我知道。”

“不，你不知道。”查理看着他，“你们这些见过月球暗面的人，很容易直接讲真相。真相太大了，讲出来像天塌下来。但洛安他们不是为了让我们震撼才死的。”

吉姆没有反驳。

查理慢慢说：“要让别人知道，他们怕过，后悔过，也想活。否则这又会变成另一种神话。”

卢博士终于低头，把这句话记了下来。

窗外天还没亮。

城市在夜色里安静运转，远处飞行车流像一条条细光。地球看上去仍然属于人类，属于钢铁、玻璃、灯光和稳定的日程。可在更深处，在没有人听见的海洋里，蓝鲸仍在唱。

查理靠回枕头，忽然觉得身体重得离谱。现实里的他没有鳞片，没有震翼，也没有能够在海水里传递记忆的器官。他只是一个刚醒来的十八岁青年，喉咙还疼，手背上插着监测针，头发被舱液黏成一团。可就在这具看起来毫无史诗感的身体里，挤着一场行星死亡后的回声。

他突然理解了洛安最后为什么没有要求被记住。

被记住太难了。

记录会漏掉体温，纪念会磨平棱角，后人总会把复杂的人修成更容易讲述的形状。也许真正能做的，只是在下一次讲述时，少撒一点谎，多留一点疼。

“我会慢慢写。”吉姆像知道他在想什么，低声说。

查理看了他一眼：“别写得太帅。”

吉姆沉默半秒：“那你可能会很安全。”

查理笑了一下，笑到伤口牵动，又轻轻吸气。

这一下笑声很短，却让房间里那股压抑的气氛松开了一点。卢博士低头调整记录权限，假装自己没有听见。屏幕上，蓝鲸声谱慢慢归档，文件名自动生成，末尾标注着一个临时编号：Phaeton-Whale-Echo。

同一时间，安娜的意识区域里，一片黑色森林正在下雨。

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

蓝鲸的歌声已经停止，余波却还留在实验室的空气里。查理忽然想，也许巨鲸真的没有完全死去。它只是把自己变成了很多很慢的东西：海里的歌，小行星带的碎光，人类身体里的矛盾，还有一只黑猫忽然抬头的瞬间。

故事没有结束。

只是下一段回声，换了一个方向。""",
}


EN = {
    "44_人类的混合遗产": """# 44 Humanity's Mixed Inheritance

The white line carried Charlie upward.

Corpse mountain, whale shadow, and Phaeton's broken ring shrank below, as if rolled into a transparent core. Charlie thought he would return directly to the Spirit Connect pod, or at least to the black-and-white record layer where Jim waited.

Halfway there, finer lights stopped him.

They drifted in the dark like dust. Each held a short image: Sunbright building towers, Scale-Kin sealing embryos, Chitinous synchronizing clusters, Abyssals giving sound to water, Wing-Shiver marking routes in high air, the whale seed sinking into the seabed.

They did not form one line.

They passed through one another, contaminated one another, changed one another.

Charlie understood that this was no single people's bloodline chart.

An old sentence shape almost rose, and he pressed it down.

This was more like a sediment layer after war had broken everything. Each people had believed it could decide Earth's future. After Phaeton fractured, every plan became fragments stirred together by time, ocean, the lunar dark-side record system, and later interventions.

Humanity was not the work of one people.

The thought did not make Charlie proud. It made him cold.

It meant the contradictions inside humanity were not mere accident. Looking upward and digging underground, longing for a group and fearing loss of self, giving memory to the sea and building roads away from home: these conflicts had remained in human myth, body, and consciousness like ancient fragments.

Jim's voice came from the other end of the line. “Charlie, do not try to remember all of it. Hold the most stable conclusion.”

“I'm looking,” Charlie answered.

He startled himself by speaking.

The lights continued to move.

He saw ancient Earth, where shadows later called gods descended into different civilizations' memories. Sometimes they resembled Sunbright. Sometimes Scale-Kin. Sometimes Abyssal echoes in flood myths. Sometimes Wing-Shiver in tales of flying beings. Humanity called what it could not understand divine, and intervention became creation.

The truth was messier.

Less dignified.

More like life.

“Not created by one people,” Charlie said slowly. “Many failed inheritances were forced to mix. Then Earth's own evolution, later Moon-dark filtering and recording, gradually made us.”

The white line fell silent.

Digital Jim spoke. “Keep that sentence. It is short enough.”

“Too short to feel true,” Charlie said.

“When truth is too long, bring back the skeleton first.”

Charlie looked at the lights.

He knew he could not bring everything. Not every dead person, every route, every argument, not all pain inside Lo'an's body. But he could bring one direction: humanity was no one's prize, no pure extension of any people.

Humanity was a mixed new question.

Perhaps frightening.

Perhaps free.

The conclusion did not turn into grand light inside him. It settled in his stomach like a stone. He remembered the first time he had seen mixed cities in Another World: orcs, elves, dwarves, everyone arguing in taverns, occasionally fighting over the distribution of quest rewards. Back then he had thought it was cool world design. Now he understood that real mixture carried more weight. There was no designer balancing the table in advance. No system guaranteed that every inheritance would survive fairly.

Some inheritance became talent.

Some became illness.

Some became dreams no one could explain: the fear a child felt during a first look at the stars, the strange familiarity an adult felt while hearing news of a tsunami, the impulse to build towers, ships, probes, even while knowing how small humanity was.

Charlie wanted to tell his younger joking self.

If someone had told him back then that his body and consciousness held the aftershock of a solar-system war, he probably would have asked whether it could be turned into a game.

He could not ask that now.

Because behind every dazzling premise, someone might truly have died.

And death did not automatically become noble.

Some deaths were rushed. Some were ugly. Some were not seen by anyone at all. History selected only a few images. The rest fell like dust into the seams of the record, waiting for some unlucky later visitor to pass by and stick to his consciousness.

Charlie thought he was that later visitor.

The white line tightened again. The lights receded. Before leaving, Charlie heard a low whale song rising beneath all fragments.

As if confirming he had heard correctly.""",

    "45_给安娜留下的问题": """# 45 A Question for Anna

After the whale song, Charlie heard another sound.

It was faint, almost hidden under the Giant Whale's low frequency. At first it sounded like wind over grass, then like a small animal stepping over stones in darkness. Charlie followed it and saw unfamiliar green.

Not ocean.

Forest.

The trees were tall, roots exposed in wet soil, small lights floating in the air. These lights did not resemble star-sea dust from whale memory. They felt more like the body heat left by animal consciousness in night. Charlie saw no clear creature, only many eyes flashing past: a feline vertical pupil, a bird's side-glance, a deer-like dark outline, and a black cat standing on a root, watching him quietly.

Charlie's chest tightened.

“Jim?” he called.

No answer.

The black cat did not approach. It only lifted its head, as if listening to whale song from far below the sea. By the time the song reached the forest it had grown faint, yet every floating light brightened at once.

Charlie did not understand.

He had seen the war of five peoples, the whale seed, the way blue whale song turned star inheritance into Earth's natural echo. This forest did not belong to Phaeton. Nor did it resemble a war slice from the Moon-dark record.

It was softer.

And more dangerous.

There were no weapons here, yet danger slowly seeped from those silent gazes. The animals did not speak, yet seemed to share an understanding older than language. Charlie suddenly thought of Anna. She was not catlike, but if anyone could stand inside this complex, quiet, ruleless forest without panicking, it might be her.

She would observe first.

She would mark where every animal appeared.

She would ask: are they listening to whale song, or answering it?

The black cat blinked.

Charlie felt it had heard his thought.

He retreated half a step by instinct, though his foot found no ground. This forest did not behave like ordinary space. It felt like a dream maintained by animal consciousness. Under the roots lay tiny white bones and new shoots just breaking through. Rot and birth pressed together in the same inch of soil without shame. Charlie saw a gray bird land on a bone and peck once. When it lifted its head, a very brief blue light crossed its eye.

The blue reminded him of the whale seed's low frequency.

Between ocean and forest, there seemed to be an extremely thin line.

At one end, vast life entrusted memory to song. At this end, countless animals entrusted experience to instinct, scent, migration, and dream. Charlie could not explain it. He only knew the place belonged to Anna. Anna could see the edge of rules while everyone else watched the spectacle. She would know what in this forest was bait, what was a plea, and what was only some ancient life turning in sleep.

Then a very soft meow came from the depths of the forest.

The sound passed through Charlie and left a question: if the whale's echo could hide inside ocean life, did other animal consciousness carry some older spiritual civilization?

The question was too large.

Too unlike something Charlie could answer.

“This is for Anna,” he thought almost immediately.

The white line trembled, as if Jim had received the thought.

Digital Jim's voice came from far away. “Do not enter. That is not Charlie's region.”

Charlie retreated at once.

This time he retreated willingly. After Phaeton, he had learned enough respect for records that did not belong to him. The black cat remained on the root, tail brushing wet soil.

It did not stop him.

It did not say goodbye.

Before the white line pulled Charlie away, he saw the cat lift its head again toward an unseen sea.

Far, far away, the blue whale was still singing.

The animal consciousness of the forest stirred like water in night.

Charlie packed the image into the last space he could carry.

For Anna.

He did not know if she would wake.

But if she did, the question belonged to her.

The black cat seemed to have waited for this decision. At last it jumped down from the root. It landed without sound. When its paws touched the wet soil, a shallow green light rippled across the mud. The light did not spread to Charlie. It traveled along the roots into the depths of the forest, like a silent notice.

A deer lowered its head.

A bird folded its wings.

Farther away, some huge dark shape slowly turned behind the trees, tilting the whole curtain of rain. Charlie could not see it clearly. He only felt it was old, old enough that perhaps it did not care whether humans woke.

The black cat looked at him one last time.

There was no invitation in its eyes, and no warning. It seemed to say: remember the door is here. Do not enter for her.

Charlie nodded.

For the first time, letting go felt like a kind of responsibility.""",

    "46_回声归档": """# 46 Echo Archive

The white line suddenly tightened.

Before Charlie could recover from the black cat's gaze, space began to fold. Whale song, forest, corpse mountain, asteroid belt, and Spirit Connect white light all collapsed toward the center, as if someone had finally pressed archive.

Digital Jim's voice sharpened for the first time. “Archiving has begun.”

Jim asked, “Meaning?”

“Charlie's region is being reclaimed by the Terasha Record. It will compress preservable information into echo and strip out the subject-core. If we are slow, he becomes part of the record.”

When Charlie heard “part of the record,” his heart dropped.

He had seen too many preserved things.

Preservation sounded gentle. If what was preserved was yourself, less so. He did not want to become a war slice for future visitors, standing forever on the corpse mountain and understanding victory again and again.

“Then hurry!” he shouted.

Jim's voice came through the white line. “Hold on.”

“I am holding!”

“Hold harder.”

“That has no technical content at all!”

“I handle the part without technical content.”

Being able to argue at a time like this made Charlie feel oddly close to returning.

The archive gave little time.

The white line began to heat.

It did not burn skin, because Charlie no longer had stable skin. It felt more like an over-stretched nerve, every tiny tremor passing directly into his “I.” Jim seemed to be suffering on the other end too. The white line flickered, and several times almost vanished into the archive layer. Charlie could even hear the aftersound of Digital Jim's rapid calculation deeper down, like countless glass flakes rubbing together.

“What happens if it breaks?” Charlie asked.

“Do not ask,” Jim said.

“That is usually not a good answer.”

“Then do not ask.”

Charlie shut up.

He suddenly knew very clearly that he was still afraid: afraid of being left behind, afraid of never waking, afraid no one would believe him, and afraid everyone would. This time the fear did not drag him backward. It was a heavy piece of iron he carried while running forward.

Images peeled away layer by layer. Lo'an's craft became a low-frequency segment, then was pulled into darkness. Sern's silver-blue wing light became a thin line. The elder's water membrane became a transparent ring. Phaeton's debris compressed into orbital parameters. Even the blue whale song began turning into indexed spectrum.

Everything was becoming clean.

Too clean.

Charlie suddenly felt fierce resistance.

He used to like clarity. Game quests should have clear goals; maps should mark routes; rewards should be written in the description. But now he watched war cleaned into archive and pain compressed into data, and he understood that excessively clear records could also lie. They made later people believe everything had a conclusion, death was only the price of a historical node, and a survivor counted as remembered if a name remained.

Lo'an was not a line of text.

Sern was not a sacrifice entry.

They joked, regretted, cursed while running, pretended to be fine when fear had almost emptied them. Charlie even remembered the tiny pain stirred by Sern's wings, the way Lo'an's throat rasped like sandpaper when he was thirsty. These things had no grand meaning, yet they were harder to counterfeit than grand meaning.

Charlie seized the parts that still hurt: blood from Lo'an's cracked fingers, the unbearable curve of Sern's grin, the elder's terrifyingly light body, Lanke's scales pressed flat after losing her canister, the gold fading when Soler burned his sun-ring.

“These cannot all be washed away,” Charlie said.

Digital Jim replied, “You cannot carry all of them.”

“Then I carry the parts that hurt.”

The white line flared.

Jim whispered, “Now.”

Charlie felt two forces pull at once. One was the Terasha archive layer, calm, huge, patient, like water grinding everything into a preservable shape. The other was Jim's white line, unstable, but warm like a human hand.

Digital Jim cut open a gap deeper in the layer.

“Subject-core passing.”

Charlie did not understand what that meant.

He only felt himself torn out of water.

All images retreated. Whale song stretched into a single line. Corpse mountain collapsed into gray. The black cat's eyes flashed once in the final second. Then Lo'an's voice came from very far away:

“Run seriously.”

Charlie gripped the white line and rushed into white light.""",

    "47_醒来之前": """# 47 Before Waking

Before waking, Charlie returned to a body.

This time there was no battlefield.

No complete human shape either.

He felt only a hand. Dark-gray fine scales covered its back, fingers long, dried blood at the tips. Lo'an's hand. It hung in darkness without arm, chest, or face, as if the host's final trace had kept only this body memory.

Charlie reached out with his own hand.

The two hands were separated by a thin layer of light.

“Are you still here?” Charlie asked.

No language answered.

The hand moved slightly.

Then many things rose together: breath on the corpse mountain, ash in supply trenches, Sern pulling him while fleeing, the cold pressure of holding the vessel, the sting when the log system recognized blood from his wound.

Lo'an did not appear as soul or hero.

He said goodbye as body memory.

That suited him better.

Charlie wanted to cry, but he had cried too many times, and tears felt insufficient here.

“Thank you,” he said.

The hand paused.

Charlie knew Lo'an would dislike the word.

So he corrected himself. “Fine. Not thank you. You ran very seriously.”

The fingers curled, almost laughing.

Charlie laughed too.

He finally understood that Lo'an had not given him courage. Courage was too clean, too easy for later people to carve into statues. Lo'an had given him something more ordinary: still knowing what not to drop while afraid, still remembering who handed you the road while wanting to run.

It was not beautiful.

It could carry a seed to the sea.

The hand moved again.

This time Charlie saw smaller fragments.

Not war. Not the Giant Whale. A low cabin where Lo'an as a child pressed his ear to the thin wall and listened to the hum of water-cycle pipes. A dusk when he and Sern lay under a maintenance rack stealing ration candy, then both pretended innocence after an inspector found them. Long ago, before Phaeton's sky had fully turned the color of war, a strip of blue-violet sunset had fallen across a metal roof.

These memories were too small.

So small a war archive might never preserve them.

Yet Charlie suddenly felt they mattered more than any strategic meeting. Lo'an had not grown out of the corpse mountain. He had once been only a child stealing candy, a child who mistook pipe hum for distant sea sound. History later pushed him to the exit, and only then had he become the survivor Charlie knew.

“I will try to remember you were not always this bitter,” Charlie said.

The hand paused.

Then the fingertips touched the membrane of light.

Like a very brief handshake.

Charlie suddenly remembered all the times he had said, in reality, that he was afraid to die. He had said it lightly, as a joke that made rooms easier. When Anna analyzed risk, he would raise a hand and say he was responsible for getting everyone home alive. When Jim wanted to rush toward a dangerous zone, Charlie would complain that next time they should at least prepare a will template. In Another World, when a monster was too strong, he was the first to shout retreat.

Now he understood that fear of death had not made him small.

Only people who feared death knew what staying cost. Lo'an had not been fearless. He had been terrified, and still reached for the switch that had to be pressed. Sern had not been born for sacrifice. He had understood that if no one reconnected the route in that second, everyone would have died for nothing.

Charlie wanted to bring that back.

For Jim, and for Anna.

If one day they stood before a similar choice, at least they would not imagine courage too lightly.

The dark began to brighten.

Jim's voice came from far away, clearer and clearer. Dr. Lune too, mixed with device alerts, draining fluid, and hurried steps. Reality approached with disinfectant, metal, and the heavy breath of a human body.

Charlie looked at the hand Lo'an left.

“I will remember the parts that hurt,” he said.

The scales on the back of the hand broke into gray light.

In the final moment, Charlie heard a faint Wing-Shiver frequency. It sounded like Sern's laugh, and like a low note inside distant blue whale song.

Then the dark split open.

Charlie rose.""",

    "48_蓝鲸在地球歌唱": """# 48 Blue Whales Sing on Earth

When Charlie woke, the first thing he did was choke.

Air rushed into his lungs like a rough brush scraping from inside. He curled up, fingers gripping the pod edge until the knuckles went pale. Someone shouted his name. Someone held his shoulders down. Instruments gave a chain of overly excited beeps.

“Charlie, can you hear me?”

Dr. Lune.

Charlie tried to answer, but coughed up a mouthful of fluid first. His throat burned. He could barely open his eyes. His body felt horribly unfamiliar, too light and too narrow, without dark-gray scales, without Lo'an's deeper chest resonance.

Then he cried.

Not the eyeless crying inside the record.

This time tears truly rolled down his face and mixed with fluid in the pod. It was an ugly cry: coughing, shaking, gasping, like someone dragged from very deep water.

Dr. Lune lowered his voice. “Slowly. Don't rush. You're back.”

Charlie grabbed his sleeve.

“Blue whale,” he said.

Dr. Lune froze. “What?”

“Find blue whale sound.”

No one understood immediately.

Jim stood nearby, his face pale as if he too had crossed a long distance. He looked at Charlie's eyes, then turned to the assistant at the console. “Open the ocean acoustics database. Blue whale low frequency. Now.”

Several seconds later, a low sound came through the lab speakers.

Long, slow, almost less sound than pressure making the chest vibrate.

Charlie closed his eyes.

He did not explain.

He could not.

When the sound began, the pod, lab, doctors, alarms all withdrew. Ocean opened inside his mind again. Phaeton's ring turned quietly farther away. Sern's wings, Lo'an's hand, the elder's water membrane, the falling shadow of the Giant Whale all touched one another inside that low frequency.

They were still there.

Not fully alive.

Not fully dead.

Charlie pressed his forehead against the pod wall, tears still falling. He thought of the first image in the dream: himself standing on a mountain of bodies, a friend beside him, someone celebrating victory in the distance. He had thought he had merely dreamed a war too magnificent to forget. Now he knew why that “victory” had felt wrong from the beginning.

The true victor had not stood on the corpse mountain.

What remained was a song in the sea, so slow most people would never bother to hear it through.

He tried to laugh, and coughed instead. Dr. Lune handed him an absorbent cloth with a careful motion. The man who usually hid feeling behind professional calm had reddened eyes now. He did not ask what Charlie had seen. He did not hurry him toward language. He only enlarged the spectrogram, letting the low-frequency curve move slowly across the screen.

Charlie thought this was one strange thing about humans.

They could compress an ancient war into a database, and they could fall silent for a whale song.

Outside the control room, someone drew a small breath.

The sound was tiny, but it made Charlie realize he was not the only one hearing the blue whale. Several researchers who had been responsible only for monitoring data stood behind the glass, their working expressions loosened. One removed his headset, as if suddenly unable to remember which metric he was supposed to record. Another young assistant stared at the screen, finger hovering above the confirmation key without pressing it.

They might not understand Phaeton.

They might not understand Lo'an.

They might not understand what the whale seed had truly left while crossing Earth's window.

But they could hear a vast loneliness slowly passing from the deepest ocean through a human laboratory.

That was already enough.

Charlie opened his eyes, voice raw. “They are still there.”

This time, no one interrupted him.

Dr. Lune looked at the spectrogram, then at Jim.

Jim said nothing. He simply sat beside Charlie, as if finally confirming he had pulled someone back.

Charlie leaned against the pod wall and listened to the whole blue whale song.

When it ended, the lab stayed quiet for several seconds.

Charlie lifted his head and looked toward Anna's sleeping pod.

“Her side...” His voice was soft. “It may not be war.”

Jim followed his gaze.

On Anna's pod, the status light flickered faintly.

Like an eye opening in darkness.""",

    "49_尾声：没有完全死去": """# 49 Epilogue: Not Fully Dead

Three hours after Charlie woke, Jim finally received the memory.

Not complete images.

What Charlie brought back resembled thread soaked in water. Inside it were Phaeton's white fracture light, the first orbits of the asteroid belt, the low frequency left by the whale seed crossing Earth's window, and the final log Lo'an burned the coordinates around:

We did not win.

The seed belongs to no people.

Do not follow.

Jim said nothing for a long time.

Dr. Lune stood beside him with a tablet in hand and forgot to record. On the screen, the blue whale spectrogram remained: a low-frequency curve like a slow undersea mountain range.

“So humanity...” Dr. Lune began, then stopped.

Charlie lay in the bed, pale and exhausted, but strangely clear.

“No one made us alone,” he said. “At least from what I saw. We are more like many failed designs mixed together, then passed through Earth's long evolution and later Moon-dark filtering and other interventions.”

He gave a bitter smile.

“Sounds insane.”

Jim shook his head. “Insanity is no longer enough for where we are.”

Charlie closed his eyes.

He was tired.

But whenever he closed them, the corpse mountain returned. Sern pointing at the battlefield: do not make this place too beautiful. Lo'an saying someone who fears death will not speak of it too lightly.

So Charlie opened his eyes again.

“Jim,” he said, “if you show this memory to anyone, don't give them only the conclusion.”

“I know.”

“No, you don't.” Charlie looked at him. “You people who've seen the Moon's dark side can jump straight to truth. Truth is huge. It sounds like the sky falling. But Lo'an and the others did not die so we could be shocked.”

Jim did not argue.

Charlie spoke slowly. “Let people know they were afraid, regretted things, wanted to live. Otherwise this becomes another myth.”

Dr. Lune finally lowered his head and wrote that down.

Outside, dawn had not yet arrived.

The city moved quietly in night, aircraft lanes thin lines of light. Earth still looked human: steel, glass, lamps, schedules. But deeper, in an ocean no one in the room could hear, blue whales were still singing.

Charlie sank back into the pillow and suddenly felt the unreasonable weight of his body. In reality he had no scales, no vibrating wings, no organ that could pass memory through seawater. He was only an eighteen-year-old who had just awakened, throat raw, monitoring needle in his hand, hair stuck together with pod fluid. Yet inside that unepic body pressed the echo of a dead planet.

He finally understood why Lo'an had not asked to be remembered.

Being remembered was too hard.

Records lost body warmth. Memorials smoothed edges. Later people always shaped complicated lives into forms easier to tell. Perhaps the best one could do was lie a little less in the next telling, and leave some pain intact.

“I will write it slowly,” Jim said, as if he knew what Charlie was thinking.

Charlie looked at him. “Do not make me too handsome.”

Jim paused half a second. “Then you may be very safe.”

Charlie laughed once, pulled the wound, and drew in a careful breath.

The small laugh loosened the room. Dr. Lune lowered his head and adjusted archive permissions, pretending not to hear. On the screen, the blue whale spectrum filed itself away. The temporary file name appeared with a final tag: Phaeton-Whale-Echo.

At the same time, in Anna's consciousness region, rain fell on a black forest.

The rain touched leaves without sound.

A black cat sat on an exposed root, ears twitching. It had been watching the forest depths, as if waiting for footsteps underground. But when blue whale low frequency crossed from far away, it suddenly lifted its head.

In the cat's eyes, a small piece of sea reflected.

Far away.

Very old.

It listened for a while, tail slowly sweeping wet soil.

Then more eyes lit in the forest.

Bird, deer, dog, fox, and other silhouettes not easily named looked from darkness toward the same direction.

The black cat gave a small call.

The sound was tiny, yet the whole forest seemed to wake.

In the real world, Anna still did not open her eyes.

But outside her Spirit Connect pod, the status light turned deep green for the first time.

Charlie heard the alert and turned.

Jim saw it too.

No one spoke.

The blue whale song had stopped, but its afterwave still remained in the lab air. Charlie thought then that perhaps the Giant Whale truly had not fully died. It had become many slow things: song in the sea, light in the asteroid belt, contradiction inside human bodies, and the instant a black cat lifted its head.

The story had not ended.

The next echo had simply turned in another direction.""",
}


def md_to_html(text):
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            out.append(f"<h1>{html.escape(s[2:])}</h1>")
        elif s.startswith("## "):
            out.append(f"<h2>{html.escape(s[3:])}</h2>")
        else:
            out.append(f"<p>{html.escape(s)}</p>")
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
<body><main>
{body}
{nav}
</main></body></html>
"""


def nav_for(stem, lang):
    base = EN_MD if lang == "en" else ZH_MD
    stems = [p.stem for p in sorted(base.glob("*.md"))]
    idx = stems.index(stem)
    links = ['<nav class="chapter-nav">']
    if idx > 0:
        links.append(f'<a href="{html.escape(stems[idx - 1])}.html">上一章 / Previous</a>')
    links.append(f'<a href="../{"index_EN.html" if lang == "en" else "index.html"}">目录 / Index</a>')
    if idx < len(stems) - 1:
        links.append(f'<a href="{html.escape(stems[idx + 1])}.html">下一章 / Next</a>')
    links.append("</nav>")
    return "\n".join(links)


def write_chapter(stem, zh, en):
    (ZH_MD / f"{stem}.md").write_text(zh + "\n", encoding="utf-8")
    (EN_MD / f"{stem}.md").write_text(en + "\n", encoding="utf-8")
    (ZH_HTML / f"{stem}.html").write_text(
        page(stem, md_to_html(zh), nav_for(stem, "zh"), "zh-CN"), encoding="utf-8"
    )
    (EN_HTML / f"{stem}.html").write_text(
        page(stem, md_to_html(en), nav_for(stem, "en"), "en"), encoding="utf-8"
    )


for key in ZH:
    write_chapter(key, ZH[key], EN[key])

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
if "- `44_人类的混合遗产`：已扩写为正文样稿。" not in text:
    marker = "- `43_所谓胜利`：已扩写为正文样稿。\n"
    insert = marker + "\n".join(
        [
            "- `44_人类的混合遗产`：已扩写为正文样稿。",
            "- `45_给安娜留下的问题`：已扩写为正文样稿。",
            "- `46_回声归档`：已扩写为正文样稿。",
            "- `47_醒来之前`：已扩写为正文样稿。",
            "- `48_蓝鲸在地球歌唱`：已扩写为正文样稿。",
            "- `49_尾声：没有完全死去`：已扩写为正文样稿。",
            "",
        ]
    )
    text = text.replace(marker, insert)
text = text.replace(
    "下一步建议从 `44_人类的混合遗产` 开始继续逐章扩写到 1500-2000 中文字，并同步更新英文版与 HTML 阅读页。",
    "V1 正文已扩写到尾声。下一步建议通读全书，做结构审稿、连续性检查和第二版修订计划。",
)
readme.write_text(text, encoding="utf-8")

print("Expanded chapters 44-49 and regenerated matching HTML files.")
