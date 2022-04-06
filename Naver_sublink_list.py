import requests
from bs4 import BeautifulSoup

url = "https://dict.naver.com/"
result = requests.get(url = url)

bs_obj = BeautifulSoup(result.content, "html.parser")
view_dic = bs_obj.find("div", {"class":"view_dic"})
print(view_dic.text)