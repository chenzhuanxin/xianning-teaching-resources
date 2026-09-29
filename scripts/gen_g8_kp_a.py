# -*- coding: utf-8 -*-
"""八年级 语文/数学/英语 知识点考点 HTML"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kp_engine import render, KP, BAR, TABLE

# =========================================================
#                        八年级语文
# =========================================================
render("八年级", "语文",
 ["人教版（统编版）", "八上 + 八下", "2024秋新修订"],
 [
  {"title":"一、字音字形","tag":"基础必考","body":
   KP("1. 八上重点字音字形",1,[
     "<strong>溃退</strong>（kuì）　<strong>锐不可当</strong>（dāng）　<strong>督战</strong>（dū）　<strong>业已</strong>",
     "<strong>要塞</strong>（sài）　<strong>负隅顽抗</strong>（yú）　<strong>歼灭</strong>（jiān）　<strong>星宿</strong>（xiù）",
     "<strong>泄气</strong>　<strong>悄然</strong>（qiǎo）　<strong>屏息敛声</strong>（bǐng liǎn）　<strong>眼花缭乱</strong>",
     "<strong>由衷</strong>（zhōng）　<strong>屏风</strong>（píng）　<strong>颁发</strong>（bān）　<strong>遗嘱</strong>（zhǔ）",
     "<strong>渗透</strong>（shèn）　<strong>摧枯拉朽</strong>　<strong>沸腾</strong>　<strong>仲裁</strong>（zhòng）",
     "<strong>胆怯</strong>（qiè）　<strong>浩瀚</strong>（hàn）　<strong>澎湃</strong>（péng pài）　<strong>凛冽</strong>（lǐn liè）",
     "<strong>娴熟</strong>（xián）　<strong>震耳欲聋</strong>　<strong>镌刻</strong>（juān）　<strong>惊心动魄</strong>（pò）",
     "<strong>篡改</strong>（cuàn）　<strong>抵赖</strong>　<strong>铭记</strong>（míng）　<strong>缅怀</strong>（miǎn）",
   ],("warn","✍","八年级字词更强调<strong>词语运用</strong>。注意「悄然」读 qiǎo 不读 qiāo；「锐不可当」的「当」读 dāng；「屏息」读 bǐng。"))+
   KP("2. 八下重点字音字形",2,[
     "<strong>怂恿</strong>（sǒng yǒng）　<strong>踊跃</strong>（yǒng yuè）　<strong>斡旋</strong>（wò xuán）　<strong>熙熙然</strong>",
     "<strong>怅惘</strong>（chàng wǎng）　<strong>亢奋</strong>（kàng）　<strong>羁绊</strong>（jī bàn）　<strong>蓦然</strong>（mò）",
     "<strong>踊跃</strong>　<strong>晦暗</strong>（huì）　<strong>冗杂</strong>（rǒng）　<strong>震撼</strong>（hàn）",
     "<strong>归省</strong>（xǐng）　<strong>行辈</strong>（háng）　<strong>撺掇</strong>（cuān duo）　<strong>凫水</strong>（fú）",
     "<strong>潺潺</strong>（chán）　<strong>弥散</strong>（mí）　<strong>蕴藻</strong>（yùn zǎo）　<strong>踊跃</strong>",
     "<strong>悄怆幽邃</strong>（qiǎo chuàng suì）　<strong>俶尔</strong>（chù）　<strong>翕忽</strong>（xī）",
     "<strong>溯洄</strong>（sù huí）　<strong>晞</strong>（xī）　<strong>跻</strong>（jī）　<strong>涘</strong>（sì）",
     "易错：「蓦然」不读 mù；「斡旋」的「斡」读 wò；「行辈」的「行」读 háng。",
   ],("tip","💡","八下文言字词密度大，务必<strong>逐课过关</strong>。建议按「通假字+古今异义+词类活用+一词多义」四类整理。")),
 },

  {"title":"二、古诗文默写与鉴赏","tag":"必考｜高频","body":
   KP("1. 八上古诗词（必背）",1,[
     "<em>《野望》王绩</em>：树树皆秋色，山山唯落晖。牧人驱犊返，猎马带禽归。",
     "<em>《黄鹤楼》崔颢</em>：日暮乡关何处是？烟波江上使人愁。",
     "<em>《使至塞上》王维</em>：大漠孤烟直，长河落日圆。",
     "<em>《渡荆门送别》李白</em>：山随平野尽，江入大荒流。月下飞天镜，云生结海楼。",
     "<em>《钱塘湖春行》白居易</em>：几处早莺争暖树，谁家新燕啄春泥。乱花渐欲迷人眼，浅草才能没马蹄。",
     "<em>《饮酒（其五）》陶渊明</em>：采菊东篱下，悠然见南山。山气日夕佳，飞鸟相与还。",
     "<em>《春望》杜甫</em>：感时花溅泪，恨别鸟惊心。烽火连三月，家书抵万金。",
     "<em>《雁门太守行》李贺</em>：黑云压城城欲摧，甲光向日金鳞开。报君黄金台上意，提携玉龙为君死。",
     "<em>《赤壁》杜牧</em>：东风不与周郎便，铜雀春深锁二乔。",
     "<em>《渔家傲》李清照</em>：九万里风鹏正举。风休住，蓬舟吹取三山去！",
   ],("key","★","<strong>《三峡》《答谢中书书》《记承天寺夜游》《与朱元思书》《富贵不能淫》《生于忧患，死于安乐》</strong>为八上文言必背篇目。"))+
   KP("2. 八下古诗词（必背）",2,[
     "<em>《关雎》</em>：关关雎鸠，在河之洲。窈窕淑女，君子好逑。",
     "<em>《蒹葭》</em>：蒹葭苍苍，白露为霜。所谓伊人，在水一方。",
     "<em>《送杜少府之任蜀州》王勃</em>：海内存知己，天涯若比邻。",
     "<em>《茅屋为秋风所破歌》杜甫</em>：安得广厦千万间，大庇天下寒士俱欢颜！",
     "<em>《卖炭翁》白居易</em>：可怜身上衣正单，心忧炭贱愿天寒。",
     "<em>《题破山寺后禅院》常建</em>：曲径通幽处，禅房花木深。山光悦鸟性，潭影空人心。",
     "<em>《卜算子·黄州定慧院寓居作》苏轼</em>：拣尽寒枝不肯栖，寂寞沙洲冷。",
     "<em>《卜算子·咏梅》陆游</em>：零落成泥碾作尘，只有香如故。",
   ],("tip","💡","名句默写按<strong>「理解性默写」</strong>考核为主——会给情境，要求填写对应诗句。务必理解句意，不能死记顺序。"))+
   KP("3. 文言文核心篇目考点",3,[
     "<strong>《桃花源记》</strong>：古今异义——「妻子」古指妻子和儿女；「无论」古指不要说，更不必说。「阡陌交通」中「交通」古指交错相通。",
     "<strong>《小石潭记》</strong>：移步换景的写法；「凄神寒骨，悄怆幽邃」借景抒情，抒发被贬的孤寂悲凉。",
     "<strong>《核舟记》</strong>：空间顺序（船舱→船头→船尾→船背）；「奇巧人」「因势象形」。",
     "<strong>《虽有嘉肴》</strong>：中心论点「教学相长」；「是故学然后知不足，教然后知困」。",
     "<strong>《大道之行也》</strong>：大同社会的基本特征——「天下为公，选贤与能，讲信修睦」。",
     "<strong>《马说》</strong>：托物寓意，以千里马喻人才，以食马者喻不识人才的统治者。",
     "<strong>《陋室铭》</strong>：主旨句「斯是陋室，惟吾德馨」；类比开头「山不在高，有仙则名」。",
   ],("warn","⚠","文言文阅读必考<strong>「翻译题」</strong>。评分点=关键实词+句式+句意通顺，缺一扣分。")),
 },

  {"title":"三、现代文阅读","tag":"重头戏｜44分","body":
   KP("1. 记叙文阅读四大题型",1,[
     "<strong>①概括题</strong>：公式＝谁 + 在什么情况下 + 做了什么 + 结果如何。注意限定字数时先提炼关键词。",
     "<strong>②赏析题</strong>：修辞角度＝「运用了××修辞，把××比作××（或赋予××人格），生动形象地写出了××的××特点，表达了作者××的情感」。",
     "<strong>③含义题</strong>：表层义（字面意思）+ 深层义（情感主旨/象征意义），必须结合上下文与文章主旨。",
     "<strong>④作用题</strong>：开头（开篇点题/总领全文/设置悬念/奠定情感基调）；中间（承上启下/为后文作铺垫）；结尾（总结全文/深化主旨/首尾呼应/戛然而止引人深思）。",
   ],("key","★","答题必须<strong>「分点作答 + 结合原文」</strong>。只写术语不结合原文，得分通常不超过一半。"))+
   KP("2. 说明文阅读",2,[
     "<strong>说明对象与特征</strong>：从标题、首段、中心句入手找。",
     "<strong>说明方法及作用</strong>：举例子（具体真切）、列数字（准确具体）、作比较（突出强调）、打比方（生动形象）、分类别（条理清晰）、下定义（准确严密）、摹状貌（形象直观）。",
     "答题格式：<strong>运用了××的说明方法，××地说明了××（对象）的××特征</strong>。",
     "<strong>说明顺序</strong>：时间顺序、空间顺序、逻辑顺序（由主到次、由现象到本质、由概括到具体）。",
     "<strong>语言准确性</strong>：「大约」「可能」「左右」「基本」等词能否删去——不能，体现了说明文语言的准确性、严密性。",
   ],("tip","💡","八上《中国石拱桥》《苏州园林》《蝉》《梦回繁华》均为说明文经典篇目，重点练习<strong>说明方法辨析</strong>。"))+
   KP("3. 议论文阅读（八下重点）",3,[
     "<strong>找中心论点</strong>：看标题、开头、结尾，注意「我认为」「可见」「总之」等标志词。",
     "<strong>论证方法及作用</strong>：举例论证（具体有力）、道理论证（权威有力）、对比论证（突出强调）、比喻论证（生动形象）。",
     "答题格式：<strong>运用了××论证方法，××地论证了××观点，使论证更××</strong>。",
     "<strong>论证思路</strong>：首先提出××观点 → 接着用××论证 → 最后得出××结论。",
   ],("key","★","八下《最后一次讲演》《应有格物致知精神》《我一生中的重要抉择》《庆祝奥林匹克运动复兴25周年》为演讲词单元，重点考<strong>观点与材料的关系</strong>。")),
 },

  {"title":"四、写作（50分）","tag":"分值最高","body":
   KP("1. 八年级作文命题趋势",1,[
     "<strong>命题形式</strong>：命题作文、半命题作文、材料作文、话题作文。",
     "<strong>常见主题</strong>：成长感悟、亲情友情、责任担当、科技与人文、传统文化、家国情怀。",
     "<strong>文体要求</strong>：以记叙文为主，鼓励写真情实感的身边事；八下开始接触简单的议论文。",
   ],("key","★","八年级作文评分看<strong>「内容（20分）+ 语言（20分）+ 结构（10分）」</strong>。内容分占比最高，切忌空洞说教。"))+
   KP("2. 高分技巧",2,[
     "<strong>拟题</strong>：新颖、有文采、能点明主旨。可用修辞（比喻/引用/对比）。",
     "<strong>开头</strong>：开门见山、环境渲染、倒叙设悬、引用名言，控制在 100 字以内。",
     "<strong>选材</strong>：<strong>以小见大</strong>，一个细节胜过十句抒情。写「妈妈的爱」不如写「妈妈把鱼肚上的肉夹给我，自己啃鱼头」这一细节。",
     "<strong>结构</strong>：一线串珠、片段组合（小标题式）、欲扬先抑、对比映衬。",
     "<strong>语言</strong>：多用修辞与描写（动作、神态、心理），适当引用诗句、运用长短句结合。",
     "<strong>结尾</strong>：回扣题目、升华主旨，忌画蛇添足。",
   ],("tip","💡","考场作文时间分配建议：<strong>审题 5 分钟 → 列提纲 5 分钟 → 写作 35 分钟 → 检查 5 分钟</strong>。字数要求 600 字以上，写到 700 字左右最佳。")),
 },
 ],
 "八年级语文重在「文言积累 + 阅读方法 + 真情写作」，八上是文言与说明文的爆发期，需提前规划背诵进度。",
 "八年级_语文_知识点考点.html")


# =========================================================
#                        八年级数学
# =========================================================
render("八年级", "数学",
 ["人教版", "八上 + 八下", "2024秋新修订"],
 [
  {"title":"一、八上·三角形与全等","tag":"几何核心","body":
   KP("1. 三角形",1,[
     "<strong>三边关系</strong>：任意两边之和大于第三边，任意两边之差小于第三边。",
     "<strong>内角和定理</strong>：三角形内角和为 180°；外角等于与它不相邻的两个内角之和。",
     "<strong>重要线段</strong>：高、中线、角平分线。中线把三角形分成面积相等的两部分。",
     "<strong>多边形</strong>：n 边形内角和 = (n−2)×180°；任意多边形外角和 = 360°。",
   ],("key","★","求「等腰三角形周长」必须<strong>分类讨论</strong>：已知两边为 a、b，要分别讨论 a 为腰和 b 为腰，并检验是否满足三边关系。"))+
   KP("2. 全等三角形",2,[
     "<strong>判定方法</strong>：SSS、SAS、ASA、AAS、HL（直角三角形专用）。",
     "<strong>注意</strong>：<strong>SSA 不能判定全等</strong>；AAA 只能判定相似，不能判定全等。",
     "<strong>性质</strong>：全等三角形的对应边相等、对应角相等、周长相等、面积相等。",
     "<strong>角平分线性质</strong>：角平分线上的点到角两边的距离相等；反之，到角两边距离相等的点在角平分线上。",
     "<strong>垂直平分线性质</strong>：线段垂直平分线上的点到线段两端点的距离相等。",
   ],("warn","⚠","证明题书写要求：必须写「在△×××和△×××中」，按 SSS/SAS/ASA/AAS 顺序列出条件，最后注明依据。书写不规范是八年级几何失分主因。"))+
   KP("3. 轴对称",3,[
     "<strong>轴对称图形</strong>：沿一条直线折叠，直线两旁部分能完全重合。",
     "<strong>坐标变换</strong>：点 (x, y) 关于 x 轴对称 → (x, −y)；关于 y 轴对称 → (−x, y)；关于原点对称 → (−x, −y)。",
     "<strong>等腰三角形</strong>：等边对等角；三线合一（顶角平分线、底边中线、底边高互相重合）。",
     "<strong>等边三角形</strong>：三边相等，三角均为 60°；有一个角是 60° 的等腰三角形是等边三角形。",
     "<strong>含 30° 角的直角三角形</strong>：30° 角所对的直角边等于斜边的一半。",
   ],("tip","💡","「三线合一」是八年级几何的<strong>超级工具</strong>：只要出现等腰三角形 + 一条线，就能推出另外两条性质。")),
 },

  {"title":"二、八上·整式乘法与因式分解","tag":"代数核心","body":
   KP("1. 幂的运算",1,[
     "<strong>同底数幂相乘</strong>：aᵐ · aⁿ = aᵐ⁺ⁿ",
     "<strong>幂的乘方</strong>：(aᵐ)ⁿ = aᵐⁿ",
     "<strong>积的乘方</strong>：(ab)ⁿ = aⁿbⁿ",
     "<strong>同底数幂相除</strong>：aᵐ ÷ aⁿ = aᵐ⁻ⁿ（a≠0）",
     "<strong>零指数幂</strong>：a⁰ = 1（a≠0）；<strong>负整数指数幂</strong>：a⁻ⁿ = 1/aⁿ（a≠0）",
   ],("tip","💡","易混：「aᵐ · aⁿ」是<strong>指数相加</strong>（乘法变加法），「(aᵐ)ⁿ」是<strong>指数相乘</strong>。做题前先圈出符号。"))+
   KP("2. 乘法公式与因式分解",2,[
     "<strong>平方差公式</strong>：(a+b)(a−b) = a² − b²",
     "<strong>完全平方公式</strong>：(a±b)² = a² ± 2ab + b²",
     "<strong>因式分解三法</strong>：①提公因式；②公式法（平方差、完全平方）；③十字相乘法（拓展）。",
     "因式分解<strong>必须分解到不能再分解为止</strong>，且结果必须是<strong>乘积形式</strong>。",
     "<strong>常用变形</strong>：a² + b² = (a+b)² − 2ab = (a−b)² + 2ab。",
   ],("warn","⚠","「完全平方公式」中间项常漏掉 2 或漏符号：(a+b)² = a² + <strong>2</strong>ab + b²，不是 a² + ab + b²。这是八年级代数第一大坑。")),
 },

  {"title":"三、八上·分式与二次根式（八下）","tag":"代数核心","body":
   KP("1. 分式",1,[
     "<strong>基本性质</strong>：分子分母同乘（除）以同一个不为零的整式，分式的值不变。",
     "<strong>运算顺序</strong>：先乘除后加减，有括号先算括号；除以一个分式等于乘以它的倒数。",
     "<strong>分式方程</strong>：去分母（两边同乘最简公分母）→ 解整式方程 → <strong>必须检验</strong>（验根）。",
     "<strong>增根</strong>：使最简公分母为零的根，必须舍去。",
   ],("key","★","分式方程<strong>不检验必扣分</strong>。解分式方程的应用题还要注意「符合实际意义」。"))+
   KP("2. 二次根式",2,[
     "<strong>性质</strong>：√a ≥ 0（a≥0）；(√a)² = a；√(a²) = |a|。",
     "<strong>乘除法则</strong>：√a · √b = √(ab)；√a ÷ √b = √(a/b)（a≥0, b>0）。",
     "<strong>化简</strong>：把根号内的完全平方因数移到根号外，如 √8 = 2√2。",
     "<strong>最简二次根式</strong>：被开方数不含分母，不含能开得尽方的因数。",
     "<strong>合并</strong>：只有<strong>同类二次根式</strong>（化简后被开方数相同）才能合并。",
   ],("tip","💡","√(a²) = |a| 而不是 a。当 a 的正负未知时，必须<strong>讨论</strong>结果，这是高频失分点。")),
 },

  {"title":"四、八下·勾股定理与四边形","tag":"几何核心","body":
   KP("1. 勾股定理",1,[
     "<strong>勾股定理</strong>：直角三角形中 a² + b² = c²（c 为斜边）。",
     "<strong>逆定理</strong>：若三角形三边满足 a² + b² = c²，则它是直角三角形（c 为最长边）。",
     "<strong>常用勾股数</strong>：(3,4,5)、(5,12,13)、(6,8,10)、(8,15,17)、(7,24,25)。",
     "<strong>应用</strong>：求斜边、求直角边、判断直角三角形、实际问题（梯子、航海、折叠）。",
   ],("warn","⚠","应用勾股定理必须先<strong>确认哪条边是斜边</strong>。题目没说直角在哪时，要分类讨论（最长边为斜边）。"))+
   KP("2. 平行四边形与特殊四边形",2,[
     "<strong>平行四边形</strong>：两组对边分别平行（定义）。性质-对边相等、对角相等、对角线互相平分。",
     "<strong>判定</strong>：①两组对边分别平行；②两组对边分别相等；③一组对边平行且相等；④对角线互相平分；⑤两组对角分别相等。",
     "<strong>矩形</strong>：四个角都是直角，对角线相等。判定：有一个角是直角的平行四边形 / 对角线相等的平行四边形 / 三个角是直角的四边形。",
     "<strong>菱形</strong>：四条边相等，对角线互相垂直且每条对角线平分一组对角。面积 = 对角线乘积的一半。",
     "<strong>正方形</strong>：既是矩形又是菱形。",
   ],("key","★","特殊四边形判定是八年级<strong>压轴题常客</strong>。记忆口诀：<strong>「矩形看角、菱形看边、正方形全都要」</strong>。")),
 },

  {"title":"五、八下·一次函数与数据分析","tag":"代数核心","body":
   KP("1. 一次函数",1,[
     "<strong>解析式</strong>：y = kx + b（k ≠ 0）。当 b = 0 时是正比例函数。",
     "<strong>图象</strong>：一条直线。k > 0 时 y 随 x 增大而增大；k < 0 时 y 随 x 增大而减小。",
     "<strong>与坐标轴交点</strong>：与 y 轴交于 (0, b)；与 x 轴交于 (−b/k, 0)。",
     "<strong>待定系数法</strong>：设 y = kx + b，代入两点坐标，解方程组求 k、b。",
     "<strong>平移规律</strong>：上加下减（对 b），左加右减（对 x）。",
   ],("tip","💡","一次函数与方程、不等式的关系是中考热点：kx + b > 0 的解集就是直线在 x 轴<strong>上方</strong>部分对应的 x 范围。"))+
   KP("2. 数据的分析",2,[
     "<strong>平均数</strong>：算术平均数、加权平均数（权越大影响越大）。",
     "<strong>中位数</strong>：排序后中间的数（偶数个取中间两数平均）。",
     "<strong>众数</strong>：出现次数最多的数，可能不止一个。",
     "<strong>方差</strong>：s² = [(x₁−x̄)² + ... + (xₙ−x̄)²] ÷ n，<strong>方差越小数据越稳定</strong>。",
     "<strong>极差</strong>：最大值 − 最小值。",
   ],("key","★","平均数、中位数、众数都描述<strong>集中趋势</strong>；方差描述<strong>离散程度（波动大小）</strong>。评价「谁的成绩更稳定」用方差。")),
 },
 ],
 "八年级数学是初中数学的「分水岭」：几何证明体系成型、函数思想登场。全等三角形与一次函数是全学年两大核心。",
 "八年级_数学_知识点考点.html")


# =========================================================
#                        八年级英语（仁爱版）
# =========================================================
render("八年级", "英语",
 ["仁爱版（科普版）", "八上 + 八下", "2024秋新教材"],
 [
  {"title":"一、核心语法体系","tag":"必考","body":
   KP("1. 时态系统（八上）",1,[
     "<strong>一般将来时</strong>：will + 动词原形 / be going to + 动词原形。表预测、计划。",
     "　　例：I <em>will</em> visit my grandma tomorrow. / She <em>is going to</em> be a teacher.",
     "<strong>过去进行时</strong>：was/were + 现在分词。表过去某时刻正在进行的动作。",
     "　　例：I <em>was doing</em> my homework at eight o'clock last night.",
     "<strong>一般过去时</strong>：与 yesterday, last week, in 2020, ago 等连用。",
     "<strong>现在完成时（重点）</strong>：have/has + 过去分词。表过去发生的动作对现在造成影响，或从过去持续到现在。",
     "　　标志词：already, yet, ever, never, just, since, for, so far, twice。",
   ],("tip","💡","<strong>since + 时间点</strong>（since 2020）与 <strong>for + 时间段</strong>（for three years）是现在完成时的经典考点，注意区分。"))+
   KP("2. 从句入门（八下核心）",2,[
     "<strong>宾语从句</strong>：三要素——①引导词（that / if / whether / 疑问词）；②语序（<strong>一律用陈述语序</strong>）；③时态（主句过去时，从句用相应过去时）。",
     "　　例：He asked me <em>where I lived</em>.（不能说 where did I live）",
     "<strong>状语从句</strong>：时间（when, while, as, before, after, until, as soon as）；条件（if, unless）；原因（because, since, as）；结果（so...that）；目的（so that）。",
     "<strong>重点</strong>：if 引导条件状语从句时，主句用将来时，从句用<strong>一般现在时</strong>表将来（主将从现）。",
     "　　例：If it <em>rains</em> tomorrow, we <em>will stay</em> at home.",
     "<strong>不定式</strong>：作宾语（want to do）、作宾语补足语（ask sb. to do）、作目的状语（to do）。",
   ],("warn","⚠","宾语从句的<strong>语序</strong>是最大失分点。无论主句是不是疑问句，从句一律用陈述语序。"))+
   KP("3. 其他重点语法",3,[
     "<strong>比较级与最高级</strong>：单音节加 -er/-est；多音节加 more/most。特殊变化：good-better-best；bad-worse-worst；many/much-more-most。",
     "<strong>同级比较</strong>：as + 原级 + as；not as/so + 原级 + as。",
     "<strong>比较级特殊句式</strong>：The more you read, the more you learn.（越……越……）",
     "<strong>被动语态（八下）</strong>：be + 过去分词。一般现在时被动：is/are done；一般过去时被动：was/were done。",
     "<strong>情态动词</strong>：can/could（能力、许可）、must（必须）、should（应该）、may（可能、许可）、need（需要）。",
   ],("key","★","仁爱版八下开始系统学习<strong>被动语态</strong>，是中考重点。记住口诀：<strong>「be + 过去分词，动作承受者作主语」</strong>。")),
 },

  {"title":"二、高频词汇与短语","tag":"积累","body":
   KP("1. 八上核心短语",1,[
     "be going to　计划做　　look forward to　盼望　　be afraid of　害怕",
     "take part in　参加　　be interested in　对……感兴趣　　be good at　擅长",
     "get on well with　与……相处融洽　　help sb. with sth.　帮助某人做某事",
     "make friends with　与……交朋友　　be sorry for　为……感到抱歉",
     "give up　放弃　　take care of　照顾　　in the future　在未来",
     "as soon as possible　尽快　　be different from　与……不同",
   ],("tip","💡","短语记忆要<strong>连例句一起记</strong>。孤立的短语容易混淆，放到句子里才能掌握搭配。"))+
   KP("2. 八下核心短语",2,[
     "depend on　依靠、取决于　　be proud of　为……骄傲　　be full of　充满",
     "take up　占据、开始从事　　come true　实现　　work out　解决、算出",
     "get rid of　摆脱　　be used to　习惯于　　in order to　为了",
     "as a result　结果　　pay attention to　注意　　make a difference　有影响",
     "thousands of　成千上万　　at least　至少　　be worth doing　值得做",
   ],("key","★","注意 <strong>be used to doing</strong>（习惯于）vs <strong>used to do</strong>（过去常常）vs <strong>be used to do</strong>（被用来做）——三大易混结构。")),
 },

  {"title":"三、写作与题型攻略","tag":"应试","body":
   KP("1. 书面表达（15分）",1,[
     "<strong>常见体裁</strong>：书信、通知、日记、演讲稿、介绍类短文、看图作文。",
     "<strong>三段式结构</strong>：①开头点题（I'm glad to.../ Let me tell you about...）；②主体展开（First... Second... Besides...）；③结尾总结（I hope... / In a word...）。",
     "<strong>加分点</strong>：正确使用连接词（however, moreover, as a result）、复合句（宾语从句、状语从句）、高级词汇。",
     "<strong>避坑</strong>：确保时态一致、主谓一致、单复数正确；不要出现中式英语。",
   ],("warn","⚠","书面表达先保证<strong>「无语法错误 + 要点齐全」</strong>，再追求高级表达。写错的高级句比简单的正确句得分更低。"))+
   KP("2. 各题型策略",2,[
     "<strong>听力</strong>：预读题干划关键词，抓数字、时间、地点、人物关系。",
     "<strong>单项选择</strong>：看语境定语法；排除法优先排除明显错误的选项。",
     "<strong>完形填空</strong>：先通读全文抓大意，再逐空选择；注意上下文的逻辑关联词与固定搭配。",
     "<strong>阅读理解</strong>：细节题回原文定位；主旨题看首尾段；猜词题根据上下文与构词法推断。",
     "<strong>任务型阅读</strong>：注意字数限制、时态一致、人称转换。",
   ],("tip","💡","仁爱版考试<strong>词汇与句型转换</strong>占比高。平时多训练「同义句转换」「按要求改写句子」这类题型。")),
 },
 ],
 "八年级英语是初中语法体系的成型期（时态 + 从句 + 被动语态）。仁爱版重视交际功能与话题词汇，需大量朗读与背诵积累语感。",
 "八年级_英语_知识点考点.html")

print("八年级 语文/数学/英语 知识点 HTML 已生成")
