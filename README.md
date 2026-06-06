# 📚 Book Data Scraper using Python

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Data Analytics Internship**.

The objective of this project is to extract book information from a website using Python Web Scraping techniques and store the collected data in a structured CSV file for further analysis.

The scraper collects data from the Books to Scrape website and generates a custom dataset containing details about books available on the site.

---

## 🎯 Objectives

- Understand the fundamentals of Web Scraping.
- Extract data from HTML web pages.
- Create a structured dataset from unstructured web content.
- Store scraped data in CSV format for analysis.
- Gain practical experience with Python data collection tools.

---

## 🌐 Website Used

https://books.toscrape.com/

---

## 🛠 Technologies Used

- Python
- Requests
- BeautifulSoup (bs4)
- Pandas
- CSV

---

## 📂 Project Structure

CodeAlpha_WebScraping/

├── scraper.py

├── books_dataset.csv

├── requirements.txt

├── README.md

└── screenshots/

---

## 📊 Extracted Data

The scraper collects the following information:

- Book Title
- Price
- Availability Status
- Rating

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <your-github-repository-link>
```

### Navigate to Project Folder

```bash
cd CodeAlpha_WebScraping
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python scraper.py
```

---

## 📈 Output

After execution, a CSV dataset named:

```text
books_dataset.csv
```

is generated containing all the scraped book information.

Example:

| Title | Price | Availability | Rating |
|---------|---------|---------|---------|
| A Light in the Attic | £51.77 | In stock | Three |
| Tipping the Velvet | £53.74 | In stock | One |

---

## 🔍 Features

- Extracts book details automatically.
- Scrapes multiple pages.
- Creates a structured dataset.
- Saves data into CSV format.
- Easy to extend for additional analysis.

---

## 📚 Learning Outcomes

Through this project, I learned:

- Web Scraping fundamentals
- HTML structure analysis
- Data extraction techniques
- Data cleaning and storage
- Working with Python libraries for data collection

---

## 📷 Screenshots

Screenshots of code execution and generated dataset are available in the **screenshots** folder.

---

## 🚀 Future Enhancements

- Export data to Excel format
- Store data in SQL databases
- Perform Exploratory Data Analysis (EDA)
- Create interactive dashboards
- Schedule automated scraping

---

## 👩‍💻 Author

**Gowthami Perolla**  
Department of Information Technology  
CodeAlpha Data Analytics Internship

---

## 📜 License

This project is developed for educational and internship purposes.