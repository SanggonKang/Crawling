import requests
from bs4 import BeautifulSoup

url = "https://www.sk2.co.kr/"

result = requests.get(url = url)
bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)