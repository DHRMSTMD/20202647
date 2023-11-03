# 다음 실시간 뉴스 기사 수집기
#   내용: 다음 실시간 뉴스 목록(list: 15개)에서 url을 추출
#   -> 15개 url 각 url
#   별로 기사 제목, 본문, 날짜 수집

import requests  # 전체 소스코드
import selenium   #원하는 정보 select
from bs4 import BeautifulSoup #원하는 정보 select
from service.service_news import get_news

count =0 #전체 기사 수

url="https://news.daum.net/breakingnews/digital"

result = requests.get(url)

if result.status_code == 200:
    print(result, "접속 성공-> 데이터를 수집합니다.") #200 성공
    #i = 0

    doc = BeautifulSoup(result.text, "html.parser")
    url_list = doc.select("ul.list_news2 a.link_txt")
    for url in url_list:
       # i += 1
        count += 1
        print(f"{count}", "=" *100)
        #기사 제목, 본문, 날짜 수집.
        get_news(url["href"])

else:
    print("url 경로가 잘못됐습니다. 확인부탁드립니다.")


