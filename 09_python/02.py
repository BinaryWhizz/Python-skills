# BeautifulSoup 

# Definition : 

# - BeautifulSoup is a Python library for parsing HTML and XML documents
# - It is widely used for web scraping 

# Key Features 

# - Extract and navigates content from web pages.
# - Supports multiple parsers like html.parser and lxml. 

# Syntax:

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# Example : 

# import requests
# from bs4 import BeautifulSoup

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Extract all links
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))


# Web Scraping and Data Extraction with Python

# You are tasked with building a web scraper to extract structured data from the Wikipedia page for "Apple Inc." (https://en.wikipedia.org/wiki/Apple_Inc.).

# Follow the steps below to complete the task.

# Step-by-Step Instructions
# 1. Import Relevant Libraries

# Import all the necessary libraries for web scraping and data manipulation:

# • requests for making HTTP requests.
# • BeautifulSoup from bs4 for parsing HTML.
# • pandas for tabular data manipulation.

# 2. Perform HTTP Request

# • Send an HTTP GET request to the URL: https://en.wikipedia.org/wiki/Apple_Inc.
# • Save the response object for further processing.

# 3. Check the Request Status

# • Ensure the HTTP request is successful by checking the status code of the response.
# • Print a message:
# Success: If the status code is 200.
# Error: If any other status code is returned. 

# 4. Build the Extraction Model

# • Parse the HTML content using BeautifulSoup.
# • Use the "html.parser" as the parser.
# • Save the parsed object for further extraction tasks.

# 5. Extract Headings

# • Use BeautifulSoup to extract all headings (<h1>, <h2>, <h3>).
# • Save the extracted text into a structured format, such as a Python dictionary or a list.

# 6. Extract All Paragraphs

# • Extract all the text content within <p> tags.
# • Combine the paragraph texts into:
# ▪ A list where each item is a paragraph.
# ▪ Or a single block of text.

# 7. Extract All Links

# • Extract all hyperlinks (links within <a> tags).
# • Collect:
# ▪ The link text.
# ▪ The URL (from the href attribute).
# • Save the data in a Python dictionary where:
# ▪ The key is the link text.
# ▪ The value is the corresponding URL.

# 8. Extract Table

# • Locate the first table on the page (typically the infobox or summary table in Wikipedia articles).
# • Extract the table structure and its data.

# 9. Convert Table into a DataFrame

# • Use pandas to convert the table into a DataFrame.
# • Ensure the table headers and rows are correctly assigned.

# 10. Export the Table

# • Export the DataFrame as a summary table into a excel file named apple_inc_summary_table.xlsx.
# • Save the file in the working directory.


# In terminal --- > 

# pip install requests
# pip install beautifulSoup 

# Step 1:

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# Step 2

# url = "https://en.wikipedia.org/wiki/Apple_Inc."
# response = requests.get(url)
# html_content = response.text

# Step 3

# if response.status_code == 200:
#     print("Request successful!")

# Step 4

# soup = BeautifulSoup(html_content, 'html.parser')

# Step 5

# headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3'])]
# print(headings)

# Request successful!

# Step 6

# paragraphs = [p.text.strip() for p in soup.find_all('p)]
# print(paragraphs)

# Step 7

# links = [a['href'] for a in soup.find_all('a', href = True)]
# print(links)

# Step 8

# infobox = soup.find('table', class_='infobox')

# if infobox:
#     rows = infobox.find_all('tr')

#     data = {}
#     for row in rows:
#         header = row.find('th')
#         value = row.find('td')
#         if header and value:
#             data[header.text.strip()] = value.text.strip()
#     print(data)
# else:
#     print("Infobox table not found.")


# Step 9

# table = pd.DataFrame(list(data.items()), columns = ['key', 'value'])
# table

# Step 10

# table.to_excel("apple_inc_summary_table.xlsx") 

