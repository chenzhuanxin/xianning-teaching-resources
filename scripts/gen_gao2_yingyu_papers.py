# -*- coding: utf-8 -*-
"""高二 英语 期末试卷 5 套（人教版 选择性必修）"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_common import save, base, Q, A

SEEDS = [
    ("第一学期期末质量检测", "期末质量检测A卷", "2025—2026学年第一学期"),
    ("第一学期期末教学质量监测", "质量监测B卷", "2025—2026学年第一学期"),
    ("第二学期期末质量检测", "期末质量检测C卷", "2025—2026学年第二学期"),
    ("第二学期期末综合能力测试", "综合能力D卷", "2025—2026学年第二学期"),
    ("学年度期末学业水平测试", "学业水平E卷", "2025—2026学年"),
]

READING = [
    ("Science and Society",
     "Scientific progress often brings both benefits and challenges. The invention of the "
     "internet, for example, has made information available to billions of people, but it has "
     "also created new problems such as the spread of false information.\n"
     "Some researchers argue that scientists should consider the social consequences of their "
     "work, not only its technical success. Others believe that science should remain "
     "independent and that society, not scientists, should decide how discoveries are used.\n"
     "What most agree on is that the relationship between science and society needs constant "
     "discussion. A discovery that seems purely technical may, years later, reshape how people "
     "live and think.",
     "What problem caused by the internet is mentioned?",
     ["A．Higher costs.", "B．The spread of false information.",
      "C．Fewer books.", "D．Slower communication."], "B"),
    ("Cultural Heritage",
     "Cultural heritage is not only about old buildings and objects. It also includes "
     "traditions, languages and skills passed down from generation to generation.\n"
     "In recent years, many young people in China have become interested in traditional "
     "crafts. Some learn paper-cutting; others study ancient musical instruments. Social media "
     "has helped them share their work with a wider audience.\n"
     "\"Heritage is not something we only protect,\" said a young craftsman. \"It is something "
     "we use and change, so that it stays alive.\"",
     "According to the passage, cultural heritage includes ______.",
     ["A．only old buildings", "B．traditions, languages and skills",
      "C．only modern art", "D．scientific inventions"], "B"),
    ("Technology and Learning",
     "Online learning platforms have changed how students study. They can watch lectures at "
     "any time and review difficult parts as often as they wish.\n"
     "However, research suggests that online learning works best when combined with "
     "face-to-face interaction. Students who only study online may feel isolated and lose "
     "motivation.\n"
     "The key, experts say, is not to choose between online and offline, but to design courses "
     "that make good use of both.",
     "What do experts suggest about online learning?",
     ["A．It should replace offline classes.", "B．It works best when combined with face-to-face learning.",
      "C．It always reduces motivation.", "D．It should be avoided by students."], "B"),
    ("Environmental Awareness",
     "Plastic pollution has become one of the most pressing environmental problems. Every "
     "year, millions of tons of plastic enter the ocean.\n"
     "Some countries have banned single-use plastic bags and encouraged people to bring their "
     "own. Others have invested in recycling technology.\n"
     "But researchers point out that recycling alone cannot solve the problem. Reducing "
     "production and changing consumption habits are equally important.",
     "What do researchers say about recycling?",
     ["A．It alone cannot solve plastic pollution.", "B．It is the only solution.",
      "C．It is unnecessary.", "D．It causes more pollution."], "A"),
    ("Global Cooperation",
     "Many of today's challenges — climate change, disease, poverty — cannot be solved by any "
     "single country alone.\n"
     "International organizations play an important role in coordinating efforts. They help "
     "countries share knowledge, provide aid, and set common goals.\n"
     "Yet cooperation is not always easy. Countries have different interests and levels of "
     "development. Building trust takes time and patience.",
     "What makes international cooperation difficult?",
     ["A．A lack of common goals.", "B．Different interests and levels of development.",
      "C．Too many organizations.", "D．A lack of technology."], "B"),
]

QIXUAN = [
    ("How to Build a Reading Habit",
     ["Reading regularly is easier when you turn it into a habit. Here are some practical tips.",
      "First, choose books you actually enjoy. ______",
      "Second, set a fixed time each day. ______",
      "Third, keep a book with you. ______",
      "Finally, do not worry about speed. ______",
      "Habits are built slowly, but they last."],
     ["A．Even fifteen minutes a day adds up to many books a year.",
      "B．Interest is what keeps you turning the pages.",
      "C．Understanding matters more than finishing quickly.",
      "D．Reading in bed always harms your eyes.",
      "E．You can read while waiting in line or on the bus.",
      "F．Books are always expensive.",
      "G．Never read more than one book at a time."],
     "1-B　2-A　3-E　4-C",
     "1. B（说明选择喜欢的书的原因：兴趣让人读下去）；2. A（说明固定时间的意义：每天15分钟即可积少成多）；3. E（说明随身带书的用处：利用零碎时间）；4. C（说明不必追求速度：理解比读完重要）。"),
    ("Learning to Manage Time",
     ["Time management is a skill that can be learned. Here is how to start.",
      "First, find out where your time goes. ______",
      "Second, decide what is most important. ______",
      "Third, learn to say no. ______",
      "Finally, review your week. ______",
      "With practice, you will feel more in control."],
     ["A．You cannot do everything, and that is fine.",
      "B．Record your activities for three days to see the truth.",
      "C．See what worked and what needs changing.",
      "D．Always finish the easiest task first.",
      "E．Not every task deserves the same amount of attention.",
      "F．Time management is natural for everyone.",
      "G．Rest is a waste of time."],
     "1-B　2-E　3-A　4-C",
     "1. B（说明如何了解时间去向：记录三天活动）；2. E（说明如何区分优先级：任务重要性不同）；3. A（说明要敢于拒绝：无法做完所有事）；4. C（说明每周回顾：检查与调整）。"),
    ("Dealing with Failure",
     ["Failure is uncomfortable, but it can be useful. Here is how to handle it well.",
      "First, allow yourself to feel disappointed. ______",
      "Second, look for the lesson. ______",
      "Third, change your approach. ______",
      "Finally, try again. ______",
      "Those who succeed are often those who failed most and gave up least."],
     ["A．Every failure contains information you can use.",
      "B．Pretending you do not care usually makes it worse.",
      "C．The same method twice will likely bring the same result.",
      "D．Failure means you have no ability.",
      "E．Do not let one bad experience stop you.",
      "F．Success comes without effort.",
      "G．Never admit that you were wrong."],
     "1-B　2-A　3-C　4-E",
     "1. B（说明要正视失望情绪：假装不在乎会更糟）；2. A（说明从失败中找教训）；3. C（说明要改变方法）；4. E（说明要再试一次）。"),
    ("The Value of Teamwork",
     ["Working with others can achieve what no individual can. Here is how to be a good teammate.",
      "First, be clear about your role. ______",
      "Second, communicate often. ______",
      "Third, support others when they struggle. ______",
      "Finally, share the credit. ______",
      "A strong team is built on trust, not on talent alone."],
     ["A．Small problems grow quickly when they are not discussed.",
      "B．Know what you are responsible for and do it well.",
      "C．A helping hand at the right moment can change everything.",
      "D．Take all the praise for yourself.",
      "E．Success belongs to everyone who contributed.",
      "F．Teams should never disagree.",
      "G．Individual work is always better."],
     "1-B　2-A　3-C　4-E",
     "1. B（说明明确自己的角色与职责）；2. A（说明经常沟通的重要性）；3. C（说明帮助他人的作用）；4. E（说明分享功劳）。"),
    ("Protecting Cultural Heritage",
     ["Cultural heritage belongs to everyone, and everyone can help protect it.",
      "First, learn about it. ______",
      "Second, visit and support it. ______",
      "Third, use it in daily life. ______",
      "Finally, pass it on. ______",
      "Heritage survives only when people care about it."],
     ["A．You cannot protect what you do not understand.",
      "B．Museums and heritage sites need visitors to stay alive.",
      "C．Traditional crafts can be part of modern design.",
      "D．Heritage should be locked away from the public.",
      "E．Teach the next generation what you have learned.",
      "F．Only experts can protect heritage.",
      "G．Old things are useless today."],
     "1-A　2-B　3-C　4-E",
     "1. A（说明了解是保护的前提）；2. B（说明参观与支持的作用）；3. C（说明让传统融入现代生活）；4. E（说明传承给下一代）。"),
]

def make_english(idx):
    title, seed, term = SEEDS[idx]
    m = base("高二英语", title, f"（人教版　{term}　满分150分　时间120分钟）", fs=150, dur=120)
    rd = READING[idx]
    qx = QIXUAN[idx]
    p = []
    p.append(dict(name="第一部分　阅读理解（共15小题，每小题2分，满分30分）",
                  tip="阅读下列短文，从每题所给的四个选项中，选出最佳选项。",
                  questions=[
                      Q("1", rd[1] + "\n\n" + rd[2] + "（2分）", 2, kind="阅读", opts=rd[3]),
                      Q("2", "根据上文，用英语回答：Why does the passage mention the internet and scientific progress?（2分）",
                        2, blanks=2),
                      Q("3", "根据上文，用英语回答：What is needed between science and society?（2分）",
                        2, blanks=2),
                      Q("4", "根据上文，用英语回答：According to a young craftsman, what should heritage be?（2分）",
                        2, blanks=2),
                      Q("5", "根据上文，用英语回答：What is the key to making online learning effective?（2分）",
                        2, blanks=2),
                  ]))
    p.append(dict(name="第二部分　七选五（共5小题，每小题2分，满分10分）",
                  tip="从短文后的选项中选出能填入空白处的最佳选项，有两项为多余选项。",
                  questions=[Q("6", f"阅读下面的短文，从A—G中选出能填入空白处的最佳选项。\n\n{qx[0]}\n\n"
                                    + "\n".join(qx[1]), 10, blanks=1)]))
    p.append(dict(name="第三部分　完形填空（共15小题，每小题1.5分，满分22.5分）",
                  tip="阅读下面的短文，从每题所给的四个选项中，选出可以填入空白处的最佳选项。",
                  questions=[
                      Q("7", "阅读下面的短文，完成下列各题。（15小题，共22.5分）\n\n"
                             "Two years ago, our class started a project to clean up a nearby river. "
                             "At first, few students believed we could 1 (1)______ anything.\n"
                             "We began by 2 (2)______ rubbish every weekend. Some of us were 3 (3)______ "
                             "at how much we collected.\n"
                             "A local company 4 (4)______ us with gloves and bags. The city government "
                             "later 5 (5)______ a new rule to stop factories from dumping waste.\n"
                             "What I learned is that change does not happen 6 (6)______. It begins "
                             "with small, repeated actions.\n\n"
                             "1．A．change　B．hide　C．avoid　D．forget\n"
                             "2．A．buying　B．collecting　C．selling　D．burning\n"
                             "3．A．angry　B．surprised　C．bored　D．tired\n"
                             "4．A．compared　B．helped　C．filled　D．replaced\n"
                             "5．A．broke　B．made　C．lost　D．copied\n"
                             "6．A．overnight　B．slowly　C．quietly　D．safely", 22.5, blanks=1),
                  ]))
    p.append(dict(name="第四部分　语法填空（共10小题，每小题1.5分，满分15分）",
                  tip="在空白处填入1个适当的单词或括号内单词的正确形式。",
                  questions=[
                      Q("8", "阅读下面的短文，在空白处填入适当的内容。\n\n"
                             "Cultural heritage is not only about old buildings. It also 1 (include) "
                             "______ traditions and skills.\n"
                             "In recent years, more young people 2 (become) ______ interested in "
                             "traditional crafts. They use social media 3 (share) ______ their work.\n"
                             "One craftsman said, \"Heritage is something we use and change, so that "
                             "it 4 (stay) ______ alive.\"\n"
                             "This attitude 5 (be) ______ important for the future of our culture.",
                        15, blanks=1),
                  ]))
    p.append(dict(name="第五部分　书面表达（共2题，满分40分）", tip="请在答题区域内作答。",
                  questions=[
                      Q("9", "假设你是李华，你校将举办「传统文化周」活动。请给外教 Mr. Smith 写一封邮件，"
                             "邀请他参加并介绍活动内容，内容包括：①活动时间与地点；②主要活动形式；"
                             "③邀请他分享本国文化。\n"
                             "注意：①词数100左右；②可以适当增加细节，以使行文连贯。（15分）", 15, blanks=10),
                      Q("10", "阅读下面的材料，根据其内容和所给段落开头语续写两段，使之构成一个完整的故事。\n\n"
                              "Anna had trained for the school marathon for months. On the day of the race, "
                              "she felt strong. But halfway through, she twisted her ankle and fell. The "
                              "other runners passed her one by one.\n\n"
                              "Paragraph 1: Anna wanted to give up. ______\n\n"
                              "Paragraph 2: When she finally crossed the finish line, no one was clapping. ______\n\n"
                              "注意：①续写词数应为150左右；②请按如下格式作答。（25分）", 25, blanks=14),
                  ]))
    ans = [
        A("1", rd[4], f"出处：{rd[0]}。{rd[2]}", kind="阅读"),
        A("2", "To show that scientific progress brings both benefits and challenges.",
          "由第一段可知，作者以互联网为例说明科学进步既带来好处也带来问题。", kind="简答"),
        A("3", "Constant discussion is needed between science and society.",
          "由第三段「the relationship between science and society needs constant discussion」可知。", kind="简答"),
        A("4", "Heritage should be something we use and change, so that it stays alive.",
          "由最后一段年轻工匠的话可知。", kind="简答"),
        A("5", "The key is to design courses that make good use of both online and offline learning.",
          "由最后一段「not to choose between online and offline, but to design courses that make good use of both」可知。", kind="简答"),
        A("6", qx[3], qx[4], kind="七选五"),
        A("7", "1.A　2.B　3.B　4.B　5.B　6.A",
          "1. change（起初很少有同学相信我们能「改变」什么）；2. collecting（每周收集垃圾）；"
          "3. surprised（对我们收集的量感到惊讶）；4. helped（当地公司「提供」帮助，help sb with sth）；"
          "5. made（政府后来「制定」新规定，make a rule）；6. overnight（变化不会「一夜之间」发生，与后文"
          "「始于细小而反复的行动」呼应）。", kind="完形"),
        A("8", "1. includes　2. have become　3. to share　4. stays　5. is",
          "1. 主语 It 为第三人称单数，一般现在时；2. 由 In recent years 可知用现在完成时，主语复数用 have；"
          "3. use sth to do sth 结构，用不定式 to share；4. so that 引导目的状语从句，从句主语 it 为第三人称单数，"
          "用 stays；5. 主语 This attitude 为第三人称单数，用 is。", kind="语法"),
        A("9", "【参考范文】\nDear Mr. Smith,\n　　I am writing to invite you to our school's "
                "\"Traditional Culture Week\", which will be held from May 10th to May 16th in the "
                "school hall.\n　　During the week, there will be many activities, such as "
                "paper-cutting workshops, traditional music performances and a Chinese painting "
                "exhibition. Students will also make and share traditional food.\n　　We would be "
                "honoured if you could join us and share something about your own culture. Your "
                "talk would certainly help us understand other cultures better.\n　　I am looking "
                "forward to your reply.\nYours sincerely,\nLi Hua",
          "评分要点：①涵盖三个要点（时间地点、活动形式、邀请分享）；②语言准确、连贯；③词数100左右；④邮件格式正确。",
          kind="写作"),
        A("10", "【参考范文】\nParagraph 1: Anna wanted to give up. Her ankle hurt badly and the "
                 "finish line seemed impossibly far away. But then she thought of all the mornings "
                 "she had got up early to train, and of her father, who had told her that finishing "
                 "matters more than winning. Slowly, she stood up and began to walk, then to jog, "
                 "one painful step after another.\n"
                 "Paragraph 2: When she finally crossed the finish line, no one was clapping. The "
                 "stands were almost empty and the other runners had long gone. But her father was "
                 "there, waiting alone by the line. He said nothing. He simply opened his arms and "
                 "held her. At that moment, Anna understood that she had won something more "
                 "important than a race.",
          "评分要点：①两段内容合理衔接原文；②情节自然、符合逻辑；③语言丰富、句式多样；④有细节与心理描写；⑤字数150左右。",
          kind="续写"),
    ]
    return m, p, ans

for i in range(5):
    m, p, ans = make_english(i)
    save(m, p, ans, SEEDS[i][1])
    print("✔ 高二英语", SEEDS[i][1])
