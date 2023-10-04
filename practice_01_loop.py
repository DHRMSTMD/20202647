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

print(num_min)