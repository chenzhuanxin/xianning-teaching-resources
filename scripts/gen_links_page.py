# -*- coding: utf-8 -*-
"""生成「全部资源在线网址一览.html」

数据源：交付物/全部资源在线网址清单.csv
规则：只保留网页类资源（知识点 HTML、试卷 HTML），排除 Word 与 Excel。
链接直接使用 CSV 中的「在线网址」列（已 urlencode）。
"""
import csv
import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "交付物", "全部资源在线网址清单.csv")
SITE = "https://chenzhuanxin.github.io/xianning-teaching-resources"

GRADES = ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级",
          "七年级", "八年级", "九年级", "高一", "高二", "高三"]
STAGES = [("小学（1–6 年级）", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"]),
          ("初中（7–9 年级）", ["七年级", "八年级", "九年级"]),
          ("高中（高一–高三）", ["高一", "高二", "高三"])]
SUBJECT_ORDER = ["语文", "数学", "英语", "物理", "化学", "生物",
                 "思想政治", "道德与法治", "历史", "地理", "科学", "音乐美术"]

# 只保留网页类型（排除 Word / Excel）
KEEP_TYPES = {"知识点", "试卷网页"}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------- 读取 CSV ----------
rows = []
with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if r.get("类型", "").strip() in KEEP_TYPES:
            rows.append(r)

# ---------- 组织数据：stage -> grade -> subject -> [ (kind, name, url) ] ----------
tree = OrderedDict()
for r in rows:
    stage, grade, subject = r["学段"].strip(), r["年级"].strip(), r["学科"].strip()
    typ = r["类型"].strip()
    name = r["名称"].strip()
    url = r["在线网址"].strip()
    kind = "kp" if typ == "知识点" else "ph"
    tree.setdefault(stage, OrderedDict()).setdefault(grade, OrderedDict()) \
        .setdefault(subject, []).append((kind, name, url))


def subj_key(s):
    return (SUBJECT_ORDER.index(s) if s in SUBJECT_ORDER else 99, s)


def display_name(kind, name, subject):
    """知识点显示为「学科 · 知识点考点」；试卷显示为「学科年级 · 卷别」"""
    if kind == "kp":
        return f"{subject} · 知识点与考点"
    parts = name.split("_")
    if len(parts) >= 2:
        return f"{parts[0]} · {parts[-1]}"
    return name


# ---------- 渲染 ----------
sections = []
n_total = 0

for stage_title, grades in STAGES:
    inner = ""
    for g in grades:
        subs = tree.get(stage_title.split("（")[0], {}).get(g)
        if not subs:
            continue
        n_g = sum(len(v) for v in subs.values())
        n_total += n_g
        inner += (f'<div class="grade"><div class="ghead"><h3>{esc(g)}</h3>'
                  f'<span>{n_g} 个网页</span></div>')
        for subj in sorted(subs.keys(), key=subj_key):
            items = subs[subj]
            n_kp = sum(1 for k, _, _ in items if k == "kp")
            inner += (f'<div class="subj"><div class="sname">{esc(subj)}'
                      f'<em>{len(items)} 个</em></div><ul class="links">')
            for kind, name, url in items:
                label = "知识点" if kind == "kp" else "试卷"
                inner += (f'<li><span class="tag {kind}">{label}</span>'
                          f'<a href="{esc(url)}" target="_blank" rel="noopener">'
                          f'{esc(display_name(kind, name, subj))}</a></li>')
            inner += "</ul></div>"
        inner += "</div>"
    if inner:
        sections.append(f'''
    <section class="block">
      <h2 class="stage">{esc(stage_title)}</h2>
      {inner}
    </section>''')

n_grades = sum(1 for _, gs in tree.items() for g in gs)
n_subjects = len({s for _, gs in tree.items() for g in gs.values() for s in gs})

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>网页资源总览 | 湖北省咸宁市中小学教学资源库</title>
<meta name="description" content="湖北省咸宁市中小学12个年级全学科知识点与期末试卷网页在线总览，点击即可打开。">
<style>
  :root {{
    --blue:#1a4b8c; --blue-lt:#2f6fb8; --gold:#c9a227; --gold-lt:#f0d97a;
    --bg:#f5f7fb; --card:#fff; --line:#e2e8f2; --txt:#1f2d3d; --txt2:#5a6b7f;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--txt);
    font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif; line-height:1.7; }}

  /* ---------- 头部 ---------- */
  header {{ position:relative; overflow:hidden;
    background:linear-gradient(135deg,#0f3357 0%,#14406f 40%,var(--blue) 72%,#2f6fb8 100%);
    color:#fff; padding:52px 24px 46px; text-align:center; border-bottom:4px solid var(--gold); }}
  header::after {{ content:""; position:absolute; right:-90px; top:-90px;
    width:300px; height:300px; border-radius:50%;
    background:radial-gradient(circle,rgba(201,162,39,.30),transparent 68%); }}
  header::before {{ content:""; position:absolute; left:-70px; bottom:-140px;
    width:260px; height:260px; border-radius:50%;
    background:radial-gradient(circle,rgba(255,255,255,.12),transparent 70%); }}
  header .inner {{ position:relative; z-index:1; max-width:900px; margin:0 auto; }}
  header .kicker {{ display:inline-block; font-size:12.5px; letter-spacing:3px;
    color:var(--gold-lt); border:1px solid rgba(240,217,122,.45); border-radius:20px;
    padding:4px 16px; margin-bottom:18px; }}
  header h1 {{ margin:0 0 14px; font-size:34px; letter-spacing:1px;
    text-shadow:0 2px 12px rgba(0,0,0,.22); }}
  header h1 span {{ color:var(--gold-lt); }}
  header .desc {{ margin:0 auto; max-width:760px; font-size:15px; line-height:1.9;
    color:rgba(255,255,255,.92); text-align:left; text-indent:2em; }}
  header .meta {{ margin-top:22px; display:flex; flex-wrap:wrap;
    justify-content:center; gap:10px 14px; font-size:13px; }}
  header .meta i {{ font-style:normal; background:rgba(255,255,255,.14);
    border:1px solid rgba(255,255,255,.22); border-radius:18px; padding:4px 14px;
    backdrop-filter:blur(2px); }}
  header .meta i b {{ color:var(--gold-lt); font-size:15px; }}
  header .entry {{ margin-top:22px; font-size:13.5px; }}
  header .entry a {{ color:var(--gold-lt); text-decoration:none;
    border-bottom:1px dashed rgba(240,217,122,.6); }}

  /* ---------- 主体 ---------- */
  .wrap {{ max-width:1180px; margin:0 auto; padding:28px 20px 60px; }}
  .tip {{ background:#fff; border-left:5px solid var(--gold); border-radius:8px;
    padding:16px 22px; margin-bottom:26px; font-size:14px; color:var(--txt2);
    box-shadow:0 1px 4px rgba(26,75,140,.07); }}
  .tip b {{ color:var(--blue); }}
  .tip .legend {{ margin-top:9px; display:flex; flex-wrap:wrap; gap:8px 18px; }}
  .tip .legend span {{ display:flex; align-items:center; gap:6px; }}

  .block {{ margin-bottom:36px; }}
  h2.stage {{ font-size:20px; color:var(--blue); margin:0 0 16px;
    padding-bottom:10px; border-bottom:2px solid var(--line); }}
  h2.stage::before {{ content:""; display:inline-block; width:5px; height:20px;
    background:var(--gold); margin-right:10px; vertical-align:-3px; border-radius:2px; }}
  h2.stage em {{ font-style:normal; font-size:13px; color:var(--txt2); margin-left:10px; }}

  .grade {{ background:var(--card); border:1px solid var(--line); border-radius:12px;
    margin-bottom:16px; box-shadow:0 2px 8px rgba(26,75,140,.06); overflow:hidden; }}
  .ghead {{ display:flex; justify-content:space-between; align-items:center;
    padding:12px 20px; background:linear-gradient(90deg,#eef4fc,#f8fbff);
    border-bottom:1px solid var(--line); }}
  .ghead h3 {{ margin:0; font-size:17px; color:var(--blue); }}
  .ghead span {{ background:#e8f0fb; color:var(--blue); font-size:12px;
    padding:3px 11px; border-radius:20px; }}

  .subj {{ padding:13px 20px 5px; border-bottom:1px dashed var(--line); }}
  .subj:last-child {{ border-bottom:none; }}
  .sname {{ font-size:13.5px; font-weight:600; color:var(--blue-lt); margin-bottom:8px; }}
  .sname em {{ font-style:normal; font-weight:400; font-size:11.5px;
    color:var(--txt2); margin-left:6px; }}
  ul.links {{ list-style:none; margin:0; padding:0 0 10px;
    display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:5px 16px; }}
  ul.links li {{ display:flex; align-items:center; gap:7px; font-size:13px; min-width:0; }}
  ul.links a {{ color:var(--txt); text-decoration:none; padding:3px 8px;
    border-radius:5px; border:1px solid transparent; transition:.15s;
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap; flex:1; }}
  ul.links a:hover {{ background:#eef4fc; border-color:#d5e3f5; color:var(--blue); }}
  .tag {{ font-size:10.5px; padding:1px 6px; border-radius:3px; font-weight:600;
    white-space:nowrap; flex-shrink:0; }}
  .tag.kp {{ background:#e6f4ea; color:#26794a; }}
  .tag.ph {{ background:#e8f0fb; color:var(--blue); }}

  footer {{ text-align:center; color:var(--txt2); font-size:13px;
    padding:26px 20px 44px; border-top:1px solid var(--line); }}
  footer a {{ color:var(--blue-lt); }}
  @media (max-width:640px) {{
    ul.links {{ grid-template-columns:1fr; }}
    header {{ padding:38px 18px 34px; }}
    header h1 {{ font-size:23px; }}
    header .desc {{ font-size:14px; }}
  }}
</style>
</head>
<body>
<header>
  <div class="inner">
    <div class="kicker">湖北省咸宁市 · 中小学教学资源库</div>
    <h1>全学科网页资源<span>在线总览</span></h1>
    <p class="desc">本页汇总了湖北省咸宁市小学一年级至高中三年级共 12 个年级、11 个学科的
      <b>知识点与考点讲解</b>和<b>期末真题试卷</b>网页。每一条链接都是一个独立的在线网址，
      点击后无需下载，浏览器会直接打开并显示网页内容，方便教师备课、学生自学与家长辅导使用。</p>
    <div class="meta">
      <i>覆盖年级 <b>{n_grades}</b> 个</i>
      <i>涵盖学科 <b>{n_subjects}</b> 个</i>
      <i>网页资源 <b>{n_total}</b> 份</i>
      <i>全部免费在线打开</i>
    </div>
    <p class="entry">站点首页：<a href="index.html">index.html</a>　·　
      仓库地址：<a href="{SITE}" target="_blank" rel="noopener">{SITE}</a></p>
  </div>
</header>
<div class="wrap">
  <div class="tip">
    <b>使用说明</b>　本页仅收录<b>网页（HTML）</b>资源，点击任意链接即可在新标签页中直接查看内容。
    <div class="legend">
      <span><span class="tag kp">知识点</span>学科知识点与考点梳理</span>
      <span><span class="tag ph">试卷</span>期末真题试卷（含答案）</span>
    </div>
    <div style="margin-top:8px">如需 Word 或 Excel 版本，请查看《全部资源在线网址清单》；
      若个别链接暂时打不开，请稍等 1–2 分钟，GitHub Pages 正在构建。</div>
  </div>
  {''.join(sections)}
</div>
<footer>
  湖北省咸宁市中小学教学资源库 ·
  <a href="{SITE}" target="_blank" rel="noopener">GitHub 仓库</a> ·
  <a href="index.html">返回导航首页</a>
</footer>
</body>
</html>'''

out = os.path.join(BASE_DIR, "交付物", "全部资源在线网址一览.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("已生成：", out)
print(f"年级数：{n_grades}　学科数：{n_subjects}　网页链接总数：{n_total}")
