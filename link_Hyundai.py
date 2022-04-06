import requests
from bs4 import BeautifulSoup

url = "https://www.hyundai.com/kr/ko/e"

result = requests.get(url = url)
bs_obj = BeautifulSoup(result.content, "html.parser")
div = bs_obj.find("div", {"class":"lnb_menu"})
ul = div.find("ul", {"class":"lnb_list"})
print(ul)
