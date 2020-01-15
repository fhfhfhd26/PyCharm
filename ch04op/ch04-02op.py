# 문자열과 숫자는 연산이 불가능
# print("100" + 1)

# print("100" + 1) : 문자열로 연산
print("100" + str(1))

# print("100" + 1) : 숫자로 연산
print(int("100") + 1)

# 11.1
print(10 + 1.1)

# 11
print(10 + int(1.1))

# 11 : int 사용시 소숫점 버림.
print(10 + int(1.6))

# 0100
a = 4
print(a << 1)
print(a >> 1)


