import requests                                         # requests 패키지를 설치한다.
from bs4 import BeautifulSoup                           # bs4 패키지를 설치한다.

url = "https://www.naver.com/"                          # website 의 url 주소를 입력한다.
result = requests.get(url = url)                        # website 를 가져온다.

bs_obj = BeautifulSoup(result.content, "html.parser")   # HTML 을 불러온다.
ul = bs_obj.find("ul", {"class":"list_nav NM_FAVORITE_LIST"})       # tag 가 ul 인 것 중에서 class 가 list... 인 것을 가져온다.
atags = ul.findAll("a")                                             # ul 에서 tag 가 a 인 것을 모두 가져온다.
for a in atags:                                                     # atags 에 있는 것을 a 로 하나씩 뽑아서
    print(a['href'])                                                # href 속성을 뽑는다.