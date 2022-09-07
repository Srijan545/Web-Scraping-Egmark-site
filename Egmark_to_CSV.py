import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=MH&Tx_District=14&Tx_Market=0&DateFrom=20-Oct-2021&DateTo=21-Oct-2021&Fr_Date=20-Oct-2021&To_Date=21-Oct-2021&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=--Select--"
data = requests.get(url)
contents = data.content
soup = BeautifulSoup(contents, "html.parser")

span = []
spns = soup.find_all('span')
for spn in spns:
    span.append(spn)
#print(span)

a=15
b=len(span)
data = []
for x in range(a,b,9):
    plc = span[x+1]
    min = span[x+5]
    max = span[x+6]
    modal = span[x+7]
    date = span[x+8]
    data.append([plc.string,min.string,max.string,modal.string,date.string])
    #print(plc.string, date.string, min.string, max.string, modal.string)

df = pd.DataFrame(data, columns = ["market", "Min-Price", "Max-Price", "Modal-Price"," Date"])
df.to_csv('GP-egmark.csv')