#!/usr/bin/env python3
import re
from pathlib import Path

from build_abebe_content import publications_all_html, SCHOLAR

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

def replace_between(html, start, end, new_body, include_start=True):
    """Replace content from start marker through end marker (exclusive of end)."""
    i = html.find(start)
    j = html.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit(f"Markers not found: {start!r} .. {end!r}")
    if include_start:
        return html[:i] + new_body + html[j:]
    return html[:i + len(start)] + new_body + html[j:]


def main():
    html = INDEX.read_text(encoding="utf-8")

    # --- Head ---
    html = re.sub(
        r"<title>.*?</title>",
        "<title>Abebe B. Adege, Ph.D. – AI &amp; Remote Sensing Researcher</title>",
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="description" content="[^"]*" />',
        '<meta name="description" content="Academic portfolio of Abebe B. Adege, Ph.D. — postdoctoral researcher in AI, data science, UAV remote sensing, and intelligent sensing at UF/IFAS TREC, Homestead, Florida." />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:title" content="[^"]*" />',
        '<meta property="og:title" content="Abebe B. Adege, Ph.D. - AI &amp; Remote Sensing Researcher" />',
        html,
        count=1,
    )
    html = re.sub(
        r'<meta property="og:description" content="[^"]*" />',
        '<meta property="og:description" content="Postdoctoral Research Associate at University of Florida UF/IFAS TREC. Data science, computer vision, multimodal fusion, and precision agriculture." />',
        html,
        count=1,
    )

    nav_brand = """      <a class="nav-brand" href="/">
        <span class="nav-brand-name">Abebe B. Adege</span>
        <span class="nav-brand-sub">AI &amp; Remote Sensing</span>
      </a>"""
    html = re.sub(
        r'<a class="nav-brand" href="/">.*?</a>',
        nav_brand,
        html,
        count=1,
        flags=re.DOTALL,
    )

    hero_block = """    <div class="hero-content">
      <div class="hero-avatar">
        <div class="avatar-img avatar-placeholder" role="img" aria-label="Portrait placeholder for Abebe B. Adege">ABA</div>
        <div class="avatar-ring" aria-hidden="true"></div>
        <div class="avatar-ring avatar-ring--outer" aria-hidden="true"></div>
      </div>

      <div class="hero-text" style="min-width:0">
        <p class="hero-pre">Postdoctoral Research Associate</p>
        <h1 class="hero-name">Abebe Belay<br><span class="hero-name-accent">Adege, Ph.D.</span></h1>
        <p class="hero-title">AI Researcher · Data Science · UAV Remote Sensing</p>
        <p class="hero-subtitle">Intelligent sensing and multimodal data fusion for agricultural and environmental decision support</p>
        <p class="hero-affiliation">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.69 18.933l.003.001C9.89 19.02 10 19 10 19s.11.02.308-.066l.002-.001.006-.003.018-.008a5.741 5.741 0 00.281-.14c.186-.096.446-.24.757-.433.62-.384 1.445-.966 2.274-1.765C15.302 14.988 17 12.493 17 9A7 7 0 103 9c0 3.492 1.698 5.988 3.355 7.584a13.731 13.731 0 002.273 1.765 11.842 11.842 0 00.976.544l.062.029.018.008.006.003zM10 11.25a2.25 2.25 0 100-4.5 2.25 2.25 0 000 4.5z" clip-rule="evenodd"/></svg>
          UF/IFAS Tropical Research and Education Center (TREC), Homestead, Florida, USA
        </p>
        <div class="hero-tags">
          <span class="hero-tag">Machine Learning</span>
          <span class="hero-tag">Remote Sensing</span>
          <span class="hero-tag">Computer Vision</span>
          <span class="hero-tag">UAV Imagery</span>
          <span class="hero-tag">Data Fusion</span>
          <span class="hero-tag">Precision Agriculture</span>
        </div>
        <div class="hero-links">
          <a class="btn btn-primary" href="https://scholar.google.com/citations?user=OZc5w3YAAAAJ&amp;hl=en" target="_blank" rel="noopener noreferrer">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 100 14 7 7 0 000-14z"/></svg>
            Google Scholar
          </a>
          <a class="btn btn-outline" href="files/Abebe_Adege_Master_CV_2026.pdf" target="_blank" rel="noopener noreferrer">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download CV
          </a>
          <a class="btn btn-ghost" href="https://ieeexplore.ieee.org/author/37086392659" target="_blank" rel="noopener noreferrer">
            IEEE Profile
          </a>
          <a class="btn btn-ghost" href="https://www.linkedin.com/in/abebe-belay-adege-9730701a0/" target="_blank" rel="noopener noreferrer">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            LinkedIn
          </a>
          <a class="btn btn-accent" href="mailto:abebeadege@ufl.edu">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            Contact Me
          </a>
          <a class="btn btn-ghost" href="#research">
            Explore Research
          </a>
        </div>
      </div>"""

    html = re.sub(
        r"    <div class=\"hero-content\">.*?      </div>\n      <!-- ═══ EO Dashboard",
        hero_block + "\n      <!-- ═══ EO Dashboard",
        html,
        count=1,
        flags=re.DOTALL,
    )

    stats = """            <span class="stat-num" data-target="18" data-suffix="+">0</span>
          </div>
          <span class="stat-label">Journal Articles</span>
        </div>

        <div class="stat-item">
          <div class="stat-icon" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
          </div>
          <div class="stat-value-wrap">
            <span class="stat-num" data-target="659" data-suffix="">0</span>
          </div>
          <span class="stat-label">Citations</span>
        </div>

        <div class="stat-item">
          <div class="stat-icon" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><path d="M2 12h20"/></svg>
          </div>
          <div class="stat-value-wrap">
            <span class="stat-num" data-target="12" data-suffix="">0</span>
          </div>
          <span class="stat-label">h-index</span>
        </div>

        <div class="stat-item">
          <div class="stat-icon" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
          </div>
          <div class="stat-value-wrap">
            <span class="stat-num" data-target="10" data-suffix="+">0</span>"""

    html = re.sub(
        r'<span class="stat-num" data-target="8" data-suffix="">0</span>\s*</div>\s*<span class="stat-label">Publications</span>.*?<span class="stat-num" data-target="8" data-suffix="\+">0</span>',
        stats,
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = html.replace(
        '<span class="stat-label">Presentations</span>',
        '<span class="stat-label">Years in AI Research</span>',
    )

    about_section = """  <!-- ========== ABOUT ========== -->
  <section class="section" id="about">
    <div class="container">
      <p class="section-label">Who I Am</p>
      <h2 class="section-title">About Me</h2>
      <p class="section-subtitle">AI and data-science researcher specializing in remote sensing, computer vision, multimodal fusion, and intelligent sensing for real-world decision support.</p>

      <div class="about-grid">
        <div class="about-text">
          <p>I am an <strong>AI and data-science researcher</strong> specializing in remote sensing, computer vision, multimodal data fusion, spatiotemporal modeling, and intelligent sensing. I build computational methods that connect machine learning with observations from satellites, UAVs, IoT systems, environmental sensors, and field experiments.</p>
          <p>At the <strong>University of Florida UF/IFAS TREC</strong>, I develop scalable AI workflows for agricultural and environmental applications — including drone-image stitching and mapping, field-boundary extraction, water-stress analysis, disease identification, soil-moisture forecasting, sensor calibration, and multi-horizon prediction from weather and high-frequency field data.</p>
          <p>Previously I served as <strong>Assistant Professor of Computer Science</strong> and <strong>Director of International Partnerships</strong> at Debre Markos University, and completed postdoctoral and doctoral research in Taiwan on localization, mobility prediction, UAV-assisted communication, and object tracking. My goal is accurate, scalable, and robust AI that turns heterogeneous data into useful decisions for agriculture, climate resilience, public safety, and healthcare.</p>
        </div>

        <div class="about-highlights">
          <div class="highlight-card">
            <div class="highlight-icon-wrap" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
            </div>
            <div>
              <h3>Precision Agriculture &amp; GeoAI</h3>
              <p>UAV and satellite imagery, geospatial integration, and computer-vision pipelines for crop health, environmental monitoring, and field-scale analytics.</p>
            </div>
          </div>

          <div class="highlight-card">
            <div class="highlight-icon-wrap" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            </div>
            <div>
              <h3>Funded Interdisciplinary Research</h3>
              <p>Coordinated competitive projects in climate action, maize-disease detection, digital transformation, and health informatics — securing more than USD 100,000 in research funding at DMU.</p>
            </div>
          </div>

          <div class="highlight-card">
            <div class="highlight-icon-wrap" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            </div>
            <div>
              <h3>Intelligent Sensing Systems</h3>
              <p>IoT and environmental sensor integration, multimodal fusion, and HPC/GPU workflows for real-time monitoring and forecasting in South Florida field conditions.</p>
            </div>
          </div>

          <div class="highlight-card">
            <div class="highlight-icon-wrap" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/><path d="M2 12h20"/></svg>
            </div>
            <div>
              <h3>Global Research Experience</h3>
              <p>Research and academic leadership across the United States, Ethiopia, and Taiwan — spanning wireless IoT, public safety, agriculture, and environmental AI.</p>
            </div>
          </div>
        </div>
      </div>


    </div>
  </section>

  <hr class="section-divider" aria-hidden="true" />
"""

    html = replace_between(
        html,
        "  <!-- ========== ABOUT ========== -->",
        "  <!-- ========== NEWS + BLOG ========== -->",
        about_section,
    )

    news_section = """  <!-- ========== NEWS + BLOG ========== -->
  <section class="section section-alt" id="news">
    <div class="container">
      <p class="section-label">Latest Updates</p>
      <h2 class="section-title">News</h2>
      <p class="section-subtitle">Recent publications, presentations, and research milestones.</p>

      <div class="event-stream" data-see-more="6">

        <div class="event-row">
          <time class="event-date" datetime="2026-10">Oct 2026</time>
          <span class="event-badge event-badge--publication">Publication</span>
          <div class="event-body">
            <p class="event-title">Sorghum yield prediction paper accepted — Discover Sustainability</p>
            <p class="event-detail">Machine learning with multisource data for challenging agricultural environments in Ethiopia.</p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2026">2026</time>
          <span class="event-badge event-badge--publication">Publication</span>
          <div class="event-body">
            <p class="event-title">YOLO-based maize pest-and-disease classifier — Array</p>
            <p class="event-detail"><a href="https://doi.org/10.1016/j.array.2026.101170" target="_blank" rel="noopener noreferrer">DOI: 10.1016/j.array.2026.101170</a></p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2026-06">Jun 2026</time>
          <span class="event-badge event-badge--presentation">Presentation</span>
          <div class="event-body">
            <p class="event-title">ASABE 2026 — AI-based soil moisture forecasting for precision agriculture</p>
            <p class="event-detail">With G. Awoke and H. K. Bayabil · Adaptive feature engineering for field capacity detection.</p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2025-06">Jun 2025</time>
          <span class="event-badge event-badge--presentation">Presentation</span>
          <div class="event-body">
            <p class="event-title">ASABE Annual Meeting — Streamlining drone imagery for agricultural decisions</p>
            <p class="event-detail">Jupiter, Florida · UAV image analysis workflows for operational decision support.</p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2025">2025</time>
          <span class="event-badge event-badge--publication">Publication</span>
          <div class="event-body">
            <p class="event-title">Teff weed detection with deep learning and UAV imagery — Scientific Reports</p>
            <p class="event-detail"><a href="https://doi.org/10.1038/s41598-025-15380-3" target="_blank" rel="noopener noreferrer">DOI: 10.1038/s41598-025-15380-3</a></p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2024-06">Jun 2024</time>
          <span class="event-badge event-badge--position">Position</span>
          <div class="event-body">
            <p class="event-title">Postdoctoral Research Associate — UF/IFAS TREC</p>
            <p class="event-detail">Homestead, Florida · Multimodal AI for agricultural and environmental monitoring.</p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2023-06">Jun 2023</time>
          <span class="event-badge event-badge--award">Funding</span>
          <div class="event-body">
            <p class="event-title">Co-PI — AI for Climate Action Innovation Research Network</p>
            <p class="event-detail">WASCAL, RUFORUM, AKADEMIYA2063 · USD 60,000 · <a href="https://wordpress.ai4d.ai/project/ai-for-climate-action-innovation-research/" target="_blank" rel="noopener noreferrer">Project page</a></p>
          </div>
        </div>

        <div class="event-row">
          <time class="event-date" datetime="2020">2020</time>
          <span class="event-badge event-badge--publication">Publication</span>
          <div class="event-body">
            <p class="event-title">Ph.D. completed — National Taipei University of Technology</p>
            <p class="event-detail">Deep machine learning for position-aware services in IoT networks · Four journal articles from doctoral research.</p>
          </div>
        </div>

      </div>
      <div class="see-more-wrap">
        <button class="see-more-btn" aria-expanded="false"
                data-label-more="Show all news" data-label-less="Show less">
          Show all news
          <svg class="see-more-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
      </div>

      <div id="linkedinPostWidget" class="linkedin-widget" style="margin-top:48px;"></div>

    </div>
  </section>

  <hr class="section-divider" aria-hidden="true" />
"""

    html = replace_between(
        html,
        "  <!-- ========== NEWS + BLOG ========== -->",
        "  <!-- ========== RESEARCH ========== -->",
        news_section,
    )

    # Research cards — replace titles/descriptions in first 3 project cards
    html = html.replace(
        "Applying AI and multi-modal satellite data to advance understanding of the cryosphere and water cycle.",
        "Data-driven methods integrating UAV and satellite imagery, sensors, and spatiotemporal models for agriculture and the environment.",
    )
    html = html.replace("<h3>Multi-Modal Satellite Data Fusion</h3>", "<h3>Remote Sensing &amp; GeoAI</h3>")
    html = html.replace(
        "Developing CrossFuse - a hybrid CNN-Transformer architecture that fuses Sentinel-1 SAR and Sentinel-2 optical imagery to produce high-resolution snow cover and water equivalent estimates for runoff prediction.",
        "Satellite and UAV imagery, geospatial integration, mapping, field-boundary extraction, and remote-sensing workflows using Google Earth Engine, QGIS, ArcGIS, and Pix4D.",
    )
    html = html.replace("<span class=\"project-tag\">Sentinel-1 SAR</span>", "<span class=\"project-tag\">UAV Imagery</span>", 1)
    html = html.replace("<span class=\"project-tag\">Sentinel-2</span>", "<span class=\"project-tag\">Google Earth Engine</span>", 1)
    html = html.replace("<span class=\"project-tag\">CNN-Transformer</span>", "<span class=\"project-tag\">GeoAI</span>", 1)
    html = html.replace("<span class=\"project-tag\">Snow Hydrology</span>", "<span class=\"project-tag\">Precision Agriculture</span>", 1)

    html = html.replace("<h3>Deep Learning for Snow Segmentation</h3>", "<h3>Computer Vision for Agriculture</h3>")
    html = html.replace(
        "Designing mDeepLabV3+ with dilated convolutions and ResNet backbone to reliably separate snow from clouds in Sentinel-2 multispectral imagery - enabling year-round snow monitoring for water resource management.",
        "Deep learning for object detection, semantic segmentation, crop-disease identification, weed mapping, and vision-based sensing from UAV and ground platforms.",
    )
    html = html.replace("<span class=\"project-tag\">DeepLabV3+</span>", "<span class=\"project-tag\">YOLO</span>", 1)
    html = html.replace("<span class=\"project-tag\">ResNet</span>", "<span class=\"project-tag\">Transfer Learning</span>", 1)
    html = html.replace("<span class=\"project-tag\">Semantic Segmentation</span>", "<span class=\"project-tag\">Crop Health</span>", 1)
    html = html.replace("<span class=\"project-tag\">Cloud Detection</span>", "<span class=\"project-tag\">Field Monitoring</span>", 1)

    html = html.replace("<h3>AI for Climate &amp; Emergency Response</h3>", "<h3>Intelligent Sensing &amp; Forecasting</h3>")
    html = html.replace(
        "Leveraging NLP and social media analytics for real-time local climate impact monitoring, and building AI-enhanced early warning systems improving emergency communication ecosystems in Nordic countries.",
        "IoT and environmental sensor fusion, soil-moisture and weather-driven forecasting, HPC/GPU training, and decision-support systems for agriculture, climate, and public safety.",
    )
    html = html.replace("<span class=\"project-tag\">NLP</span>", "<span class=\"project-tag\">IoT Sensing</span>", 1)
    html = html.replace("<span class=\"project-tag\">Social Media Analytics</span>", "<span class=\"project-tag\">Time-Series ML</span>", 1)
    html = html.replace("<span class=\"project-tag\">Early Warning Systems</span>", "<span class=\"project-tag\">Sensor Fusion</span>", 1)
    html = html.replace("<span class=\"project-tag\">Climate AI</span>", "<span class=\"project-tag\">HPC / GPU</span>", 1)

    html = html.replace("<p class=\"research-anchor\">Observe <span aria-hidden=\"true\">→</span> Learn <span aria-hidden=\"true\">→</span> Predict</p>", "<p class=\"research-anchor\">Sense <span aria-hidden=\"true\">→</span> Fuse <span aria-hidden=\"true\">→</span> Decide</p>")
    html = html.replace("<span class=\"project-index\">01 — Observe</span>", "<span class=\"project-index\">01 — Sense</span>")
    html = html.replace("<h4 class=\"pillar-title\">Geospatial AI &amp; Earth Observation</h4>", "<h4 class=\"pillar-title\">Data Science &amp; Predictive Analytics</h4>")
    html = html.replace(
        "Scalable AI pipelines that fuse SAR, optical, multispectral, thermal, LiDAR, DEM, and climate reanalysis data into a single coherent view of the planet — from pixel-level classification to geophysical parameter retrieval at continental scale.",
        "Machine learning, statistical modeling, time-series forecasting, spatiotemporal modeling, feature engineering, and validation on large heterogeneous datasets.",
    )
    html = html.replace("<p class=\"project-row-meta\">SAR Fusion · Multi-Sensor · GeoAI · Sentinel</p>", "<p class=\"project-row-meta\">Forecasting · Ensembles · Spatiotemporal · Validation</p>")

    html = html.replace("<span class=\"project-index\">02 — Learn</span>", "<span class=\"project-index\">02 — Fuse</span>")
    html = html.replace("<h4 class=\"pillar-title\">Computer Vision &amp; Foundation Models</h4>", "<h4 class=\"pillar-title\">Remote Sensing &amp; Computer Vision</h4>")
    html = html.replace(
        "Semantic segmentation and scene understanding tailored to the scale, illumination, and spectral complexity of satellite imagery, adapting large geospatial foundation models (SAM, DINOv2, SatMAE, Prithvi) to downstream Earth-observation tasks.",
        "CNN, transformer, and YOLO architectures for detection, segmentation, and multimodal image analysis from UAV and satellite platforms.",
    )
    html = html.replace("<p class=\"project-row-meta\">Segmentation · SAM · DINOv2 · SatMAE · Prithvi</p>", "<p class=\"project-row-meta\">YOLO · CNN · Transformers · UAV · Satellite</p>")

    html = html.replace("<span class=\"project-index\">03 — Predict</span>", "<span class=\"project-index\">03 — Decide</span>")
    html = html.replace("<h4 class=\"pillar-title\">Environmental &amp; Climate Monitoring</h4>", "<h4 class=\"pillar-title\">Application Domains</h4>")
    html = html.replace(
        "Multi-temporal satellite analysis turned into hydrological and climate intelligence — snow water equivalent, flood mapping, land-cover change, and long-term cryosphere and ecosystem monitoring.",
        "Precision agriculture, soil moisture and water stress, disaster response, localization and tracking, healthcare AI, and digital transformation for policy.",
    )
    html = html.replace("<p class=\"project-row-meta\">Hydrology · Flood Mapping · Cryosphere · Climate AI</p>", "<p class=\"project-row-meta\">Agriculture · Environment · Public Safety · Health</p>")

    projects_inner = """
        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">01 — AgTech</span>
            <span class="project-status is-active">Active</span>
          </div>
          <h3 class="project-row-title">UF TREC Precision Agriculture AI</h3>
          <p class="project-row-desc">Multimodal workflows integrating UAV and satellite imagery, weather, and field sensors for soil-moisture forecasting, water-stress analysis, disease ID, and Fertilizer4Life soil-fertility support.</p>
          <p class="project-row-meta">Pix4D · GEE · PyTorch · TensorFlow · HPC · Homestead, FL</p>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">02 — Platform</span>
            <span class="project-status is-active">Active</span>
          </div>
          <h3 class="project-row-title">N-DIP — Nursery Disease Intelligence Platform</h3>
          <p class="project-row-desc">Multi-disease early-warning platform combining sensor and imagery data for detection, monitoring, and phenotype-based diagnosis in nursery environments.</p>
          <p class="project-row-meta">IoT · Computer Vision · Decision Support</p>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">03 — Software</span>
            <span class="project-status is-published">Deployed</span>
          </div>
          <h3 class="project-row-title">AgriSense AI</h3>
          <p class="project-row-desc">IoT-enabled application integrating real-time sensors, weather APIs, and ML models for environmental estimation, monitoring, and alerts.</p>
          <p class="project-row-meta">Python · IoT · Real-time Analytics</p>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">04 — Research Tool</span>
            <span class="project-status is-published">Released</span>
          </div>
          <h3 class="project-row-title">Deep Learning Studio</h3>
          <p class="project-row-desc">Desktop ML research platform with GUI workflows for CNN, RNN, and transformer development from preprocessing through evaluation.</p>
          <p class="project-row-meta">GUI · PyTorch · TensorFlow · Teaching &amp; Research</p>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">05 — Crop Vision</span>
            <span class="project-status is-published">Published</span>
          </div>
          <h3 class="project-row-title">Coffee &amp; Corn Disease Detection</h3>
          <p class="project-row-desc">Mobile and desktop transfer-learning systems for multiclass crop-disease detection with field-oriented recommendations (&gt;95% reported accuracy).</p>
          <p class="project-row-meta">YOLO · Mobile Deployment · Ethiopia field trials</p>
          <a class="project-row-link" href="https://doi.org/10.1016/j.array.2026.101170" target="_blank" rel="noopener noreferrer">Related publication <span aria-hidden="true">↗</span></a>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">06 — Climate</span>
            <span class="project-status is-published">Funded</span>
          </div>
          <h3 class="project-row-title">AI for Climate Action Innovation Research Network</h3>
          <p class="project-row-desc">Co-PI and project coordinator for WASCAL/RUFORUM/AKADEMIYA2063 network on AI for climate action (USD 60,000).</p>
          <p class="project-row-meta">2023–2024 · Debre Markos University</p>
          <a class="project-row-link" href="https://wordpress.ai4d.ai/project/ai-for-climate-action-innovation-research/" target="_blank" rel="noopener noreferrer">Project page <span aria-hidden="true">↗</span></a>
        </div>
"""

    html = replace_between(
        html,
        '      <div class="projects-grid" data-see-more="3">',
        "      </div>\n      <div class=\"see-more-wrap\">",
        '      <div class="projects-grid" data-see-more="3">' + projects_inner,
    )
    html = html.replace(
        "Selected research and engineering projects - from satellite image analysis to assistive robotics and climate AI.",
        "Research software, funded initiatives, and field-ready AI systems for agriculture, sensing, and climate.",
    )

    pub_featured = """
      <div class="pub-featured">
        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">01 · Applied Sciences · 2018</span>
          </div>
          <h3 class="project-row-title">Robust Indoor Localization (DNN)</h3>
          <p class="project-row-desc">Deep neural network for robust indoor localization in multi-building environments.</p>
          <p class="project-row-meta">105+ citations · DOI: 10.3390/app8071062</p>
          <a class="project-row-link" href="https://doi.org/10.3390/app8071062" target="_blank" rel="noopener noreferrer">Paper <span aria-hidden="true">↗</span></a>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">02 · IEEE IoT Journal · 2020</span>
          </div>
          <h3 class="project-row-title">GRU Mobility Prediction for IoT</h3>
          <p class="project-row-desc">Gated recurrent unit network for mobility predictions of IoT devices.</p>
          <p class="project-row-meta">74+ citations · DOI: 10.1109/JIOT.2019.2948075</p>
          <a class="project-row-link" href="https://doi.org/10.1109/JIOT.2019.2948075" target="_blank" rel="noopener noreferrer">Paper <span aria-hidden="true">↗</span></a>
        </div>

        <div class="project-card-full">
          <div class="project-row-top">
            <span class="project-index">03 · Scientific Reports · 2025</span>
          </div>
          <h3 class="project-row-title">Teff Weed Detection with UAV Deep Learning</h3>
          <p class="project-row-desc">Deep learning and UAV imagery for precision herbicide application in teff crops.</p>
          <p class="project-row-meta">21+ citations · DOI: 10.1038/s41598-025-15380-3</p>
          <a class="project-row-link" href="https://doi.org/10.1038/s41598-025-15380-3" target="_blank" rel="noopener noreferrer">Paper <span aria-hidden="true">↗</span></a>
        </div>
      </div>
"""

    html = re.sub(
        r'<div class="pub-featured">.*?</div>\s*\n\s*<h3 class="subsection-title">All Publications</h3>',
        pub_featured + '\n\n      <h3 class="subsection-title">All Publications</h3>',
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = html.replace(
        "8 publications · 50+ citations - journals, conference papers, and preprints in AI, remote sensing, and hydrology.",
        "18+ peer-reviewed journal articles · 659 citations (Google Scholar, Oct 2026) — AI, remote sensing, IoT, and agriculture.",
    )

    pubs_all = publications_all_html()
    html = replace_between(
        html,
        '      <!-- 2026 -->',
        '      <div id="pubNoResults"',
        "      " + pubs_all.strip() + "\n\n      ",
    )

    html = html.replace(
        'href="https://scholar.google.com/citations?user=Xz_tNToAAAAJ&hl=en"',
        f'href="{SCHOLAR}"',
    )
    html = html.replace("user=Xz_tNToAAAAJ", "user=OZc5w3YAAAAJ")

    # Service section header
    html = html.replace("<h2 class=\"section-title\">Academic Service</h2>", "<h2 class=\"section-title\">Leadership &amp; Service</h2>")
    html = html.replace(
        "Workshop organisation, conference activities, and professional contributions to the research community.",
        "Institutional leadership, editorial service, peer review, and conference contributions.",
    )

    service_layout = """
      <div class="service-layout">
        <div class="service-block">
          <div class="service-block-header">
            <div class="service-block-icon" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
            </div>
            <h3>Leadership</h3>
          </div>
          <div class="service-event">
            <div class="service-event-dot"></div>
            <div>
              <p class="service-event-title">Director, International Partnerships — DMU</p>
              <p class="service-event-meta">2021–2024 · Academic exchange, joint research, and international grant development</p>
            </div>
          </div>
          <div class="service-event">
            <div class="service-event-dot dot-accent"></div>
            <div>
              <p class="service-event-title">AI Cross-Disciplinary Research Coordinator</p>
              <p class="service-event-meta">Interdisciplinary AI teams in agriculture, health, and climate adaptation</p>
            </div>
          </div>
          <div class="service-event">
            <div class="service-event-dot dot-purple"></div>
            <div>
              <p class="service-event-title">University Strategy &amp; Research Policy</p>
              <p class="service-event-meta">Five-year research strategy and policy for interdisciplinary collaboration (2020–2024)</p>
            </div>
          </div>
        </div>

        <div class="service-block">
          <div class="service-block-header">
            <div class="service-block-icon" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="22" height="22"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            </div>
            <h3>Editorial &amp; Review</h3>
          </div>
          <div class="service-event">
            <div class="service-event-dot"></div>
            <div>
              <p class="service-event-title">Associate Editor — Advanced Journal of Interdisciplinary Studies</p>
              <p class="service-event-meta">2022–2024</p>
            </div>
          </div>
          <div class="service-event">
            <div class="service-event-dot dot-accent"></div>
            <div>
              <p class="service-event-title">Peer reviewer — IEEE, MDPI, Springer Nature, Elsevier, SAGE</p>
              <p class="service-event-meta">Journals and conferences including ICT4DA, IEEE ICPAI, EAI ICAST, IEEE GLOBECOM</p>
            </div>
          </div>
          <div class="service-event">
            <div class="service-event-dot dot-purple"></div>
            <div>
              <p class="service-event-title">Conference presentations — ASABE, IEEE VTC, ICPAI</p>
              <p class="service-event-meta">Soil moisture forecasting, UAV networks, and IoT localization research</p>
            </div>
          </div>
        </div>
      </div>
"""

    html = replace_between(
        html,
        '      <div class="service-layout">',
        '      <div class="skills-redesign">',
        service_layout.strip() + "\n\n      ",
    )

    html = html.replace(
        "<p class=\"skills-summary\">Python · PyTorch · TensorFlow · Google Earth Engine · GDAL · QGIS · Docker · HPC</p>",
        "<p class=\"skills-summary\">Python · PyTorch · TensorFlow · R · MATLAB · Google Earth Engine · QGIS · ArcGIS · Pix4D · CUDA · HPC</p>",
    )
    html = html.replace("Foundation Models &amp; MLOps", "Intelligent Sensing &amp; HPC")
    html = html.replace("<span class=\"skill-pill\"><img src=\"https://cdn.simpleicons.org/meta/ffffff\"", "<span class=\"skill-pill\">Environmental Sensors")
    # Fix broken skill pills - simpler replace for FM section pills
    html = re.sub(
        r'<div class="skill-cat skill-cat--fm">.*?</div>\s*\n\s*<div class="skill-cat skill-cat--prog">',
        """<div class="skill-cat skill-cat--fm">
            <div class="skill-cat-head">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
              Intelligent Sensing &amp; HPC
            </div>
            <div class="skill-pills">
              <span class="skill-pill">IoT &amp; Sensor Networks</span>
              <span class="skill-pill">Multimodal Fusion</span>
              <span class="skill-pill">CUDA / GPU</span>
              <span class="skill-pill">MLflow</span>
              <span class="skill-pill"><img src="https://cdn.simpleicons.org/docker/2496ED" class="sp-icon" alt="" width="13" height="13" loading="lazy"> Docker</span>
              <span class="skill-pill">Cloud Workflows</span>
              <span class="skill-pill"><img src="https://cdn.simpleicons.org/linux/FCC624" class="sp-icon" alt="" width="13" height="13" loading="lazy"> Linux / HPC</span>
            </div>
          </div>

          <div class="skill-cat skill-cat--prog">""",
        html,
        count=1,
        flags=re.DOTALL,
    )

    lang_strip = """
        <div class="lang-strip">
          <div class="lang-card">
            <span class="lang-name">Amharic</span>
            <span class="lang-badge lang-badge--native">Native</span>
          </div>
          <div class="lang-card">
            <span class="lang-name">English</span>
            <span class="lang-badge lang-badge--professional">Professional</span>
          </div>
        </div>"""
    html = re.sub(
        r'<div class="lang-strip">.*?</div>\s*</div>\s*</div>\s*</section>',
        lang_strip + "\n      </div>\n    </div>\n  </section>",
        html,
        count=1,
        flags=re.DOTALL,
    )

    cv_sub = "Academic training, research positions, and leadership across the United States, Ethiopia, and Taiwan."
    html = html.replace(
        "Academic training, research positions, international visits, and professional experience across five countries.",
        cv_sub,
    )

    cv_timeline = """
      <!-- Research & Positions -->
      <div class="tl-group" aria-label="Research and positions">
        <h3 class="tl-group-title">Research &amp; Positions</h3>
        <div class="cv-timeline">

          <div class="cv-entry cv-entry--left" data-category="position">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2024">June 2024 – present</time>
              <span class="tl-cat">Current Position</span>
              <p class="tl-headline">Postdoctoral Research Associate — UF/IFAS TREC</p>
              <p class="tl-body">Multimodal AI integrating UAV and satellite imagery, environmental sensors, and field data for agricultural and environmental monitoring, forecasting, and decision support in Homestead, Florida.</p>
              <span class="timeline-badge">Current Position</span>
            </div>
          </div>

          <div class="cv-entry cv-entry--right" data-category="position">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2021">Jan 2021 – Jun 2024</time>
              <span class="tl-cat">Faculty</span>
              <p class="tl-headline">Assistant Professor of Computer Science — Debre Markos University</p>
              <p class="tl-body">Led AI and data-science research; Co-PI for AI for Climate Action; secured USD 100k+ funding; taught AI/ML courses; supervised graduate researchers; Director of International Partnerships.</p>
            </div>
          </div>

          <div class="cv-entry cv-entry--left" data-category="position">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2020">Feb – Dec 2020</time>
              <span class="tl-cat">Postdoc</span>
              <p class="tl-headline">Postdoctoral Researcher — NYCU, Taiwan</p>
              <p class="tl-body">Multimodal fusion for pedestrian detection and forecasting; UAV and IoT field experiments.</p>
            </div>
          </div>

          <div class="cv-entry cv-entry--right" data-category="position">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2016">Sep 2016 – Jan 2020</time>
              <span class="tl-cat">Doctoral Research</span>
              <p class="tl-headline">Research Scholar — National Taipei University of Technology</p>
              <p class="tl-body">Deep learning for localization, mobility prediction, object detection, and tracking in IoT and public-safety applications.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- Education -->
      <div class="tl-group" aria-label="Education" style="margin-top:48px;">
        <h3 class="tl-group-title">Education</h3>
        <div class="cv-timeline">

          <div class="cv-entry cv-entry--left" data-category="education">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2020">2020</time>
              <span class="tl-cat">Doctoral Degree</span>
              <p class="tl-headline">Ph.D., Electrical Engineering and Computer Science</p>
              <p class="tl-body">National Taipei University of Technology, Taiwan. Dissertation: deep machine learning for position-aware services in IoT networks.</p>
              <span class="timeline-badge">Taiwan Govt. Scholarship 2016–2020</span>
            </div>
          </div>

          <div class="cv-entry cv-entry--right" data-category="education">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2011">2011</time>
              <span class="tl-cat">Master's Degree</span>
              <p class="tl-headline">M.Sc., Information Science</p>
              <p class="tl-body">Addis Ababa University, Ethiopia. Thesis on rule-based information retrieval for Ge'ez text.</p>
            </div>
          </div>

          <div class="cv-entry cv-entry--left" data-category="education">
            <div class="cv-dot"></div>
            <div class="cv-card">
              <time class="tl-date" datetime="2007">2007</time>
              <span class="tl-cat">Bachelor's Degree</span>
              <p class="tl-headline">B.Sc., Computer Science</p>
              <p class="tl-body">Addis Ababa University, Ethiopia. Capstone expert system for diabetic disease diagnosis.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- CV PDF -->
      <div class="flowcv-wrap" style="margin-top:48px;">
        <div class="flowcv-header">
          <h3 class="flowcv-title">Curriculum Vitae (PDF)</h3>
          <div class="flowcv-actions">
            <a class="btn btn-primary btn-sm" href="files/Abebe_Adege_Master_CV_2026.pdf" target="_blank" rel="noopener noreferrer">
              Open Full CV
            </a>
            <a class="btn btn-ghost btn-sm" href="files/Abebe_Adege_Master_CV_2026.pdf" download>
              Download PDF
            </a>
          </div>
        </div>
        <div class="flowcv-frame-wrap">
          <iframe
            src="files/Abebe_Adege_Master_CV_2026.pdf"
            class="flowcv-iframe"
            title="Abebe B. Adege — Curriculum Vitae"
            loading="lazy"
          ></iframe>
        </div>
      </div>
"""

    html = replace_between(
        html,
        "      <!-- Research & Positions -->",
        "    </div>\n  </section>\n\n  <!-- ========== FOOTER ========== -->",
        cv_timeline.strip() + "\n\n    ",
    )

    footer = """
  <footer class="footer" id="contact">
    <div class="footer-inner container">
      <div class="footer-socials-only" aria-label="Contact and profiles">
        <a class="footer-social-link" href="mailto:abebeadege@ufl.edu" title="Email" aria-label="Email">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </a>
        <a class="footer-social-link" href="https://www.linkedin.com/in/abebe-belay-adege-9730701a0/" target="_blank" rel="noopener noreferrer" title="LinkedIn" aria-label="LinkedIn">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="15" height="15"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        </a>
        <a class="footer-social-link" href="https://scholar.google.com/citations?user=OZc5w3YAAAAJ&amp;hl=en" target="_blank" rel="noopener noreferrer" title="Google Scholar" aria-label="Google Scholar">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="15" height="15"><path d="M5.242 13.769L0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 100 14 7 7 0 000-14z"/></svg>
        </a>
        <a class="footer-social-link" href="https://ieeexplore.ieee.org/author/37086392659" target="_blank" rel="noopener noreferrer" title="IEEE" aria-label="IEEE">
          IEEE
        </a>
      </div>
      <p class="footer-copy-center">Abebe B. Adege, Ph.D. · Postdoctoral Research Associate · UF/IFAS TREC · Homestead, FL</p>
      <p class="footer-copy-center">&copy; <span id="year"></span> Abebe Belay Adege</p>
    </div>
  </footer>
"""

    html = replace_between(
        html,
        "  <!-- ========== FOOTER ========== -->",
        "  <script src=\"js/main.js\">",
        footer,
    )

    # Nav: remove blog tab link behavior target - simplify nav
    html = html.replace("<li><a href=\"#blog\">Blog</a></li>", "")
    html = html.replace("<li><a href=\"#service\">Activity</a></li>", "<li><a href=\"#service\">Leadership</a></li>")

    if "Getnet" in html or "getnet" in html.lower():
        print("WARNING: leftover Getnet references may remain")

    INDEX.write_text(html, encoding="utf-8")
    print("Patched", INDEX)


if __name__ == "__main__":
    main()
