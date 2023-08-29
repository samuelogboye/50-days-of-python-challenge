#!/usr/bin/python3

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the desired data
table = soup.find('table', {'class': 'wikitable'})

# Read the HTML table into a pandas DataFrame
data = pd.read_html(str(table), header=0)[0]


# Modify the desired_columns list based on the actual column names
desired_columns = ['Type', 'Mutability']
extracted_data = data[desired_columns]

# Display the extracted data
print(extracted_data)
