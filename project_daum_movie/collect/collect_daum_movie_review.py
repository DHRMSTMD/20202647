from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta
import math
import re
import time
from bs4 import BeautifulSoup

from project_daum_movie.db.movie_dao import add_review
# Selenium + BeautifulSoup4
#  - Selenium: 전체 소스코드 가져오기(+동적으로 페이지 조작)
#  - BeautifulSoup4: 필요한 데이터만 Select

# **Selenium
#   - 웹브라우저 검사(Test) 도구 -> 데이터 수집
#   - 전용 브라우저를 동작(크롬, 파이어폭스, 등등)로 동작
#   - 전용 브라우저 Open -> 작업 -> 브라우저 Close(Default)


def review_collector(movie_code, last_date):
    # ** Selenium 사용방법 2가지
    #   1.직접 다운로드(크롬 브라우저)해서 사용
    #     url: https://sites.google.com/chromium.org/driver/

    # 2.실시간 다운로드 후 사용
    options = Options()
    # Selenium이 작업 완료 후에 전용 브라우저 종료 X
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # URL 접속
    url = f"https://movie.daum.net/moviedb/grade?movieId={movie_code}"
    driver.get(url)
    time.sleep(1)

    # 페이지 소스 가져오기
    doc_html = driver.page_source

    doc = BeautifulSoup(doc_html, "html.parser")

    # 영화 제목 수집
    movie_title = doc.select("span.txt_tit")[0].get_text()
    print(movie_title)

    total_review_cnt = doc.select("span.txt_netizen")[0].get_text()
    # (187명) 에서 숫자만 추출하는 방법
    #   1. 문자열 슬라이싱 방법
    #print(total_review_cnt[1:-2])
    #   2. 정규식 사용한 방법
    num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))
    #print(num_review)

    # 187 = 최초(10), 버튼1개(30개)
    click_cnt = math.ceil((num_review - 10) / 30)

    for i in range(click_cnt):
        # "평점 더보기" 버튼 클릭
        driver.find_element(By.CLASS_NAME, "link_fold").click()
        time.sleep(2)

    # 전체 소스코드 가져오기2(평점이 모두 출력된 페이지)
    doc_html = driver.page_source
    doc = BeautifulSoup(doc_html, "html.parser")
    review_list = doc.select("ul.list_comment > li")

    print(f"전체리뷰 : {len(review_list)}")

    # 반복 1회마다 리뷰 1건씩 수집
    count = 0 # 수집리뷰 건수 카운터
    for item in review_list:
        #Check: 데이터베이스 저장 된 리뷰인지 확인(중복)
        #1. 오늘 리뷰건수 - DB 저장된 리뷰 건수 = 수집 건수
        # 수집건수만큼 수집하고 멈추기(삭제된 리뷰를 고려x)
        #2.DB에 저장된 리뷰 중에서 가장 최근에 수집한 리뷰의 날짜
        #  last_date(2023.11.27.02:25)
        # 수집하는 리뷰의 date와 last)date를 비교


        # 다음 영화리뷰 날짜 표기법 4가지
        # 1. 조금전    : 현재시간(분) - 1분
        # 2. ?분전     : 현재시간(분) - ?분
        # 3. ?시간전   : 현재시간(시간) - ?시간
        # 4. 2023.11.29. 13:12 : 그대로
        # 24시간 이내에 작성된 글은 날짜 -> 예: 21시간전, 17시간 전
        # 실제 날짜 표기법 -> 2023. 11. 17. 12:15
        # 표기법: 21시간 전 -> 2023. 11. 17. 12:15

        review_date = item.select("span.txt_date")[0].get_text()

        # review_date -> 4가지 표기법 중 1개
        if review_date == "조금전":
            review_date = (datetime.now() - timedelta(minutes=1))  # 현재시간 - 1분
            review_date = review_date.strftime("%Y. %m. %d. %H:%M")
        elif review_date[-2:] == "분전":
            # 1분전 ~ 59분전 -> "분전"
            reg_minute = int(re.sub(r"[^~0-9]", "", review_date))
            review_date = (datetime.now() - timedelta(minutes=reg_minute))
            review_date = review_date.strftime("%Y. %m. %d. %H:%M")
        elif review_date[-3:] == "시간전":
            # 1시간~23시간 -> "시간전"
            reg_hour = int(re.sub(r"[^~0-9]", "", review_date))
            review_date = (datetime.now() - timedelta(hours=reg_hour))
            review_date = review_date.strftime("%Y. %m. %d. %H:%M")
        #review_date = 수집 리뷰의 날짜

        #DB에 저장된 리뷰 중 최신 날짜 가져오기
        #날짜 비교-> 숫자
        #2023.11.30. 10:30    202311301030
        # Collect: 2023.12.01 10:40   202312011040
        collect_date = int(re.sub(r"[^~0-9]", "", review_date))
        if last_date >= collect_date:
            continue

        count += 1
        print("="*100)
        review_score = item.select("div.ratings")[0].get_text()
        print(f"  - 평점: {review_score}")
        review_content = item.select("p.desc_txt")[0].get_text().strip()
        # \n : 한 줄 개행
        # 수집한 리뷰가 개행 -> 문자열 안에 \n 포함
        review_content = re.sub("\n", "", review_content)
        print(f"  - 리뷰: {review_content}")
        review_writer = item.select("a.link_nick > span")[1].get_text()  # [댓글 작성자, 작성자, 댓글 모아보기]
        print(f"  - 작성자: {review_writer}")

        print(f"  - 날짜: {review_date}")
        # 21시간 전 잘못 뜨는 경우를 어떤 조건으로 찾을 수 있을지?
        #print("수정 필요!")

        #MariaDB에 저장
        # 1) DB에 보낼 데이터 만들기
        # Tip: key값, -> Table의 coulmn(열)과 동일하게
        data = {
            "title": movie_title,
            "score": review_score,
            "review": review_content,
            "writer": review_writer,
            "reg_date": review_date
        }
        add_review(data)
        #현재시간 get -> 날짜표기법 "2023.12.1 11:40:25"
    now = datetime.now().strftime("%Y. %m. %d. %H:%M:%S")
    print(f"{now}수집 된 리뷰 {count}건")


