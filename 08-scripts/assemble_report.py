#!/usr/bin/env python3
"""Assemble the final report from intro, ranked profiles and blueprint.

Inputs (in /home/ubuntu/school_mgmt_research):
  ranking_global.json, ranking_india.json  -> output of rank_platforms.py
  parts/00-intro.md                         -> title, criteria, overview tables
  parts/90-blueprint.md                     -> blueprint
  profiles/<id>.md                          -> per-platform profiles ({{RANK}} placeholder)
Output: report/School_Management_Platforms_Report.md
"""
import json
import os
import re

BASE = "/home/ubuntu/school_mgmt_research"


def load(name):
    return json.load(open(os.path.join(BASE, name), encoding="utf-8"))


def profile_text(item, rank_label):
    path = os.path.join(BASE, "profiles", item["id"] + ".md")
    text = open(path, encoding="utf-8").read().strip()
    text = text.replace("{{RANK}}", rank_label)
    # Make sure the first heading is a level-2 heading with the rank.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("#"):
            title = re.sub(r"^#+\s*", "", line)
            if not title.startswith(rank_label):
                title = re.sub(r"^(\{\{RANK\}\}|\d+|IN-?\d+)\.\s*", "", title)
                title = f"{rank_label}. {title}"
            lines[i] = "## " + title
            break
    body = "\n".join(lines)
    # Demote any stray level-1/level-2 headings after the title.
    out, seen_title = [], False
    for line in body.splitlines():
        if line.startswith("## ") and not seen_title:
            seen_title = True
            out.append(line)
            continue
        if re.match(r"^#{1,2} ", line):
            line = "### " + re.sub(r"^#+\s*", "", line)
        out.append(line)
    return "\n".join(out)


def demote(path, title):
    text = open(os.path.join(BASE, path), encoding="utf-8").read().strip()
    out = []
    for i, line in enumerate(text.splitlines()):
        if i == 0 and line.startswith("# "):
            out.append("# " + title)
            continue
        if line.startswith("#"):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def main():
    g = load("ranking_global.json")
    ind = load("ranking_india.json")
    gx = load("ranking_global_extra.json")
    ix = load("ranking_india_extra.json")
    parts = [open(os.path.join(BASE, "parts", "00-intro.md"), encoding="utf-8").read().strip()]
    parts.append("# Part I. Top 20 Worldwide Platforms: Full Profiles")
    for item in g:
        parts.append(profile_text(item, f"#{item['rank']}"))
    parts.append("# Part II. Top 10 Indian Platforms: Full Profiles")
    for item in ind:
        parts.append(profile_text(item, f"India #{item['rank']}"))
    parts.append("# Part III. Also Evaluated: Full Profiles of the 10 Candidates That Did Not Make the Lists\n\n"
                 "These platforms were researched to the same standard but scored below the cut-off. They are kept for completeness and comparison.")
    for item in gx:
        parts.append(profile_text(item, f"Global #{item['rank']} (evaluated)"))
    for item in ix:
        parts.append(profile_text(item, f"India #{item['rank']} (evaluated)"))
    parts.append(demote("context/X4-top3-backend-teardown.md",
                        "Part IV. Backend Teardown of the Top 3 System-of-Record Platforms (REA-assisted): PowerSchool, Infinite Campus, Ellucian"))
    parts.append(open(os.path.join(BASE, "parts", "90-blueprint.md"), encoding="utf-8").read().strip())
    parts.append(demote("context/X1-standards-regulation.md", "Appendix A. Interoperability, Privacy, Accessibility, Security and India DPI Requirements"))
    parts.append(demote("context/X2-tech-stack-open-source.md", "Appendix B. Open-Source Technical Approach, Free Tiers and Deployment Costs"))
    parts.append(demote("context/X3-market-pain-points.md", "Appendix C. Market Size, Consolidation, Security Incidents and Buyer Pain Points"))
    os.makedirs(os.path.join(BASE, "report"), exist_ok=True)
    out = os.path.join(BASE, "report", "School_Management_Platforms_Report.md")
    open(out, "w", encoding="utf-8").write("\n\n".join(parts) + "\n")
    print("wrote", out, sum(len(p.split()) for p in parts), "words")


if __name__ == "__main__":
    main()
