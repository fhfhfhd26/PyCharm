import random


# 함수 선언 부분
def getNumber():
    return random.randrange(1, 46)


# 전역 변수 선언 부분
lotto = []
num = 0

# 메인 코드 부분
print("** 로또 추첨을 시작합니다. \n")

while True:
    num = getNumber()
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6:
        break

print("당첨번호 :", end=" ")
lotto.sort()

for i in range(0, 6):
    print("%d " % lotto[i], end = " ")


print("\n\n set 사용 시작")

lotto2 = set([])

# 메인 코드 부분
print("** 로또2 추첨을 시작합니다. \n")

while len(lotto2) < 6:
    lotto2.add(getNumber())

print("당첨번호2 :", end=" ")
print(lotto2)

