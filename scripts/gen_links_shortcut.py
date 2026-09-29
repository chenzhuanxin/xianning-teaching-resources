# -*- coding: utf-8 -*-
"""生成英文短路径副本：links.html
把「交付物/全部资源在线网址一览.html」复制为仓库根目录的 links.html，
便于用简短英文网址访问：{SITE}/links.html
"""
import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE_DIR, "交付物", "全部资源在线网址一览.html")
DST = os.path.join(BASE_DIR, "links.html")

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

# 根目录副本需把页脚/头部的相对链接修正为根目录视角
html = html.replace('href="index.html"', 'href="index.html"')

with open(DST, "w", encoding="utf-8") as f:
    f.write(html)

print("已生成：", DST)
print("线上短址： https://chenzhuanxin.github.io/xianning-teaching-resources/links.html")
