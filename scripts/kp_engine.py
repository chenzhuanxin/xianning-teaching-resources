# -*- coding: utf-8 -*-
"""
通用「知识点 / 考点」HTML 渲染引擎
所有年级、所有学科共用同一套样式，保证风格统一、排版美观。
"""
import os, html, json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "交付物", "02_知识点考点HTML")
os.makedirs(BASE, exist_ok=True)

CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:"Microsoft YaHei","PingFang SC","Hiragino Sans GB",sans-serif;
background:linear-gradient(165deg,#f5f9ff 0%,#eef4fc 42%,#fdfaf3 100%);
color:#1f2430;line-height:1.92;padding-bottom:56px;}
.wrap{max-width:1080px;margin:0 auto;padding:0 22px;}

.hero{background:linear-gradient(135deg,#1f3864 0%,#2e5c9a 55%,#4a7fc1 100%);
color:#fff;padding:44px 22px 38px;position:relative;overflow:hidden;
box-shadow:0 8px 28px rgba(31,56,100,.22);}
.hero::after{content:"";position:absolute;right:-70px;top:-70px;width:300px;height:300px;
background:radial-gradient(circle,rgba(255,255,255,.16),transparent 70%);border-radius:50%;}
.hero .wrap{position:relative;z-index:2;}
.hero .badge{display:inline-block;background:rgba(255,255,255,.18);
border:1px solid rgba(255,255,255,.42);padding:5px 15px;border-radius:20px;
font-size:13px;letter-spacing:1px;margin-bottom:14px;}
.hero h1{font-size:31px;font-weight:800;letter-spacing:1px;margin-bottom:10px;}
.hero h1 .em{color:#ffd966;}
.hero .sub{font-size:14.5px;opacity:.93;}
.hero .meta{margin-top:16px;display:flex;flex-wrap:wrap;gap:10px;}
.hero .meta span{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);
padding:4px 13px;border-radius:14px;font-size:12.5px;}

.section{background:#fff;border-radius:16px;margin-top:26px;overflow:hidden;
box-shadow:0 4px 20px rgba(31,56,100,.09);border:1px solid #e3ecf8;}
.sec-head{display:flex;align-items:center;gap:13px;padding:17px 24px;
background:linear-gradient(90deg,#eaf1fa,#f7fbff);border-bottom:2px solid #dbe8f8;}
.sec-no{width:40px;height:40px;border-radius:11px;flex:0 0 40px;
background:linear-gradient(135deg,#2e5c9a,#4a7fc1);color:#fff;display:flex;
align-items:center;justify-content:center;font-size:17px;font-weight:800;
box-shadow:0 3px 10px rgba(46,92,154,.32);}
.sec-head h2{font-size:19.5px;color:#1f3864;font-weight:800;letter-spacing:.5px;}
.sec-head .tag{margin-left:auto;font-size:12px;color:#8a6d1f;background:#fff3cd;
border:1px solid #ffe08a;padding:3px 11px;border-radius:12px;white-space:nowrap;}
.sec-body{padding:22px 26px 26px;}

.kp{margin-bottom:22px;}.kp:last-child{margin-bottom:0;}
.kp-title{font-size:16px;font-weight:800;color:#22406e;margin-bottom:11px;
padding-left:13px;border-left:5px solid #f0b429;line-height:1.5;}
.kp-title .n{display:inline-block;background:#22406e;color:#fff;font-size:12px;
padding:1px 8px;border-radius:8px;margin-right:8px;vertical-align:2px;}
.kp ul{list-style:none;padding-left:4px;}
.kp ul li{position:relative;padding-left:22px;margin-bottom:8px;font-size:14.6px;color:#333a48;}
.kp ul li::before{content:"◆";position:absolute;left:2px;top:0;color:#4a7fc1;font-size:10px;}
.kp ul li strong{color:#c0392b;font-weight:700;}
.kp ul li em{font-style:normal;background:#fff8e1;padding:1px 5px;border-radius:4px;
color:#8a6d1f;font-weight:600;}

.box{border-radius:11px;padding:13px 18px;margin:12px 0 4px;font-size:14.2px;
border-left:5px solid;display:flex;gap:10px;align-items:flex-start;}
.box .ico{font-size:16px;flex:0 0 auto;}
.box-tip{background:#eef7ff;border-color:#3d8bfd;color:#1c4f8f;}
.box-warn{background:#fff6f5;border-color:#e74c3c;color:#a5322a;}
.box-key{background:#f3fbf5;border-color:#27ae60;color:#1c7a44;}
.box b{font-weight:800;}

table{width:100%;border-collapse:collapse;margin:12px 0 6px;font-size:14px;}
th{background:#2e5c9a;color:#fff;padding:10px 8px;font-weight:700;font-size:13.6px;}
td{padding:9px 10px;border:1px solid #dbe8f8;vertical-align:top;color:#333a48;}
tr:nth-child(even) td{background:#f6faff;}
td.c{text-align:center;}

.bar{display:flex;align-items:center;gap:10px;margin-bottom:9px;font-size:14px;}
.bar .name{width:130px;flex:0 0 130px;color:#22406e;font-weight:600;}
.bar .track{flex:1;height:19px;background:#eef3fa;border-radius:10px;overflow:hidden;}
.bar .fill{height:100%;border-radius:10px;background:linear-gradient(90deg,#4a7fc1,#7fb0e8);}
.bar .pct{width:56px;flex:0 0 56px;text-align:right;color:#c0392b;font-weight:700;font-size:13px;}

.nav{display:flex;flex-wrap:wrap;gap:9px;margin-top:22px;}
.nav a{text-decoration:none;color:#2e5c9a;background:#fff;border:1px solid #cfe0f5;
padding:8px 16px;border-radius:22px;font-size:13.6px;font-weight:600;transition:.2s;
box-shadow:0 2px 6px rgba(46,92,154,.07);}
.nav a:hover{background:#2e5c9a;color:#fff;transform:translateY(-2px);}
.foot{margin-top:34px;text-align:center;font-size:12.6px;color:#8a94a6;line-height:2;
border-top:1px dashed #d5e0ef;padding-top:18px;}
@media print{body{background:#fff;}.section{box-shadow:none;border:1px solid #ccc;page-break-inside:avoid;}}
"""

def render(grade, subject, badges, sections, footer_note, filename):
    secs = []
    for i, s in enumerate(sections, 1):
        tag = f'<span class="tag">{s["tag"]}</span>' if s.get("tag") else ""
        secs.append(f'''<div class="section" id="sec{i}">
<div class="sec-head"><div class="sec-no">{i}</div><h2>{s["title"]}</h2>{tag}</div>
<div class="sec-body">{s["body"]}</div></div>''')
    nav = "".join(f'<a href="#sec{i}">{s["title"]}</a>' for i, s in enumerate(sections, 1))
    bdg = "".join(f'<span>{b}</span>' for b in badges)
    doc = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{html.escape(grade)}{html.escape(subject)} 知识点考点全解</title>
<style>{CSS}</style></head><body>
<div class="hero"><div class="wrap">
<div class="badge">湖北省咸宁市 · 2025—2026 学年</div>
<h1>{html.escape(grade)}<span class="em">{html.escape(subject)}</span> 知识点 · 考点全解</h1>
<div class="sub">依据《义务教育课程标准（2022年版）》与教材编写 · 知识点逐条讲透 · 考点精准定位</div>
<div class="meta">{bdg}</div></div></div>
<div class="wrap">{''.join(secs)}
<div class="nav">{nav}</div>
<div class="foot">{footer_note}</div></div></body></html>'''
    path = os.path.join(BASE, filename)
    open(path, "w", encoding="utf-8").write(doc)
    return path


# ---------- 便捷构造函数 ----------
def KP(title, n, items, box=None):
    lis = "".join(f"<li>{i}</li>" for i in items)
    b = ""
    if box:
        b = f'<div class="box box-{box[0]}"><span class="ico">{box[1]}</span><div>{box[2]}</div></div>'
    return f'<div class="kp"><div class="kp-title"><span class="n">{n}</span>{title}</div><ul>{lis}</ul>{b}</div>'

def BAR(pairs):
    out = []
    for name, pct in pairs:
        w = min(96, max(8, pct))
        out.append(f'<div class="bar"><div class="name">{name}</div>'
                   f'<div class="track"><div class="fill" style="width:{w}%"></div></div>'
                   f'<div class="pct">{pct}%</div></div>')
    return "".join(out)

def TABLE(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f'<td class="c">{c}</td>' for c in r) + "</tr>" for r in rows)
    return f'<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'


# ============ 安全辅助（新版脚本推荐使用，避免括号嵌套错误） ============
def SEC(title, kps, tag=None):
    """构造一个 section：kps 为 KP() 返回值组成的列表，自动拼接"""
    return {"title": title, "tag": tag, "body": "".join(kps)}


def KPS(title, n, items, box=None):
    """同 KP，但语义更清晰（保留兼容）"""
    return KP(title, n, items, box)
