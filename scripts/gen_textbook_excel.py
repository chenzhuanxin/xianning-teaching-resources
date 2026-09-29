# -*- coding: utf-8 -*-
"""生成《湖北省咸宁市2025-2026学年中小学教材版本总表》Excel（美观排版）"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data"))

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.formatting.rule import CellIsRule
from textbook_data import TEXTBOOKS, OFFICIAL_PLATFORMS

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "交付物", "01_教材版本总表",
                   "湖北省咸宁市2025-2026学年中小学教材版本总表.xlsx")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ---------- 配色（中国风 教育蓝金）----------
C_TITLE_BG   = "1F3864"   # 深蓝
C_HEADER_BG  = "2E5C9A"   # 主蓝
C_BAND       = "EAF1FA"   # 浅蓝条带
C_SECTION_XS = "FFF2CC"   # 小学 浅金
C_SECTION_CZ = "DEEBF7"   # 初中 浅蓝
C_BORDER     = "B4C6E7"
C_LINK       = "0563C1"

thin = Side(style="thin", color=C_BORDER)
border = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()

# ============================================================
# Sheet 1 : 教材版本总表
# ============================================================
ws = wb.active
ws.title = "教材版本总表"

HEADERS = ["学段", "年级", "学科", "上册版本", "上册版次", "下册版本", "下册版次",
           "出版社", "官方查看/下载链接", "备注"]
WIDTHS  = [7, 9, 12, 17, 11, 17, 11, 24, 44, 40]

# ---- 标题行（合并）----
ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(HEADERS))
t = ws.cell(row=1, column=1, value="湖北省咸宁市 2025—2026 学年 中小学教材版本总表（小学一年级—初中九年级）")
t.font = Font(name="微软雅黑", size=15, bold=True, color="FFFFFF")
t.fill = PatternFill("solid", fgColor=C_TITLE_BG)
t.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 34

# ---- 副标题 ----
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(HEADERS))
st = ws.cell(row=2, column=1,
             value="依据：湖北省教育厅教材选用目录 · 义务教育三科统编教材三年替换计划（2024秋→2026秋全覆盖） · 国家中小学智慧教育平台")
st.font = Font(name="微软雅黑", size=9, italic=True, color="44546A")
st.fill = PatternFill("solid", fgColor="F2F6FC")
st.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[2].height = 22

# ---- 表头 ----
HDR_ROW = 3
for c, (h, w) in enumerate(zip(HEADERS, WIDTHS), start=1):
    cell = ws.cell(row=HDR_ROW, column=c, value=h)
    cell.font = Font(name="微软雅黑", size=10.5, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=C_HEADER_BG)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = border
    ws.column_dimensions[get_column_letter(c)].width = w
ws.row_dimensions[HDR_ROW].height = 26

# ---- 数据行 ----
r = HDR_ROW + 1
for row_i, (grade, subj, v1, e1, v2, e2, pub, link, note) in enumerate(TEXTBOOKS):
    seg = "小学" if grade in ("一年级","二年级","三年级","四年级","五年级","六年级") else "初中"
    vals = [seg, grade, subj, v1, e1, v2, e2, pub, link, note]
    for c, v in enumerate(vals, start=1):
        cell = ws.cell(row=r, column=c, value=v)
        cell.font = Font(name="微软雅黑", size=9.5, color="1F1F1F")
        cell.alignment = Alignment(horizontal="center" if c in (1,2,3,5,7) else "left",
                                   vertical="center", wrap_text=True)
        cell.border = border
        # 斑马纹按学段着色
        if seg == "小学":
            cell.fill = PatternFill("solid", fgColor=C_SECTION_XS if row_i % 2 == 0 else "FFFBF0")
        else:
            cell.fill = PatternFill("solid", fgColor=C_SECTION_CZ if row_i % 2 == 0 else "F4F9FE")
    # 链接列做超链接样式（去掉超链接以免过长，仅样式提示）
    lc = ws.cell(row=r, column=9)
    lc.font = Font(name="Consolas", size=8.5, color=C_LINK, underline="single")
    lc.hyperlink = link
    # 学段列加粗
    ws.cell(row=r, column=1).font = Font(name="微软雅黑", size=9.5, bold=True, color="1F3864")
    ws.cell(row=r, column=3).font = Font(name="微软雅黑", size=9.5, bold=True, color="203864")
    ws.row_dimensions[r].height = 30
    r += 1

LAST = r - 1

# ---- 页脚说明 ----
r += 1
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(HEADERS))
f = ws.cell(row=r, column=1,
            value="说明：① 咸宁市小学语文/数学/道德与法治、初中语文/数学/历史/道德与法治/生物/地理/化学均为人教版（统编版）；"
                  "初中英语为仁爱版（科普版）；初中物理为北师大版（部分区县人教版）；小学科学为人教·鄂教版。"
                  "② 「版次」反映新教材替换进度，部分年级2026秋起完成统编替换。"
                  "③ 官方电子教材均可通过国家中小学智慧教育平台或湖北省数字教材平台免费浏览/下载。")
f.font = Font(name="微软雅黑", size=8.5, color="595959")
f.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
f.fill = PatternFill("solid", fgColor="F7F9FC")
ws.row_dimensions[r].height = 46

# 冻结窗格 + 筛选
ws.freeze_panes = "A4"
ws.auto_filter.ref = f"A{HDR_ROW}:J{LAST}"

# ============================================================
# Sheet 2 : 官方平台导航
# ============================================================
ws2 = wb.create_sheet("官方平台与链接")
H2 = ["平台名称", "提供内容", "官方网址", "使用说明", "权威性"]
W2 = [26, 34, 34, 50, 20]

ws2.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(H2))
t2 = ws2.cell(row=1, column=1, value="官方电子教材 / 资源平台导航（可直接查询、在线查看、下载）")
t2.font = Font(name="微软雅黑", size=14, bold=True, color="FFFFFF")
t2.fill = PatternFill("solid", fgColor=C_TITLE_BG)
t2.alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[1].height = 32

for c, (h, w) in enumerate(zip(H2, W2), start=1):
    cell = ws2.cell(row=2, column=c, value=h)
    cell.font = Font(name="微软雅黑", size=10.5, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=C_HEADER_BG)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = border
    ws2.column_dimensions[get_column_letter(c)].width = w
ws2.row_dimensions[2].height = 24

r2 = 3
for i, (name, content, url, usage, auth) in enumerate(OFFICIAL_PLATFORMS):
    for c, v in enumerate([name, content, url, usage, auth], start=1):
        cell = ws2.cell(row=r2, column=c, value=v)
        cell.font = Font(name="微软雅黑", size=9.5, color="1F1F1F")
        cell.alignment = Alignment(horizontal="center" if c == 5 else "left",
                                   vertical="center", wrap_text=True)
        cell.border = border
        cell.fill = PatternFill("solid", fgColor=C_BAND if i % 2 == 0 else "FFFFFF")
    uc = ws2.cell(row=r2, column=3)
    uc.font = Font(name="Consolas", size=9, color=C_LINK, underline="single")
    uc.hyperlink = url
    ws2.row_dimensions[r2].height = 34
    r2 += 1
ws2.freeze_panes = "A3"

wb.save(OUT)
print("已生成：", OUT)
print("总表行数：", len(TEXTBOOKS))
