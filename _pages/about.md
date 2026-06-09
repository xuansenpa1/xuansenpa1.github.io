---
permalink: /
title: "Homepage"
excerpt: "Yuxuan Liu"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi, I am **Yuxuan Liu (刘宇轩)**, a Ph.D. student at the **Hong Kong University of Science and Technology (HKUST)**, supervised by Prof. [Yangqiu Song](https://www.cse.ust.hk/~yqsong/). My research interests include **LLMs**, **Agents**, and **Skills**, with a focus on how language agents acquire, revise, and use procedural knowledge.

Before joining HKUST, I received my Bachelor's degree in Artificial Intelligence from **Harbin Institute of Technology**. I was also fortunate to intern at the **Research Center for Social Computing and Information Retrieval (SCIR)** under the guidance of Prof. [Wanxiang Che](https://ir.hit.edu.cn/~car/).

<span class='anchor' id='research'></span>

# 🔬 Research Interests

- **LLMs:** improving the reasoning, tool-use, and self-improvement abilities of large language models.
- **Agents:** building language agents that can act in environments, use tools, validate outcomes, and recover from failures.
- **Skills:** studying how reusable agent skills are authored, revised, evaluated, and transferred across tasks and models.

<span class='anchor' id='news'></span>

# 🔥 News

- **Jun 2026:** Our paper **SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision** is available on arXiv. [[Paper](https://arxiv.org/abs/2606.01139)] [[Code](https://github.com/xuansenpa1/skillrevise)]
- **2026:** I started my Ph.D. journey at HKUST.

<span class='anchor' id='publications'></span>

# 📝 Publications

**SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision**

Yuxuan Liu, Zhaochen Su, Lingyun Xie, Yuhao Zhang, Qing Zong, Jiahe Guo, Zhongwei Xie, Yiyan Ji, Yauwai Yim, Hongyu Luo, Xiyu Ren, Chenyu Ruan, Haoran Li, Yangqiu Song

*arXiv preprint*, 2026

[[Paper](https://arxiv.org/abs/2606.01139)] [[Code](https://github.com/xuansenpa1/skillrevise)]

<span class='anchor' id='projects'></span>

# 🛠 Projects

**SkillRevise**

An execution-grounded framework for improving cold-start LLM-authored agent skills. Starting from an initial skill, SkillRevise executes the task, diagnoses verifier-facing failures, retrieves reusable repair principles, revises the skill with execution anchors, re-executes the candidate, and keeps the best observed version under a utility gate.

[[Repository](https://github.com/xuansenpa1/skillrevise)] [[arXiv](https://arxiv.org/abs/2606.01139)]

<span class='anchor' id='education'></span>

# 📖 Education

- **Hong Kong University of Science and Technology (HKUST)**
  Ph.D. student in Artificial Intelligence / Computer Science, supervised by Prof. Yangqiu Song.

- **Harbin Institute of Technology**
  Bachelor's degree in Artificial Intelligence.

<span class='anchor' id='experience'></span>

# 💻 Experience

- **Research Center for Social Computing and Information Retrieval (SCIR), Harbin Institute of Technology**
  Research intern, advised by Prof. Wanxiang Che.
