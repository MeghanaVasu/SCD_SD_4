 Created by - Meghana V
🕸️ SkillCraft Technology — Web Scraper Task

 A highly efficient, automated Python application designed to extract product parameters—including names, structured prices, and star ratings—from an online e-commerce infrastructure. The extracted data is processed dynamically and mapped into a structured CSV dataset.

This repository serves as my official project submission for the **SkillCraft Technology Web Scraping Internship Portfolio**.

---

Key Framework Features:

* Data Optimization: Extracts raw structural targets (`Product Name`, `Price`, `Rating`) smoothly from target document structures.
* Smart Name Truncation: Automatically enforces a maximum length (`MAX_NAME_LENGTH = 25`) to simplify long catalog strings for a cleaner spreadsheet viewport.
* Dynamic Currency Conversion: Parses baseline European market prices (GBP) and updates them to Indian Rupees (₹) using dynamic runtime processing.
* Excel Alignment Fix:Utilizes the UTF-8 with BOM (`utf-8-sig`) encoding format, eliminating typical spreadsheet formatting bugs and instantly generating perfectly populated rows and cells upon loading.
* Runtime Guardrails: Standardized `try-except` defensive blocks to insulate the loop from breaking on unpopulated DOM attributes.

---

System Requirements & Architecture:

The application is written in vanilla Python 3 using highly performant extraction frameworks.

* Python 3.x
* Requests (HTTP network request engine)
* BeautifulSoup4 (HTML parser and DOM navigator)

---

Installation & Local Deployment

Follow these quick commands to spin up the automation workspace locally:

```bash
# Clone this repository to your machine
git clone [https://github.com/MeghanaVasu/SkillCraft-Web-Scraper.git]
# Move into the deployment workspace
cd SkillCraft-Web-Scraper

# Install core extraction dependencies
pip install requests beautifulsoup4

# Run the automation script
python scraper.py
