#리뷰 데이터 저장
from db.common.connection import connection
def add_review(data):

    conn = connection()

    try:
       # 2) 일꾼 생성
        curs = conn.cursor()
        sql = """
        INSERT INTO tbl_review(title, review, score, writer, reg_date)
        VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s);
        
        """
       #4) 작업 시작
        curs.execute(sql, data)
        # 3) JOB 생성(SQL) -> INSERT, DELETE, UPDATE, SELECT
    except Exception as e:
        print(e)
    finally:
        #5.자원 반납
        conn.close()