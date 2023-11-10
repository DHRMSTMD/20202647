# 데이터베이스(DB): 데이터를 효율적으로 저장하는 시스템(이론)
# FileSystem: 폴더를 사용한 저장

# 데이터베이스관리시스템(DBMS): DB 이론을 실제로 구현!
# ** DBMS 종류
# 1) 관계형 데이터베이스(RDB) : 전통적인(스키마:명세서)
# - ORACLE
# - MYSQL
# - MariaDB

#2) NoSQL : NEW
# - MongoDB
# - Redis

# ** DB 프로세스
# Pycharm(Python)  ------------------- DB(MongoDB)
# - DO: ID와 PW 저장
# 1) Pycharm과 DB가 Connection 맺기
#    -IP : 컴퓨터를 찾아갈 수 있는 주소!
#    -PORT : 컴퓨터 내에서 특정 프로그램의 위치!
#    -ID and PW :
# 2) SQL을 사용해서 DB에 CRUD 작업 진행
#    - SQL(구조질의어) : DB와 소통할 수 있는 언어(반드시)
#    - RDB(SQL)을 사용, NOSQL(SQL X)
# Create(삽입)-> INSERT
# Read(조회)-> SELECT
# Update(수정)-> UPDATE
# Delete(삭제)-> DELETE

#MONGO DB 설정 방법
#1. 직접 설치(local)
#2. MongoDB에서 제공하는 웹 클라우드 사용(설치x)
# - MONGODB 회원가입 필수
#IP와 PORT -> URL 제공

# ** MongoDB 구조
# 설치: MongoDB(DBMS) : 전체 시스템
#      ㄴDB(카카오톡): 폴더
#         ㄴCOLLECTION(회원): 표
#         ㄴcollection(톡)
#         ㄴcollection(선물)
#         ㄴcollection(친구)
#       ㄴDB(카카오뱅크)
#         ㄴcollection(계좌)
#         ㄴcollection(대출)
#         ㄴcollection(회원)
#       ㄴDB(카카오페이)
# 데이터를 CRUD Collection


from pymongo import MongoClient


#MongoDB Connection
def conn_mongodb():
#IP, PORT, ID, PW
    DB_ID= "root" #상수 (전체 대문자로 변수명을 사용)
    DB_PW = "1234" # ex) 은행권 -> 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}<password>@daumcluster.unebehj.mongodb.net")
    db= client["daum"]
    collection = db.get_collection("news")
    return collection