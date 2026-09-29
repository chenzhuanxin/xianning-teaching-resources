# -*- coding: utf-8 -*-
"""九年级 英语 期末试卷 5 套（仁爱版）"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_common import save, base, Q, A
out = []

SEEDS = [
    ("第一学期期末质量检测", "期末质量检测A卷", "2025—2026学年第一学期"),
    ("第二学期中考模拟测试", "中考模拟测试B卷", "2025—2026学年第二学期"),
    ("中考英语综合能力测试", "综合能力C卷", "中考复习阶段"),
    ("第二学期期末教学质量监测", "质量监测D卷", "2025—2026学年第二学期"),
    ("中考学业水平模拟考试", "学业水平E卷", "中考复习阶段"),
]

SINGLES = [
 [("The old man ______ in this village since he was born.", ["A. lives", "B. lived", "C. has lived", "D. is living"], "C"),
  ("—Have you ever ______ to Beijing?\n—Yes, I ______ there last summer.", ["A. been; went", "B. gone; went", "C. been; have gone", "D. gone; have been"], "A"),
  ("The homework ______ by the students yesterday.", ["A. finishes", "B. finished", "C. was finished", "D. is finished"], "C"),
  ("I don't know ______ .", ["A. where does he live", "B. where he lives", "C. where did he live", "D. where he live"], "B"),
  ("This is the book ______ I bought yesterday.", ["A. who", "B. whom", "C. which", "D. whose"], "C"),
  ("You'd better ______ too much junk food.", ["A. not eat", "B. not to eat", "C. don't eat", "D. not eating"], "A"),
  ("Neither Tom nor I ______ interested in the film.", ["A. am", "B. is", "C. are", "D. be"], "A"),
  ("The more you practice, ______ you will be.", ["A. the good", "B. the better", "C. the best", "D. better"], "B"),
  ("It's important ______ us to protect the environment.", ["A. of", "B. for", "C. to", "D. with"], "B"),
  ("—Would you mind ______ the window?\n—Not at all.", ["A. open", "B. opening", "C. to open", "D. opened"], "B"),
  ("He used to ______ late, but now he is used to ______ early.", ["A. get up; getting up", "B. getting up; get up", "C. get up; get up", "D. getting up; getting up"], "A"),
  ("The population of China ______ about 1.4 billion.", ["A. is", "B. are", "C. has", "D. have"], "A"),
  ("—How long have you ______ the bike?\n—For three years.", ["A. bought", "B. borrowed", "C. had", "D. lent"], "C"),
  ("We should prevent people ______ cutting down trees.", ["A. to", "B. from", "C. for", "D. of"], "B"),
  ("______ hard, and you will succeed.", ["A. Work", "B. Working", "C. To work", "D. Worked"], "A")],
 [("My sister ______ TV when I got home.", ["A. watches", "B. watched", "C. was watching", "D. has watched"], "C"),
  ("He asked me ______ I had finished my homework.", ["A. that", "B. if", "C. what", "D. which"], "B"),
  ("The trees ______ by the workers last year.", ["A. plant", "B. planted", "C. were planted", "D. are planted"], "C"),
  ("This is the most interesting book ______ I have ever read.", ["A. which", "B. who", "C. that", "D. what"], "C"),
  ("—Must I finish it now?\n—No, you ______ .", ["A. mustn't", "B. needn't", "C. can't", "D. shouldn't"], "B"),
  ("It's too noisy. Could you please ______ the radio?", ["A. turn up", "B. turn down", "C. turn on", "D. turn off"], "B"),
  ("______ of the two boys is good at swimming.", ["A. Both", "B. All", "C. Neither", "D. None"], "C"),
  ("He is ______ young ______ go to school.", ["A. so; that", "B. too; to", "C. such; that", "D. enough; to"], "B"),
  ("Look! The children ______ football on the playground.", ["A. play", "B. played", "C. are playing", "D. have played"], "C"),
  ("—How soon will the meeting begin?\n—______ .", ["A. In ten minutes", "B. Ten minutes ago", "C. For ten minutes", "D. Ten minutes"], "A"),
  ("I prefer reading books ______ watching TV.", ["A. than", "B. to", "C. for", "D. with"], "B"),
  ("She is the girl ______ helped me yesterday.", ["A. which", "B. whom", "C. who", "D. what"], "C"),
  ("The film ______ for ten minutes.", ["A. has begun", "B. began", "C. has been on", "D. is beginning"], "C"),
  ("If it ______ tomorrow, we will stay at home.", ["A. rain", "B. rains", "C. will rain", "D. rained"], "B"),
  ("I think English is ______ useful language.", ["A. a", "B. an", "C. the", "D. /"], "A")],
 [("Neither he nor I ______ from Canada.", ["A. is", "B. am", "C. are", "D. be"], "B"),
  ("The number of the students in our school ______ 2000.", ["A. is", "B. are", "C. has", "D. have"], "A"),
  ("Not only he but also I ______ interested in music.", ["A. am", "B. is", "C. are", "D. be"], "A"),
  ("He told me he ______ the Great Wall before.", ["A. visits", "B. visited", "C. had visited", "D. has visited"], "C"),
  ("This kind of paper ______ soft.", ["A. feel", "B. feels", "C. is feeling", "D. felt"], "B"),
  ("There ______ a pen and two books on the desk.", ["A. is", "B. are", "C. have", "D. has"], "A"),
  ("He has been in Beijing ______ three years ago.", ["A. for", "B. since", "C. in", "D. from"], "B"),
  ("______ good advice it is!", ["A. What a", "B. What", "C. How a", "D. How"], "B"),
  ("He ______ his homework at eight last night.", ["A. does", "B. did", "C. was doing", "D. has done"], "C"),
  ("It is the third time that he ______ late.", ["A. is", "B. was", "C. has been", "D. had been"], "C"),
  ("—I have never been to Shanghai.\n—______ .", ["A. So have I", "B. Neither have I", "C. So I have", "D. Neither I have"], "B"),
  ("I'd like to know ______ .", ["A. what can I do", "B. what I can do", "C. how can I do", "D. how I can do"], "B"),
  ("The little boy is old enough ______ himself.", ["A. dress", "B. to dress", "C. dressing", "D. dressed"], "B"),
  ("It is ______ that we can't go out.", ["A. such a cold weather", "B. so cold weather", "C. such cold weather", "D. so a cold weather"], "C"),
  ("We are looking forward to ______ from you soon.", ["A. hear", "B. hearing", "C. heard", "D. be heard"], "B")],
 [("He suggested ______ a meeting to discuss the problem.", ["A. hold", "B. holding", "C. to hold", "D. held"], "B"),
  ("The teacher asked us to hand in ______ .", ["A. as soon as possible", "B. as soon as possibly", "C. so soon as possible", "D. as soon as impossible"], "A"),
  ("I have ______ to tell you.", ["A. something important", "B. important something", "C. anything important", "D. important anything"], "A"),
  ("He is the only person ______ can solve the problem.", ["A. which", "B. whom", "C. that", "D. what"], "C"),
  ("—Why not ______ a rest?\n—Good idea.", ["A. take", "B. taking", "C. to take", "D. took"], "A"),
  ("The room ______ I live in is very big.", ["A. where", "B. which", "C. who", "D. what"], "B"),
  ("I ______ here since I came to this city.", ["A. work", "B. worked", "C. have worked", "D. am working"], "C"),
  ("He was so tired that he ______ .", ["A. fell asleep", "B. felt asleep", "C. fell sleep", "D. felt sleep"], "A"),
  ("The old man ______ for two years.", ["A. died", "B. has died", "C. has been dead", "D. is dying"], "C"),
  ("If I ______ you, I would accept the invitation.", ["A. am", "B. was", "C. were", "D. be"], "C"),
  ("He made a decision ______ a new job.", ["A. take", "B. taking", "C. to take", "D. took"], "C"),
  ("It's high time we ______ .", ["A. go", "B. went", "C. will go", "D. have gone"], "B"),
  ("Not until he came back ______ the truth.", ["A. I knew", "B. did I know", "C. I know", "D. do I know"], "B"),
  ("The homework ______ tomorrow morning.", ["A. must hand in", "B. must be handed in", "C. must handed in", "D. must be hand in"], "B"),
  ("I would rather ______ at home than go out.", ["A. stay", "B. staying", "C. to stay", "D. stayed"], "A")],
 [("The government has taken measures ______ the pollution.", ["A. reduce", "B. reducing", "C. to reduce", "D. reduced"], "C"),
  ("______ the help of my teacher, I made great progress.", ["A. Under", "B. With", "C. In", "D. By"], "B"),
  ("He devoted all his life ______ the poor.", ["A. help", "B. helping", "C. to help", "D. to helping"], "D"),
  ("The book is worth ______ .", ["A. read", "B. reading", "C. to read", "D. reads"], "B"),
  ("It is ten years ______ we last met.", ["A. when", "B. since", "C. before", "D. after"], "B"),
  ("There is little water in the bottle, ______ ?", ["A. is there", "B. isn't there", "C. is it", "D. isn't it"], "A"),
  ("Let's go for a walk, ______ ?", ["A. shall we", "B. will you", "C. do we", "D. don't we"], "A"),
  ("All the students went to the park ______ Tom.", ["A. except", "B. besides", "C. beside", "D. with"], "A"),
  ("I don't like the way ______ he speaks.", ["A. which", "B. in that", "C. how", "D. in which"], "D"),
  ("______ he is young, he knows a lot.", ["A. Because", "B. Though", "C. Since", "D. As"], "B"),
  ("The reason ______ he was late is unknown.", ["A. why", "B. which", "C. what", "D. when"], "A"),
  ("No sooner had he arrived ______ he was asked to leave.", ["A. when", "B. than", "C. then", "D. as"], "B"),
  ("He is the very person ______ I am looking for.", ["A. who", "B. whom", "C. that", "D. which"], "C"),
  ("Only in this way ______ improve your English.", ["A. you can", "B. can you", "C. you will", "D. will you"], "B"),
  ("He ______ his best but failed at last.", ["A. tried", "B. has tried", "C. had tried", "D. tries"], "A")],
]

CLOZES = [
 ["A good memory is a great help for 1 (1)______ every subject. Everyone 2 (2)______ his memory to work in a right way during his studies. Study 3 (3)______ , if you do not use it, you will 4 (4)______ it. So you must 5 (5)______ your memory often.",
  "When you find that your memory is not good 6 (6)______ , you should 7 (7)______ about your study methods. Maybe you do not 8 (8)______ enough sleep, or you are 9 (9)______ at something. You should 10 (10)______ a good habit of studying.",
  "Please remember that a good memory comes from 11 (11)______ practice. If you want to have a good memory, you must 12 (12)______ hard at any time. 13 (13)______ you study, the better your memory will be. And you will find that 14 (14)______ is easier for you to remember things than before. 15 (15)______ you keep on doing like this, you will be successful one day."],
 ["A famous scientist once said, \"Never 1 (1)______ up what you are doing for lack of confidence.\" He had failed many times 2 (2)______ he finally succeeded. His story 3 (3)______ us that we should not be afraid of failure.\nEveryone may 4 (4)______ failures in his life. The most important thing is to learn 5 (5)______ failures. Failure is the mother of 6 (6)______ .",
  "When you 7 (7)______ in something, do not lose heart. You should find out the 8 (8)______ and try again. If you 9 (9)______ trying, you will succeed 10 (10)______ day. Many great people achieved success 11 (11)______ they had failed many times. They never 12 (12)______ up.",
  "So, 13 (13)______ you meet with difficulties, please remember: never give up. Keep 14 (14)______ hard and believe in 15 (15)______ . Then your dream will come true."],
 ["The Internet has 1 (1)______ our life greatly. We can 2 (2)______ information, send emails 3 (3)______ talk with friends online. It 4 (4)______ our world smaller. 5 (5)______ , the Internet also brings some problems.",
  "Some students 6 (6)______ too much time playing games. It is 7 (7)______ for their eyes and study. Some people 8 (8)______ their personal information on the Internet, which may 9 (9)______ them in danger. So we should 10 (10)______ the Internet properly.",
  "First, we should use the Internet 11 (11)______ the right way. Second, we should not 12 (12)______ our personal information easily. 13 (13)______ , we should spend more time 14 (14)______ sports or reading books. If we do 15 (15)______ , the Internet will be a good helper for us."],
 ["Everyone has a dream. So does Li Ming, a 1 (1)______ boy from a small village. His dream is to 2 (2)______ a teacher in the future. He works very 3 (3)______ at school. Every morning he 4 (4)______ up early and reads English aloud. His teachers 5 (5)______ him very much.",
  "However, his family is 6 (6)______ poor. He has to 7 (7)______ money by doing part-time jobs. But he never 8 (8)______ up his dream. He says, \"If I keep 9 (9)______ , my dream will come true 10 (10)______ day.\"",
  "Last year, he 11 (11)______ a scholarship and continued his studies. Now he is 12 (12)______ harder than before. He often 13 (13)______ help to other students. Everyone 14 (14)______ him. We should learn 15 (15)______ him."],
 ["Protecting the environment is very important. The earth is our 1 (1)______ , and we should 2 (2)______ good care of it. There 3 (3)______ many ways to protect it.\nFirst, we should not 4 (4)______ rubbish everywhere. We should 5 (5)______ it into the dustbin. Second, we should 6 (6)______ water and electricity. Third, we should plant more 7 (7)______ .",
  "8 (8)______ the three Rs — reduce, reuse and recycle. We should 9 (9)______ rubbish as much as possible. For example, we can 10 (10)______ old bottles to make new things. We can also 11 (11)______ plastic bags with cloth bags.",
  "If everyone 12 (12)______ a contribution to protecting the environment, the world will 13 (13)______ more and more beautiful. Let's 14 (14)______ action right now. The 15 (15)______ you start, the better it will be."],
]

CLOZE_OPTS = [
 "",
]

def make_paper(idx):
    title, seed, term = SEEDS[idx]
    m = base("九年级英语", title,
             f"（仁爱版　{term}　满分120分　时间120分钟）", fs=120, dur=120)
    p = []

    p.append({"name": "一、单项选择（每题1分，共15分）",
              "questions": [Q(i, s, 1, opts=o, kind="单选") for i, (s, o, _) in enumerate(SINGLES[idx], 1)]})

    p.append({"name": "二、完形填空（每题1分，共15分）",
              "questions": [
                  Q(16, CLOZES[idx][0] + "\n" + CLOZES[idx][1] + "\n" + CLOZES[idx][2], 15, kind="完形填空")
              ]})

    p.append({"name": "三、阅读理解（每题2分，共30分）", "questions": [
        Q(17, "（一）阅读下面短文，判断正误（T/F）。\n"
              "Mr. Green is a doctor. He works in a big hospital in the city. He is very busy every day, "
              "but he still tries his best to help his patients. He often says, \"Health is more important than money.\"\n"
              "判断正误（正确的写 T，错误的写 F）：\n"
              "（1）Mr. Green works in a small hospital.\n"
              "（2）He is free every day.\n"
              "（3）He thinks health is more important than money.\n"
              "（4）He doesn't like helping his patients.\n"
              "（5）He works as a doctor.", 10, kind="阅读判断"),
        Q(22, "（二）阅读下面短文，选择最佳答案。\n"
              "In China, the Spring Festival is the most important festival. Before it comes, people clean their houses "
              "and buy new clothes. On the eve of the festival, families get together and have a big dinner. "
              "Children can get red packets from their parents and relatives. On the first day of the new year, "
              "people visit their friends and relatives. The Spring Festival lasts fifteen days.\n"
              "（1）What is the most important festival in China?（　）\n"
              "A. The Mid-Autumn Festival　B. The Spring Festival　C. The Lantern Festival　D. The Dragon Boat Festival\n"
              "（2）What do people do before the festival?（　）\n"
              "A. Clean houses　B. Buy new clothes　C. Both A and B　D. Nothing\n"
              "（3）What can children get?（　）\n"
              "A. Clothes　B. Books　C. Red packets　D. Money from school\n"
              "（4）How long does the Spring Festival last?（　）\n"
              "A. Five days　B. Ten days　C. Fifteen days　D. Twenty days\n"
              "（5）On the first day of the new year, people usually ______ .（　）\n"
              "A. stay at home　B. visit friends and relatives　C. go to work　D. go shopping", 10, kind="阅读选择"),
        Q(27, "（三）任务型阅读。\n"
              "Dear Editor,\n"
              "I am a middle school student. I have a problem. My parents don't allow me to watch TV or play computer games. "
              "They say these things are bad for my study. But I think I need some time to relax. What should I do?\n"
              "Yours,\nLi Hua\n\n"
              "请根据短文内容回答下列问题：\n"
              "（1）Who writes the letter?\n"
              "（2）What problem does Li Hua have?\n"
              "（3）Why don't Li Hua's parents allow him to watch TV?\n"
              "（4）What does Li Hua think he needs?\n"
              "（5）What do you think Li Hua should do?", 10, kind="任务型阅读"),
    ]})

    p.append({"name": "四、词汇与句型（每题1分，共20分）", "questions": [
        Q(32, "（一）根据句意及首字母提示补全单词。\n"
              "（1）The p______ of China is about 1.4 billion.\n"
              "（2）We should p______ the environment from being polluted.\n"
              "（3）He is very h______ ; he often helps others.\n"
              "（4）The d______ between the two cities is about 300 kilometers.\n"
              "（5）She has a good m______ , so she can remember things quickly.", 5, kind="词汇"),
        Q(37, "（二）用所给词的适当形式填空。\n"
              "（1）He has been ______ (teach) English for ten years.\n"
              "（2）It is ______ (importance) to learn English well.\n"
              "（3）The trees ______ (plant) by us last year.\n"
              "（4）She is good at ______ (dance).\n"
              "（5）If it ______ (be) fine tomorrow, we will go hiking.", 5, kind="词形变化"),
        Q(42, "（三）按要求完成句子（每空一词）。\n"
              "（1）I have already finished my homework.（改为否定句）\nI ______ finished my homework ______ .\n"
              "（2）Tom is a very clever boy.（改为感叹句）\n______ ______ clever boy Tom is!\n"
              "（3）They built the bridge last year.（改为被动语态）\nThe bridge ______ ______ last year.\n"
              "（4）He asked me, \"Do you like English?\"（改为宾语从句）\nHe asked me ______ I ______ English.\n"
              "（5）The film began ten minutes ago.（用现在完成时改写）\nThe film ______ ______ ______ for ten minutes.", 10, kind="句型转换"),
    ]})

    WRITING = [
        "近年来，环境问题日益严重。请以「How to Protect the Environment」为题，用英语写一篇短文，"
        "谈谈我们中学生应该怎样保护环境。\n提示：①不乱扔垃圾；②节约用水用电；③多种树；④绿色出行。\n"
        "要求：①80—100 词；②文中不得出现真实的人名、校名、地名；③可适当发挥。",
        "请以「My Dream」为题，用英语写一篇短文，介绍你的梦想以及你打算如何实现它。\n"
        "要求：①80—100 词；②文中不得出现真实的人名、校名、地名；③可适当发挥。",
        "假设你叫李华，你的笔友 Peter 想了解中国的传统节日。请你写一封信，向他介绍中秋节（the Mid-Autumn Festival）。\n"
        "提示：①时间：农历八月十五；②活动：赏月、吃月饼、家人团聚；③意义：象征团圆。\n"
        "要求：①80—100 词；②文中不得出现真实的人名、校名、地名；③可适当发挥。",
        "学校英语俱乐部正在招募新成员。请你以「Join Us!」为题写一则招募启事。\n"
        "提示：①活动内容：英语角、英语演讲比赛、看英文电影；②时间：每周五下午；③联系邮箱：englishclub@school.com。\n"
        "要求：①80—100 词；②文中不得出现真实的人名、校名、地名；③可适当发挥。",
        "请以「An Unforgettable Experience」为题，用英语写一篇短文，讲述一次令你难忘的经历及你的感受。\n"
        "要求：①80—100 词；②文中不得出现真实的人名、校名、地名；③可适当发挥。",
    ][idx]
    p.append({"name": "五、书面表达（15分）", "questions": [Q(47, WRITING, 15, kind="书面表达")]})

    cloze_ans = [
        "1. with　2. should train　3. hard　4. forget　5. use\n6. enough　7. think　8. get　9. worried　10. form\n11. constant　12. work　13. The more　14. it　15. If",
        "1. give　2. before　3. tells　4. meet　5. from\n6. success　7. fail　8. reason　9. keep　10. some\n11. because　12. give　13. when　14. working　15. yourself",
        "1. changed　2. search for　3. and　4. makes　5. However\n6. spend　7. bad　8. put　9. put　10. use\n11. in　12. give out　13. Third　14. doing　15. so",
        "1. young　2. become　3. hard　4. gets　5. like\n6. very　7. make　8. gives　9. trying　10. one\n11. got　12. working　13. offers　14. loves　15. from",
        "1. home　2. take　3. are　4. throw　5. put\n6. save　7. trees　8. Remember　9. reduce　10. reuse\n11. replace　12. makes　13. become　14. take　15. earlier",
    ][idx]

    answers = []
    for i, (_, _, ans) in enumerate(SINGLES[idx], 1):
        answers.append(A(i, ans, "本题考查时态、语态、从句、固定搭配等核心语法点。"))
    answers.append(A(16, cloze_ans, "完形填空要通读全文、把握上下文逻辑，注意固定搭配与词形变化。"))
    answers.append(A(17, "（1）F　（2）F　（3）T　（4）F　（5）T", "判断正误题须在文中找到对应依据。"))
    answers.append(A(22, "（1）B　（2）C　（3）C　（4）C　（5）B", "细节理解题，答案均可在原文中定位。"))
    answers.append(A(27, "（1）Li Hua.\n（2）His parents don't allow him to watch TV or play computer games.\n"
                         "（3）Because they think these things are bad for his study.\n"
                         "（4）He thinks he needs some time to relax.\n"
                         "（5）He should talk with his parents and make a plan to balance study and rest.（答案合理即可）",
                    "任务型阅读要求成句作答，注意疑问词的对应关系。"))
    answers.append(A(32, "（1）population　（2）protect　（3）helpful　（4）distance　（5）memory", "考查核心词汇的拼写。"))
    answers.append(A(37, "（1）teaching　（2）important　（3）were planted　（4）dancing　（5）is", "考查词形变化与非谓语动词。"))
    answers.append(A(42, "（1）haven't; yet　（2）What a　（3）was built　（4）if/whether; liked　（5）has been on",
                    "句型转换要严格按要求，注意每空一词、语序与时态。"))
    answers.append(A(47, "参考范文（以第 %d 篇为例）：\n"
                         "How to Protect the Environment\n"
                         "The environment is becoming worse and worse. As middle school students, we should do something to protect it.\n"
                         "First, we should not throw rubbish everywhere. We should put it into the dustbin. "
                         "Second, we should save water and electricity. Third, we should plant more trees. "
                         "What's more, we'd better go to school by bike or on foot instead of by car.\n"
                         "If everyone makes a contribution, our world will be more and more beautiful. Let's take action right now!"
                         % (idx + 1),
                    "书面表达评分要点：内容完整（要点齐全）、语言准确（语法拼写）、行文连贯（连接词）、书写规范。\n"
                    "字数不足 60 词扣分；出现真实人名校名酌情扣分。"))

    out.append(save(m, p, answers, seed))


if __name__ == "__main__":
    for i in range(5):
        make_paper(i)
    print("已生成 %d 套：" % len(out))
    for s in out:
        print(" -", s)
