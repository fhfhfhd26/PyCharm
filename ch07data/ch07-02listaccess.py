# List
aa = [10, 20, 30, 40]

print("앞에서 두번째 데이터 : ", aa[1])

print("뒤에서 두번째 데이터 : ", aa[-2])

print("뒤에서 세번째 데이터 : ", aa[-3])

print("2번째 3번째 데이터 : ", aa[1:3])
print("2번째 3번째 데이터 타입 : ", type(aa[1:3]))

print("1번째 3번째 데이터 : ", aa[0:3])
print("1번째 3번째 데이터 : ", aa[:3])

print("2번째 4번째 데이터 : ", aa[2:])

bb = aa[2:]
print(bb)

# list 연산자 +, *
# 2개의 리스트를 합치자. aa, bb 합친다.
print(aa+bb)

# 2개의 리스트 곱셈연산은 불가능
# print(aa*bb)

# 1개의 리스트 데이터를 3번 반복해서 데이터 만들기
print(aa*3)
