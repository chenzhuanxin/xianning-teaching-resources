# -*- coding: utf-8 -*-
"""试卷生成公共助手：供各年级复用"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_engine import render_paper_html, gen_word_paper, WORD_DIR, HTML_DIR

REGION = "湖北省咸宁市"

def Q(no, text, score=None, opts=None, blanks=0, kind=""):
    return dict(no=no, text=text, score=score, opts=opts or [], blanks=blanks, kind=kind)

def A(no, val, analy="", kind=""):
    return dict(no=no, val=val, analy=analy, kind=kind)

def save(meta, parts, answers, seed):
    fname = f"{meta['subject_grade']}_{meta['title']}_{seed}"
    open(os.path.join(HTML_DIR, fname + ".html"), "w", encoding="utf-8").write(
        render_paper_html(meta, parts, answers))
    gen_word_paper(meta, parts, answers, os.path.join(WORD_DIR, fname + ".docx"))
    return fname

def base(grade_subject, title, info, fs=100, dur=60):
    return dict(region=REGION, subject_grade=grade_subject, title=title, info=info,
                full_score=fs, duration=dur)
