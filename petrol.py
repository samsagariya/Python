from requests import get
from openpyxl import load_workbook
from datetime import datetime
from bs4 import BeautifulSoup

response = get('https://www.goodreturns.in/petrol-price-in-chennai.html')
soup = BeautifulSoup(response.text, 'html.parser')

tmsp = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')

a = soup.find('div', class_='fuel-block-details').text
b = a.replace(" ", "").replace("\n", "")
c = b[0:6]


mylist = []

for i in [tmsp, c]:
    mylist.append(i)

wb = load_workbook("C:\\Users\\Sam\\Desktop\\Petrol.xlsx")
# Select First Worksheet
ws = wb.worksheets[0]

#Append 2 new Rows - Columns A - D
ws.append(mylist)

wb.save("C:\\Users\\Sam\\Desktop\\Petrol.xlsx")
print(mylist)
