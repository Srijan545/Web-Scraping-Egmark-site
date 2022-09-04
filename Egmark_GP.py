import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.append(['data'])

url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=MH&Tx_District=14&Tx_Market=0&DateFrom=20-Oct-2021&DateTo=21-Oct-2021&Fr_Date=20-Oct-2021&To_Date=21-Oct-2021&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=--Select--"
data = requests.get(url)
contents = data.content
soup = BeautifulSoup(contents, "html.parser")

#print(soup.prettify)

title = soup.title
print(title.string)

sets = soup.find_all('tr')
#print(sets)

for oneset in sets:
    tds = oneset.find_all('td')
    #print(tds)

spns = soup.find_all('span')
for spn in spns:
    op = spn.string
    print(op)
    sheet.append([op])

excel.save('Egmark data.xlsx')