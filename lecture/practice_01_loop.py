# #input() 활용해서 사용자가 입력한 값(2~9) 해당 단 출력
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i} = {dan*i}")

#2단부터 9단까지 문제2)
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}x{j} = {j * i}")

# 문제3 list a의 평균값을 계산하세요.

a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]

total = 0
for i in a:
    total += i

length =int(len(a))
result = total / length
#round(값, 소수섬숫자): 반올림
print(round(result, 2)) # 평균값

#숙제 list b에서 최솟값 찾기!

b = [22, 1,4,7, 98]


# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]



num_min = b[0]
for x in b:
   if x < num_min:
       num_min = x

print(num_min)  # 1 출력

#list c의 최소값, 최대값 찾기

c = [2, 5, 7,1, 8]

num_min = c[0]
num_max = c[0]
for a in c:
   if a < num_min:
       num_min = a
   if a > num_max:
       num_max = a
print(num_min)
print(num_max)

# 사용자가 입력한 값 1, 2, 3 통과
# 아닌 경우 다시 입력하도록

# count = 0 # 잘못 입력한 횟수
# while True:
#     if count >= 3:
#         print("프로그램을 사용할 수 없습니다.")
#         break
#     num = int(input("값 :"))
#     #if 0 < num < 4:
#
#     if num in [1, 2, 3]:
#         print(f"{num}을 입력하셨습니다.")
#         break
#     else:
#          print("1, 2, 3의 값만 입력해주세요.")
#          count += 1

#문제7) 1부터 100까지 총합을 출력하는 코드
# for 문으로 작성
# while문으로 작성

total = 0
for num in range(1, 101):
    total += num
print(f"총합(for): {total}")

num = 0
total = 0
while True:
    num += 1
    total += num

    if num == 100:
        break

print(f"총합(while): {total}")


