#URL - 기사(제목, 본문, 날짜) 수집
import requests  # 전체 소스코드
import selenium  # 원하는 정보 select
from bs4 import BeautifulSoup  # 원하는 정보 select


def get_news(url: str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    reg_date = doc.select("span.num_date")[0].get_text()
    print(f"날짜: {reg_date}")

    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목: {title}")

    content_list = doc.select("div.article_view p")
    content = ""
    for p in content_list:
        content += p.get_text()
    print(f"본문: {content}")
