import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

SONG_URLS = {
    "君の名は希望": "https://j-lyric.net/artist/a0560d3/l02c306.html",
    "インフルエンサー": "https://j-lyric.net/artist/a0560d3/l03ec2d.html",
}


def scrape_lyrics(url):
    """Scrape from J-Lyric"""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    """print(soup.prettify())"""
    lyrics_p = soup.find("p", id="Lyric")

    if lyrics_p:
        lyrics_text = lyrics_p.get_text(separator="\n", strip=True)
        lines = lyrics_text.split("\n")
        return lines
    else:
        return []


def main():
    all_rows = []

    for title, url in SONG_URLS.items():
        print(f"Scraping {title}")
        lines = scrape_lyrics(url)

        for i, line in enumerate(lines):
            if line.strip():
                all_rows.append({
                    "song_title": title,
                    "line_number": i+1,
                    "line_text": line.strip()
                })
        time.sleep(2)

    df = pd.DataFrame(all_rows)
    df.to_csv("../data/processed/lyrics_cleaned.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()
