#!/usr/bin/env python3
"""Generate HTML fragments for Abebe site (run once to patch index.html)."""

SCHOLAR = "https://scholar.google.com/citations?user=OZc5w3YAAAAJ&hl=en"

JOURNALS = [
    (2026, "Discover Sustainability", "journal", "Machine Learning-Based Sorghum Yield Prediction Using Multisource Data in Challenging Agricultural Environments of Ethiopia.", "Adege, A. B., Abate, A. W., Nigussie, Y. M., Limenih, H. H., Eneyew, L. M., and Aycheh, D. A.", "Accepted 7 October 2026.", None),
    (2026, "Array", "journal", "YOLO-Based Transfer Learning for Accurate and Efficient Pest-and-Disease Classifier of Maize Crop.", "Adege, A. B., Murugan, T., Mohamed, A. A., Ahamed, N. N., Megersa, Z. M., Alemu, G., Hasen, J. Y., and Abebe, N. A.", "31, 101170.", "https://doi.org/10.1016/j.array.2026.101170"),
    (2026, "Computers", "journal", "Research Advances in Maize Crop Disease Detection Using Machine Learning and Deep Learning Techniques.", "Murugan, T., Ahamed, N. N., Musa, N. S., Alahbabi, E. M., Alyammahi, R. A. A., Adege, A. B., Abdi, A., and Megersa, Z. M.", "15(2), 99.", "https://doi.org/10.3390/computers15020099"),
    (2026, "Discover Global Society", "journal", "Digital Transformation Maturity in Ethiopia's Priority Sectors.", "Fikirte, Z., Adege, A. B., Getinet, T., Anchala, C., and Wassie, G.", "4(1), 29.", "https://doi.org/10.1007/s44282-026-00347-0"),
    (2025, "Scientific Reports", "journal", "Detection of Weeds in Teff Crops Using Deep Learning and UAV Imagery for Precision Herbicide Application.", "Kebede, A. S., Muluneh, T. W., and Adege, A. B.", "15, 30708.", "https://doi.org/10.1038/s41598-025-15380-3"),
    (2025, "International Journal of Clinical Practice", "journal", "Advancing Biomedical Engineering with Artificial Intelligence and Machine Learning: A Review.", "Adege, A. B.", "9888902.", "https://doi.org/10.1155/ijcp/9888902"),
    (2025, "IET Image Processing", "journal", "AI-Powered Human Activity Detection and Tracking in Dense Crowds Using YOLOv8-DeepSORT.", "Adege, A. B., Admas, M. F., Tehone, Y., Tulu, B. B., and Endalamaw, E. T.", "19(1), e70227.", "https://doi.org/10.1049/ipr2.70227"),
    (2025, "Digital Health", "journal", "Integrating Expert Knowledge with Machine Learning for AI-Based Stroke Identification and Treatment Systems.", "Yimenu, T. K., Adege, A. B., and Techan, S. Y.", "11.", "https://doi.org/10.1177/20552076251336853"),
    (2025, "IEEE Access", "journal", "Automatic Identification of Amharic Text Idiomatic Expressions Using a Deep Learning Approach.", "Limenih, H. H., Adege, A. B., Alene, A. Y., Demasu, H. T., and Belachew, H. M.", None, "https://doi.org/10.1109/ACCESS.2025.3567811"),
    (2025, "Agronomy Journal", "journal", "On-Farm Observations of Socio-Environmental Impacts of Humulus lupulus L. Cultivation in Brazil.", "Viriato, V., Rodrigues, G. S., Nunes, M. R., Adege, A. B., and Bonfim, F. P. G.", "117(5), e70175.", "https://doi.org/10.1002/agj2.70175"),
    (2024, "Advanced Journal of Interdisciplinary Studies", "journal", "Real-Time Pedestrian Detection and Tracking in Disaster Areas Using Deep Learning Algorithms.", "Adege, A. B.", "1206–1218.", None),
    (2024, "Knowledge", "journal", "Real-Time Common Rust Maize Leaf Disease Severity Identification and Pesticide Dose Recommendation Using Deep Neural Network.", "Megersa, Z. M., Adege, A. B., and Rashid, F.", "4(4), 615–634.", "https://doi.org/10.3390/knowledge4040032"),
    (2020, "IEEE Internet of Things Journal", "journal", "Mobility Predictions for IoT Devices Using a Gated Recurrent Unit Network.", "Adege, A. B., Lin, H. P., and Wang, L. C.", "7(1), 505–517.", "https://doi.org/10.1109/JIOT.2019.2948075"),
    (2020, "IEEE Internet of Things Journal", "journal", "D-FOPS: Deep-Learning-Based Fingerprinting Outdoor Positioning Scheme in Hybrid Networks.", "Tarekegn, G. B., Juang, R. T., Lin, H. P., Adege, A. B., and Munaye, Y. Y.", "8(5), 3717–3729.", "https://doi.org/10.1109/JIOT.2020.3024845"),
    (2020, "Microelectronics Reliability", "journal", "Deep Learning Approach to Channel Selection Strategy for Minimizing Co-Channel Interference in Unlicensed Channels.", "Yen, L., Adege, A. B., Lin, H. P., Ho, C., and Lever, K.", "105, 113558.", "https://doi.org/10.1016/j.microrel.2019.113558"),
    (2019, "Sensors", "journal", "UAV Positioning for Throughput Maximization Using Deep Learning Approaches.", "Munaye, Y. Y., Lin, H. P., Adege, A. B., and Tarekegn, G. B.", "19(12), 2775.", "https://doi.org/10.3390/s19122775"),
    (2018, "Applied Sciences", "journal", "Applying Deep Neural Network (DNN) for Robust Indoor Localization in a Multi-Building Environment.", "Adege, A. B., Lin, H. P., Tarekegn, G. B., and Jeng, S. S.", "8(7), 1062.", "https://doi.org/10.3390/app8071062"),
    (2018, "Journal of Sensors", "journal", "Indoor and Outdoor Positioning Using a Hybrid of Support Vector Machine and Deep Neural Network Algorithms.", "Adege, A. B., Lin, H. P., Tarekegn, G. B., Munaye, Y. Y., and Yen, L.", "2018, 1–12.", "https://doi.org/10.1155/2018/1253752"),
]

CONFERENCES = [
    (2026, "ASABE 2026", "conference", "AI-Based Soil Moisture Forecasting and Field Capacity Detection Using Adaptive Feature Engineering for Precision Agriculture.", "Adege, A. B., Awoke, G., and Bayabil, H. K.", "June 10–12, 2026.", None),
    (2025, "ASABE Annual Meeting", "conference", "Streamlining Drone Imagery Analysis for Agricultural Decision-Making.", "Adege, A. B., Tulu, B. B., Teshome, F., Awoke, G., Hussain, S., and Bayabil, H. K.", "Jupiter, Florida, 11–13 June 2025.", None),
    (2025, "EAI ICAST 2025", "conference", "Spatio-Temporal Deep Learning for Video Filtering and Safe Content Governance in Digital Platforms.", "Tulu, B. B., Fante, K. A., Shewajo, F. A., Endalamaw, E. T., and Adege, A. B.", None, None),
    (2020, "IEEE ICPAI 2020", "conference", "Improving UAV Personalized-Tracking Services by Fusing Visual and Radio Data.", "Adege, A. B., Li, Y. R., Shuai, H. H., Lin, H. P., and Wang, L. C.", None, "https://doi.org/10.1109/ICPAI.2020.00009"),
    (2019, "IEEE CCNC 2019", "conference", "Machine Learning Based Rapid 3D Channel Modeling for UAV Communication Networks.", "Wang, J. L., Li, Y. R., Adege, A. B., Wang, L. C., Jeng, S. S., and Chen, J. Y.", None, None),
    (2019, "IEEE VTC 2019-Fall", "conference", "Deep Learning-Based Throughput Estimation for UAV-Assisted Network.", "Munaye, Y. Y., Adege, A. B., Tarekegn, G. B., Li, Y. R., Lin, H. P., and Jeng, S. S.", None, "https://doi.org/10.1109/VTCFall.2019.8891283"),
]


def bold_adege(authors: str) -> str:
    parts = authors.replace("Adege, A. B.", "<strong>Adege, A. B.</strong>")
    parts = parts.replace("A. B. Adege", "<strong>A. B. Adege</strong>")
    return parts


def pub_card(year, venue_label, ptype, title, authors, venue_detail, link):
    badge = "pub-badge-journal" if ptype == "journal" else "pub-badge-conf"
    badge_text = "Journal" if ptype == "journal" else "Conference"
    title_html = (
        f'<a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a>'
        if link
        else title
    )
    venue_line = f"<em>{venue_label}</em>"
    if venue_detail:
        venue_line += f", {venue_detail}"
    return f"""
          <div class="publication-card" data-type="{ptype}">
            <div class="pub-meta-row">
              <span class="pub-badge {badge}">{badge_text}</span>
              <span class="pub-cites">{venue_label}</span>
            </div>
            <p class="pub-title">{title_html}</p>
            <p class="pub-authors">{bold_adege(authors)}</p>
            <p class="pub-venue">{venue_line}</p>
          </div>"""


def publications_all_html():
    by_year = {}
    for row in JOURNALS + CONFERENCES:
        y = row[0]
        by_year.setdefault(y, []).append(row)
    chunks = []
    for year in sorted(by_year.keys(), reverse=True):
        cards = "".join(pub_card(*r) for r in by_year[year])
        count = len(by_year[year])
        chunks.append(f"""
      <div class="pub-year-group">
        <div class="pub-year-label" data-count="{count}">{year}</div>
        <div class="publications-list">{cards}
        </div>
      </div>""")
    return "\n".join(chunks)


if __name__ == "__main__":
    print(publications_all_html())
