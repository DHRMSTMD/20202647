from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import re
import math
# selenium + beautifulSoup4
# selenium 전체소스코드 가져오기(+동적으로 페이지 조작)
# BeautifulSoup4 필요한 데이터만 select

#selenium
# 웹브라우저 검사 도구! -> 데이터 수집
# 전용 브라우저(크롬, 파이어폭스)를 동작
# 전용 브라우저 Open -> 작업 -> 브라우저 Close(Default)

# Selenium 사용방법 2가지
# 1. 직접 다운로드해서 사용
# url: https://sites.google.com.chromium.org/driver/
# 2. 실시간 다운로드 후 사용

options = Options()
# selenium이 작업 완료 후에 전용 브라우저 종료 x
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(3)
#URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=169137"
driver.get(url)
time.sleep(1)

#페이지 소스 가져오기
doc_html = driver.page_source

doc = BeautifulSoup(doc_html, "html.parser")

#영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()

total_review_cnt = doc.select("span.txt_netizen")[0].get_text()
#print(total_review_cnt[1:-2])

# (187명)에서 숫자만 추출
# 문자열 슬라이싱 방법
# print(total_review_cnt[1:-2])
# 정규식 사용하는 방법
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))
print(num_review)

#187 = 최초(10), 버튼1개(30)
click_cnt = math.ceil((num_review-10) /30)

for i in range(click_cnt):
    #평점 "더보기" 버튼 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(2)
#전체 소스코드 가져오기2(평점 모두 출력)
doc.html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")

#print(len(review_list))

for item in review_list:
    review_score = item.select("div.ratings")[0].get_text()
    print(f"   - 평점: {review_score}")

    review_content = item.select("p.desc_txt")[0].get_text().strip()
    review_content = re.sub("\n", "", review_content)
    #\n : 한 줄 개행
    #수집한 리뷰가 개행 -> 문자열 \n 포함
    print(f"   - 리뷰: {review_content}")
    review_writer = item.select("a.link_nick > span")[1].get_text()#[댓글 작성자, 작성자, 댓글 모아보기]
    print(f"   - 작성자: {review_writer}")
    # 24시간이내에 작성된 글은 날짜 -> 예 : 21시간전, 17시간전
    # 실제날짜표기법 -> 2023.11.17. 12:15
    # 표기법: 2023.11.17. 12:15
    # review_date -> 17시간전 or 2023.11.17 12:17

    review_date = item.select("span.txt_date")[0].get_text()

    if len(review_date) < 7:
        #예: 17시간전 -> 숫자만 추출:17
     reg_hour = int(re.sub(r"[^~0-9]", "", review_date))
     #print(reg_hour)
     #print(datetime.now())
     #예) 현재시간에서 빼기
     review_date = datetime.now()-timedelta(hours=reg_hour)
     #예) 2023-11-16 18:32:59.482053 -> 2023.11.16.18:32
     review_date = review_date.strftime("%Y. %m. %d. %H:%M")
    print(f"   - 날짜: {review_date}")