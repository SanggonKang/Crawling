import requests
from bs4 import BeautifulSoup

url = "https://www.hyundai.com/kr/ko/e"

result = requests.get(url = url)
bs_obj = BeautifulSoup(result.content, "html.parser")
section = bs_obj.find("section", {"class":"section-wrap benefit"})
div1 = section.find("div", {"class":"box-list-slide el-carousel el-carousel--horizontal el-carousel--v2 el-carousel--hide-l-arrow"})
div2 = div1.find("div", {"class":"el-carousel__container"})
div3 = div2.findAll("div2", {"class":"el-carousel__item is-active is-animating"})
print(div3)