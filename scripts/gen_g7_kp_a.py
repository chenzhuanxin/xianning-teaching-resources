# -*- coding: utf-8 -*-
"""七年级 语文/数学/英语 知识点考点 HTML"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kp_engine import render, KP, BAR, TABLE

# =========================================================
#                        七年级语文
# =========================================================
render("七年级", "语文",
 ["人教版（统编版）", "七上 + 七下", "2024秋新修订"],
 [
  {"title":"一、字音字形","tag":"基础必考","body":
   KP("1. 七上重点字音字形",1,[
     "<strong>朗润</strong>（rùn）　<strong>酝酿</strong>（yùn niàng）　<strong>卖弄</strong>（nòng）　<strong>喉咙</strong>（hóu lóng）",
     "<strong>应和</strong>（yìng hè）　<strong>嘹亮</strong>（liáo）　<strong>烘托</strong>（hōng）　<strong>抖擞</strong>（dǒu sǒu）",
     "<strong>瘫痪</strong>（tān huàn）　<strong>暴怒无常</strong>　<strong>侍弄</strong>（shì nòng）　<strong>捶打</strong>（chuí）",
     "<strong>烂漫</strong>（làn màn）　<strong>翻来覆去</strong>　<strong>喜出望外</strong>　<strong>絮絮叨叨</strong>（xù dāo）",
     "<strong>匿笑</strong>（nì）　<strong>沐浴</strong>（mù yù）　<strong>祷告</strong>（dǎo）　<strong>荫蔽</strong>（yīn bì）",
     "<strong>分歧</strong>（qí）　<strong>各得其所</strong>　<strong>粼粼</strong>（lín）　<strong>一霎</strong>（shà）",
     "<strong>攲斜</strong>（qī xié）　<strong>恍然大悟</strong>　<strong>花团锦簇</strong>（cù）　<strong>感慨</strong>（kǎi）",
     "易错字：<strong>「诀别」</strong>不写「决别」；<strong>「粗犷」</strong>（guǎng）不读 kuàng；<strong>「静谧」</strong>（mì）；<strong>「咄咄逼人」</strong>（duō）",
   ],("warn","✍","七年级字词量骤增，必须建立<strong>错字本</strong>。重点辨析<strong>形近字</strong>（诀/决、蔽/弊、嘹/缭）和<strong>多音字</strong>（和、薄、落、载）。"))
   + KP("2. 七下重点字音字形",2,[
     "<strong>元勋</strong>（xūn）　<strong>奠基</strong>（diàn）　<strong>选聘</strong>（pìn）　<strong>谣言</strong>（yáo）",
     "<strong>昼夜</strong>（zhòu）　<strong>昆仑</strong>（lún）　<strong>挚友</strong>（zhì）　<strong>可歌可泣</strong>",
     "<strong>鲜为人知</strong>（xiǎn）　<strong>至死不懈</strong>（xiè）　<strong>鞠躬尽瘁</strong>（cuì）　<strong>当之无愧</strong>",
     "<strong>梳头</strong>　<strong>抱歉</strong>　<strong>秩序</strong>　<strong>深恶痛绝</strong>（wù）",
     "<strong>疙瘩</strong>（gē da）　<strong>粗拙</strong>（zhuō）　<strong>守寡</strong>（guǎ）　<strong>震悚</strong>（sǒng）",
     "<strong>憎恶</strong>（zēng wù）　<strong>烦琐</strong>（suǒ）　<strong>诘问</strong>（jié）　<strong>霹雳</strong>（pī lì）",
     "<strong>孤孀</strong>（shuāng）　<strong>伛</strong>（yǔ）　<strong>滞笨</strong>（zhì bèn）　<strong>愧怍</strong>（kuì zuò）",
     "<strong>修葺</strong>（qì）　<strong>折损</strong>　<strong>陡峭</strong>　<strong>妥帖</strong>（tiē）",
   ],("tip","💡","注意<strong>「载」</strong>字：装载（zài）/ 记载（zǎi）；<strong>「强」</strong>：强壮（qiáng）/ 勉强（qiǎng）/ 倔强（jiàng）。")),
 },

  {"title":"二、古诗文默写与鉴赏","tag":"必考｜高频","body":
   KP("1. 七上古诗词（必背）",1,[
     "<em>《观沧海》曹操</em>：日月之行，若出其中；星汉灿烂，若出其里。",
     "<em>《闻王昌龄左迁龙标遥有此寄》李白</em>：我寄愁心与明月，随君直到夜郎西。",
     "<em>《次北固山下》王湾</em>：海日生残夜，江春入旧年。乡书何处达？归雁洛阳边。",
     "<em>《天净沙·秋思》马致远</em>：枯藤老树昏鸦，小桥流水人家，古道西风瘦马。夕阳西下，断肠人在天涯。",
     "<em>《峨眉山月歌》李白</em>：峨眉山月半轮秋，影入平羌江水流。",
     "<em>《江南逢李龟年》杜甫</em>：正是江南好风景，落花时节又逢君。",
     "<em>《行军九日思长安故园》岑参</em>：遥怜故园菊，应傍战场开。",
     "<em>《夜上受降城闻笛》李益</em>：不知何处吹芦管，一夜征人尽望乡。",
     "<em>《秋词》刘禹锡</em>：自古逢秋悲寂寥，我言秋日胜春朝。",
     "<em>《夜雨寄北》李商隐</em>：何当共剪西窗烛，却话巴山夜雨时。",
   ])
   + KP("2. 七下古诗词（必背）",2,[
     "<em>《木兰诗》</em>：万里赴戎机，关山度若飞。朔气传金柝，寒光照铁衣。",
     "将军百战死，壮士十年归。……雄兔脚扑朔，雌兔眼迷离；双兔傍地走，安能辨我是雄雌？",
     "<em>《竹里馆》王维</em>：深林人不知，明月来相照。",
     "<em>《春夜洛城闻笛》李白</em>：此夜曲中闻折柳，何人不起故园情。",
     "<em>《逢入京使》岑参</em>：马上相逢无纸笔，凭君传语报平安。",
     "<em>《晚春》韩愈</em>：杨花榆荚无才思，惟解漫天作雪飞。",
     "<em>《登幽州台歌》陈子昂</em>：念天地之悠悠，独怆然而涕下。",
     "<em>《望岳》杜甫</em>：会当凌绝顶，一览众山小。",
     "<em>《登飞来峰》王安石</em>：不畏浮云遮望眼，自缘身在最高层。",
     "<em>《游山西村》陆游</em>：山重水复疑无路，柳暗花明又一村。",
     "<em>《己亥杂诗》龚自珍</em>：落红不是无情物，化作春泥更护花。",
     "<em>《泊秦淮》杜牧</em>：商女不知亡国恨，隔江犹唱后庭花。",
   ])
   + KP("3. 文言文（七上）",3,[
     "<em>《世说新语》二则</em>：《咏雪》——「未若柳絮因风起」；《陈太丘与友期行》——「日中不至，则是无信；对子骂父，则是无礼」。",
     "<em>《论语》十二章</em>：学而时习之；有朋自远方来；人不知而不愠；温故而知新；学而不思则罔，思而不学则殆；三人行必有我师焉；逝者如斯夫，不舍昼夜。",
     "<em>《诫子书》诸葛亮</em>：静以修身，俭以养德。非淡泊无以明志，非宁静无以致远。",
     "<em>《狼》蒲松龄</em>：一狼得骨止，一狼仍从……乃悟前狼假寐，盖以诱敌。狼亦黠矣，而顷刻两毙，禽兽之变诈几何哉？止增笑耳。",
     "<strong>重点实词</strong>：说（通假「悦」，yuè）　愠（yùn，生气）　罔（wǎng，迷惑）　殆（dài，疑惑）　笃（dǔ，坚定）　黠（xiá，狡猾）",
   ],("key","★","《<strong>论语</strong>》十二章是七年级文言文重中之重，<strong>逐句默写+翻译</strong>必须过关。"))
   + KP("4. 文言文（七下）",4,[
     "<em>《孙权劝学》</em>：卿今当涂掌事，不可不学！士别三日，即更刮目相待。（成语：吴下阿蒙、刮目相待）",
     "<em>《卖油翁》欧阳修</em>：无他，但手熟尔。我亦无他，惟手熟尔。（道理：熟能生巧）",
     "<em>《陋室铭》刘禹锡</em>：斯是陋室，惟吾德馨。苔痕上阶绿，草色入帘青。",
     "<em>《爱莲说》周敦颐</em>：予独爱莲之出淤泥而不染，濯清涟而不妖。（托物言志，象征君子）",
     "<em>《活板》沈括</em>：活字印刷术（毕昇）流程：刻字—排版—印刷—拆版。",
     "<strong>一词多义</strong>：为（wéi/wèi）、之（助词/代词/动词）、而（并列/转折/修饰）",
   ])
   + KP("5. 古诗文鉴赏高频考点",5,[
     "<strong>炼字题</strong>：先解字义→描绘画面→点明情感/作用。（如「海日<em>生</em>残夜，江春<em>入</em>旧年」中「生」「入」的妙处）",
     "<strong>意境分析</strong>：<em>《天净沙·秋思》</em>用「枯藤/老树/昏鸦」等意象渲染萧瑟凄凉，抒游子思乡之悲。",
     "<strong>情感把握</strong>：思乡怀人（次北固山下、春夜洛城闻笛）、壮志豪情（观沧海、望岳、登飞来峰）、离愁别绪（闻王昌龄左迁龙标遥有此寄）。",
     "<strong>手法辨析</strong>：借景抒情、托物言志（爱莲说）、虚实结合、以小见大、用典（闻王昌龄左迁龙标遥有此寄）。",
   ]),
 },

  {"title":"三、现代文阅读","tag":"重难点","body":
   KP("1. 记叙文阅读核心考点",1,[
     "<strong>概括事件</strong>：谁 + 在什么情况下 + 做了什么 + 结果如何（找准「时间、地点、人物、起因、经过、结果」）",
     "<strong>品味语言</strong>：修辞角度（比喻/拟人/夸张/排比）+ 内容 + 效果 + 情感",
     "<strong>人物形象</strong>：结合描写方法（外貌/语言/动作/神态/心理）与具体事件分析性格品质",
     "<strong>环境描写作用</strong>：交代背景、渲染气氛、烘托心情、推动情节、突出主题",
     "<strong>句段作用</strong>：开头（总领全文、设置悬念、引出下文）；中间（承上启下）；结尾（总结全文、深化主题、首尾呼应）",
     "<strong>标题作用</strong>：概括内容、点明中心、设置悬念、吸引读者、贯穿全文线索",
   ],("tip","💡","答题模板：<strong>手法 + 内容 + 效果（情感）</strong>　例如：「运用比喻，把××比作××，生动形象地写出了××的特点，表达了作者××的感情。」"))
   + KP("2. 说明文阅读核心考点",2,[
     "<strong>说明方法及作用</strong>：举例子（具体真切）｜列数字（准确具体）｜作比较（突出强调）｜打比方（生动形象）｜分类别（条理清楚）｜下定义（准确严密）｜列图表（直观明了）",
     "<strong>说明顺序</strong>：时间顺序、空间顺序、逻辑顺序（由主到次、由现象到本质、由概括到具体）",
     "<strong>语言准确性</strong>：如「大约」「左右」「基本上」「之一」等词不能删，因为体现了说明文语言的准确性、严密性。",
     "<strong>找中心句</strong>：多在段首（总起）或段尾（总结）",
     "七下典型篇目：《大自然的语言》《恐龙无处不有》《被压扁的沙子》《阿西莫夫短文两篇》",
   ])
   + KP("3. 散文阅读核心考点",3,[
     "<strong>线索梳理</strong>：时间线、空间线、情感线、事物线（如《紫藤萝瀑布》以「花」为线索）",
     "<strong>情感把握</strong>：抓议论抒情句，如《紫藤萝瀑布》——「花和人都会遇到各种各样的不幸，但是生命的长河是无止境的」",
     "<strong>手法赏析</strong>：借景抒情、托物言志、欲扬先抑、以小见大、首尾呼应",
     "<strong>主旨概括</strong>：通过写……表达了……（的思想感情/人生感悟）",
   ]),
 },

  {"title":"四、名著阅读","tag":"必考","body":
   KP("七年级必读名著",1,[
     "<strong>《朝花夕拾》（鲁迅）</strong>：回忆性散文集，共10篇。代表作《从百草园到三味书屋》《阿长与〈山海经〉》《藤野先生》《范爱农》《父亲的病》。主题：回忆往事、批判封建、怀念亲友。",
     "<strong>《西游记》（吴承恩）</strong>：四大名著之一，共100回。主要人物：孙悟空（机智勇敢、桀骜不驯）、猪八戒（憨厚贪吃）、唐僧（善良执着）、沙僧（忠厚老实）。经典情节：三打白骨精、大闹天宫、真假美猴王、三借芭蕉扇、车迟国斗法。",
     "<strong>《骆驼祥子》（老舍）</strong>：七下重点。主人公祥子——从勤劳要强到堕落自私。三起三落。虎妞、小福子。主题：旧社会不让好人有出路。",
     "<strong>《海底两万里》（凡尔纳）</strong>：七下重点。尼摩船长、阿龙纳斯教授、康塞尔、尼德·兰。「诺第留斯号」潜艇。科学幻想与人文精神。",
   ],("key","★","名著阅读常考：<strong>人物形象+性格</strong>、<strong>典型情节</strong>、<strong>主题思想</strong>。建议整理「人物—情节—性格」三栏表。")),
 },

  {"title":"五、写作与综合性学习","tag":"提分项","body":
   KP("1. 作文评分与提分策略",1,[
     "<strong>审题立意</strong>：抓关键词、抓限制词、化大为小。如「这也是一种美」——重点在「也」字。",
     "<strong>选材</strong>：真实、新颖、从小事入手，「以小见大」。避免老套（送伞、让座、考试失利）。",
     "<strong>结构</strong>：凤头（开门见山/设悬念）—猪肚（详略得当，2~3个详写）—豹尾（点题升华，首尾呼应）",
     "<strong>语言</strong>：多用修辞（比喻、拟人、排比）、紧扣细节描写、活用成语诗句。",
     "<strong>卷面</strong>：字迹工整、不涂改、不少于600字。",
   ],("tip","💡","七年级作文常见题型：<strong>命题作文</strong>（《那一次，我真××》）、<strong>半命题作文</strong>（《××的力量》）、<strong>材料作文</strong>、<strong>话题作文</strong>。"))
   + KP("2. 综合性学习与口语交际",2,[
     "<strong>七上</strong>：有朋自远方来（交友之道）｜少年正是读书时（阅读现状调查、制定计划）｜文学部落（创办班刊）",
     "<strong>七下</strong>：天下国家（爱国人物故事）｜孝亲敬老（孝道）｜我的语文生活（正眼看招牌、我来写广告词）",
     "<strong>图表分析</strong>：读标题—看要素—比数据—得结论",
     "<strong>拟写标语/广告词</strong>：简洁、有针对性、有文采（可运用对偶、比喻、谐音）",
   ])
   + KP("3. 语法与修辞知识",3,[
     "<strong>词性</strong>：名词、动词、形容词、数词、量词、代词、副词、介词、连词、助词、叹词、拟声词",
     "<strong>短语结构</strong>：并列（雄伟壮丽）、偏正（我的老师）、动宾（热爱祖国）、主谓（精力充沛）、补充（跑得快）",
     "<strong>句子成分</strong>：主语 / 谓语 / 宾语 / 定语 / 状语 / 补语",
     "<strong>修辞</strong>：比喻（明喻/暗喻/借喻）、比拟（拟人/拟物）、夸张、排比、对偶、反复、设问、反问",
     "<strong>病句类型</strong>：成分残缺、搭配不当、语序不当、重复啰嗦、前后矛盾、滥用否定",
   ]),
 },
 ]
,"资料依据：人教版（统编版）七年级语文 2024年秋新修订教材 · 《义务教育语文课程标准（2022年版）》<br>湖北省咸宁市 2025—2026 学年 · 知识点考点全解", "七年级_语文_知识点考点.html")

print("七年级语文知识点完成")

# =========================================================
#                        七年级数学
# =========================================================
render("七年级", "数学",
 ["人教版", "七上 + 七下", "2024秋新版"],
 [
  {"title":"一、有理数","tag":"七上｜基础","body":
   KP("1. 有理数的概念与分类",1,[
     "<strong>有理数</strong>：整数和分数统称有理数。可分为正有理数、0、负有理数。",
     "<strong>数轴</strong>：规定了原点、正方向、单位长度的直线。任何一个有理数都可用数轴上的点表示。",
     "<strong>相反数</strong>：只有符号不同的两个数。a 的相反数是 <strong>−a</strong>，0 的相反数是 0。",
     "<strong>绝对值</strong>：数轴上表示数 a 的点与原点的距离，记作 |a|。|a| ≥ 0，且 |a| = |−a|。",
     "<strong>倒数</strong>：乘积为 1 的两个数互为倒数（0 没有倒数）。",
   ],("key","★","比较大小：正数>0>负数；两个负数比较，<strong>绝对值大的反而小</strong>。"))
   + KP("2. 有理数的运算",2,[
     "<strong>加法法则</strong>：同号相加取相同符号，绝对值相加；异号相加取绝对值较大的加数符号，并用较大的绝对值减去较小的绝对值。",
     "<strong>减法法则</strong>：减去一个数等于加上这个数的相反数。<em>a − b = a + (−b)</em>",
     "<strong>乘法法则</strong>：两数相乘，同号得正，异号得负；任何数乘 0 都得 0。",
     "<strong>除法法则</strong>：除以一个不为 0 的数，等于乘这个数的倒数。",
     "<strong>乘方</strong>：<em>aⁿ</em> 表示 n 个 a 相乘。<strong>负数的偶次幂为正，奇次幂为负。</strong>",
     "<strong>混合运算顺序</strong>：先乘方 → 再乘除 → 后加减 → 有括号先算括号内。",
     "运算律：加法交换律/结合律、乘法交换律/结合律/分配律。",
   ],("warn","✍","易错：<strong>−2² = −4</strong>，而 <strong>(−2)² = 4</strong>；<strong>|−3| = 3</strong>，但 <strong>−|−3| = −3</strong>。"))
   + KP("3. 科学记数法与近似数",3,[
     "<strong>科学记数法</strong>：<em>a × 10ⁿ</em>（1 ≤ |a| < 10，n 为整数）。如 6 500 000 = 6.5×10⁶。",
     "<strong>精确度</strong>：精确到哪一位或保留几位小数。",
     "<strong>有效数字</strong>：一个近似数中，从左边第一个非 0 数字起到末位数字止的所有数字。",
   ]),
 },

  {"title":"二、整式的加减","tag":"七上｜重点","body":
   KP("1. 单项式与多项式",1,[
     "<strong>单项式</strong>：数或字母的乘积。单独一个数或一个字母也是单项式。",
     "<strong>单项式的系数</strong>：单项式中的数字因数；<strong>次数</strong>：所有字母的指数之和。",
     "<strong>多项式</strong>：几个单项式的和。多项式的<strong>项</strong>是每个单项式，<strong>次数</strong>是最高次项的次数。",
     "<strong>整式</strong>：单项式和多项式统称整式。",
   ])
   + KP("2. 合并同类项与去括号",2,[
     "<strong>同类项</strong>：所含字母相同，且相同字母的指数也相同。与系数无关。",
     "<strong>合并同类项</strong>：字母和指数不变，系数相加。",
     "<strong>去括号法则</strong>：括号前是「+」，去括号各项符号不变；括号前是「−」，去括号各项符号都改变。",
     "<em>a + (b − c) = a + b − c</em>　　<em>a − (b − c) = a − b + c</em>",
   ],("warn","✍","去括号是失分重灾区，特别是「<strong>−</strong>」号后面。建议先写「不动的项」，再逐项变号。"))
   + KP("3. 整式的加减运算",3,[
     "步骤：<strong>去括号 → 合并同类项</strong>。",
     "<strong>化简求值</strong>：先去括号、合并同类项化成最简，再代入数值。",
     "<strong>规律探究</strong>：观察数列/图形规律，用含 n 的式子表示第 n 项。",
   ]),
 },

  {"title":"三、一元一次方程","tag":"七上｜核心","body":
   KP("1. 方程与解方程",1,[
     "<strong>一元一次方程</strong>：只含一个未知数，未知数的次数是 1，等号两边都是整式。",
     "<strong>等式的性质</strong>：①两边加（减）同一个数（式），结果仍相等；②两边乘同一个数（或除以同一个不为 0 的数），结果仍相等。",
     "<strong>解一元一次方程步骤</strong>：去分母 → 去括号 → 移项 → 合并同类项 → 系数化为 1。",
     "<strong>移项</strong>要变号！如 x + 3 = 5 → x = 5 − 3。",
   ],("key","★","<strong>去分母</strong>时，方程两边每一项都要乘各分母的最小公倍数，<strong>不要漏乘不含分母的项</strong>。"))
   + KP("2. 实际问题与一元一次方程",2,[
     "<strong>行程问题</strong>：路程 = 速度 × 时间；相遇（速度和）、追及（速度差）",
     "<strong>工程问题</strong>：工作总量 = 工作效率 × 工作时间（常设总量为 1）",
     "<strong>销售问题</strong>：利润 = 售价 − 进价；利润率 = 利润/进价 × 100%；打折：售价 = 标价 × 折扣",
     "<strong>配套问题</strong>：找等量关系（如 1 个螺栓配 2 个螺母）",
     "<strong>数字问题</strong>：两位数 = 十位数字×10 + 个位数字",
     "<strong>年龄问题</strong>：抓住「年龄差不变」",
     "解题步骤：<strong>审题 → 设未知数 → 找等量关系 → 列方程 → 解方程 → 检验作答</strong>",
   ]),
 },

  {"title":"四、几何图形初步","tag":"七上｜几何入门","body":
   KP("1. 几何图形与直线、射线、线段",1,[
     "<strong>立体图形</strong>：棱柱、棱锥、圆柱、圆锥、球。平面图形：三角形、四边形、圆等。",
     "<strong>直线</strong>：两点确定一条直线；<strong>射线</strong>：有一个端点；<strong>线段</strong>：有两个端点。",
     "<strong>线段公理</strong>：两点之间，<strong>线段最短</strong>。两点间的距离：连接两点的线段的长度。",
     "<strong>线段中点</strong>：把线段分成两条相等线段的点。",
     "<strong>两点间距离</strong>与«线段最短»常考几何证明与计算。",
   ])
   + KP("2. 角",2,[
     "<strong>角的度量</strong>：1° = 60′，1′ = 60″（60进制）",
     "<strong>角的分类</strong>：锐角（<90°）、直角（90°）、钝角（>90°且<180°）、平角（180°）、周角（360°）",
     "<strong>角平分线</strong>：把角分成两个相等的角。",
     "<strong>余角</strong>：两角和为 90°；<strong>补角</strong>：两角和为 180°。",
     "<strong>性质</strong>：同角（等角）的余角相等；同角（等角）的补角相等。",
   ],("key","★","方位角是高频考点：北偏东 30°、南偏西 60° 等，注意「先南北后东西」。")),
 },

  {"title":"五、相交线与平行线","tag":"七下｜重点","body":
   KP("1. 相交线与垂线",1,[
     "<strong>对顶角</strong>：两直线相交，对顶角相等。",
     "<strong>邻补角</strong>：互补（和为 180°）。",
     "<strong>垂线</strong>：两直线相交成直角。垂线段最短。",
     "<strong>点到直线的距离</strong>：直线外一点到这条直线的垂线段的长度。",
   ])
   + KP("2. 平行线的判定与性质",2,[
     "<strong>三线八角</strong>：同位角（F型）、内错角（Z型）、同旁内角（U型）。",
     "<strong>判定</strong>：同位角相等 → 两直线平行；内错角相等 → 两直线平行；同旁内角互补 → 两直线平行。",
     "<strong>性质</strong>：两直线平行 → 同位角相等；内错角相等；同旁内角互补。",
     "<strong>平行公理</strong>：过直线外一点，有且只有一条直线与已知直线平行。",
     "<strong>平行线间的距离处处相等</strong>。",
   ],("warn","✍","<strong>判定</strong>是「由角推平行」，<strong>性质</strong>是「由平行推角」，切勿混用。"))
   + KP("3. 平移",3,[
     "平移不改变图形的<strong>形状和大小</strong>，只改变位置。",
     "平移后：对应线段平行（或共线）且相等；对应角相等；对应点连线平行且相等。",
   ]),
 },

  {"title":"六、实数","tag":"七下｜核心","body":
   KP("1. 平方根与立方根",1,[
     "<strong>算术平方根</strong>：正数 a 的正的平方根，记作 √a（a ≥ 0）。",
     "<strong>平方根</strong>：一个正数有两个平方根，互为相反数，记作 ±√a；0 的平方根是 0；负数没有平方根。",
     "<strong>立方根</strong>：任何数都有立方根，正数立方根为正，负数立方根为负，记作 ∛a。",
     "<strong>重要公式</strong>：(√a)² = a（a≥0）；√(a²) = |a|；∛(a³) = a；∛(−a) = −∛a",
   ],("key","★","易混：√16 = 4（算术平方根），16 的平方根 = ±4，16 的立方根 = ∛16。"))
   + KP("2. 实数的概念与运算",2,[
     "<strong>无理数</strong>：无限不循环小数（如 √2、π、0.1010010001…）。",
     "<strong>实数</strong>：有理数和无理数统称实数。实数与数轴上的点<strong>一一对应</strong>。",
     "<strong>实数的性质</strong>：相反数、绝对值、倒数的定义与有理数一致。",
     "<strong>估算</strong>：用「夹逼法」估算无理数大小，如 2 < √5 < 3。",
     "<strong>运算</strong>：实数的加减乘除、乘方、开方（开不尽的保留根号）。",
   ]),
 },

  {"title":"七、平面直角坐标系","tag":"七下｜基础","body":
   KP("1. 坐标系与点的坐标",1,[
     "<strong>有序数对</strong> (a, b)：a 是横坐标，b 是纵坐标。",
     "<strong>象限</strong>：第一象限 (+,+)｜第二象限 (−,+)｜第三象限 (−,−)｜第四象限 (+,−)。坐标轴上的点不属于任何象限。",
     "<strong>x 轴上的点</strong>纵坐标为 0；<strong>y 轴上的点</strong>横坐标为 0。",
     "<strong>对称点</strong>：关于 x 轴对称（x 不变，y 变号）；关于 y 轴对称（y 不变，x 变号）；关于原点对称（x、y 都变号）。",
   ])
   + KP("2. 坐标与平移",2,[
     "<strong>平移规律</strong>：向右（左）平移 a 个单位，横坐标加（减）a；向上（下）平移 b 个单位，纵坐标加（减）b。",
     "简记：<strong>左减右加，下减上加</strong>。",
   ]),
 },

  {"title":"八、二元一次方程组与不等式","tag":"七下｜重点","body":
   KP("1. 二元一次方程组",1,[
     "<strong>解法</strong>：代入消元法、加减消元法。核心思想：<strong>消元</strong>（二元→一元）。",
     "<strong>实际应用</strong>：和差倍分、配套、行程、销售、方案设计等。",
     "列方程组步骤：审题→设未知数→找等量关系→列方程组→解→检验。",
   ])
   + KP("2. 不等式与不等式组",2,[
     "<strong>不等式性质</strong>：①两边加（减）同一个数，不等号方向不变；②两边乘（除）同一个<strong>正数</strong>，方向不变；③两边乘（除）同一个<strong>负数</strong>，方向<strong>改变</strong>。",
     "<strong>解集在数轴上表示</strong>：实心点「≥、≤」，空心圈「>、<」。",
     "<strong>一元一次不等式组</strong>：取各解集的公共部分。口诀：<strong>大大取大，小小取小，大小小大中间找，大大小小无解了</strong>。",
   ],("warn","✍","<strong>不等式两边乘除负数，一定要变号！</strong>这是七年级最高频失分点。")),
 },
 ]
,"资料依据：人教版七年级数学 2024年秋新版教材 · 《义务教育数学课程标准（2022年版）》<br>湖北省咸宁市 2025—2026 学年 · 知识点考点全解", "七年级_数学_知识点考点.html")

print("七年级数学知识点完成")

# =========================================================
#                        七年级英语
# =========================================================
render("七年级", "英语",
 ["仁爱版（科普版）", "七上 + 七下", "2024秋新教材·6单元制"],
 [
  {"title":"一、语音基础","tag":"入门必过","body":
   KP("1. 26个字母与音标",1,[
     "<strong>元音字母</strong>：a, e, i, o, u（5个）；其余为辅音字母。",
     "<strong>元音音素</strong>：单元音 12 个 / 双元音 8 个；辅音音素 28 个。",
     "字母按读音归类：/eɪ/ 类 A、H、J、K；/iː/ 类 B、C、D、E、G、P、T、V；/e/ 类 F、L、M、N、S、X、Z；/juː/ 类 Q、U、W；/aɪ/ 类 I、Y；/əʊ/ 类 O；/ɑː/ 类 R。",
   ])
   + KP("2. 常见字母组合发音",2,[
     "<strong>元音组合</strong>：ee /iː/（see）｜ea /iː/ 或 /e/（tea, bread）｜ai/ay /eɪ/（rain, day）｜oa /əʊ/（boat）｜oo /uː/ 或 /ʊ/（food, book）",
     "<strong>辅音组合</strong>：th /θ/ 或 /ð/（think, this）｜sh /ʃ/（she）｜ch /tʃ/（chair）｜ck /k/（back）｜wh /w/ 或 /h/（what, who）",
     "<strong>结尾 -s/-es 读音</strong>：清辅音后读 /s/，浊辅音和元音后读 /z/，/s、z、ʃ、tʃ、dʒ/ 后读 /ɪz/。",
     "<strong>词尾 -ed 读音</strong>：/t/、/d/ 后读 /ɪd/；清辅音后读 /t/；浊辅音和元音后读 /d/。",
   ],("tip","💡","仁爱版七年级上册以<strong>音标教学</strong>开篇，务必掌握 48 个国际音标的认读与拼读。")),
 },

  {"title":"二、核心词汇主题","tag":"高频词块","body":
   KP("1. 七上核心话题词汇",1,[
     "<strong>问候与介绍</strong>：hello, hi, good morning/afternoon/evening, nice to meet you, how do you do",
     "<strong>个人信息</strong>：name, age, class, grade, school, telephone number, address, family",
     "<strong>家庭成员</strong>：father, mother, parents, brother, sister, grandfather, grandmother, aunt, uncle, cousin",
     "<strong>外貌描述</strong>：tall, short, thin, heavy, long/short hair, big/small eyes, round face, glasses",
     "<strong>学校生活</strong>：classroom, library, playground, teacher, student, subject, lesson, homework",
     "<strong>食物与饮料</strong>：rice, noodles, bread, egg, meat, fish, vegetable, fruit, milk, juice, water",
     "<strong>颜色与衣物</strong>：red, blue, green, yellow, black, white; coat, shirt, T-shirt, dress, skirt, shoes",
     "<strong>时间与日期</strong>：Monday—Sunday, January—December, morning, afternoon, evening, o'clock",
   ])
   + KP("2. 七下核心话题词汇",2,[
     "<strong>日常活动</strong>：get up, have breakfast, go to school, do homework, go to bed, take a walk, watch TV",
     "<strong>交通方式</strong>：by bus/bike/car/subway, on foot, take a bus, ride a bike",
     "<strong>天气</strong>：sunny, cloudy, rainy, windy, snowy, warm, hot, cool, cold",
     "<strong>季节与节日</strong>：spring, summer, autumn, winter; Spring Festival, Christmas, Mid-Autumn Festival",
     "<strong>方位与地点</strong>：bank, hospital, post office, supermarket, restaurant, library, museum, park",
     "<strong>职业</strong>：doctor, nurse, teacher, driver, farmer, worker, policeman, cook, engineer",
   ]),
 },

  {"title":"三、核心语法","tag":"必考语法","body":
   KP("1. 名词与代词",1,[
     "<strong>名词的数</strong>：规则复数加 -s/-es；不规则：man→men, child→children, foot→feet, tooth→teeth, mouse→mice, sheep→sheep。",
     "<strong>可数与不可数</strong>：不可数名词（water, milk, bread, money, information）无复数，用 a lot of / some / much 修饰。",
     "<strong>人称代词</strong>：主格（I, you, he, she, it, we, they）/ 宾格（me, you, him, her, it, us, them）",
     "<strong>物主代词</strong>：形容词性（my, your, his, her, its, our, their）+ 名词；名词性（mine, yours, his, hers, ours, theirs）。",
     "<strong>指示代词</strong>：this/that（单数）、these/those（复数）。",
   ],("key","★","名词所有格：单数加 <strong>’s</strong>；以 s 结尾的复数加 <strong>’</strong>；无生命名词用 <strong>of</strong> 结构。"))
   + KP("2. 冠词与数词",2,[
     "<strong>不定冠词</strong> a / an：a 用于辅音音素前，an 用于元音音素前（an hour, a useful book）。",
     "<strong>定冠词</strong> the：特指、独一无二、乐器前、序数词/最高级前、姓氏复数前（the Smiths）。",
     "<strong>零冠词</strong>：球类运动、三餐、星期、月份、季节前不加冠词。",
     "<strong>序数词</strong>：first, second, third, fourth… 21st = twenty-first。",
   ])
   + KP("3. 时态（七年级重点三个）",3,[
     "<strong>一般现在时</strong>：表示经常性、习惯性动作。主语第三人称单数动词加 -s/-es。",
     "　　标志词：often, usually, always, sometimes, every day, on Sundays",
     "<strong>现在进行时</strong>：be (am/is/are) + doing，表示正在进行的动作。",
     "　　标志词：now, look, listen, at the moment",
     "<strong>一般过去时</strong>：动词用过去式，表示过去发生的动作。",
     "　　标志词：yesterday, last week, ago, in 2020, just now",
     "　　规则过去式加 -ed；不规则：go→went, have→had, do→did, see→saw, eat→ate, buy→bought",
   ],("warn","✍","<strong>现在进行时</strong>必须「be + doing」缺一不可；<strong>一般现在时</strong>第三人称单数千万别漏 -s。"))
   + KP("4. 情态动词与句型",4,[
     "<strong>can</strong>：能够，会（can + 动词原形，无人称变化）。",
     "<strong>must / have to</strong>：必须。must 强调主观，have to 强调客观。",
     "<strong>There be 句型</strong>：There is + 单数/不可数；There are + 复数。<strong>就近原则</strong>。",
     "<strong>祈使句</strong>：动词原形开头（Open the door.）；否定 Don’t + 动词原形。",
     "<strong>特殊疑问句</strong>：What / Who / Where / When / Why / How / How many / How much / How old",
   ]),
 },

  {"title":"四、功能句型与交际用语","tag":"口语+写作","body":
   KP("高频交际功能句",1,[
     "<strong>问候</strong>：—How are you? —I’m fine, thank you. And you?",
     "<strong>介绍</strong>：—What’s your name? —My name is… / I’m…　—Where are you from? —I’m from China.",
     "<strong>询问时间</strong>：—What time is it? / What’s the time? —It’s eight o’clock.",
     "<strong>购物</strong>：—Can I help you? —I’d like… / How much is it? —It’s ten yuan.",
     "<strong>打电话</strong>：—Hello, may I speak to…? —This is… speaking. / Hold on, please.",
     "<strong>提建议</strong>：Why not…? / What about…? / Let’s… / You’d better…",
     "<strong>表达喜好</strong>：I like/love/enjoy… I don’t like… My favourite… is…",
     "<strong>问路指路</strong>：—Excuse me, where is…? —Go along this street and turn left/right.",
   ]),
 },

  {"title":"五、写作与应试技巧","tag":"提分","body":
   KP("1. 书面表达常见题型",1,[
     "<strong>自我介绍</strong>（Myself）：姓名、年龄、班级、爱好、家庭",
     "<strong>我的家庭/朋友</strong>（My family / My friend）",
     "<strong>我的学校/一天</strong>（My school / My day）",
     "<strong>看图写话 / 提示词作文</strong>",
     "<strong>写通知、便条、邀请函</strong>",
     "写作步骤：<strong>审题（人称、时态、要点）→ 列提纲 → 写草稿 → 检查修改 → 誊写</strong>",
   ],("tip","💡","写作得分诀窍：<strong>要点齐全 + 语法正确 + 书写工整 + 适当发挥</strong>。人称时态别搞错！"))
   + KP("2. 常见失分点",2,[
     "主谓一致错误（He like → He likes）",
     "be 动词与实义动词混用（I am go to school → I go to school）",
     "时态不一致（记叙文全篇应统一时态）",
     "名词单复数、冠词漏用",
     "首字母不大写、句末无标点",
   ]),
 },
 ]
,"资料依据：仁爱版（科普版）七年级英语 2024年秋新教材（6单元制）· 《义务教育英语课程标准（2022年版）》<br>湖北省咸宁市 2025—2026 学年 · 知识点考点全解", "七年级_英语_知识点考点.html")

print("七年级英语知识点完成")
