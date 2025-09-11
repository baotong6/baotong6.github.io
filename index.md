---
layout: home
title: "Tong Bao (鲍通)"
subtitle: "Postdoctoral Researcher at INAF – Osservatorio Astronomico di Brera"
permalink: /
---

<link rel="stylesheet" href="/assets/css/custom.css">

<div style="text-align:center;">
  <img src="/thumbnail.png" width="180" class="hero-avatar">
</div>

**Postdoctoral Researcher**  
INAF – Osservatorio Astronomico di Brera  
Merate, Italy  

📧 baotong@smail.nju.edu.cn  
[CV](bao_cv.pdf){: .btn} [Google Scholar](https://scholar.google.com/citations?user=8Fr_PVwAAAAJ&hl=zh-CN&oi=sra){: .btn} [Github](https://github.com/baotong6){: .btn} [ORCID](https://orcid.org/my-orcid?orcid=0000-0002-5082-5049){: .btn}

---

## 🔹 About Me
<div class="card fade-in">
I am a Postdoctoral researcher at **INAF-Merate**, collaborating with Dr. Gabriele Ponti.  
I obtained my PhD in Astrophysics at **Nanjing University** (2019–2024), supervised by Prof. Zhiyuan Li.  

Research focuses on **X-ray population in globular clusters and the Galactic center**, especially:  
- Periodic variations of compact binaries (X-ray binaries, cataclysmic variables)  
- Stellar populations and dynamics in dense environments  
- Quasi-periodic oscillations and eruptions in AGNs  
- Origin of nuclear star clusters and their link to globular clusters  

Also interested in **data-intensive methods** for time-domain astrophysics.
</div>

---

## 🔹 Research Interests
<div class="card fade-in">
- Stellar populations & dynamics in globular clusters  
- Periodic X-ray variations of compact binaries  
- Quasi-periodic oscillations / eruptions of AGNs  
- X-ray populations of nuclear star clusters  
</div>

---

## 🔹 Projects / Recent Work
<div class="card fade-in">
### X-ray binaries in 47 Tucanae
Study of periodic variations and light curves in globular cluster 47 Tuc.

### QPO search in AGN (CDFS)
Application of statistical methods to detect quasi-periodic oscillations.

### Nuclear star clusters
Investigating stellar populations and X-ray sources in galactic centers.
</div>

---

## 🔹 Selected Publications
<div class="card fade-in">
Full list on [ADS Library](https://ui.adsabs.harvard.edu/public-libraries/K1kOb_WdRjqt3FJZWBtBWw)
1. **Bao. T.**, Li, Z., Cheng, Z., Belloni, Diogo. 2024, MNRAS, 527, 7173 — Periodic X-ray sources [[ADS]](https://ui.adsabs.harvard.edu/abs/2024MNRAS.527.7173B/abstract)
2. **Bao, T.**, Li, Z., Cheng, Z. 2023, MNRAS, 521, 4257 — Periodic X-ray sources [[ADS]](https://ui.adsabs.harvard.edu/abs/2023MNRAS.521.4257B)
3. **Bao, T.**, & Li, Z. 2022, MNRAS, 509, 3504 — Searching for QPOs in AGN [[ADS]](https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.3504B)
4. **Bao, T.**, & Li, Z. 2020, MNRAS, 498, 3513 — Periodic X-ray sources [[ADS]](https://ui.adsabs.harvard.edu/abs/2020MNRAS.498.3513B)
</div>

---

## 🔹 Conferences & Seminars
<div class="card fade-in">
- **Columbia University Colloquium** (2023): *Periodicities in X-ray sources*  
- **HEAD Meeting (AAS 2023, Hawaii)**: Poster — *Periodic X-ray sources in globular clusters*  
- **Chandra Frontiers in Time-Domain Science** (2020): Talk — *Periodic X-ray Sources in the Galactic Center*  
- **Chandra Data Science 2021**: *Searching for Quasi-periodic Oscillations of AGN in the CDFS*
</div>

---

## 🔹 Awards
<div class="card fade-in">
- Principal Special Scholarship, Nanjing University (2019)  
- Annual scholarship of National Astronomical Observatory, CAS (2017)
</div>

<script>
  // Fade-in on scroll
  const faders = document.querySelectorAll('.fade-in');
  const appearOptions = { threshold: 0.1 };
  const appearOnScroll = new IntersectionObserver(function(entries, observer){
    entries.forEach(entry => { if(entry.isIntersecting){ entry.target.classList.add('visible'); observer.unobserve(entry.target); }});
  }, appearOptions);
  faders.forEach(fader => { appearOnScroll.observe(fader); });
</script>
