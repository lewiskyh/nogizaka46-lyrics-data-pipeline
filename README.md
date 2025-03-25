# 🎤 Nogizaka46 Lyrics Data Pipeline (乃木坂46 歌詞數據工程專案)

This project is a personal data engineering portfolio project that combines my interest in Nogizaka46 with end-to-end data engineering skills.  
It collects, processes, and analyzes lyrics from Nogizaka46 songs, then stores the data in an **Azure SQL Database**, and presents the results via a **Streamlit web application**.

---

## 🔍 Project Overview / 專案簡介

| 階段 | 說明 |
|------|------|
| **資料來源** | 歌詞網站（Uta-Net / J-Lyric） |
| **資料擷取** | 使用 Python 網路爬蟲擷取歌詞與歌曲資訊 |
| **資料清洗** | 使用 `pandas` + `fugashi` 處理日文歌詞、斷詞、清洗 |
| **資料儲存** | 儲存至 Azure SQL Database 作為資料倉儲 |
| **展示層** | 使用 Streamlit 製作互動式分析介面（詞頻、情感分析） |

---

## 🧱 Tech Stack / 使用技術

- **Python**: `requests`, `BeautifulSoup`, `pandas`, `fugashi`, `sqlalchemy`
- **Azure SQL Database**: 雲端資料儲存與結構設計
- **Streamlit**: 構建Web應用，展示分析結果
- **Power BI (Optional)**: 額外的BI呈現選項
- **GitHub**: 版本控制與公開展示

---

## 📊 Features & Goals / 功能與目標

- ✅ 自動化擷取乃木坂46歌詞資料
- ✅ 清洗與斷詞處理，支援日文自然語言
- ✅ 匯入 Azure SQL Database 模擬 Data Warehouse
- ✅ 建立 Streamlit App 展示分析結果
- 🚧（未來）情感分析、主題建模、成員貢獻分析

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

