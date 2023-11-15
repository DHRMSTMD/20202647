from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
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

#URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=165591"
driver.get(url)
time.sleep(1)

#페이지 소스 가져오기
doc_html = driver.page_source

doc = BeautifulSoup(doc_html, "html_parser")

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
review_list = doc.select("")