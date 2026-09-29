# -*- coding: utf-8 -*-
"""高一 英语 期末试卷 5 套（人教版）"""
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

# 阅读理解语篇（4 篇/套，每套差异化）
READING = [
    [("A",
      "When Li Hua first entered senior high school, he felt lost. The courses were harder, "
      "the teachers spoke faster, and he had few friends. For two weeks he sat alone in the "
      "canteen, eating quickly and returning to the classroom.\n"
      "Everything changed on a rainy afternoon. He forgot his umbrella, and a girl named Wang "
      "Fang shared hers with him. They walked together and talked about their favourite books. "
      "By the time they reached the school gate, Li Hua had made his first friend.\n"
      "\"It is not the big things that make you feel at home,\" Li Hua later wrote in his diary. "
      "\"It is an umbrella, a smile, or simply someone who waits for you.\"",
      "Li Hua felt lost at first because ______.",
      ["A．he had no money", "B．the courses were harder and he had few friends",
       "C．he disliked his teachers", "D．he missed his primary school"], "B"),
     ("B",
      "A new study from a Chinese university suggests that students who sleep less than seven "
      "hours a night perform worse in memory tests than those who sleep eight hours. The "
      "researchers tested 1,200 students over three years.\n"
      "The finding is not surprising to doctors. During deep sleep, the brain organizes what "
      "we have learned during the day. Without enough sleep, this process is interrupted.\n"
      "The study also found that students who used phones before bed took longer to fall "
      "asleep. The light from screens tells the brain that it is still daytime.",
      "According to the passage, deep sleep helps students ______.",
      ["A．grow taller", "B．organize what they have learned",
       "C．use phones less", "D．eat more healthily"], "B"),
     ("C",
      "Every spring, thousands of birds fly over the wetlands of Xianning. They stop there to "
      "rest and eat before continuing their long journey north.\n"
      "Local volunteers have built a small station to watch and protect the birds. They record "
      "the number of each species and check whether the water is clean.\n"
      "\"Birds are like visitors,\" said one volunteer. \"If they keep coming back, it means we "
      "are doing something right.\"",
      "The volunteers' main purpose is to ______.",
      ["A．catch birds for study", "B．watch and protect the birds",
       "C．build houses for people", "D．grow more plants"], "B"),
     ("D",
      "Imagine a school where there are no bells. Students decide when to start a task and "
      "when to finish it. This is called \"self-paced learning\", and it is being tried in "
      "some schools.\n"
      "Supporters say it helps students take responsibility for their own progress. Critics "
      "argue that young students may delay their work without a fixed schedule.\n"
      "Most teachers agree that the answer lies in balance: some structure, plus some freedom.",
      "What is the main idea of the passage?",
      ["A．Schools should have more bells.", "B．Self-paced learning has both benefits and risks.",
       "C．Students should never choose tasks.", "D．Teachers dislike all new methods."], "B"),
    ],
    [("A",
      "Zhang Wei is a volunteer teacher in a mountain village. Every morning he walks forty "
      "minutes to school along a narrow path.\n"
      "\"At first I wanted to leave,\" he says. \"The weather was cold, and there was no "
      "internet. But the children's eyes kept me there.\"\n"
      "In three years, he has helped twelve students enter senior high school. He has also "
      "started a small library with books donated by people in the city.\n"
      "\"I did not change the world,\" he says with a smile. \"But maybe I changed twelve "
      "worlds.\"",
      "Zhang Wei decided to stay mainly because of ______.",
      ["A．the high salary", "B．the children's eyes", "C．the good weather", "D．the internet"], "B"),
     ("B",
      "The bicycle is one of the most efficient machines ever invented. It uses human power "
      "and produces no pollution.\n"
      "In many Chinese cities, shared bicycles have become popular in the last ten years. "
      "People can find a bicycle with a phone app, ride it, and leave it almost anywhere.\n"
      "However, the system has problems. Some bicycles are broken or parked badly, blocking "
      "the pavement. Cities are now working on better rules.",
      "What problem with shared bicycles is mentioned?",
      ["A．They are too expensive.", "B．They produce much pollution.",
       "C．Some are broken or parked badly.", "D．They cannot be found by phone."], "C"),
     ("C",
      "Scientists have found that trees in a forest can share food and even send warnings "
      "through their roots. A network of fungi connects the roots of different trees.\n"
      "Through this network, a tree that has enough sugar can send some to a weaker "
      "neighbour. When one tree is attacked by insects, others can prepare their defences.\n"
      "This discovery has changed how we see forests. A forest is not just many trees; it is "
      "a community.",
      "According to the passage, the fungi network helps trees ______.",
      ["A．grow taller than others", "B．share food and send warnings",
       "C．produce more seeds", "D．stay away from each other"], "B"),
     ("D",
      "A museum in Wuhan opened a special room last year. Visitors wear glasses and step into "
      "a \"virtual\" palace from the Tang Dynasty.\n"
      "The room uses digital technology to show old buildings, clothes and music. Visitors "
      "can \"walk\" through the palace and \"talk\" to figures from history.\n"
      "\"We cannot bring people back in time,\" said the director. \"But we can bring the past "
      "closer to them.\"",
      "The special room in the museum uses technology to ______.",
      ["A．repair old buildings", "B．bring the past closer to visitors",
       "C．sell Tang Dynasty clothes", "D．train young directors"], "B"),
    ],
    [("A",
      "Wang Lei loves cooking. Every weekend, she cooks dinner for her family. Her father "
      "used to say it was a \"girl's job\", but now he helps her in the kitchen.\n"
      "\"Cooking is not about gender,\" Wang Lei says. \"It is about caring for people you "
      "love.\"\n"
      "Last year she won a cooking competition at her school. The judges praised not only her "
      "food but also her idea: a family meal can bring people together.",
      "What did Wang Lei's father do after she started cooking?",
      ["A．He stopped eating her food.", "B．He began to help her in the kitchen.",
       "C．He cooked for the school.", "D．He joined a competition."], "B"),
     ("B",
      "Reading is like exercising a muscle. The more you read, the stronger your ability to "
      "concentrate becomes.\n"
      "But not all reading is equal. Studies show that reading a long story trains attention "
      "better than quickly reading many short messages.\n"
      "If you want to improve your reading, start with something you enjoy. Interest is the "
      "best teacher, and it can keep you going when a book becomes difficult.",
      "According to the passage, which kind of reading trains attention better?",
      ["A．Short messages", "B．A long story", "C．News headlines", "D．Ads"], "B"),
     ("C",
      "The Grand Canal, which connects Beijing and Hangzhou, is the longest man-made waterway "
      "in the world. It was built over many centuries.\n"
      "In the past, the canal carried rice and other goods. Today, it is used less for "
      "transport but more for tourism and water supply.\n"
      "Some sections were polluted, so the government has taken action to clean the water and "
      "protect the ancient bridges and buildings along it.",
      "The Grand Canal is used today mainly for ______.",
      ["A．carrying rice", "B．tourism and water supply", "C．military transport", "D．fishing"], "B"),
     ("D",
      "Many students feel nervous before exams. A simple method can help: write down your "
      "worries for ten minutes before the test.\n"
      "In an experiment, students who wrote down their worries scored higher than those who "
      "did not. Writing seems to free the mind from anxious thoughts.\n"
      "\"You cannot stop worrying,\" said a researcher. \"But you can put the worry on paper "
      "and leave it there.\"",
      "What is the passage mainly about?",
      ["A．How to write good exams", "B．A method to reduce exam nerves",
       "C．Why students dislike school", "D．How to choose universities"], "B"),
    ],
    [("A",
      "Chen Ming joined the school swimming team last year. He was the slowest at first and "
      "often finished last in training.\n"
      "Instead of giving up, he asked the fastest swimmer for advice. He practised an extra "
      "hour every morning.\n"
      "Six months later, he took third place in the city competition. \"I did not beat "
      "everyone,\" he said. \"But I beat the person I was yesterday.\"",
      "What did Chen Ming do to improve?",
      ["A．He asked for advice and practised more.", "B．He gave up swimming.",
       "C．He joined another team.", "D．He changed schools."], "A"),
     ("B",
      "Food waste is a serious problem. It is reported that about one third of the food "
      "produced in the world is never eaten.\n"
      "In many restaurants, too much food is thrown away every day. Some cities have started "
      "programmes to collect leftover food and give it to people in need.\n"
      "Experts say that the simplest solution is also the most effective: order only what "
      "you can eat.",
      "According to the experts, the simplest solution to food waste is ______.",
      ["A．to order only what you can eat", "B．to build more restaurants",
       "C．to produce more food", "D．to eat faster"], "A"),
     ("C",
      "In the past, farmers in some areas relied on rainfall to water their crops. When there "
      "was little rain, the harvest was poor.\n"
      "Now, some farms use small sensors in the soil. The sensors measure how much water the "
      "soil holds and send the information to a phone.\n"
      "Farmers can then decide exactly when and how much to water. This has saved both water "
      "and money.",
      "The soil sensors help farmers to ______.",
      ["A．sell their crops faster", "B．decide when and how much to water",
       "C．grow taller plants", "D．protect crops from insects"], "B"),
     ("D",
      "Some people believe that talent decides success. Others believe that effort matters "
      "more.\n"
      "A famous study followed a group of young musicians. The best players were not those "
      "with the greatest natural talent, but those who practised the most hours.\n"
      "This does not mean talent is useless. It means that without effort, talent may never "
      "show itself.",
      "What does the study suggest?",
      ["A．Talent always decides success.", "B．Effort matters greatly for success.",
       "C．Musicians are born, not made.", "D．Practice is useless."], "B"),
    ],
    [("A",
      "Liu Fang works in a small bookshop. She noticed that many children came in but few "
      "bought books.\n"
      "So she started a \"reading corner\" with cushions and a small lamp. Children could sit "
      "and read for free.\n"
      "At first, some parents worried that the children would only play. But after a month, "
      "sales of children's books had doubled.\n"
      "\"If a child falls in love with reading here,\" Liu Fang says, \"they will come back "
      "for the rest of their life.\"",
      "What happened after Liu Fang started the reading corner?",
      ["A．Fewer children came in.", "B．Sales of children's books doubled.",
       "C．Parents stopped buying books.", "D．The shop closed."], "B"),
     ("B",
      "The number of electric cars in Chinese cities has grown quickly. They produce no "
      "exhaust gas, which helps improve air quality.\n"
      "But electric cars also bring new problems. Charging stations are not yet everywhere, "
      "and the batteries must eventually be recycled.\n"
      "Governments and companies are working together to build more stations and to develop "
      "better recycling methods.",
      "Which problem of electric cars is mentioned in the passage?",
      ["A．They are too slow.", "B．Charging stations are not everywhere.",
       "C．They use too much oil.", "D．They are too noisy."], "B"),
     ("C",
      "Honey has been used as food and medicine for thousands of years. Ancient Egyptians "
      "put it in tombs, and it was still edible after 3,000 years.\n"
      "Honey contains very little water and is acidic, so bacteria cannot easily grow in it. "
      "This is why it does not spoil quickly.\n"
      "Today, doctors still use special honey to help heal some wounds.",
      "Why does honey not spoil quickly?",
      ["A．It is kept in tombs.", "B．It contains little water and is acidic.",
       "C．It is always frozen.", "D．It is mixed with salt."], "B"),
     ("D",
      "When you learn a new language, making mistakes is not a failure — it is part of the "
      "process.\n"
      "Children learn their first language by trying, failing and trying again. They are not "
      "afraid of being wrong.\n"
      "Older learners often stop speaking because they fear mistakes. Teachers suggest "
      "starting with simple sentences and speaking a little every day.",
      "What do teachers suggest to language learners?",
      ["A．To avoid speaking until perfect.", "B．To start with simple sentences and speak daily.",
       "C．To stop making mistakes.", "D．To learn only grammar rules."], "B"),
    ],
]

# 七选五（每套固定一篇结构不同的）
QIXUAN = [
    ("How to Make a Good Study Plan",
     ["A good study plan helps you use your time well. Here are some tips.",
      "First, write down all your tasks for the week. ______",
      "Second, put the most difficult task first. ______",
      "Third, take short breaks. ______ For example, study for 45 minutes, then rest for 10.",
      "Finally, check your plan every evening. ______",
      "With a good plan, you will feel calmer and learn more."],
     ["A．Your brain is freshest in the morning or after a rest.",
      "B．Do not try to do everything at once.",
      "C．See what you finished and what you still need to do.",
      "D．This helps you remember what you have learned.",
      "E．Being organized is the key to success.",
      "F．A long break is better than a short one.",
      "G．It will be easier to see what really needs doing."],
     "1-G　2-A　3-B　4-C",
     "1. G（承上，说明列出任务的作用）；2. A（说明为何把最难的任务放前面）；3. B（引出「不要一次做完」并说明要短休）；4. C（说明每晚检查计划的内容）。"),
    ("How to Keep Healthy",
     ["Keeping healthy is not as hard as many people think.",
      "First, sleep enough. ______",
      "Second, eat a balanced diet. ______",
      "Third, move your body every day. ______ You do not need a gym; walking is enough.",
      "Finally, keep a good mood. ______",
      "Small habits, repeated daily, make a big difference."],
     ["A．Try to eat more vegetables and less sugar.",
      "B．Most students need about eight hours a night.",
      "C．Talking with friends can reduce stress.",
      "D．Sleep is more important than exercise.",
      "E．Even twenty minutes of walking helps.",
      "F．Drink as much water as possible.",
      "G．Fast food is always unhealthy."],
     "1-B　2-A　3-E　4-C",
     "1. B（说明睡眠时长）；2. A（说明均衡饮食的具体做法）；3. E（承接「无需健身房」，说明步行即可）；4. C（说明保持好心情的方法）。"),
    ("Learning from Mistakes",
     ["Everyone makes mistakes. What matters is what we do next.",
      "First, admit the mistake. ______",
      "Second, find out why it happened. ______",
      "Third, fix it if you can. ______",
      "Finally, remember the lesson. ______",
      "In this way, a mistake becomes a teacher rather than a wound."],
     ["A．A mistake may be caused by carelessness or by lack of knowledge.",
      "B．Do not pretend that nothing happened.",
      "C．Write down what you have learned so you will not repeat it.",
      "D．Mistakes should always be punished.",
      "E．Say sorry or make up for it as soon as possible.",
      "F．Never make the same mistake twice.",
      "G．Nobody likes to be wrong."],
     "1-B　2-A　3-E　4-C",
     "1. B（说明承认错误，不要装作无事）；2. A（分析错误原因）；3. E（说明如何弥补）；4. C（说明记住教训）。"),
    ("The Value of Reading",
     ["Reading is one of the best habits you can build.",
      "First, reading widens your world. ______",
      "Second, reading improves your language. ______",
      "Third, reading builds patience. ______",
      "Finally, reading gives you pleasure. ______",
      "So pick up a book today, and let it change you."],
     ["A．You meet people and places you may never see in real life.",
      "B．A long book requires you to keep going.",
      "C．It is a cheap and lasting source of happiness.",
      "D．Watching films is better than reading.",
      "E．You learn new words and better ways to express ideas.",
      "F．Reading is only for students.",
      "G．Books are always expensive."],
     "1-A　2-E　3-B　4-C",
     "1. A（说明阅读如何拓宽世界）；2. E（说明阅读如何提升语言）；3. B（说明阅读如何培养耐心）；4. C（说明阅读带来的快乐）。"),
    ("Being a Good Team Member",
     ["Working in a team is an important skill for life.",
      "First, listen to others. ______",
      "Second, share your ideas clearly. ______",
      "Third, do your part. ______",
      "Finally, accept the final decision. ______",
      "A good team member makes everyone stronger."],
     ["A．Others may have better ideas than you think.",
      "B．Speak simply, and give reasons for what you suggest.",
      "C．If you do not finish your task, the whole team suffers.",
      "D．You should always lead the team.",
      "E．Not everyone can be the leader, and that is fine.",
      "F．Teams are always better than individuals.",
      "G．Disagreement should be avoided at all costs."],
     "1-A　2-B　3-C　4-E",
     "1. A（说明倾听他人）；2. B（说明清晰表达自己的想法）；3. C（说明做好自己的部分）；4. E（说明接受最终决定）。"),
]

def make_english(idx):
    title, seed, term = SEEDS[idx]
    m = base("高一英语", title,
             f"（人教版　{term}　满分150分　时间120分钟）", fs=150, dur=120)
    p = []
    # 第一部分 阅读（4篇，共15小题，37.5分→简化为30分）
    rd = READING[idx]
    p.append(dict(name="第一部分　阅读理解（共15小题，每小题2分，满分30分）",
                  tip="阅读下列短文，从每题所给的四个选项中，选出最佳选项。",
                  questions=[
                      Q("1", rd[0][1] + "\n\n" + rd[0][2] + "（2分）", 2, kind="阅读A", opts=rd[0][3]),
                      Q("2", rd[1][1] + "\n\n" + rd[1][2] + "（2分）", 2, kind="阅读B", opts=rd[1][3]),
                      Q("3", rd[2][1] + "\n\n" + rd[2][2] + "（2分）", 2, kind="阅读C", opts=rd[2][3]),
                      Q("4", rd[3][1] + "\n\n" + rd[3][2] + "（2分）", 2, kind="阅读D", opts=rd[3][3]),
                      Q("5", "根据短文 A，用英语回答：What made Li Hua feel at home at last?（2分）",
                        2, blanks=2) if idx == 0 else
                      Q("5", "根据短文 A，用英语回答：Why did Zhang Wei decide to stay?（2分）",
                        2, blanks=2) if idx == 1 else
                      Q("5", "根据短文 A，用英语回答：What did Wang Lei's father do later?（2分）",
                        2, blanks=2) if idx == 2 else
                      Q("5", "根据短文 A，用英语回答：How did Chen Ming improve his swimming?（2分）",
                        2, blanks=2) if idx == 3 else
                      Q("5", "根据短文 A，用英语回答：What happened after Liu Fang started the reading corner?（2分）",
                        2, blanks=2),
                  ]))
    # 七选五
    qx = QIXUAN[idx]
    p.append(dict(name="第二部分　七选五（共5小题，每小题2分，满分10分）",
                  tip="从短文后的选项中选出能填入空白处的最佳选项，有两项为多余选项。",
                  questions=[
                      Q("6", f"阅读下面的短文，从A—G中选出能填入空白处的最佳选项。\n\n{qx[0]}\n\n"
                             + "\n".join(f"{c}" for c in qx[1]), 10, blanks=1),
                  ]))
    # 完形填空
    p.append(dict(name="第三部分　完形填空（共15小题，每小题1.5分，满分22.5分）",
                  tip="阅读下面的短文，从每题所给的四个选项中，选出可以填入空白处的最佳选项。",
                  questions=[
                      Q("7", "阅读下面的短文，完成下列各题。（15小题，共22.5分）\n\n"
                             "Last summer I 1 (1)______ a small village with my classmates. We stayed "
                             "there for a week and helped the farmers 2 (2)______ vegetables.\n"
                             "On the first day, I was 3 (3)______ because I had never worked on a farm "
                             "before. An old man 4 (4)______ me how to pick tomatoes without hurting "
                             "the plants.\n"
                             "By the end of the week, I had learned a lot 5 (5)______ farming. More "
                             "importantly, I learned that 6 (6)______ work can also be joyful.\n\n"
                             "1．A．visited　B．built　C．sold　D．closed\n"
                             "2．A．eat　B．cook　C．pick　D．buy\n"
                             "3．A．excited　B．nervous　C．angry　D．bored\n"
                             "4．A．asked　B．told　C．taught　D．warned\n"
                             "5．A．about　B．for　C．with　D．by\n"
                             "6．A．easy　B．hard　C．short　D．boring", 22.5, blanks=1),
                  ]))
    # 语法填空
    p.append(dict(name="第四部分　语法填空（共10小题，每小题1.5分，满分15分）",
                  tip="在空白处填入1个适当的单词或括号内单词的正确形式。",
                  questions=[
                      Q("8", "阅读下面的短文，在空白处填入适当的内容。\n\n"
                             "Reading is one of the 1 (good) ______ habits a student can have. "
                             "It 2 (help) ______ us learn new words and ideas.\n"
                             "When I was young, my mother 3 (read) ______ stories to me every "
                             "night. Now I read by 4 (I) ______.\n"
                             "Books are 5 (friend) ______ that never leave us.", 15, blanks=1),
                  ]))
    # 写作
    p.append(dict(name="第五部分　书面表达（共2题，满分40分）",
                  tip="请在答题区域内作答。",
                  questions=[
                      Q("9", "假设你是李华，你的英国朋友 Peter 即将到你校交流。请给他写一封邮件，内容包括："
                             "①表示欢迎；②介绍学校的基本情况；③说明你将如何帮助他适应新环境。\n"
                             "注意：①词数100左右；②可以适当增加细节，以使行文连贯。（15分）",
                        15, blanks=10),
                      Q("10", "阅读下面的材料，根据其内容和所给段落开头语续写两段，使之构成一个完整的故事。\n\n"
                              "Tom was a shy boy who seldom spoke in class. One day, his teacher asked him "
                              "to give a short speech in front of the whole class. His heart raced. He "
                              "wanted to run away.\n\n"
                              "Paragraph 1: But then he remembered what his father had told him. ______\n\n"
                              "Paragraph 2: When he finished, the classroom was silent. ______\n\n"
                              "注意：①续写词数应为150左右；②请按如下格式作答。（25分）",
                        25, blanks=14),
                  ]))
    ans = [
        A("1", rd[0][4], f"出处：短文 A。{rd[0][2]} 对应原文信息点。", kind="阅读A"),
        A("2", rd[1][4], f"出处：短文 B。{rd[1][2]}", kind="阅读B"),
        A("3", rd[2][4], f"出处：短文 C。{rd[2][2]}", kind="阅读C"),
        A("4", rd[3][4], f"出处：短文 D。{rd[3][2]}", kind="阅读D"),
        A("5", ["He made his first friend through an umbrella shared by a girl.",
                "Because the children's eyes kept him there.",
                "He began to help her in the kitchen.",
                "He asked the fastest swimmer for advice and practised an extra hour every morning.",
                "Sales of children's books doubled."][idx], "见短文 A 末段。", kind="简答"),
        A("6", qx[3], qx[4], kind="七选五"),
        A("7", "1.A　2.C　3.B　4.C　5.A　6.B",
          "1. visited（「我」和同学去村子，此处为参观访问）；2. pick（帮农民「摘」菜）；"
          "3. nervous（此前从未在农场干过活，因此紧张）；4. taught（老人「教」我如何摘番茄）；"
          "5. about（learn about「了解关于……的知识」）；6. hard（下文「也能充满欢乐」，与「辛苦」形成转折）。",
          kind="完形"),
        A("8", "1. best　2. helps　3. read　4. myself　5. friends",
          "1. 「one of the + 最高级 + 复数名词」，故 good→best；2. 主语 It 为第三人称单数，一般现在时，help→helps；"
          "3. 由 every night 与 Now 对比可知为一般过去时，read→read；4. by oneself 固定搭配，I→myself；"
          "5. friend 为可数名词，此处指一类事物，用复数 friends。",
          kind="语法"),
        A("9", "【参考范文】\nDear Peter,\n　　I am glad to hear that you will come to our school. "
                "Welcome!\n　　Our school is not very large but beautiful. There are about 40 teachers "
                "and 600 students. We have a library, a playground and several science labs. "
                "Students here are friendly and hard-working.\n　　When you arrive, I will show you "
                "around the school and introduce you to my classmates. I will also help you with "
                "Chinese if you need it. Please tell me what you are interested in, so that I can "
                "make better plans for your stay.\n　　Looking forward to seeing you.\nYours,\nLi Hua",
          "评分要点：①涵盖三个要点（欢迎、介绍学校、帮助适应）；②语言准确、连贯；③词数100左右；④格式正确（称呼、正文、落款）。",
          kind="写作"),
        A("10", "【参考范文】\nParagraph 1: But then he remembered what his father had told him. "
                 "\"Courage is not the absence of fear,\" his father had said. \"It is doing what you "
                 "must do even when you are afraid.\" Tom took a deep breath and looked up at his "
                 "classmates. He began to speak, slowly at first, and then more confidently.\n"
                 "Paragraph 2: When he finished, the classroom was silent. Then someone clapped, and "
                 "soon the whole class was applauding. Tom could hardly believe it. From that day on, "
                 "he was no longer afraid to speak in front of others. He had learned that the hardest "
                 "step is always the first one.",
          "评分要点：①两段内容合理衔接原文；②情节自然、符合逻辑；③语言丰富、句式多样；④有细节描写；⑤字数150左右。",
          kind="续写"),
    ]
    return m, p, ans

for i in range(5):
    m, p, ans = make_english(i)
    save(m, p, ans, SEEDS[i][1])
    print("✔ 高一英语", SEEDS[i][1])
