# 1 ~ 10 까지 출력

# i = 1
# while i < 11:
#     print(i)
#     i += 1

# # 1부터 숫자를 계속 더해서 더한 숫자가 100보다 커지면 빠져나가서 출력
# i = 1
# sum = 0
# while True:
#     sum += i
#     i += 1
#     if sum > 100:
#         break
# print(sum)

# 1 ~ 10 출력 홀수만 출력
# 1부터 시작하면서 2씩증가, --> 1번째 방법
# 짝수인 경우 출력하지 않고 반복처리를 계속 할수 있도록 한다 ->continue

i = 1
while i < 10:
    print(i)
    i += 2


i = 1
while i < 11:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1



