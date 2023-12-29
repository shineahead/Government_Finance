import requests
from bs4 import BeautifulSoup
import csv

url = "https://yss.mof.gov.cn/2022zyczys/202203/t20220324_3797801.htm"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

resp = requests.get(url, headers=headers)
# 网页数据的编码格式为'utf-8'
resp.encoding = 'utf-8'

with open("./data/2022finance.csv", mode="w", newline="", encoding="utf-8-sig") as f:
    csvwriter = csv.writer(f)

    page = BeautifulSoup(resp.text, "html.parser")
    table = page.find("table")

    trs = table.find_all("tr")[2:]
    for tr in trs:
        tds = tr.find_all("td")
        name, num_20, num_20_1 = [td.text for td in tds[:3]]
        csvwriter.writerow([name, num_20, num_20_1])

print("over!")
