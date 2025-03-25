# 🎤 Nogizaka46 Lyrics Data Pipeline (乃木坂46 歌詞數據工程專案)

This project is a personal data engineering portfolio project that combines my interest in Nogizaka46 with end-to-end data engineering skills.  
It collects, processes, and analyzes lyrics from Nogizaka46 songs, then stores the data in an **Azure SQL Database**, and presents the results via a **Streamlit web application**.

---

## 🔍 Project Overview

| Stage            | Description |
|------------------|-------------|
| **Data Source**  | Lyrics websites (e.g. Uta-Net, J-Lyric) |
| **Ingestion**    | Python-based web scraping (lyrics + metadata) |
| **Cleaning & NLP** | Japanese tokenization using `fugashi` (MeCab wrapper) |
| **Storage**      | Structured data stored in Azure SQL Database |
| **Visualization**| Streamlit app showing frequency charts, lyric insights |

---

## 🧱 Tech Stack

- **Python**: `requests`, `BeautifulSoup`, `pandas`, `fugashi`, `sqlalchemy`
- **Azure SQL Database**: Cloud-based data warehouse
- **Streamlit**: Interactive data visualization web app
- **Power BI (Optional)**: Business Intelligence dashboard (extra)
- **GitHub**: Version control and project sharing

---

## 📊 Features & Goals

- ✅ Automatically scrape Nogizaka46 lyrics and metadata
- ✅ Clean and tokenize Japanese text using NLP tools
- ✅ Load structured data into Azure SQL Database
- ✅ Build an interactive Streamlit web app for visualizing results
- 🚧 (Planned) Sentiment analysis, topic modeling, member-level contribution analysis

---

## 🗂️ Folder Structure

```bash
nogizaka46-lyrics-data-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── scrape_lyrics.py
│   └── clean_lyrics.py
├── sql/
│   └── create_tables.sql
├── app/
│   └── lyrics_app.py
├── README.md
└── requirements.txt
```

## How to Run

1.	Clone this repo 
2. Install dependencies: pip install -r requirements.txt 
3. Run Streamlit app:

```bash
cd app
streamlit run lyrics_app.py
```

