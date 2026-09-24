import requests 
import re
import subprocess
from bs4 import BeautifulSoup

def get_html():
    response = requests.get('https://www.tgju.org/profile/price_dollar_rl')
    with open('demofile.txt', 'w', encoding="utf-8") as f:
        f.write(response.text)
    
def find_price():
    with open('demofile.txt', 'r', encoding='UTF-8') as f: 
        lookthis = f.read()
    soup = BeautifulSoup(lookthis, 'html.parser')
    dollar = soup.find("li", id="l-price_dollar_rl")
    return  dollar.find("span", class_="info-price")

def format_price():
    price2 = find_price().text
    price3 = price2[:len(price2) - 1]
    return re.sub(r'[^\w\s]', '', price3)
    
def format_json():
    price = format_price()
    json_txt = f'{{"generated_by_tomanify_at": "2026-09-20","values": {{"USD": {price},"EUR": 262290,"AED": 62355,"TRY": 4745,"CNY": 34240}}}}'
    with open('rates.json', 'w', encoding="utf-8") as f:
        f.write(json_txt)

def calling_funcs():
    get_html()
    find_price()
    format_price()
    format_json()
    subprocess.run(["git", "add", "rates.json"])
    subprocess.run(["git", "commit", "-m", "Update data"])
    subprocess.run(["git", "push"])

calling_funcs()



