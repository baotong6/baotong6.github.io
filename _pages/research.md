---
permalink: /research/
title: "Research"
author_profile: true
classes: wide
redirect_from:
  - /research.html
---

<style>
.research-hero {
  padding: 1.8rem 2rem;
  margin-bottom: 2rem;
  border-radius: 14px;
  background: linear-gradient(135deg, #eef6ff 0%, #f8fbff 55%, #f3f0ff 100%);
  border: 1px solid #dbeafe;
}

.research-hero h1 {
  margin-top: 0.3rem;
  margin-bottom: 0.8rem;
  font-size: 2.1rem;
  line-height: 1.2;
}

.research-kicker {
  margin: 0;
  color: #2563eb;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.research-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1.2rem;
}

.research-tag {
  display: inline-block;
  padding: 0.3rem 0.7rem;
  border-radius: 999px;
  background: white;
  border: 1px solid #bfdbfe;
  color: #1e3a8a;
  font-size: 0.82rem;
  font-weight: 600;
}

.research-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(235px, 1fr));
  gap: 1.1rem;
  margin: 1.3rem 0 2.2rem;
}

.research-card {
  padding: 1.25rem 1.35rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: #ffffff;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

.research-card h3 {
  margin-top: 0;
  margin-bottom: 0.6rem;
  color: #1e3a8a;
}

.research-card p {
  margin-bottom: 0;
}

.research-figure {
  margin: 1.5rem 0 2rem;
}

.research-figure img {
  width: 100%;
  max-height: 430px;
  object-fit: cover;
  border-radius: 12px;
}

.research-figure figcaption {
  margin-top: 0.55rem;
  color: #64748b;
  font-size: 0.85rem;
  text-align: center;
}

.research-highlight {
  padding: 1.2rem 1.4rem;
  margin: 1.2rem 0 2rem;
  border-left: 4px solid #2563eb;
  border-radius: 0 10px 10px 0;
  background: #f8fafc;
}

@media (max-width: 600px) {
  .research-hero {
    padding: 1.3rem;
  }

  .research-hero h1 {
    font-size: 1.7rem;
  }
}
</style>

<div class="research-hero">

<p class="research-kicker">Research overview</p>

<h1>Galactic X-ray populations and time-domain high-energy astrophysics</h1>

My research focuses on the origin, evolution, and observational properties of
X-ray source populations in the Milky Way. I am particularly interested in
compact binaries, stellar X-ray sources, crowded Galactic environments, and
time-variable high-energy phenomena.

<div class="research-tags">
  <span class="research-tag">X-ray astronomy</span>
  <span class="research-tag">Compact binaries</span>
  <span class="research-tag">Galactic Center</span>
  <span class="research-tag">Globular clusters</span>
  <span class="research-tag">Time-domain astronomy</span>
  <span class="research-tag">Population studies</span>
</div>

</div>

<figure class="research-figure">
  <img src="{{ '/images/galactic-plane.png' | relative_url }}"
       alt="The Galactic plane viewed at high energies">
  <figcaption>
    The Galactic plane contains a rich mixture of stellar coronae,
    accreting compact binaries, and unresolved diffuse emission.
  </figcaption>
</figure>

## Research themes

<div class="research-grid">

<div class="research-card" markdown="1">

### Galactic X-ray source populations

I study the physical origin and spectral properties of X-ray sources across
the Galactic disk and central regions. By combining XMM-Newton, eROSITA,
Chandra, and Gaia data, I investigate how different source populations
contribute to the observed Galactic X-ray emission.

</div>

<div class="research-card" markdown="1">

### Compact binaries in dense environments

Globular clusters and nuclear stellar environments efficiently form and
reshape close binary systems. I use X-ray observations and periodic signals
to identify cataclysmic variables, X-ray binaries, and other compact systems,
and to explore their formation histories.

</div>

<div class="research-card" markdown="1">

### Time-domain high-energy astrophysics

Variability provides a direct view of the physical processes operating near
compact objects. My work includes searches for coherent periodicities,
quasi-periodic oscillations, transients, and long-term variability in compact
binaries and active galactic nuclei.

</div>

<div class="research-card" markdown="1">

### Data-intensive population analysis

I develop reproducible pipelines for source classification, spectral
stacking, timing analysis, catalogue cross-matching, and population
inference. These methods connect individual detections to the broader
astrophysical populations from which they arise.

</div>

</div>

## Current focus: resolving the Galactic ridge X-ray emission

<div class="research-highlight">

The Galactic ridge X-ray emission is produced by a mixture of resolved and
unresolved source populations. A central goal of my current work is to
determine how coronal stars, active binaries, non-magnetic cataclysmic
variables, and magnetic cataclysmic variables contribute at different
X-ray energies.

</div>

I combine large XMM-Newton source catalogues with Gaia counterparts,
energy-dependent source classification, and stacked X-ray spectra. This
allows the total resolved emission to be separated into physically
interpretable populations and compared with the spectral properties of the
Galactic ridge.

The main questions include:

- Which source populations dominate at soft and hard X-ray energies?
- How do iron-line properties distinguish different classes of accreting binaries?
- How much of the Galactic ridge can be explained by detected point sources?
- What populations remain hidden below current survey sensitivity limits?

## Compact binaries and periodic X-ray sources

Periodic variability is a powerful diagnostic of compact systems. Orbital
modulation, eclipses, white-dwarf spin signals, and neutron-star pulsations
can reveal the nature of a source even when its optical counterpart is faint
or uncertain.

My work uses timing information to study:

- X-ray binaries and cataclysmic variables in globular clusters;
- periodic source populations near the Galactic Center;
- the influence of dense stellar environments on close-binary formation;
- the detectability and selection effects of periodic X-ray signals.

## Multiwavelength and multi-mission analysis

Modern population studies require information from several observatories and
catalogues. My research commonly combines:

- **XMM-Newton and Chandra** for imaging, spectroscopy, and timing;
- **eROSITA** for wide-area X-ray source samples;
- **Gaia** for distances and stellar classifications;
- **JWST and optical/infrared catalogues** for environmental and counterpart information;
- Bayesian classification and simulation-based selection-function analysis.

## Broader interests

Beyond Galactic stellar populations, I am interested in time-variable
phenomena associated with active galactic nuclei, including
quasi-periodic oscillations and episodic eruptions. More broadly, I am
interested in developing scalable methods for extracting physical
information from large, heterogeneous astronomical datasets.

---

[View my publications](/publications/){: .btn .btn--primary}
[View my GitHub](https://github.com/baotong6){: .btn .btn--info}