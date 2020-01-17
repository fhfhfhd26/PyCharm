ss = "파이썬최고"

print(ss)
print(ss[1:3])

ss = "파이썬" + "최고!"
print(ss)
print(ss * 3)

#문자열을 입력 받아서 역순으로 출력
# inStr = input("문자열을 입력하세요 : ")
inStr = "즐거운 Python 프로그래밍~~~. python IS funny."
print("입력 문자열:", inStr, type(inStr))

count = len(inStr)

for i in range(count):
    print(inStr[count - i - 1], end="")
print()
# 0 - 1, 마지막 0의 위치는 포함되지 않으므로 -1 해준다.
for i in range(count - 1, 0-1, -1):
    print(inStr[i], end="")
print()
# list의 검색데이터 처리 이용
print(inStr[::-1])

# print(inStr.reverse()) - list type이 아니므로 오류
# print(list(inStr).reverse()) - None : 논리오류

print(inStr.upper())
print(inStr.lower())
print(inStr.swapcase())
print(inStr.title())
