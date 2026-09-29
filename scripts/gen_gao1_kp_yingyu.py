# -*- coding: utf-8 -*-
"""高一 英语 知识点考点 HTML"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kp_engine import render, KP, SEC

S = []

S.append(SEC("语法专题一：时态与语态", [
    KP("十大时态系统梳理", "1", [
        "<strong>一般现在时</strong>：表示经常性动作、客观真理。标志词：<em>always, usually, often, every day</em>。",
        "<strong>一般过去时</strong>：过去发生的动作。标志词：<em>yesterday, last week, ago, in 2020</em>。",
        "<strong>一般将来时</strong>：will do / be going to do / be to do / be about to do。",
        "<strong>现在进行时</strong>：am/is/are doing，表示现在正在进行的动作。",
        "<strong>过去进行时</strong>：was/were doing，表示过去某时刻正在进行的动作。",
        "<strong>现在完成时</strong>：have/has done，表示过去动作对现在造成影响。标志词：<em>already, yet, just, ever, never, since, for</em>。",
        "<strong>过去完成时</strong>：had done，表示「过去的过去」。",
        "<strong>过去将来时</strong>：would do，常用于宾语从句。",
    ], ("key", "🔑", "现在完成时与一般过去时的区别是高频考点：<strong>现在完成时强调对现在的影响，不能与具体过去时间连用</strong>。错例：I have seen him yesterday.（✗）")),
    KP("被动语态", "2", [
        "基本结构：<strong>be + 过去分词</strong>，时态通过 be 的变化体现。",
        "各时态被动：<em>is done；was done；will be done；is being done；has been done；had been done</em>。",
        "情态动词被动：<strong>can/must/should + be + done</strong>。",
        "特殊结构：<em>It is said that...；He is said to have done...</em>。",
        "不用被动的动词：<em>happen, occur, take place, break out, belong to, consist of</em>（这些是不及物动词或短语，无被动）。",
    ]),
], tag="核心 · 必考"))

S.append(SEC("语法专题二：非谓语动词", [
    KP("三种非谓语形式", "1", [
        "<strong>不定式 to do</strong>：表将来、目的、一次性动作。<em>I want to go.</em>",
        "<strong>动名词 doing</strong>：表习惯性、抽象、已发生动作。<em>I enjoy reading.</em>",
        "<strong>现在分词 doing</strong>：主动、进行。<em>The boy standing there is Tom.</em>",
        "<strong>过去分词 done</strong>：被动、完成。<em>The book written by him is popular.</em>",
        "关键判断：<em>①是否作主语/宾语（用 doing 或 to do）；②是否作定语/状语（看主动被动关系）</em>。",
    ], ("warn", "⚠️", "非谓语动词是高考英语<strong>最难也最容易失分</strong>的语法点。核心判断顺序：①句子是否已有谓语；②非谓语与逻辑主语是主动还是被动；③动作是发生在谓语前、同时还是之后。")),
    KP("非谓语高频搭配", "2", [
        "只接 doing 的动词：<strong>enjoy, mind, avoid, finish, suggest, practise, consider, imagine, admit, deny, keep</strong>。",
        "只接 to do 的动词：<strong>want, hope, wish, expect, decide, plan, agree, refuse, manage, offer, pretend</strong>。",
        "接 doing 与 to do 意义不同的动词：<em>remember/forget/regret（do 表示已做，to do 表示未做）；stop/go on/try/mean（意义不同）</em>。",
        "常见结构：<em>be used to doing（习惯于）/ used to do（过去常常）/ be used to do（被用来做）</em>。",
        "独立主格：<em>Weather permitting, we will go out.（天气允许的话）</em>。",
    ]),
], tag="难点 · 高频"))

S.append(SEC("语法专题三：三大从句", [
    KP("定语从句", "1", [
        "<strong>关系代词</strong>：who（指人作主语/宾语）、whom（指人作宾语）、whose（表所属）、which（指物）、that（指人/物）。",
        "<strong>关系副词</strong>：when（时间）、where（地点）、why（原因）。",
        "判断步骤：<em>①找先行词；②看先行词在从句中充当什么成分；③成分完整用关系副词，不完整用关系代词</em>。",
        "只用 that 的情况：<strong>先行词为 all, everything, nothing, little, much 等不定代词；先行词被 the only, the very, the same、序数词或形容词最高级修饰；先行词既有人又有物</strong>。",
        "非限制性定语从句：<em>用逗号隔开，不能用 that，不能用 why</em>。",
    ], ("key", "🔑", "定语从句解题口诀：<strong>「先找先行词，再看从句缺什么」</strong>。缺主语或宾语→关系代词；主语宾语都齐→关系副词。这是唯一可靠的判断方法。")),
    KP("名词性从句", "2", [
        "四类：<strong>主语从句、宾语从句、表语从句、同位语从句</strong>。",
        "连接词三类：<em>①that（无意义，不作成分）；②whether/if（是否）；③特殊疑问词 what, who, which, when, where, why, how（有意义，作成分）</em>。",
        "关键区分：<strong>that 在名词性从句中不作任何成分，只起连接作用；what 在从句中作主语、宾语或表语</strong>。",
        "it 作形式主语：<em>It is important that...；It doesn&#39;t matter whether...</em>。",
        "同位语从句与定语从句区分：<strong>同位语从句解释说明前面的名词内容（that 不作成分）；定语从句修饰前面的名词（that/which 作成分）</strong>。",
    ]),
    KP("状语从句", "3", [
        "<strong>时间</strong>：when, while, as, before, after, until, since, as soon as, the moment。",
        "<strong>地点</strong>：where, wherever。",
        "<strong>原因</strong>：because, since, as, now that, in that。",
        "<strong>结果</strong>：so...that, such...that。",
        "<strong>目的</strong>：so that, in order that。",
        "<strong>条件</strong>：if, unless, as long as, in case。",
        "<strong>让步</strong>：although, though, even if, even though, while, no matter how。",
        "<strong>比较</strong>：than, as...as。",
        "主将从现原则：<em>在时间和条件状语从句中，主句用将来时，从句用一般现在时表将来</em>。",
    ]),
], tag="核心 · 必考"))

S.append(SEC("语法专题四：虚拟语气与特殊句式", [
    KP("虚拟语气", "1", [
        "与现在事实相反：<strong>条件句用 did/were，主句用 would/could/should/might + do</strong>。",
        "与过去事实相反：<em>条件句用 had done，主句用 would/could + have done</em>。",
        "与将来事实相反：<strong>条件句用 did/were to do/should do，主句用 would + do</strong>。",
        "if 省略倒装：<em>Were I you...；Had I known...；Should it rain...</em>。",
        "wish 宾语从句：<strong>与现在相反用过去时，与过去相反用过去完成时，与将来相反用 would do</strong>。",
        "建议、命令、要求类动词后的从句用 (should) do：<em>suggest, advise, propose, demand, require, request, insist, order</em>。",
    ], ("tip", "💡", "虚拟语气速记：<strong>现在用过去，过去用完成，将来用过去式/were to/should</strong>。记住这条主线，做题时先判断时间，再套结构。")),
    KP("强调句与倒装句", "2", [
        "强调句结构：<strong>It is/was + 被强调部分 + that/who + 其余部分</strong>。",
        "强调句判断方法：<em>去掉 It is/was 和 that，句子仍然完整，即为强调句</em>。",
        "not until 强调句：<strong>It was not until... that...</strong>。",
        "完全倒装：<em>Here comes the bus.；There goes the bell.；On the wall hangs a picture.</em>",
        "部分倒装：<strong>否定词置于句首（Never, Hardly, Seldom, Not only）；Only + 状语置于句首；so/neither/nor 置于句首</strong>。",
    ]),
], tag="难点"))

S.append(SEC("核心词汇与短语", [
    KP("必修一高频词汇", "1", [
        "<strong>Unit 1 Teenage Life</strong>：senior, graduate, recommend, extra-curricular, volunteer, responsible, confused。",
        "<strong>Unit 2 Travelling Around</strong>：transport, destination, arrangement, breathtaking, ancient, souvenir。",
        "<strong>Unit 3 Sports and Fitness</strong>：athlete, champion, medal, compete, strength, determination, injury。",
        "<strong>Unit 4 Natural Disasters</strong>：earthquake, flood, drought, rescue, survivor, destroy, shelter。",
        "<strong>Unit 5 Languages Around the World</strong>：dialect, character, symbol, translate, communicate, culture。",
    ], ("key", "🔑", "高考英语要求掌握 <strong>3500 词</strong>。建议按「教材单元 + 话题分类」双重维度记忆，比按字母顺序背效率高得多。")),
    KP("必修二、三高频词汇", "2", [
        "<strong>必修二</strong>：heritage, preserve, promote, tradition, customs, festival, sacrifice, ancestor。",
        "<strong>必修三</strong>：diverse, significance, influence, civilization, innovation, sustainable, resource。",
        "高考高频动词短语：<em>come up with, put up with, look forward to, get rid of, make up for, take advantage of, keep up with</em>。",
        "高频形容词：<em>significant, essential, considerable, available, effective, efficient, appropriate</em>。",
    ]),
    KP("构词法与词汇拓展", "3", [
        "常见前缀：<strong>un-（不）、dis-（否定）、re-（再）、pre-（预先）、mis-（错误）、over-（过度）、under-（不足）</strong>。",
        "常见后缀：<em>-tion/-sion（名词）、-ment（名词）、-less（无）、-ful（充满）、-able（可…的）、-ive（…的）</em>。",
        "词性转换：<em>succeed(v.) → success(n.) → successful(adj.) → successfully(adv.)</em>。",
        "高考重点考查<strong>词性转换</strong>，尤其是语法填空和短文改错中。",
    ]),
], tag="积累 · 必背"))

S.append(SEC("写作专题", [
    KP("应用文写作", "1", [
        "常见体裁：<strong>书信、邮件、通知、演讲稿、倡议书、日记</strong>。",
        "书信结构：<em>称呼（Dear...）→ 开头（说明写信目的）→ 主体（分点陈述）→ 结尾（表达期待）→ 落款（Yours sincerely, Li Hua）</em>。",
        "演讲稿结构：<strong>问候（Good morning, everyone!）→ 提出话题 → 分点论述 → 号召呼吁 → 致谢（Thank you.）</strong>。",
        "高分表达：<em>I&#39;m writing to...；I would like to...；It is my great honour to...；I would appreciate it if...；Looking forward to your reply.</em>",
    ], ("key", "🔑", "应用文评分看重三点：<strong>格式正确、要点齐全、语言得体</strong>。三段式结构 + 高级句型替换，能从 12 分提到 20 分以上。")),
    KP("读后续写", "2", [
        "基本要求：<em>根据给定材料和两段首句续写，词数 150 左右</em>。",
        "结构安排：<strong>第一段承接上文，推进情节；第二段收束全文，点明主题或情感升华</strong>。",
        "关键技巧：①<strong>读懂原文（人物、情节、情感基调）</strong>；②<strong>把握首句信息的约束</strong>；③<strong>前后呼应，与原文情节闭环</strong>。",
        "常用情感描写：<em>relief（宽慰）、gratitude（感激）、overwhelmed（激动不已）、determined（坚定）、ashamed（羞愧）</em>。",
        "常用动作描写：<em>trembling hands, a lump in my throat, tears welling up, heart pounding, with a broad smile</em>。",
    ]),
    KP("写作常见失分点", "3", [
        "①<strong>时态混乱</strong>——读后续写应用一般过去时；②<strong>人称错误</strong>——注意原文是第一人称还是第三人称。",
        "③<strong>要点遗漏</strong>——应用文漏点直接扣分；④<strong>句式单一</strong>——全篇简单句，无高级结构。",
        "⑤<strong>拼写与语法错误</strong>——影响语言分；⑥<strong>字数不达标</strong>——不足或过多都会扣分。",
    ], ("warn", "⚠️", "读后续写最大的陷阱是<strong>情节跑偏</strong>——脱离原文设定自由发挥。务必严格顺着两段首句的指向写，让情节与原文自然衔接。")),
], tag="必考 · 25分"))

render("高一", "英语",
       ["必修一", "必修二", "必修三", "人教版", "高考词汇3500"],
       S,
       "本资料依据《普通高中英语课程标准（2017年版2020年修订）》与人教版必修教材编写 · 高一上下学期适用",
       "高一_英语_知识点考点.html")
print("✔ 高一英语")
