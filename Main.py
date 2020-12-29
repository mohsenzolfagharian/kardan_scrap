from requests import Session
from bs4 import BeautifulSoup
from unidecode import unidecode

s = Session()
page = 1
all_scraped_numbers = []
while page < 10:
    url = f'https://iran-kfunds2.ir/Reports/FundDailyEfficiency?page={page}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    tbody = soup.tbody
    tr = tbody.find_all('tr')
    for row in tr:
        neg = False
        if '(' in row:
            neg = True
        per = unidecode(row.find_all('td')[2].text.replace('(', '').replace(')', '').strip())
        if neg:
            per = float(per)
            per = per * -1
            all_scraped_numbers.append(per)
        else:
            per = float(per)
            all_scraped_numbers.append(per)
    page += 1

print(sum(all_scraped_numbers)/len(all_scraped_numbers))
