import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.amazon.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = []

product_elements = soup.find_all('div', class_='product')
for product_element in product_elements:
    name = product_element.find('h2').text.strip()
    price = product_element.find('span', class_='price').text.strip()

    product_data = {
        'name': name,
        'price': price
    }
    data.append(product_data)

fieldnames = ['name', 'price']
filename = 'data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print('Data extraction and saving completed.')
