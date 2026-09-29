# -*- coding: utf-8 -*-
"""生成「全部资源在线网址一览」页面 links.html（可直接点击打开）"""
import os
from urllib.parse import quote

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://chenzhuanxin.github.io/xianning-teaching-resources"
KP = os.path.join(BASE_DIR, "交付物", "02_知识点考点HTML")
PH = os.path.join(BASE_DIR, "交付物", "03_期末真题试卷", "HTML")
PW = os.path.join(BASE_DIR, "交付物", "03_期末真题试卷", "Word_PDF")
XLS = os.path.join(BASE_DIR, "交付物", "01_教材版本总表")

def uri(path):
    rel = os.path.relpath(path, BASE_DIR).replace("\\", "/")
    return quote(rel)

G = ["一年级","二年级","三年级","四年级","五年级","六年级","七年级","八年级","九年级","高一","高二","高三"]

def grade_of(stem):
    for g in G:
        if stem.startswith(g):
            return g
    return "其他"

def stage_of(g):
    if g in ("高一","高二","高三"):
        return "高中"
    if g in ("七年级","八年级","九年级"):
        return "初中"
    return "小学"

# 收集
data = {}   # stage -> grade -> subject -> [(type, name, url)]
def add(path, typ):
    rel = uri(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    if typ == "Excel":
        data.setdefault("总表", {}).setdefault("-", {}).setdefault("-", []).append((typ, stem, rel))
        return
    g = grade_of(stem)
    st = stage_of(g)
    subj = stem.split("_")[1] if "_" in stem and typ == "知识点" else stem.split("_")[0]
    if typ == "知识点":
        # 形如 高三_语文_知识点考点 => 学科在第二段
        parts = stem.split("_")
        subj = parts[1] if len(parts) > 1 else stem
    data.setdefault(st, {}).setdefault(g, {}).setdefault(subj, []).append((typ, stem, rel))

if os.path.isdir(XLS):
    for f in sorted(os.listdir(XLS)):
        if f.endswith(".xlsx"):
            add(os.path.join(XLS, f), "Excel")
for f in sorted(os.listdir(KP)):
    if f.endswith(".html"):
        add(os.path.join(KP, f), "知识点")
for f in sorted(os.listdir(PH)):
    if f.endswith(".html"):
        add(os.path.join(PH, f), "试卷网页")
for f in sorted(os.listdir(PW)):
    if f.endswith(".docx"):
        add(os.path.join(PW, f), "试卷Word")

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

sections = []
n_total = 0

# 总表区
if "总表" in data:
    items = ""
    for typ, stem, rel in data["总表"]["-"]["-"]:
        n_total += 1
        items += f'<li><span class="tag xls">Excel</span><a href="{rel}" target="_blank">{esc(stem)}</a></li>'
    sections.append(f'''
    <section class="block">
      <h2 class="stage">教材版本总表</h2>
      <ul class="links">{items}</ul>
    </section>''')

for stage in ["小学", "初中", "高中"]:
    if stage not in data:
        continue
    inner = ""
    for g in G:
        if g not in data.get(stage, {}):
            continue
        subs = data[stage][g]
        n_g = sum(len(v) for v in subs.values())
        inner += f'<div class="grade"><div class="ghead"><h3>{g}</h3><span>{n_g} 个链接</span></div>'
        for subj in sorted(subs.keys()):
            group = {}
            for typ, stem, rel in subs[subj]:
                group.setdefault(typ, []).append((stem, rel))
            inner += f'<div class="subj"><div class="sname">{esc(subj)}</div><ul class="links">'
            for typ in ["知识点", "试卷网页", "试卷Word"]:
                for stem, rel in group.get(typ, []):
                    n_total += 1
                    if typ == "知识点":
                        cls, lab = "kp", "知识点"
                        short = stem
                    elif typ == "试卷网页":
                        cls, lab = "ph", "网页版"
                        parts = stem.split("_")
                        short = f"{parts[0]} · {parts[-1]}"
                    else:
                        cls, lab = "wd", "Word"
                        parts = stem.split("_")
                        short = f"{parts[0]} · {parts[-1]}"
                    inner += (f'<li><span class="tag {cls}">{lab}</span>'
                              f'<a href="{rel}" target="_blank">{esc(short)}</a></li>')
            inner += "</ul></div>"
        inner += "</div>"
    sections.append(f'''
    <section class="block">
      <h2 class="stage">{stage}</h2>
      {inner}
    </section>''')

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全部资源在线网址一览 · 湖北省咸宁市教学资源库</title>
<style>
  :root {{
    --blue:#1a4b8c; --blue-lt:#2f6fb8; --gold:#c9a227;
    --bg:#f5f7fb; --card:#fff; --line:#e2e8f2; --txt:#1f2d3d; --txt2:#5a6b7f;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--txt);
    font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif; line-height:1.7; }}
  header {{ background:linear-gradient(135deg,#14406f 0%,var(--blue) 55%,#2f6fb8 100%);
    color:#fff; padding:36px 24px 30px; text-align:center; border-bottom:4px solid var(--gold); }}
  header h1 {{ margin:0 0 8px; font-size:26px; }}
  header p {{ margin:0; opacity:.9; font-size:14px; }}
  header a {{ color:#ffd75e; }}
  .wrap {{ max-width:1180px; margin:0 auto; padding:26px 20px 60px; }}
  .tip {{ background:#fff; border-left:5px solid var(--gold); border-radius:8px;
    padding:14px 20px; margin-bottom:24px; font-size:14px; color:var(--txt2);
    box-shadow:0 1px 4px rgba(26,75,140,.07); }}
  .tip b {{ color:var(--blue); }}
  .block {{ margin-bottom:34px; }}
  h2.stage {{ font-size:19px; color:var(--blue); margin:0 0 14px;
    padding-bottom:10px; border-bottom:2px solid var(--line); }}
  h2.stage::before {{ content:""; display:inline-block; width:5px; height:19px;
    background:var(--gold); margin-right:10px; vertical-align:-3px; border-radius:2px; }}
  .grade {{ background:var(--card); border:1px solid var(--line); border-radius:12px;
    margin-bottom:16px; box-shadow:0 2px 8px rgba(26,75,140,.06); overflow:hidden; }}
  .ghead {{ display:flex; justify-content:space-between; align-items:center;
    padding:12px 20px; background:linear-gradient(90deg,#eef4fc,#f8fbff);
    border-bottom:1px solid var(--line); }}
  .ghead h3 {{ margin:0; font-size:17px; color:var(--blue); }}
  .ghead span {{ background:#e8f0fb; color:var(--blue); font-size:12px;
    padding:3px 11px; border-radius:20px; }}
  .subj {{ padding:12px 20px 4px; border-bottom:1px dashed var(--line); }}
  .subj:last-child {{ border-bottom:none; }}
  .sname {{ font-size:13.5px; font-weight:600; color:var(--blue-lt); margin-bottom:7px; }}
  ul.links {{ list-style:none; margin:0; padding:0 0 10px;
    display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:5px 16px; }}
  ul.links li {{ display:flex; align-items:center; gap:7px; font-size:13px;
    min-width:0; }}
  ul.links a {{ color:var(--txt); text-decoration:none; padding:3px 8px;
    border-radius:5px; border:1px solid transparent; transition:.15s;
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap; flex:1; }}
  ul.links a:hover {{ background:#eef4fc; border-color:#d5e3f5; color:var(--blue); }}
  .tag {{ font-size:10.5px; padding:1px 6px; border-radius:3px; font-weight:600;
    white-space:nowrap; flex-shrink:0; }}
  .tag.kp {{ background:#e6f4ea; color:#26794a; }}
  .tag.ph {{ background:#e8f0fb; color:var(--blue); }}
  .tag.wd {{ background:#fdf0e3; color:#a05a12; }}
  .tag.xls {{ background:#ede7f6; color:#5e35b1; }}
  footer {{ text-align:center; color:var(--txt2); font-size:13px; padding:24px 20px 40px; }}
  footer a {{ color:var(--blue-lt); }}
  @media (max-width:640px) {{ ul.links {{ grid-template-columns:1fr; }} header h1 {{ font-size:20px; }} }}
</style>
</head>
<body>
<header>
  <h1>全部资源在线网址一览</h1>
  <p>共 <b>{n_total}</b> 个可直接打开的网页链接 · 点击即在新标签页中显示网页内容</p>
  <p style="margin-top:8px;font-size:13px">站点首页：<a href="index.html">index.html</a> ·
    仓库：<a href="{SITE}" target="_blank">{SITE}</a></p>
</header>
<div class="wrap">
  <div class="tip">
    <b>使用说明</b>　本页列出所有资源的在线网址。<b>知识点</b>与<b>试卷网页版</b>为 HTML，
    点击直接在浏览器中显示网页内容；<b>Word</b> 文件点击后浏览器会下载，可用 Word/WPS 打开编辑。
    如某个链接打不开，请稍等 1–2 分钟（GitHub Pages 首次构建需要一点时间）。
  </div>
  {''.join(sections)}
</div>
<footer>
  湖北省咸宁市中小学教学资源库 ·
  <a href="{SITE}" target="_blank">GitHub 仓库</a> ·
  <a href="index.html">返回导航首页</a>
</footer>
</body>
</html>'''

out = os.path.join(BASE_DIR, "交付物", "全部资源在线网址一览.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("已生成：", out)
print("链接总数：", n_total)
