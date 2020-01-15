# 구구단 처리를 하는데 시작 단수와 마지막 단수를 입력받아서
# 시작단수부터 마지막 단수 사이의 모든 단수를 출력한다.

sNum, eNum = 0,0

sNum = int(input("시작 단을 입력해 주세요 : "))
eNum = int(input("끝 단을 입력해 주세요 : "))

# 세로출력
for i in range(sNum, eNum+1):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i*j))
    print("\n")

# 가로출력
for j in range(1, 10):
    for i in range(sNum, eNum + 1):
        print("%2d * %2d = %2d      " % (i, j, i*j), end="")
    print()

# range(시작값, 끝값-1, 변화값)
for i in range(1, 10, 2):
    print(i)
