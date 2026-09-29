# -*- coding: utf-8 -*-
"""生成 GitHub Pages 总导航页 index.html"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KP_DIR = os.path.join(BASE, "交付物", "02_知识点考点HTML")
PH_DIR = os.path.join(BASE, "交付物", "03_期末真题试卷", "HTML")
PW_DIR = os.path.join(BASE, "交付物", "03_期末真题试卷", "Word_PDF")

GRADES = ["一年级", "二年级", "三年级", "四年级", "五年级",
          "六年级", "七年级", "八年级", "九年级",
          "高一", "高二", "高三"]

# 各年级学科顺序
SUBJECT_ORDER = {
    "一年级": ["语文", "数学", "道德与法治", "科学", "音乐美术"],
    "二年级": ["语文", "数学", "道德与法治", "科学", "音乐美术"],
    "三年级": ["语文", "数学", "英语", "道德与法治", "科学"],
    "四年级": ["语文", "数学", "英语", "道德与法治", "科学"],
    "五年级": ["语文", "数学", "英语", "道德与法治", "科学"],
    "六年级": ["语文", "数学", "英语", "道德与法治", "科学"],
    "七年级": ["语文", "数学", "英语", "道德与法治", "历史", "地理", "生物"],
    "八年级": ["语文", "数学", "英语", "道德与法治", "历史", "地理", "生物", "物理"],
    "九年级": ["语文", "数学", "英语", "道德与法治", "历史", "物理", "化学"],
    "高一": ["语文", "数学", "英语", "物理", "化学", "生物",
             "思想政治", "历史", "地理"],
    "高二": ["语文", "数学", "英语", "物理", "化学", "生物",
             "思想政治", "历史", "地理"],
    "高三": ["语文", "数学", "英语", "物理", "化学", "生物",
             "思想政治", "历史", "地理"],
}

# 学段分组（用于分区展示）
STAGES = [
    ("小学（1–6 年级）", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"]),
    ("初中（7–9 年级）", ["七年级", "八年级", "九年级"]),
    ("高中（高一–高三）", ["高一", "高二", "高三"]),
]

# 试卷类型 -> 显示顺序
PAPER_LABELS = ["第一学期期末质量检测", "第二学期期末教学质量监测",
                "上学期期末学业水平测试", "下学期期末综合检测",
                "期末复习质量检测", "期末学业质量监测",
                "第一学期期末学业质量综合评价", "第二学期期末学业水平测试",
                "期末综合能力提升测试", "第二学期中考模拟测试",
                "第一学期期末教学质量监测", "第二学期期末质量检测",
                "第二学期期末综合能力测试", "学年度期末学业水平测试",
                "中考", "综合能力"]


def uri(path):
    """相对仓库根的 URL 路径（POSIX 风格 + URL 编码）"""
    rel = os.path.relpath(path, BASE).replace("\\", "/")
    from urllib.parse import quote
    return quote(rel)


def scan_kp():
    out = {}
    if not os.path.isdir(KP_DIR):
        return out
    for f in os.listdir(KP_DIR):
        if not f.endswith(".html"):
            continue
        stem = f[:-5]
        parts = stem.split("_")
        if len(parts) < 2:
            continue
        grade, subject = parts[0], parts[1]
        out.setdefault(grade, {}).setdefault(subject, []).append(
            (stem, os.path.join(KP_DIR, f)))
    return out


def scan_papers():
    html = {}
    word = {}
    if os.path.isdir(PH_DIR):
        for f in os.listdir(PH_DIR):
            if not f.endswith(".html"):
                continue
            stem = f[:-5]
            parts = stem.split("_")
            if len(parts) < 2:
                continue
            html.setdefault(parts[0], {}).setdefault(parts[1], []).append(
                (stem, os.path.join(PH_DIR, f)))
    if os.path.isdir(PW_DIR):
        for f in os.listdir(PW_DIR):
            if not f.endswith(".docx"):
                continue
            stem = f[:-5]
            parts = stem.split("_")
            if len(parts) < 2:
                continue
            word.setdefault(parts[0], {}).setdefault(parts[1], []).append(
                (stem, os.path.join(PW_DIR, f)))
    return html, word


def paper_sort_key(stem):
    for i, lab in enumerate(PAPER_LABELS):
        if lab in stem:
            return i
    return len(PAPER_LABELS)


def build():
    kp = scan_kp()
    ph, pw = scan_papers()

    total_kp = sum(len(v) for g in kp.values() for v in g.values())
    total_ph = sum(len(v) for g in ph.values() for v in g.values())

    def make_card(grade):
        subjects = SUBJECT_ORDER.get(grade, [])
        # ---- 知识点 ----
        kp_items = ""
        for subj in subjects:
            for stem, path in sorted(kp.get(grade, {}).get(subj, [])):
                kp_items += (f'<li><a href="{uri(path)}" target="_blank">'
                             f'<span class="tag kp">知识点</span>{subj}</a></li>')
        # ---- 试卷 ----
        ph_items = ""
        for subj in subjects:
            papers = sorted(ph.get(grade, {}).get(subj, []), key=lambda x: paper_sort_key(x[0]))
            if not papers:
                continue
            ph_items += f'<div class="subj-block"><div class="subj-name">{subj}</div><ul class="papers">'
            for stem, path in papers:
                # 卷别：取最后一段
                label = stem.split("_")[-1]
                ph_items += (f'<li><a href="{uri(path)}" target="_blank">'
                             f'<span class="tag ph">{label}</span>网页版</a>')
                # 对应 Word
                wpath = None
                for wstem, wp in pw.get(grade, {}).get(subj, []):
                    if wstem == stem:
                        wpath = wp
                        break
                if wpath:
                    ph_items += (f'<a class="dl" href="{uri(wpath)}" download>'
                                 f'<span class="tag wd">Word</span>下载</a>')
                ph_items += "</li>"
            ph_items += "</ul></div>"

        n_kp = sum(len(v) for v in kp.get(grade, {}).values())
        n_ph = sum(len(v) for v in ph.get(grade, {}).values())

        return f"""
    <section class="grade-card">
      <div class="grade-head">
        <h2>{grade}</h2>
        <div class="counts"><span>{n_kp} 份知识点</span><span>{n_ph} 套试卷</span></div>
      </div>
      <div class="grade-body">
        <div class="col">
          <h3>知识点 / 考点讲解</h3>
          <ul class="kp-list">{kp_items or '<li class="empty">暂无</li>'}</ul>
        </div>
        <div class="col">
          <h3>期末真题试卷</h3>
          <div class="paper-wrap">{ph_items or '<div class="empty">暂无</div>'}</div>
        </div>
      </div>
    </section>"""

    # 按学段分组
    stage_blocks = []
    for stage_name, gs in STAGES:
        n_kp = sum(len(v) for g in gs for v in kp.get(g, {}).values())
        n_ph = sum(len(v) for g in gs for v in ph.get(g, {}).values())
        stage_blocks.append(
            f'<div class="stage-title"><h2>{stage_name}</h2>'
            f'<div class="stage-counts"><span>{n_kp} 份知识点</span>'
            f'<span>{n_ph} 套试卷</span></div></div>')
        stage_blocks.extend(make_card(g) for g in gs)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>湖北省咸宁市中小学教学资源库（小学—高中）</title>
<style>
  :root {{
    --blue: #1a4b8c; --blue-lt: #2f6fb8; --gold: #c9a227;
    --bg: #f5f7fb; --card: #ffffff; --line: #e2e8f2;
    --txt: #1f2d3d; --txt2: #5a6b7f;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 0; background: var(--bg); color: var(--txt);
    font-family: "Microsoft YaHei", "PingFang SC", "Hiragino Sans GB", sans-serif;
    line-height: 1.7;
  }}
  header {{
    background: linear-gradient(135deg, #14406f 0%, var(--blue) 55%, #2f6fb8 100%);
    color: #fff; padding: 44px 28px 38px; text-align: center;
    border-bottom: 4px solid var(--gold);
  }}
  header h1 {{ margin: 0 0 10px; font-size: 30px; letter-spacing: 1px; }}
  header p {{ margin: 0; opacity: .9; font-size: 15px; }}
  .stats {{
    display: flex; justify-content: center; gap: 44px; margin-top: 26px; flex-wrap: wrap;
  }}
  .stats div {{ text-align: center; }}
  .stats b {{ display: block; font-size: 30px; color: #ffd75e; line-height: 1.2; }}
  .stats span {{ font-size: 13px; opacity: .85; }}
  .wrap {{ max-width: 1180px; margin: 0 auto; padding: 30px 20px 60px; }}
  .version-note {{
    background: #fff; border-left: 5px solid var(--gold); border-radius: 8px;
    padding: 16px 22px; margin-bottom: 28px; font-size: 14px; color: var(--txt2);
    box-shadow: 0 1px 4px rgba(26,75,140,.07);
  }}
  .version-note b {{ color: var(--blue); }}
  .grade-card {{
    background: var(--card); border-radius: 12px; margin-bottom: 22px;
    box-shadow: 0 2px 10px rgba(26,75,140,.08); overflow: hidden;
    border: 1px solid var(--line);
  }}
  .grade-head {{
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 22px; background: linear-gradient(90deg, #eef4fc, #f8fbff);
    border-bottom: 1px solid var(--line); flex-wrap: wrap; gap: 10px;
  }}
  .grade-head h2 {{ margin: 0; font-size: 20px; color: var(--blue); letter-spacing: .5px; }}
  .grade-head h2::before {{
    content: ""; display: inline-block; width: 4px; height: 18px;
    background: var(--gold); margin-right: 10px; vertical-align: -2px; border-radius: 2px;
  }}
  .counts {{ display: flex; gap: 10px; }}
  .counts span {{
    background: #e8f0fb; color: var(--blue); font-size: 12.5px;
    padding: 3px 12px; border-radius: 20px;
  }}
  .grade-body {{ display: grid; grid-template-columns: 1fr 1.35fr; gap: 0; }}
  .col {{ padding: 18px 22px 22px; }}
  .col + .col {{ border-left: 1px dashed var(--line); }}
  .col h3 {{
    margin: 0 0 12px; font-size: 14px; color: var(--txt2);
    font-weight: 600; letter-spacing: .5px;
  }}
  ul.kp-list {{ list-style: none; margin: 0; padding: 0; }}
  ul.kp-list li {{ margin-bottom: 7px; }}
  ul.kp-list a {{
    display: flex; align-items: center; gap: 8px; text-decoration: none;
    color: var(--txt); font-size: 14px; padding: 7px 10px; border-radius: 6px;
    transition: .16s;
  }}
  ul.kp-list a:hover {{ background: #eef4fc; color: var(--blue); }}
  .tag {{
    font-size: 11px; padding: 1px 7px; border-radius: 3px;
    font-weight: 600; white-space: nowrap;
  }}
  .tag.kp {{ background: #e6f4ea; color: #26794a; }}
  .tag.ph {{ background: #e8f0fb; color: var(--blue); }}
  .tag.wd {{ background: #fdf0e3; color: #a05a12; }}
  .paper-wrap {{ display: flex; flex-direction: column; gap: 12px; }}
  .subj-block {{ border-left: 3px solid #dde7f5; padding-left: 12px; }}
  .subj-name {{
    font-size: 13.5px; font-weight: 600; color: var(--blue); margin-bottom: 5px;
  }}
  ul.papers {{ list-style: none; margin: 0; padding: 0; }}
  ul.papers li {{
    display: flex; align-items: center; gap: 6px; flex-wrap: wrap;
    font-size: 13px; margin-bottom: 4px;
  }}
  ul.papers a {{
    text-decoration: none; color: var(--txt); display: inline-flex;
    align-items: center; gap: 5px; padding: 3px 9px; border-radius: 5px;
    border: 1px solid transparent; transition: .16s;
  }}
  ul.papers a:hover {{ background: #eef4fc; border-color: #d5e3f5; color: var(--blue); }}
  ul.papers a.dl {{ color: var(--txt2); }}
  ul.papers a.dl:hover {{ background: #fdf6ec; border-color: #f0dcc0; color: #a05a12; }}
  .empty {{ color: #9aa8b8; font-size: 13px; }}
  .stage-title {{
    display: flex; align-items: center; justify-content: space-between;
    margin: 34px 0 16px; padding: 0 4px 10px; flex-wrap: wrap; gap: 10px;
    border-bottom: 2px solid var(--line);
  }}
  .stage-title:first-child {{ margin-top: 8px; }}
  .stage-title h2 {{
    margin: 0; font-size: 18px; color: var(--blue); letter-spacing: 1px;
  }}
  .stage-title h2::before {{
    content: ""; display: inline-block; width: 5px; height: 20px;
    background: var(--blue); margin-right: 10px; vertical-align: -4px;
    border-radius: 2px;
  }}
  .stage-counts {{ display: flex; gap: 10px; }}
  .stage-counts span {{
    background: #f0f4fa; color: var(--txt2); font-size: 12.5px;
    padding: 3px 12px; border-radius: 20px;
  }}
  footer {{
    text-align: center; color: var(--txt2); font-size: 13px;
    padding: 26px 20px 40px; line-height: 2;
  }}
  footer a {{ color: var(--blue-lt); }}
  @media (max-width: 820px) {{
    .grade-body {{ grid-template-columns: 1fr; }}
    .col + .col {{ border-left: none; border-top: 1px dashed var(--line); }}
    header h1 {{ font-size: 22px; }}
    .stats {{ gap: 24px; }}
  }}
</style>
</head>
<body>
<header>
  <h1>湖北省咸宁市中小学教学资源库</h1>
  <p>小学一年级 ~ 高中三年级 · 教材版本总表 · 知识点考点 · 期末真题试卷</p>
  <div class="stats">
    <div><b>12</b><span>年级</span></div>
    <div><b>{total_kp}</b><span>份知识点考点</span></div>
    <div><b>{total_ph}</b><span>套期末真题试卷</span></div>
    <div><b>11</b><span>门学科</span></div>
  </div>
</header>

<div class="wrap">
  <div class="version-note">
    <b>教材版本（咸宁本地）</b>　小学：语文/道法统编版、数学人教版、英语人教版PEP、科学人教·鄂教版；
    初中：语文/道法/历史统编版，数学/地理/生物/化学人教版，
    <b>英语仁爱版（科普版）</b>、<b>物理北师大版</b>；
    高中：语文/数学（人教A版）/英语/物理/化学/生物/思想政治/历史为人教·统编版，
    <b>地理为中国地图出版社版</b>。
    官方电子教材见页面底部链接。
  </div>
{''.join(stage_blocks)}
</div>

<footer>
  官方电子教材平台：
  <a href="https://basic.smartedu.cn/tchMaterial" target="_blank">国家中小学智慧教育平台</a> ·
  <a href="https://dzkb.e21.cn" target="_blank">湖北省数字教材服务平台</a> ·
  <a href="https://dzkb.pep.com.cn" target="_blank">人教数字教材</a> ·
  <a href="https://dm.bnup.com" target="_blank">北师大数字教材</a> ·
  <a href="http://www.renai.cn" target="_blank">仁爱版教材</a>
  <br>
  试卷为依据各科教材版本与课程标准编制的全真模拟卷，与咸宁所用版本严格对应。
</footer>
</body>
</html>"""

    out = os.path.join(BASE, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("已生成 index.html")
    print("  知识点条目：", total_kp)
    print("  试卷网页版：", total_ph)


if __name__ == "__main__":
    build()
