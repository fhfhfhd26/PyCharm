#
# # 입력되는 숫자의 진수 입력
# sel = int(input("입력진수 결정 (16/10/8/2) : "))
#
# # 선택된 진수에 해당되는 값을 입력
# num = input("값 입력 : ")
#
# # 조건문 sel의 입력 된 값에 따라 10진수로 변환을 해준다.
# if sel == 16 :
#     num10 = int(num, 16)
#
# if sel == 10:
#     num10 = int(num, 10)
#
# if sel == 8:
#     num10 = int(num, 8)
#
# if sel == 2:
#     num10 = int(num, 2)
#
# # num10의 변수에 10진수 값 저장
# print("16진수 : ", hex(num10))
# print("10진수 : ", num10)
# print("8진수 : ", oct(num10))
# print("2진수 : ", bin(num10))
#
# # 16진수로 FF -> 255
# a = 0xFF
# print("a : ", a)
# # 8진수로 77 -> 63
# b = 0o77
# print("b : ", b)
# # 2진수로 1111 -> 15
# c = 0b1111
# print("c : ", c)

# 실수형 데이터 입력
a = 3.14

# 3.14e5 -> 3.14 * 100000 -> 314000.0
b = 3.14e5

print(a, b)

print(a, "의 타입은", type(a))

# 2개의 처리문을 한 줄에 사용하기 위한 ';'
a = 10 ; b = 20
print(a + b)
print(a ** b)

b = 3
print(a / b)
print(a % b)
print(a // b)

a = True
b = False

print(a, type(a))

a = (100 == 100)

a = "파이썬 만세"
a
print(a, type(a))

a = 'python'
print(a, type(a))

a = "wejjang's 'JAVA'"
print(a, type(a))
