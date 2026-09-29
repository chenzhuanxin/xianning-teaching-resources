# -*- coding: utf-8 -*-
"""高二 语文 / 数学 / 英语 知识点考点 HTML"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kp_engine import render, KP, SEC

# ==================== 高二语文 ====================
S = []

S.append(SEC("现代文阅读进阶", [
    KP("信息类文本阅读（多文本）", "1", [
        "新高考信息类文本常考<strong>多文本组合</strong>（2~3 则材料），需先分别概括每则材料的核心观点，再比较异同。",
        "常见设问：<em>①下列对材料相关内容的理解和分析，不正确的一项是；②根据材料内容，下列说法不正确的一项是；③请根据材料，概括……的原因（措施、意义）</em>。",
        "概括题答题方法：<strong>定位区间 → 划分层次 → 提取关键词 → 组织成句</strong>。切忌整段抄录，要提炼。",
        "「观点与材料的关系」是新高考热点：需判断材料是为哪个观点服务的，或哪则材料能支撑某观点。",
        "图表类材料题：<em>先看标题、图例、坐标轴，再横向纵向比较数据变化趋势，最后得出结论</em>。",
    ], ("key", "🔑", "多文本阅读的核心技巧：<strong>先读题目再看材料</strong>。题目会告诉你需要什么信息，带着问题去读，效率成倍提升，也避免被无关信息干扰。")),
    KP("文学类文本深度鉴赏", "2", [
        "叙述艺术三要素：<strong>叙述视角、叙述人称、叙述顺序</strong>。<em>视角分全知视角和有限视角；人称分第一、二、三人称；顺序分顺叙、倒叙、插叙、补叙、平叙</em>。",
        "叙述视角的作用：<em>第一人称→真实亲切、便于抒情；第二人称→拉近距离、增强感染力；第三人称→客观全面、自由灵活</em>。",
        "「叙述视角转换」是新高考热点，常考查儿童视角、女性视角、动物视角等特殊视角的表达效果。",
        "文本特征（文体特征）分析：<e>散文化小说、诗化小说、历史小说、科幻小说</e>等各有独特特征。",
        "探究题答题：<strong>观点明确 + 文本依据 + 逻辑分析</strong>，允许个性化解读但要言之有据。",
    ], ("tip", "💡", "新高考文学类文本越来越重视<strong>「叙述艺术」</strong>而非传统的情节人物分析。遇到「本文的叙述有什么特点」这类题，优先从视角、人称、顺序、节奏四个方向切入。")),
], tag="必考 · 现代文"))

S.append(SEC("文言文深度阅读", [
    KP("文言实词与虚词进阶", "1", [
        "高频实词补充：<strong>除、辞、从、殆、当、道、得、度、非、复、负、盖、故、顾、固、归、国、过、何、恨、胡、患、或、疾、及、即、既、假、间、见、解、就、举、绝、堪、克、类、怜、弥、莫、乃、内、期、奇、迁、请、穷、求、去、劝、却、如、若、善、少、涉、胜、识、使、是、适、书、孰、属、数、率、说、私、素、汤、涕、徒、亡、王、望、恶、微、悉、相、谢、信、兴、行、幸、修、徐、许、阳、要、宜、遗、贻、易、阴、右、再、造、知、致、质、治、诸、贼、族、卒、走、左、坐</strong>等。",
        "偏义复词：<em>「作息」（偏「作」）、「异同」（偏「异」）、「得失」（偏「失」）、「缓急」（偏「急」）</em>。",
        "虚词「以」的用法：<strong>①介词（用、凭借、因为、按照）；②连词（因为、以便、来）；③动词（认为）</strong>。",
        "虚词「于」的用法：<em>①介词（在、到、从、向、对于、比、被）</em>。",
    ], ("warn", "⚠️", "虚词辨析的黄金法则是<strong>「代入法」</strong>：把每个义项代回原句，看哪个读得通、合逻辑。不要死记义项列表，要在语境中判断。")),
    KP("文言文综合题型", "2", [
        "断句题：<em>①找名词代词定主宾；②找动词定谓语；③看虚词定位置（「夫」「盖」常居句首，「也」「矣」「焉」「耳」常居句尾）；④看句式（对称、排比）</em>。",
        "文化常识题：重点积累<em>科举制度（童生、秀才、举人、贡士、进士；乡试、会试、殿试）、官职变动（迁、谪、贬、擢、拜、除、出、入）、称谓（庙号、谥号、年号、字号）、礼仪（稽首、顿首、再拜）</em>。",
        "概括分析题：<strong>「事件 + 人物 + 结果」</strong>三要素核对，选项常在人名、时间、事件因果上设错。",
        "主观概括题（新高考新增）：<em>要求概括人物品质、事情原因、为政措施等，需回归原文分点作答</em>。",
    ], ("key", "🔑", "文化常识题的正确率取决于<strong>平时的分类积累</strong>。建议按「科举、官职、称谓、礼仪、历法、音乐、刑罚」七大板块建立笔记，每类整理 10~15 个高频词。")),
], tag="必考 · 文言文"))

S.append(SEC("古代诗歌鉴赏进阶", [
    KP("诗歌鉴赏九大题型", "1", [
        "<strong>形象题</strong>：概括人物形象 / 景物形象 / 事物形象。答题：<em>「特征词 + 具体诗句分析 + 情感」</em>。",
        "<strong>语言题</strong>：炼字、炼句、语言风格。<em>炼字答题：解释字义 → 描绘景象 → 指出效果 → 表达情感</em>。",
        "<strong>表达技巧题</strong>：<em>指出手法 → 结合诗句分析 → 说明效果</em>。",
        "<strong>思想感情题</strong>：<em>「通过……的描写，表达了……的情感」</em>。",
        "<strong>形象比较题</strong>：先分别概括，再指出异同。",
        "<strong>情景关系题</strong>：借景抒情、寓情于景、情景交融、以景结情。",
    ], ("tip", "💡", "诗歌鉴赏的通用答题公式：<strong>「手法 + 内容 + 效果 + 情感」</strong>四要素。无论题目怎么问，都按这四步组织答案，能确保不遗漏得分点。")),
    KP("必背篇目（选择性必修）", "2", [
        "《论语》十二章——<strong>「朝闻道，夕死可矣」「君子喻于义，小人喻于利」</strong>。",
        "《大学之道》——<strong>「大学之道，在明明德，在亲民，在止于至善」</strong>。",
        "《老子》四章——<strong>「合抱之木，生于毫末；九层之台，起于累土」</strong>。",
        "《离骚》（节选）——<strong>「长太息以掩涕兮，哀民生之多艰」</strong>。",
        "《蜀道难》李白——<strong>「蜀道之难，难于上青天」</strong>。",
        "《锦瑟》李商隐——<strong>「此情可待成追忆，只是当时已惘然」</strong>。",
        "《春江花月夜》张若虚——<strong>「春江潮水连海平，海上明月共潮生」</strong>。",
        "《燕歌行》高适——<strong>「战士军前半死生，美人帐下犹歌舞」</strong>。",
        "《客至》杜甫——<strong>「花径不曾缘客扫，蓬门今始为君开」</strong>。",
    ], ("key", "🔑", "名著阅读已成必考：《<strong>红楼梦</strong>》《<strong>乡土中国</strong>》是高中必读书目。《红楼梦》重点把握人物关系与性格；《乡土中国》重点理解「差序格局」「礼治秩序」「无讼」等核心概念。")),
], tag="必考 · 诗歌"))

S.append(SEC("写作进阶", [
    KP("高考作文评分标准与提分策略", "1", [
        "<strong>基础等级（40分）</strong>：符合题意、符合文体要求、感情真挚、思想健康、内容充实、中心明确、语言通顺、结构完整、标点正确、书写规范。",
        "<strong>发展等级（20分）</strong>：<em>深刻、丰富、有文采、有创意</em>。",
        "<strong>「深刻」的体现</strong>：①透过现象深入本质；②揭示事物内在的因果关系；③观点具有启发性。",
        "<strong>「丰富」的体现</strong>：①材料丰富；②论据充足；③形象丰满；④意境深远。",
        "<strong>「有文采」的体现</strong>：<em>用词贴切、句式灵活、善用修辞、文句有表现力</em>。",
    ], ("key", "🔑", "从 45 分到 55 分的关键是<strong>发展等级</strong>。最有效的三个抓手：①<strong>思维深度</strong>（用辩证观点分析问题）；②<strong>材料新颖</strong>（避免老掉牙的素材）；③<strong>语言表现力</strong>（善用排比、引用、比喻）。")),
    KP("思辨类作文写法", "2", [
        "思辨类作文是新高考主流，常给<strong>关系型话题</strong>：如「变与不变」「快与慢」「得与失」「内卷与躺平」「科技与人文」。",
        "核心写法：<em>既看到 A 的价值，也看到 B 的意义，最终揭示二者的辩证统一关系</em>。",
        "避免「和稀泥」：不要简单地说「两者都重要」，而要<strong>指出在什么条件下侧重哪一方</strong>。",
        "常用思辨框架：<em>①现象层（是什么）→ ②本质层（为什么）→ ③价值层（怎么办）→ ④升华层（时代意义）</em>。",
        "高级论证技巧：<strong>让步说理</strong>（承认对方合理处再转折）、<strong>归谬法</strong>（假设对方成立推出荒谬结论）。",
    ], ("tip", "💡", "思辨类作文的高分秘诀是<strong>「在张力中寻求平衡」</strong>。阅卷老师最欣赏的是能指出「看似矛盾的双方其实在更高层面统一」的考生。")),
], tag="必考 · 60分"))

render("高二", "语文",
       ["选择性必修上", "选择性必修中", "选择性必修下", "统编版", "高考导向"],
       S,
       "本资料依据《普通高中语文课程标准（2017年版2020年修订）》与统编版选择性必修教材编写 · 高二上下学期适用",
       "高二_语文_知识点考点.html")
print("✔ 高二语文")

# ==================== 高二数学 ====================
M = []

M.append(SEC("空间向量与立体几何", [
    KP("空间向量及其运算", "1", [
        "空间向量基本定理：<em>如果三个向量 a、b、c 不共面，那么对空间任一向量 p，存在唯一的有序实数组 (x,y,z)，使 p = xa + yb + zc</em>。",
        "坐标运算：<strong>a·b = x₁x₂ + y₁y₂ + z₁z₂</strong>；|a| = √(x²+y²+z²)。",
        "共线与垂直：<em>a∥b ⇔ a = λb；a⊥b ⇔ a·b = 0</em>。",
        "夹角公式：<strong>cos⟨a,b⟩ = (a·b)/(|a||b|)</strong>。",
    ], ("key", "🔑", "空间向量的价值在于<strong>把几何证明转化为代数计算</strong>。传统方法需要「作、证、算」三步，向量法只需建系、写坐标、算结果，大幅降低思维难度。")),
    KP("空间角与距离的向量求法", "2", [
        "<strong>异面直线所成角</strong>：cosθ = |cos⟨a,b⟩|（a、b 为两直线的方向向量），范围 <em>(0°, 90°]</em>。",
        "<strong>直线与平面所成角</strong>：sinθ = |cos⟨a,n⟩|（a 为直线方向向量，n 为平面法向量），范围 <em>[0°, 90°]</em>。",
        "<strong>二面角</strong>：cosθ = ±cos⟨n₁,n₂⟩（n₁、n₂ 为两平面法向量）。<em>需结合图形判断二面角是锐角还是钝角</em>。",
        "<strong>点到平面距离</strong>：<strong>d = |AP·n| / |n|</strong>（A 为平面内一点，P 为平面外一点，n 为平面法向量）。",
        "<strong>线面平行判定</strong>：a·n = 0（方向向量与法向量垂直）。<strong>面面平行</strong>：n₁∥n₂。",
    ], ("warn", "⚠️", "最容易错的是<strong>线面角用 sin 而非 cos</strong>——因为线面角与方向向量和法向量的夹角是<strong>互余</strong>关系。这一步错了整道题就废了，务必牢记。")),
], tag="选择性必修1 · 必考"))

M.append(SEC("直线与圆", [
    KP("直线方程与位置关系", "1", [
        "直线方程五种形式：<em>点斜式 y-y₀=k(x-x₀)、斜截式 y=kx+b、两点式、截距式、一般式 Ax+By+C=0</em>。",
        "斜率公式：<strong>k = (y₂-y₁)/(x₂-x₁) = tanα</strong>（α 为倾斜角，范围 [0,π)）。",
        "平行条件：<em>A₁B₂ - A₂B₁ = 0 且不重合</em>。垂直条件：<strong>A₁A₂ + B₁B₂ = 0</strong>。",
        "点到直线距离：<strong>d = |Ax₀+By₀+C| / √(A²+B²)</strong>。",
        "两平行线间距离：<em>d = |C₁-C₂| / √(A²+B²)</em>（需先化成相同系数）。",
    ]),
    KP("圆的方程与位置关系", "2", [
        "圆的标准方程：<strong>(x-a)² + (y-b)² = r²</strong>，圆心 (a,b)，半径 r。",
        "圆的一般方程：<em>x² + y² + Dx + Ey + F = 0（D²+E²-4F &gt; 0）</em>。",
        "直线与圆的位置关系：<em>d &gt; r 相离（0 个交点）；d = r 相切（1 个交点）；d &lt; r 相交（2 个交点）</em>。",
        "切线方程：过圆上一点 (x₀,y₀) 的切线，可用<strong>「圆心与切点连线垂直于切线」</strong>求解。",
        "弦长公式：<strong>l = 2√(r² - d²)</strong>（d 为圆心到直线的距离）。",
        "圆与圆的位置关系：<em>外离、外切、相交、内切、内含</em>，由圆心距与半径和差比较判断。",
    ], ("tip", "💡", "直线与圆的综合题，<strong>「几何法」往往比「代数法」快得多</strong>。优先考虑用圆心到直线的距离 d 与半径 r 的关系，避免联立方程的繁琐计算。")),
], tag="选择性必修1 · 必考"))

M.append(SEC("圆锥曲线", [
    KP("椭圆", "1", [
        "定义：<strong>|PF₁| + |PF₂| = 2a（2a &gt; |F₁F₂| = 2c）</strong>。",
        "标准方程：<em>x²/a² + y²/b² = 1（焦点在 x 轴）；y²/a² + x²/b² = 1（焦点在 y 轴）</em>。",
        "关系式：<strong>a² = b² + c²</strong>（a 最大）。",
        "离心率：<strong>e = c/a ∈ (0,1)</strong>。<em>e 越大，椭圆越扁；e 越小，越接近圆</em>。",
        "焦点三角形：<em>|PF₁|·|PF₂| 的最大值为 a²（当 P 在短轴端点时）</em>。",
    ], ("key", "🔑", "圆锥曲线三大定义的记忆要点：<strong>椭圆「和为定值」，双曲线「差为定值」，抛物线「等于到准线距离」</strong>。抓住定义就能解决大部分基础题。")),
    KP("双曲线", "2", [
        "定义：<strong>||PF₁| - |PF₂|| = 2a（0 &lt; 2a &lt; 2c）</strong>。",
        "标准方程：<em>x²/a² - y²/b² = 1；y²/a² - x²/b² = 1</em>。",
        "关系式：<strong>c² = a² + b²</strong>（c 最大，与椭圆不同！）。",
        "离心率：<strong>e = c/a &gt; 1</strong>。",
        "渐近线：<em>x²/a² - y²/b² = 1 的渐近线为 y = ±(b/a)x</em>。",
        "等轴双曲线：<em>a = b，渐近线为 y = ±x，离心率 e = √2</em>。",
    ], ("warn", "⚠️", "椭圆与双曲线的 a、b、c 关系<strong>恰好相反</strong>：椭圆 a²=b²+c²（a 最大）；双曲线 c²=a²+b²（c 最大）。这是最容易混淆的地方，务必区分记忆。")),
    KP("抛物线", "3", [
        "定义：<strong>|PF| = d（d 为 P 到准线的距离）</strong>。",
        "标准方程四种形式：<em>y² = 2px（开口向右）、y² = -2px（向左）、x² = 2py（向上）、x² = -2py（向下）</em>。",
        "焦点与准线（以 y²=2px 为例）：<strong>焦点 (p/2, 0)，准线 x = -p/2</strong>。",
        "焦半径（以 y²=2px 为例）：<em>|PF| = x₀ + p/2</em>。",
        "通径：<strong>过焦点且垂直于对称轴的弦，长度为 2p</strong>（抛物线所有焦点弦中最短的）。",
        "抛物线中「焦点弦」是高频考点，常用性质：<em>以焦点弦为直径的圆与准线相切</em>。",
    ]),
], tag="选择性必修1 · 高频"))

M.append(SEC("数列", [
    KP("等差数列", "1", [
        "定义：<strong>aₙ₊₁ - aₙ = d（常数）</strong>。",
        "通项公式：<em>aₙ = a₁ + (n-1)d</em>。",
        "前 n 项和：<strong>Sₙ = n(a₁+aₙ)/2 = na₁ + n(n-1)d/2</strong>。",
        "中项性质：<em>2aₙ = aₙ₋₁ + aₙ₊₁</em>。",
        "重要结论：<strong>Sₙ, S₂ₙ-Sₙ, S₃ₙ-S₂ₙ 仍成等差数列</strong>。",
        "判断方法：<em>定义法、中项法、通项公式法（aₙ = pn+q）、前n项和法（Sₙ = An²+Bn）</em>。",
    ], ("key", "🔑", "等差数列的<strong>「下标和相等则项和相等」</strong>：若 m+n = p+q，则 aₘ+aₙ = aₚ+a_q。这个性质能极大简化计算，是解题利器。")),
    KP("等比数列", "2", [
        "定义：<strong>aₙ₊₁/aₙ = q（q≠0 的常数）</strong>。",
        "通项公式：<em>aₙ = a₁q^(n-1)</em>。",
        "前 n 项和：<strong>q≠1 时 Sₙ = a₁(1-qⁿ)/(1-q)；q=1 时 Sₙ = na₁</strong>。",
        "中项性质：<em>aₙ² = aₙ₋₁·aₙ₊₁</em>。",
        "重要结论：<strong>Sₙ, S₂ₙ-Sₙ, S₃ₙ-S₂ₙ 仍成等比数列（q≠-1）</strong>。",
        "注意：等比数列求和<strong>必须讨论 q=1 与 q≠1</strong>两种情况。",
    ], ("warn", "⚠️", "等比数列求和的<strong>分类讨论</strong>是必考点，也是最常见的失分点。只要题目未明确 q≠1，就必须分两种情况讨论，否则答案不完整。")),
    KP("数列求和方法与递推", "3", [
        "<strong>公式法</strong>：直接用等差、等比求和公式。",
        "<strong>错位相减法</strong>：适用于<em>「等差×等比」型通项</em>，如 aₙ = n·2ⁿ。",
        "<strong>裂项相消法</strong>：适用于<em>1/[n(n+1)] 型</em>，注意「裂项后剩余项」的规律。",
        "<strong>分组求和法</strong>：适用于<em>通项可拆分为几部分分别求和</em>的情况。",
        "<strong>倒序相加法</strong>：适用于<em>满足 f(x) + f(1/x) = 常数</em>型。",
        "常见递推：<em>aₙ₊₁ = aₙ + f(n)（累加法）；aₙ₊₁ = aₙ·f(n)（累乘法）；aₙ₊₁ = paₙ + q（构造等比数列）</em>。",
    ], ("tip", "💡", "识别求和方法的关键是<strong>看通项的结构</strong>：看到「n 乘以指数」→ 错位相减；看到「分母是乘积」→ 裂项相消。通项决定方法。")),
], tag="选择性必修2 · 高频"))

M.append(SEC("导数及其应用", [
    KP("导数概念与运算", "1", [
        "导数定义：<strong>f&#39;(x₀) = lim(Δx→0) [f(x₀+Δx) - f(x₀)]/Δx</strong>。",
        "几何意义：<em>f&#39;(x₀) 是曲线 y=f(x) 在点 (x₀, f(x₀)) 处切线的斜率</em>。",
        "基本求导公式：<strong>(xⁿ)&#39; = nxⁿ⁻¹；(sinx)&#39; = cosx；(cosx)&#39; = -sinx；(eˣ)&#39; = eˣ；(aˣ)&#39; = aˣlna；(lnx)&#39; = 1/x；(logₐx)&#39; = 1/(xlna)</strong>。",
        "运算法则：<em>(u±v)&#39; = u&#39;±v&#39;；(uv)&#39; = u&#39;v + uv&#39;；(u/v)&#39; = (u&#39;v - uv&#39;)/v²；[f(g(x))]&#39; = f&#39;(g(x))·g&#39;(x)</em>。",
    ], ("key", "🔑", "导数的三大应用：<strong>①求切线方程；②判断单调性；③求极值与最值</strong>。这三类问题占据高考导数题 90% 以上的分值，务必熟练掌握。")),
    KP("导数与函数单调性、极值", "2", [
        "单调性判定：<strong>f&#39;(x) &gt; 0 ⇒ 递增；f&#39;(x) &lt; 0 ⇒ 递减</strong>。",
        "极值判定：<em>f&#39;(x₀) = 0 且 f&#39;(x) 在 x₀ 两侧变号，则 x₀ 为极值点</em>。",
        "注意：<strong>f&#39;(x₀) = 0 是极值点的必要不充分条件</strong>（如 y=x³ 在 x=0 处导数为 0 但非极值点）。",
        "求极值步骤：<em>求导 → 令 f&#39;(x)=0 求根 → 列表判断符号变化 → 确定极大（小）值</em>。",
        "含参单调性讨论：<strong>按参数分类讨论（开口方向、判别式、根的大小关系）</strong>。",
    ], ("warn", "⚠️", "「f&#39;(x₀)=0」<strong>不等于</strong>「x₀ 是极值点」。必须验证导数在该点两侧是否变号。这个陷阱每年都有考生掉进去。")),
    KP("导数与不等式、零点问题", "3", [
        "<strong>证明不等式 f(x) ≥ g(x)</strong>：构造 h(x) = f(x) - g(x)，证明 h(x) 的最小值 ≥ 0。",
        "<strong>恒成立问题</strong>：<em>f(x) ≥ a 恒成立 ⇔ f(x)_min ≥ a；f(x) ≥ a 有解 ⇔ f(x)_max ≥ a</em>。",
        "<strong>零点个数问题</strong>：转化为<em>函数图像与 x 轴交点个数</em>，或<em>两函数图像交点个数</em>。",
        "<strong>分离参数法</strong>：把参数分离到一侧，转化为求另一侧函数的最值。",
        "<strong>洛必达（超纲但实用）</strong>：处理 0/0 或 ∞/∞ 型极限，可快速求出，但正式答题须用高中方法书写。",
    ], ("tip", "💡", "导数压轴题的三大类型：<strong>①讨论单调性（基础）；②证明不等式（中档）；③零点或参数范围（压轴）</strong>。核心思想都是「构造辅助函数」，把问题转化为求最值。")),
], tag="选择性必修2 · 压轴"))

M.append(SEC("计数原理与概率统计", [
    KP("排列组合与二项式定理", "1", [
        "两个基本原理：<strong>分类加法计数原理；分步乘法计数原理</strong>。",
        "排列数：<em>A(n,m) = n!/(n-m)!</em>；组合数：<strong>C(n,m) = n!/[m!(n-m)!]</strong>。",
        "组合数性质：<em>C(n,m) = C(n,n-m)；C(n,m) = C(n-1,m-1) + C(n-1,m)</em>。",
        "二项式定理：<strong>(a+b)ⁿ = ΣC(n,k)a^(n-k)b^k</strong>。",
        "通项公式：<em>T(k+1) = C(n,k)a^(n-k)b^k（第 k+1 项）</em>。",
        "常用技巧：<strong>特殊元素优先、相邻问题捆绑、不相邻问题插空、定序问题除法</strong>。",
    ], ("key", "🔑", "排列组合的四种典型模型：<strong>①相邻捆绑（把相邻元素看作一个整体）；②不相邻插空（先排其他再插空）；③定序（除以定序元素的排列数）；④分组分配（注意是否均匀分组）</strong>。")),
    KP("随机变量及其分布", "2", [
        "<strong>离散型随机变量</strong>：取值可一一列举。分布列必须满足<em>①Pᵢ ≥ 0；②ΣPᵢ = 1</em>。",
        "期望：<strong>E(X) = Σxᵢpᵢ</strong>，反映随机变量的平均水平。",
        "方差：<em>D(X) = Σ(xᵢ-E(X))²pᵢ = E(X²) - [E(X)]²</em>，反映离散程度。",
        "<strong>二项分布 X~B(n,p)</strong>：<em>P(X=k) = C(n,k)p^k(1-p)^(n-k)；E(X) = np；D(X) = np(1-p)</em>。",
        "<strong>超几何分布</strong>：从 N 件产品（含 M 件次品）中取 n 件，次品数 X 服从超几何分布。",
        "<strong>正态分布 X~N(μ,σ²)</strong>：曲线关于 x=μ 对称；<em>P(μ-σ&lt;X≤μ+σ) ≈ 0.6827；P(μ-2σ&lt;X≤μ+2σ) ≈ 0.9545</em>。",
    ], ("tip", "💡", "区分二项分布与超几何分布：<strong>二项分布是「有放回」抽样</strong>（每次概率相同）；<strong>超几何分布是「无放回」抽样</strong>（概率随抽取改变）。题目里的「放回」「不放回」是关键提示词。")),
], tag="选择性必修3 · 必考"))

render("高二", "数学",
       ["选择性必修1", "选择性必修2", "选择性必修3", "人教A版", "高考核心"],
       M,
       "本资料依据《普通高中数学课程标准（2017年版2020年修订）》与人教A版选择性必修教材编写 · 高二上下学期适用",
       "高二_数学_知识点考点.html")
print("✔ 高二数学")

# ==================== 高二英语 ====================
E = []

E.append(SEC("语法专题：高级句式与特殊结构", [
    KP("独立主格与with复合结构", "1", [
        "<strong>独立主格结构</strong>：非谓语动词有自己的逻辑主语，且与主句主语不同。<em>Weather permitting, we will go out.（= If weather permits）</em>",
        "常见形式：<em>①名词/代词 + doing（主动、进行）；②名词/代词 + done（被动、完成）；③名词/代词 + to do（将来）；④名词/代词 + 形容词/副词/介词短语</em>。",
        "<strong>with 复合结构</strong>：<em>with + 宾语 + doing/done/to do/adj./adv./介词短语</em>。",
        "例句：<em>With the work finished, he went home.（工作完成后他回家了）</em>；<em>With so much work to do, he can&#39;t go out.（有这么多工作要做，他不能出去）</em>。",
    ], ("key", "🔑", "独立主格是<strong>高考写作的加分利器</strong>。掌握 3~5 个独立主格例句并灵活运用，能显著提升作文档次。例如：<em>Everything taken into consideration, I prefer the latter.</em>")),
    KP("倒装、强调与省略", "2", [
        "<strong>as/though 引导的让步状语从句倒装</strong>：<em>Child as he is, he knows a lot.（= Although he is a child）</em>。注意<strong>表语或状语提前，且名词前不用冠词</strong>。",
        "<strong>「so + adj. + be + 主语」</strong>：<em>So difficult was the task that we gave up.</em>",
        "<strong>「such + be + 主语」</strong>：<em>Such was his anger that he left.</em>",
        "<strong>强调句的特殊疑问形式</strong>：<em>Who was it that broke the window?</em>",
        "<strong>强调句的 not...until 结构</strong>：<em>It was not until midnight that he came back.</em>",
        "<strong>省略</strong>：<em>①状语从句中「主语 + be」可省（When (he was) asked, he said nothing）；②不定式的省略（to 后动词省略，保留 to）</em>。",
    ], ("tip", "💡", "「as 引导让步状语从句」的倒装是高频考点。<strong>公式：形容词/副词/名词（无冠词）+ as + 主语 + 谓语</strong>。例：<em>Hard as he tried, he failed.</em>")),
], tag="高级语法"))

E.append(SEC("读后续写专项突破", [
    KP("情节构思与冲突设计", "1", [
        "读后续写的核心是<strong>「情节合理 + 情感真挚 + 语言地道」</strong>。",
        "五步法：<em>①读原文（抓人物、情节、基调）；②析首句（明确写作方向）；③列提纲（关键情节节点）；④写初稿（注重细节描写）；⑤润色（检查时态、人称、语法）</em>。",
        "冲突设计：<em>人与人的冲突、人与自然的冲突、人与自我的冲突</em>。高潮通常在第二段中后部。",
        "结尾三选一：<strong>温情式（亲情友情升华）、成长式（人物获得感悟）、呼应式（与原文首尾呼应）</strong>。",
    ], ("key", "🔑", "读后续写最大的分水岭是<strong>「细节描写」</strong>。平庸的续写只有情节推进；高分的续写有动作、神态、心理、环境的细腻刻画。要学会「show, don&#39;t tell」。")),
    KP("高分描写素材库", "2", [
        "<strong>心理描写</strong>：<em>My heart pounded against my ribs.（心砰砰跳）；A surge of relief washed over me.（一阵宽慰涌上心头）；I felt a lump rise in my throat.（喉咙哽咽）</em>。",
        "<strong>动作描写</strong>：<em>He dashed to the door, his face pale with worry.（冲向门口，脸因担忧而苍白）；She clutched the letter with trembling hands.（用颤抖的手紧攥着信）</em>。",
        "<strong>环境烘托</strong>：<em>The sun broke through the clouds, casting a warm glow.（阳光破云而出，洒下温暖的光）；A cold wind howled, as if echoing my despair.（冷风呼啸，仿佛在回应我的绝望）</em>。",
        "<strong>对话描写</strong>：<em>「Don&#39;t worry,」 he murmured, patting my shoulder gently.</em>",
        "<strong>时间推进</strong>：<em>A few minutes later...；Before I knew it...；Hardly had I sat down when...</em>",
    ], ("tip", "💡", "建议建立<strong>「描写素材本」</strong>，按「心理、动作、环境、对话」四类各积累 20 个句子。考前反复朗读，写作时自然能调用。")),
], tag="新高考 · 25分"))

E.append(SEC("应用文写作提升", [
    KP("六大常考文体模板", "1", [
        "<strong>建议信</strong>：<em>I&#39;m writing to offer some suggestions on... First of all... In addition... Last but not least... I hope you will find these suggestions helpful.</em>",
        "<strong>邀请信</strong>：<em>I&#39;m writing to invite you to... The event will be held on... I would be honoured if you could come.</em>",
        "<strong>申请信</strong>：<em>I am writing to apply for... I believe I am qualified for... I would appreciate it if you could give me a chance.</em>",
        "<strong>感谢信</strong>：<em>I&#39;m writing to express my sincere gratitude for... Without your help, I couldn&#39;t have...</em>",
        "<strong>通知</strong>：<em>Attention please, everyone. This is to inform you that... Everyone is welcome to attend.</em>",
        "<strong>演讲稿</strong>：<em>Good morning, everyone! It is my great honour to stand here and talk about... Thank you for your listening.</em>",
    ], ("key", "🔑", "应用文的提分核心是<strong>「高级句型替换」</strong>：把 I think 换成 From my perspective；把 I want to 换成 I am eager to；把 important 换成 of vital significance。")),
    KP("高级句型储备", "2", [
        "<strong>非谓语动词作状语</strong>：<em>Faced with difficulties, we should...；Having finished the task, he...</em>。",
        "<strong>倒装句</strong>：<em>Not only does it benefit us, but it also...</em>。",
        "<strong>强调句</strong>：<em>It is through hard work that we can achieve our goals.</em>",
        "<strong>名词性从句</strong>：<em>What matters most is that...</em>；<em>It is widely acknowledged that...</em>。",
        "<strong>定语从句</strong>：<em>..., which plays an important role in our daily life.</em>",
        "<strong>虚拟语气</strong>：<em>Were I in your position, I would...</em>；<em>It is high time that we took action.</em>",
        "<strong>独立主格</strong>：<em>Everything taken into account, I believe...</em>",
    ], ("tip", "💡", "背句型比背单词更高效。建议掌握 <strong>20 个万能高级句型</strong>，写作时根据语境替换主谓宾即可，能在短时间内显著提升语言分。")),
], tag="必考 · 15分"))

render("高二", "英语",
       ["选择性必修一", "选择性必修二", "选择性必修三", "人教版", "读后续写"],
       E,
       "本资料依据《普通高中英语课程标准（2017年版2020年修订）》与人教版选择性必修教材编写 · 高二上下学期适用",
       "高二_英语_知识点考点.html")
print("✔ 高二英语")
