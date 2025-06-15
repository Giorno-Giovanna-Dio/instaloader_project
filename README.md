# Instagram Public Post Collector - Anti-RateLimit Stable Version

## 📌 Project Overview

This project utilizes Python + Instaloader to collect public posts from a specified Instagram account, extracting post content, like counts, comment counts, and exporting the data into both Excel and JSON formats. The collected data can be used for downstream Natural Language Processing (NLP), behavioral analysis, sentiment analysis, and other research applications.

This version has been optimized to handle Instagram's recent anti-scraping restrictions by introducing randomized delays and controlled request frequencies to minimize the risk of being temporarily blocked.

---

## ✅ Current Functionalities

- [x] Session-based authenticated login
- [x] Public post extraction for any target account
- [x] Extracted data includes:
  - Post date
  - Post caption
  - Like count
  - Comment count
- [x] Supports both Excel and JSON export formats
- [x] Random sleep intervals and batch-based throttling for anti-rate-limit protection
- [x] Basic error handling with auto-retry logic

---

## ⚠️ Current Challenges

- Instagram has strengthened its anti-scraping mechanisms, particularly against `profile.get_posts()` which internally relies on the GraphQL API (`graphql/query`), resulting in:
  - 401 Unauthorized errors
  - "Please wait a few minutes before you try again." rate-limit messages
  - Temporary access restrictions triggered by high-frequency requests

- Instaloader's native `get_posts()` method has become increasingly unreliable for scraping public accounts, requiring architectural adjustments.

---

## 🚀 Future Development Roadmap

### 📊 Technical Directions
- [ ] V3.0 Add checkpoint & resume feature (continue from last successfully scraped post)
- [ ] V3.1 Multi-profile batch processing support
- [ ] V3.2 Proxy pool & IP rotation integration for enhanced stability
- [ ] V3.3 Switch to Selenium + Headless Browser Anti-Bot architecture (long-term stable version)
- [ ] V3.4 Text cleaning pipeline for NLP preprocessing (emoji, special character filtering)

### 📈 Analytical Directions
- [ ] Keyword frequency & topic modeling analysis
- [ ] Sentiment classification & opinion mining
- [ ] Influence score modeling with integrated social metrics

---

## 💡 Technical Notes

- This project is built on Instaloader combined with:
  - pandas
  - openpyxl
  - json
  - time / random for throttling
- Required packages installation:
  ```bash
  pip install instaloader pandas openpyxl
  
👨‍💻 Research Motivation
This project was originally developed as part of an AI/NLP data collection experiment, focusing on large-scale semantic understanding of social media content. The collected dataset will be used for academic research and AI-driven analytical model development.

🔒 Legal Disclaimer
This project is strictly for academic and non-commercial use, and must comply with Instagram's Terms of Service and applicable local laws.
Users are responsible for assessing and bearing any risks associated with the scraping process.
