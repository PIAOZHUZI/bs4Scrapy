import re
import requests
from bs4 import BeautifulSoup
import pyautogui
import json

# search = pyautogui.prompt('검색하고 번호: ')

search = input('검색할 번호를 입력하세요 : ')
url=f"https://www.3gpp.org/dynareport/{search}.htm"
response = requests.get(url)
#
html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
all = soup.select('#SpecificationReleaseControl1_rpbReleases > ul > li.rpItem > div.rpSlide tr[class *=Row]')
ans = []
# f = open( '../data.txt', 'w',encoding='utf-8')
for i  in (all):
    meet = i.select_one('td > div.text-center > a').text.strip()
    version = i.select_one('td:nth-child(2) > div.text-center > a').text.strip()
    update = i.select_one('td:nth-child(3)').text.strip()
    ans.append({'Meettings' : meet , 'Version' : version, 'upload_date': update})

with open('./data.json', 'w', encoding='utf-8') as f:
    json.dump(ans, f, ensure_ascii=False, indent=4)

#f.write(ans)

# print(ans)
#f.close()


