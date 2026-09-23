# Automated Data Extraction - Web Scraping

## Objective

Scrape publicly available real estate listing data from a practice website, clean the extracted data, and export it as a structured CSV file.

## Tech Stack

- Python
- Requests
- BeautifulSoup
- Pandas
- Jupyter Notebook

## Website

Nestly Real Estate Practice Website

## Tasks Completed

1. Sent an HTTP request to the webpage using Requests.
2. Parsed the webpage using BeautifulSoup.
3. Identified property listing cards using CSS selectors.
4. Extracted property information from 16 listings.
5. Extracted:
   - Price
   - Bedrooms
   - Bathrooms
   - Area in square feet
   - Address
6. Cleaned numeric columns using Pandas.
7. Handled different price formats such as sale and monthly rental values.
8. Stored the scraped information in a Pandas DataFrame.
9. Exported the cleaned data to a CSV file.
10. Verified that the CSV contains 16 records.

## Output

The project generates:

`real_estate_listings.csv`

The CSV contains the following columns:

- Price
- Bedrooms
- Bathrooms
- Area_sqft
- Address

## Project Files

```text
Task2_WebScraping/
├── task2_web_scraping.ipynb
├── real_estate_listings.csv
└── README.md
