# -*- coding: utf-8 -*-
"""导出所有 HTML 资源的在线网址清单（Markdown + CSV）"""
import os, csv
from urllib.parse import quote

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://chenzhuanxin.github.io/xianning-teaching-resources"

KP = os.path.join(BASE_DIR, "交付物", "02_知识点考点HTML")
PH = os.path.join(BASE_DIR, "交付物", "03_期末真题试卷", "HTML")
PW = os.path.join(BASE_DIR, "交付物", "03_期末真题试卷", "Word_PDF")
XLS = os.path.join(BASE_DIR, "交付物", "01_教材版本总表")

GRADE_ORDER = ["一年级","二年级","三年级","四年级","五年级","六年级",
               "七年级","八年级","九年级","高一","高二","高三"]
SUBJ_ORDER = ["语文","数学","英语","道德与法治","思想政治","科学","物理","化学",
              "生物","历史","地理","音乐美术","音乐","美术","劳动","音乐（欣赏）"]

def url_of(path):
    rel = os.path.relpath(path, BASE_DIR).replace("\\", "/")
    return SITE + "/" + quote(rel)

def gk(stem):
    for i, g in enumerate(GRADE_ORDER):
        if stem.startswith(g):
            return i
    return 99

def sk(stem):
    for i, s in enumerate(SUBJ_ORDER):
        if s in stem:
            return i
    return 99

rows = []   # (学段, 年级, 学科, 类型, 显示名, 网址)

# 教材总表
if os.path.isdir(XLS):
    for f in sorted(os.listdir(XLS)):
        if f.endswith(".xlsx"):
            rows.append(("教材版本总表", "-", "-", "Excel", f, url_of(os.path.join(XLS, f))))

# 知识点
if os.path.isdir(KP):
    for f in sorted(os.listdir(KP)):
        if f.endswith(".html"):
            stem = f[:-5]
            g = next((x for x in GRADE_ORDER if stem.startswith(x)), "其他")
            if g in ("高一","高二","高三"):
                stage = "高中"
            elif g in ("七年级","八年级","九年级"):
                stage = "初中"
            else:
                stage = "小学"
            subj = next((s for s in SUBJ_ORDER if s in stem), "其他")
            rows.append((stage, g, subj, "知识点", stem, url_of(os.path.join(KP, f))))

# 试卷 HTML
if os.path.isdir(PH):
    for f in sorted(os.listdir(PH)):
        if f.endswith(".html"):
            stem = f[:-5]
            g = next((x for x in GRADE_ORDER if stem.startswith(x)), "其他")
            stage = "高中" if g in ("高一","高二","高三") else ("初中" if g in ("七年级","八年级","九年级") else "小学")
            subj = next((s for s in SUBJ_ORDER if s in stem), "其他")
            rows.append((stage, g, subj, "试卷网页", stem, url_of(os.path.join(PH, f))))

# 试卷 Word
word_set = set()
if os.path.isdir(PW):
    for f in sorted(os.listdir(PW)):
        if f.endswith(".docx"):
            stem = f[:-5]
            g = next((x for x in GRADE_ORDER if stem.startswith(x)), "其他")
            stage = "高中" if g in ("高一","高二","高三") else ("初中" if g in ("七年级","八年级","九年级") else "小学")
            subj = next((s for s in SUBJ_ORDER if s in stem), "其他")
            rows.append((stage, g, subj, "试卷Word", stem, url_of(os.path.join(PW, f))))

# 排序
rows.sort(key=lambda r: (r[3], gk(r[1]), sk(r[4]), r[4]))

# ---- 输出 CSV ----
csv_path = os.path.join(BASE_DIR, "交付物", "全部资源在线网址清单.csv")
with open(csv_path, "w", encoding="utf-8-sig", newline="") as fp:
    w = csv.writer(fp)
    w.writerow(["学段", "年级", "学科", "类型", "名称", "在线网址"])
    for r in rows:
        w.writerow(r)

# ---- 输出 Markdown ----
md_path = os.path.join(BASE_DIR, "交付物", "全部资源在线网址清单.md")
with open(md_path, "w", encoding="utf-8") as fp:
    fp.write("# 全部资源在线网址清单\n\n")
    fp.write(f"站点首页：<{SITE}/>\n\n")
    fp.write(f"共 **{len(rows)}** 个资源链接。\n\n")
    order = ["教材版本总表", "小学", "初中", "高中"]
    for st in order:
        sub = [r for r in rows if r[0] == st]
        if not sub:
            continue
        fp.write(f"\n## {st}（{len(sub)} 项）\n\n")
        for typ in ["Excel", "知识点", "试卷网页", "试卷Word"]:
            sub2 = [r for r in sub if r[3] == typ]
            if not sub2:
                continue
            fp.write(f"\n### {typ}（{len(sub2)} 项）\n\n")
            for r in sub2:
                fp.write(f"- [{r[4]}]({r[5]})\n")

print("资源总数：", len(rows))
from collections import Counter
c = Counter(r[3] for r in rows)
for k, v in c.items():
    print(f"  {k}: {v}")
print("已生成：", csv_path)
print("已生成：", md_path)
