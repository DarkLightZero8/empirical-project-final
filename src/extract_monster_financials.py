import os
import re
import pdfplumber
import pandas as pd

#Setup
PDF_DIR = "data/raw/monster_reports"
OUTPUT_FILE = "data/processed/monster_sales.csv"

os.makedirs("data/processed", exist_ok=True)

#Regex to grab numbers
SALES_REGEX = re.compile(
    r"(?i)(net sales[^0-9$]*)(\$?\s?[\d,]+(?:\.\d+)?)(?:\s*(billion|million)?)"
)

#Func
def extract_sales_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    match = SALES_REGEX.search(text)
    if not match:
        return None

    raw_number = match.group(2)
    unit = match.group(3)

    #Clean
    number = float(raw_number.replace("$", "").replace(",", ""))

    #Convert to USD millions
    if unit and unit.lower() == "billion":
        number = number * 1000
    elif unit and unit.lower() == "million":
        number = number
    else:
        number = number

    return number

records = []

#Pull loop
for filename in os.listdir(PDF_DIR):
    if filename.endswith(".pdf"):
        year_match = re.search(r"(20\d{2})", filename)
        if not year_match:
            continue
        year = int(year_match.group(1))
        pdf_path = os.path.join(PDF_DIR, filename)
        sales_value = extract_sales_from_pdf(pdf_path)

#Save
df = pd.DataFrame(records).sort_values("year")
df.to_csv(OUTPUT_FILE, index=False)