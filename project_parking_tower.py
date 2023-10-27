# 주차타워 구현
# 조건 1. 5층까지 있고 층별로 1대만 주차
# 차량번호: 숫자4자리
#기능 1) 차량입고
# 2)차량 출고
# 3)차량 조회
# 4)프로그램 종료

# 설정
max_car = 5#타워주차 최대 5대
car_cnt = 0 #주차 대수 카운트
tower = []
# tower 생성
#List Comprehension 기법!
tower = ["" for i in range(max_car)]

#2 for list.append() 방법
# for i in range(max_car):
#     tower.append("")

while True:
    print("=" * 50)
    print("= 주차 타워 시스템 ver1.1 ==")
    print("="*50)
    print("= 1. 입고")
    print("= 2. 출고")
    print("= 3. 조회")
    print("= 4. 종료")
    print("=" * 50)

    while True:
        select_num = int(input(">>번호:"))
        if 4>=select_num >=1:
            break
        else:
            print("올바른 번호를 입력하세요.")
    if select_num == 1: #입고
        #입고 1. 주차타워 공간 확인
        if car_cnt < max_car:
            car_num = input(">>입고")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("입고 불가")


    elif select_num == 2: #출고
        car_num = input(">>출고: ") # 출고할 차량 번호 입력
        if car_num in tower:
            for car in enumerate (tower):  #차량번호 입고 된 차량인지 검색
                if car == car_num:
                    tower[i] = "" #차량제거
                    car_cnt -= 1 # 현재 주차 개수 동기화
                    break
        else:
            print("입고 된 해당 차량이 없습니다.")

    elif select_num == 3: #조회
        print("== 주차 타워 현황 ==")
        for i in range(len(tower)-1, -1, -1):
            print(f">{i+1}층 {tower[i]}")

    elif select_num == 4: #종료
        print("프로그램을 종료합니다.")
        exit()

