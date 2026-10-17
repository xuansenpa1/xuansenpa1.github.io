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

Hi, I am **Yuxuan Liu (刘宇轩)**, a Ph.D. student at the **Hong Kong University of Science and Technology (HKUST)**, supervised by Prof. [Yangqiu Song](https://www.cse.ust.hk/~yqsong/). Before joining HKUST, I received my Bachelor's degree in Artificial Intelligence from **Harbin Institute of Technology**. I was also fortunate to intern at the **Research Center for Social Computing and Information Retrieval (SCIR)** under the guidance of Prof. [Wanxiang Che](https://ir.hit.edu.cn/~car/).

<span class='anchor' id='education'></span>

# 📖 Education

- **Hong Kong University of Science and Technology (HKUST)**
  Ph.D. student in the Department of Computer Science and Engineering, supervised by Prof. Yangqiu Song.

- **Harbin Institute of Technology**
  Bachelor's degree in the School of Future Technology (GPA: 92.89 / 100, Rank: 1 / 165).

<span class='anchor' id='research'></span>

# 🔬 Research Interests

I’m mainly interested in the research of Natural Language Processing.

- Large Language Models
- Recursive Self-Improvement
- Harness Engineering

<span class='anchor' id='news'></span>

# 🔥 News

- **Oct 2026:** Our paper **JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.19589)]
- **Oct 2026:** Our paper **Jev-ToM: Evaluating Theory of Mind in Typed Decision Models** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.18610)]
- **Oct 2026:** Our paper **Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.18326)]
- **Oct 2026:** Our paper **RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.18143)]
- **Oct 2026:** Our paper **Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.16838)]
- **Oct 2026:** Our paper **SkillHorizon: Constructing Long-Horizon Agent Tasks through Skill Composition** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.14966)]
- **Oct 2026:** Our paper **You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.06496)]
- **Oct 2026:** Our paper **SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown** is available on arXiv. [[Paper](https://arxiv.org/abs/2610.04008)]
- **Sep 2026:** Our paper **CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning** is available on arXiv. [[Paper](https://arxiv.org/abs/2609.36820)]
- **Sep 2026:** Our paper **SoFT: Soft Targets for Generalizable LLM Fine-Tuning** is available on arXiv. [[Paper](https://arxiv.org/abs/2609.32493)]
- **Aug 2026:** Our paper **SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision** has been accepted to **Findings of EMNLP 2026**. [[Paper](https://arxiv.org/abs/2606.01139)] [[Code](https://github.com/xuansenpa1/skillrevise)]
- **Aug 2026:** Our paper **MultivationBench: A Benchmark for Multimodal Sequential Motivation Reasoning** has been accepted to **Findings of EMNLP 2026**. [[Paper](https://arxiv.org/abs/2607.26465)]
- **Aug 2026:** Our paper **Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design** is available on arXiv. [[Paper](https://arxiv.org/abs/2608.10299)]
- **Aug 2026:** Our paper **Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs** is available on arXiv. [[Paper](https://arxiv.org/abs/2608.06967)]
- **Aug 2026:** Our paper **Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds** is available on arXiv. [[Paper](https://arxiv.org/abs/2608.02636)] [[Code](https://github.com/HKUST-KnowComp/rethinkskill)]
- **Jul 2026:** Our paper **RLPF: Reinforcement Learning from Performance Feedback for Code Generation** is available on arXiv. [[Paper](https://arxiv.org/abs/2607.27271)]

<span class='anchor' id='publications'></span>

# 📝 Publications

<div id="google-scholar-publications">
  <h2>First-Author Publications</h2>

  <div class="google-scholar-publication">
    <strong>SkillHorizon: Constructing Long-Horizon Agent Tasks through Skill Composition</strong>
    <p><strong><u>Yuxuan Liu</u></strong>, Zhaochen Su, Hangyu Guo, Shijue Huang, Zhixiong Zhang, Kawai Chung, Zhongwei Xie, Tianshi Zheng, Wei Fan, Qing Zong, Haochen Shi, Baixuan Xu, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.14966">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>SkillScriptBench: Benchmarking Self-Evolution of Executable Agent Skill Packages Beyond Markdown</strong>
    <p><strong><u>Yuxuan Liu</u></strong>, Haoran Li, Yuhao Zhang, Jiahe Guo, Hongyu Luo, Wenbin Hu, Huihao Jing, Kawai Chung, Junle Chen, Changxuan Fan, Qing Zong, Lingyun Xie, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.04008">[Paper]</a> <a href="https://github.com/HKUST-KnowComp/SkillScriptBench">[Code]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>Rethinking Self-Evolving Agent Skills: Feedback Dynamics over Multiple Rounds</strong>
    <p><strong><u>Yuxuan Liu</u></strong>, Zhaochen Su, Yuhao Zhang, Jiahe Guo, Zhongwei Xie, Huihao Jing, Lingyun Xie, Qing Zong, Yauwai Yim, Zhixiong Zhang, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2608.02636">[Paper]</a> <a href="https://github.com/HKUST-KnowComp/rethinkskill">[Code]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>SkillRevise: Improving LLM-Authored Agent Skills via Trace-Conditioned Skill Revision</strong>
    <p><strong><u>Yuxuan Liu</u></strong>, Zhaochen Su, Lingyun Xie, Yuhao Zhang, Qing Zong, Jiahe Guo, Zhongwei Xie, Yiyan Ji, Yauwai Yim, Hongyu Luo, Xiyu Ren, Chenyu Ruan, Haoran Li, Yangqiu Song</p>
    <p><em>Findings of EMNLP, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2606.01139">[Paper]</a> <a href="https://github.com/xuansenpa1/skillrevise">[Code]</a></p>
  </div>

  <h2>Non-First-Author Publications</h2>

  <div class="google-scholar-publication">
    <strong>JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making</strong>
    <p>Zhongwei Xie, Xingsu Li, Jingqiao Yu, Zihao Wang, Hong ChiTat, Zhaowei Wang, Weizhi Du, <strong><u>Yuxuan Liu</u></strong>, Huihao Jing, Jiaxin Bai, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.19589">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>Jev-ToM: Evaluating Theory of Mind in Typed Decision Models</strong>
    <p>Kawai Chung, Chunkit Chan, <strong><u>Yuxuan Liu</u></strong>, Yauwai Yim, Xi Yang, Wenbin Hu, Huihao Jing, Chiu Yeung Tang, Changxuan Fan, Ki Sen Hung, Tsun On Kwok, Haoran Li</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.18610">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees</strong>
    <p>Wenbin Hu, Huihao Jing, Haochen Shi, <strong><u>Yuxuan Liu</u></strong>, Changxuan Fan, Sirui Zhang, Kawai Chung, Hanyu Yang, Zhenhuan Wang, Ziyi Chen, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.18326">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving</strong>
    <p>Huihao Jing, Wenbin Hu, Shaojin Chen, Haochen Shi, Haoyu Huang, Sirui Zhang, <strong><u>Yuxuan Liu</u></strong>, Zhongwei Xie, Haoran Li</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.18143">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization</strong>
    <p>Huihao Jing, Shaojin Chen, Wenbin Hu, <strong><u>Yuxuan Liu</u></strong>, Haochen Shi, Zhongwei Xie, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.16838">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue</strong>
    <p>Junle Chen, Wei Chen, Zhengjun Huang, Zhoujin Tian, <strong><u>Yuxuan Liu</u></strong>, Kai Wang, Rui Chen, Xiaofang Zhou</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2610.06496">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning</strong>
    <p>Wenbin Hu, Huihao Jing, Haochen Shi, <strong><u>Yuxuan Liu</u></strong>, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2609.36820">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>SoFT: Soft Targets for Generalizable LLM Fine-Tuning</strong>
    <p>Huihao Jing, Wenbin Hu, Shaojin Chen, Haochen Shi, Zhongwei Xie, Guijia Zhang, <strong><u>Yuxuan Liu</u></strong>, Haoyu Huang, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2609.32493">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design</strong>
    <p>Qing Zong, Jiayu Liu, Junhao Shen, Zecong Tang, Linsi Wu, <strong><u>Yuxuan Liu</u></strong>, Rui Wang, Zhaowei Wang, Weiqi Wang, Cheng Qian, Xiusi Chen, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2608.10299">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs</strong>
    <p>Hongyu Luo, He Wang, Huihao Jing, Hong Ting Tsang, <strong><u>Yuxuan Liu</u></strong>, Wuganjing Song, Yauwai Yim, Chunyang Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2608.06967">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>RLPF: Reinforcement Learning from Performance Feedback for Code Generation</strong>
    <p>Huihao Jing, Haozhe Cui, Wenbin Hu, Shaojin Chen, Haochen Shi, Changxuan Fan, <strong><u>Yuxuan Liu</u></strong>, Hanyu Yang, Sirui Zhang, Ziyi Chen, Haoran Li, Yangqiu Song</p>
    <p><em>arXiv preprint, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2607.27271">[Paper]</a></p>
  </div>

  <div class="google-scholar-publication">
    <strong>MultivationBench: A Benchmark for Multimodal Sequential Motivation Reasoning</strong>
    <p>Kawai Chung, Chunkit Chan, Yauwai Yim, <strong><u>Yuxuan Liu</u></strong>, Haochen Shi, Weiqi Wang, Qing Zong, Tianshi Zheng, Yixuan Fu, Kai Chung Wong, Hao Liang, Yifan Gao, Xi Yang, Janet Hui-wen Hsiao, Yangqiu Song</p>
    <p><em>Findings of EMNLP, 2026</em></p>
    <p><a href="https://arxiv.org/abs/2607.26465">[Paper]</a></p>
  </div>

</div>

<span class='anchor' id='awards'></span>

# 🏆 Honors & Awards

- **2025.08** RedBird PhD Award Program
- **2024.06** Top Ten Academic Tutoring Volunteers at Harbin Institute of Technology (Ranked 1st)
- **2024.05** Meritorious Winner, Interdisciplinary Contest in Modeling
- **2024.03** Song Qingling Future Scholarship
- **2023.12** Shenzhen Stock Exchange Scholarship
- **2023.11** First Prize, China Undergraduate Mathematical Contest in Modeling
- **2023.10** Outstanding Student in Heilongjiang Province
- **2023.10** Outstanding Student Model at Harbin Institute of Technology
- **2022.10** National Scholarship (Ranked 1st)
- **2022.07** First Prize, National University Students' Opt-Sci-Tech Competition
- **2022.05** Top Ten Learning Stars of the Fundamental Division at Harbin Institute of Technology
- **Multiple** The Chinese Mathematics Competitions (Second in the same graduating class at HIT)
- **Multiple** First-class People's Scholarship in China * 6 (Top 3%)

<span class='anchor' id='experience'></span>

# 💻 Experience

- **Center on Machine Learning Research**
  Research intern, advised by Prof. Wangmeng Zuo.

- **Research Center for Social Computing and Information Retrieval (SCIR), Harbin Institute of Technology**
  Research intern, advised by Prof. Wanxiang Che.
