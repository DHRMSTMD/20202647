# 다음 영화 리뷰 Table
# TODO: 1분전 -> 날짜 계산해서 저장(?시간 전 완료)

# 다음 영화 DATE -> 조금전, ?분전, ?시간 전, 2023.11.24 11:09
#TODO: 스케줄러 등록 하루에 1번 수집
#	   -> 중복 방지를 위해서(DB에 저장된 리뷰의 마지막 날짜보다 큰 애들만 수집)

CREATE TABLE `tbl_review` (
	`no` INT(10) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(100) NOT NULL,
	`review` VARCHAR(500),
	`score` INT(10) NOT NULL DEFAULT '0',
	`writer` VARCHAR(50) NULL,
	`reg_date` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`no`) USING BTREE
);
COMMENT = '다음 영화 리뷰'
AUTO_INCREMENT = 1
;

TRUNCATE tbl_review;


