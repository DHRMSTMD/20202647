#조건문(condition) : if ~elif~else
# -특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# 모든 조건은 boolean으로 표현 됨
# 조건문의 경우 if, elif, else 블록 내 종속된 코드 들여쓰기
# 모든 블록문의 시작점은 마지막에 : (콜론,colon)추가
# python에서 블록내의 코드는 반드시 들여쓰기(tap) 강제

# # if(조건1){                             if 조건1:
# # code                                        code
# } else if (조건2){                       elif 조건2:
#     code                                      code
# }

# # if 조건1:
#     code
# elif 조건2:
#     code
# elif 조건3:
#     code
# else:
#     code

#조건문 4가지 조합
# if
# if~elif~elif
# if~else
# if~elif~else

#점수 계산기
# 91~100 :A
# 81~90 :B
# 71~80 :C
# 61~70 :D
# - 60 이하 : F
score = 95 # 0~100

if score>=91:
    print("A")
elif score>=81:
    print("B")
elif score>=71:
    print("C")
elif score>=61:
    print("D")
else:
    print("F")

#논리 연산자: AND, OR, NOT
#조건 1 조건 2 결과

#AND
# F     F      F
# T     F      F
# F     T      F
# T     T      T
#OR
# F     F      F
# T     F      T
# F     T      T
# T     T      T

#NOT
#T->F
#F->T

# 문제 1 어떤 종류의 학생인지 맞히기?
# 초중고대 학생x)

from datetime import datetime
#input() : 키보드 값 입력 => String(문자열)
born = input("당신의 태어난 년도를 입력하세요.") #"2004"

print(born)

today = datetime.today().year
print(today)
age = today - int(born)+1
print(age)

if 8 <= age <= 26:
    if age >=20:
        print("대학생")
    elif age>=17:
        print("고등학생")
    elif age>=14:
        print("중학생")
    elif age>=8:
        print("초등학생")
else:
    print("학생이 아닙니다.")

