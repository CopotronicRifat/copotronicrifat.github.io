---
layout: homepage
description: Research, publications, teaching, mentoring, and academic service of S M (Rifat) Rafiuddin.
---

## About Me

<p class="lead">I am a Ph.D. student in Computer Science at <a href="https://go.okstate.edu/" target="_blank" rel="noopener">Oklahoma State University</a>, where I work in the <a href="https://cas.okstate.edu/computer_science/about_us/dr_sen_lab/" target="_blank" rel="noopener">Reasoning and Artificial Intelligence (rAIson) Lab</a> with <a href="https://experts.okstate.edu/atriya.sen" target="_blank" rel="noopener">Dr. Atriya Sen</a>. I expect to complete my Ph.D. in July 2027.</p>

I develop **efficient, interpretable, and controllable language models** through representation-guided adaptation and targeted intervention. My work connects parameter-efficient learning, mechanistic analysis, causal and counterfactual reasoning, and multimodal representation learning.

Before beginning my Ph.D., I taught computer science for more than five years as a lecturer at the University of Asia Pacific and Uttara University. I aim to build an academic program that combines rigorous research, effective teaching, and sustained student mentorship.

<div class="research-vision">
  <p><strong>Dissertation direction.</strong> <em>Efficient, Interpretable, and Controllable Language Models through Representation-Guided Adaptation and Intervention.</em></p>
</div>

## Research

<div class="theme-grid">
  <div class="theme-card">
    <h3>Efficient Adaptation</h3>
    <p>Parameter-efficient fine-tuning, dynamic rank routing, token retention, memory efficiency, and throughput-aware learning.</p>
  </div>
  <div class="theme-card">
    <h3>Interpretability and Control</h3>
    <p>Mechanistic analysis, representation-guided intervention, symbolic planning, and faithful model behavior.</p>
  </div>
  <div class="theme-card">
    <h3>Causal Language Reasoning</h3>
    <p>Counterfactual editing, causal analysis of sentiment shifts, and controllable reasoning over conversations.</p>
  </div>
  <div class="theme-card">
    <h3>Multimodal Representation Learning</h3>
    <p>Text–image alignment, aspect-based sentiment analysis, robustness, and cross-modal feedback mechanisms.</p>
  </div>
</div>

### Research Highlights

<div class="metric-grid">
  <div class="metric-card">
    <h3>MaskLoRA</h3>
    <p>Representation-guided token retention delivered 1.3–2.6× end-to-end speedups on encoder benchmarks and 1.5–3.6× on long-context tasks while preserving near-baseline quality.</p>
  </div>
  <div class="metric-card">
    <h3>CCM-LoRA</h3>
    <p>Input-conditioned rank routing matched or improved static LoRA while using 61% fewer adapter FLOPs and increasing training throughput by approximately 8%.</p>
  </div>
</div>

## News

<ul class="news-list">
  <li><span class="news-date">August 2026</span><span>Our paper <strong>“C³T: Counterfactual Causal Reasoning for Sentiment Shifts in Social-Media Conversation Trees”</strong> was accepted to the <strong>EMNLP 2026 Main Conference</strong>.</span></li>
  <li><span class="news-date">July 2026</span><span>Presented our counterfactual editing work at <a href="https://haim-lab.github.io/hhaikeml2026" target="_blank" rel="noopener">HHAI-KEML 2026</a>.</span></li>
  <li><span class="news-date">June 2026</span><span>Served as a reviewer for the NeurIPS 2026 Position Paper Track.</span></li>
  <li><span class="news-date">May 2026</span><span>Our paper on constraint-aware counterfactual editing was accepted to HHAI-KEML 2026.</span></li>
  <li><span class="news-date">May 2026</span><span>A mentored project on cross-domain adversarial augmentation was published following IEEE RAAICON 2025.</span></li>
  <li><span class="news-date">April 2026</span><span>Our CCM-LoRA paper appeared in <a href="https://aclanthology.org/2026.findings-acl.1329/" target="_blank" rel="noopener">Findings of ACL 2026</a>.</span></li>
  <li><span class="news-date">March 2026</span><span>Received ICLR 2026 financial assistance, including registration and $1,600 in travel support.</span></li>
  <li><span class="news-date">January 2026</span><span>Our symbolic-planning paper was accepted to ICLR 2026, and MaskLoRA was accepted to Findings of EACL 2026.</span></li>
</ul>

[View the news archive →]({{ '/news/' | relative_url }}){: .text-link }

## Selected Publications

My name is shown in **bold**. See the [complete publication list]({{ '/publications/' | relative_url }}).

{% assign selected_publications = site.data.publications.main | where: "selected", true %}
{% include publications.html items=selected_publications %}

## Academic Appointments

<ul class="timeline">
  <li class="timeline-item">
    <div class="timeline-heading"><strong>Oklahoma State University</strong><span class="timeline-date">2022–present</span></div>
    <p>Graduate Teaching Assistant; Graduate Research Assistant in the rAIson Lab (summers 2025 and 2026) and Complex Systems Lab (summers 2023 and 2024).</p>
  </li>
  <li class="timeline-item">
    <div class="timeline-heading"><strong>University of Asia Pacific</strong><span class="timeline-date">2018–2022</span></div>
    <p>Lecturer, Department of Computer Science and Engineering.</p>
  </li>
  <li class="timeline-item">
    <div class="timeline-heading"><strong>Uttara University</strong><span class="timeline-date">2017–2018</span></div>
    <p>Lecturer, Department of Computer Science and Engineering.</p>
  </li>
</ul>

### Education

<ul class="timeline">
  <li class="timeline-item">
    <div class="timeline-heading"><strong>Ph.D. in Computer Science, Oklahoma State University</strong><span class="timeline-date">2022–expected 2027</span></div>
    <p>Advisor: Dr. Atriya Sen.</p>
  </li>
  <li class="timeline-item">
    <div class="timeline-heading"><strong>B.Sc. in Computer Science and Engineering, RUET</strong><span class="timeline-date">2012–2016</span></div>
    <p>Rajshahi University of Engineering and Technology, Bangladesh.</p>
  </li>
</ul>

## Teaching and Mentoring

My teaching interests include natural language processing, machine learning, deep learning, responsible AI, data mining, algorithms, and introductory programming. At Oklahoma State, I have supported courses spanning operating systems, databases, data structures, discrete mathematics, computer security, and social issues in computing. As an instructor of record in Bangladesh, I designed and delivered courses in machine learning, pattern recognition, algorithms, discrete mathematics, operating systems, and programming.

I have mentored student research in counterfactual generation, multimodal sentiment analysis, and adversarial augmentation. These collaborations have led to peer-reviewed workshop and conference publications.

[Teaching, mentoring, and course materials →]({{ '/teaching/' | relative_url }}){: .text-link }

## Honors and Service

<ul class="compact-list">
  <li><strong>ICLR 2026 Financial Assistance Award</strong> — complimentary registration and $1,600 in travel support.</li>
  <li><strong>AIRS Travel Fund</strong>, Oklahoma State University, 2025.</li>
  <li><strong>GPSGA Travel and Research Awards</strong>, Oklahoma State University, 2024–2025.</li>
  <li><strong>Peer review:</strong> ACM TOIT; NeurIPS Position Paper Track; ICWSM; PAKDD; COLING; and IJCNN.</li>
  <li><strong>Academic outreach:</strong> competitive programming team coach and National High School Programming Contest volunteer.</li>
</ul>

## A Favorite PhD Comic

A small personal tradition from the original site—kept here because research rarely moves in a straight line.

<figure class="comic-card">
  <a href="https://phdcomics.com/comics/archive.php?comicid=1759" target="_blank" rel="noopener">
    <img src="https://phdcomics.com/comics/archive/phd110714s.gif" alt="PhD Comics: The Research Cycle, strip 1759" loading="lazy">
  </a>
  <figcaption>“The Research Cycle” — <em>Piled Higher and Deeper</em> by Jorge Cham. © Piled Higher and Deeper Publishing, LLC. <a href="https://phdcomics.com/comics/archive.php?comicid=1759" target="_blank" rel="noopener">Source</a>.</figcaption>
</figure>

[More personal links and research resources →]({{ '/personal/' | relative_url }}){: .text-link }
