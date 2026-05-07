import os
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://investors.monsterbevcorp.com/financial-information/annual-reports"
OUTPUT_DIR = "data/raw/monster_reports"

#Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

#Webpage
response = requests.get(BASE_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

#Pdfs
pdf_links = []

for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.lower().endswith(".pdf"):
        #Try to extract year from link text or filename
        text = link.get_text(strip=True)
        year_match = re.search(r"(20\d{2})", text) or re.search(r"(20\d{2})", href)

        if year_match:
            year = int(year_match.group(1))
            full_url = href if href.startswith("http") else "https://investors.monsterbevcorp.com" + href

            pdf_links.append({"year": year, "url": full_url})

# Sort by year (descending)
pdf_links = sorted(pdf_links, key=lambda x: x["year"], reverse=True)

#Download pdfs
for item in pdf_links:
    year = item["year"]
    url = item["url"]

    filename = f"monster_{year}.pdf"
    filepath = os.path.join(OUTPUT_DIR, filename)

    pdf_data = requests.get(url)
    pdf_data.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(pdf_data.content)
