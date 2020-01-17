from builtins import print

ss = "파이썬을 열심히 공부하는 중"
print(ss, type(ss))
print(ss.split(), type(ss.split()))

ss = "하나:둘:셋"
print(ss, type(ss))
print(ss.split(":"), type(ss.split(":")))

# 전화번호 3개 -> 010-1111-2222
# 각각의 위치에 따른 데이터 출력
# 010 , 1111, 2222 따로 출력이된다.
tel = "010-1111-2222"

sep = "-"

tels = tel.split(sep)
for t in tels:
    print(t)
print(tels)

# 분리되어 있는 데이터를 중간에 "-"를 이용해서 완성된 전화번호를 출력
# list -> str : 010-1111-2222
print(sep.join(tels))

tel = ""
for t in tels:
    tel += t + "-"

tel = tel[:len(tel)-1]
print(tel)

# 정렬:가운데, 왼쪽,오른쪽, 채우기
ss = "파이썬"
# 가운데 정렬
print("[", end="")
print(ss.center(10), end="")
print("]")
# 왼쪽 정렬
print("[", end="")
print(ss.ljust(10), end="")
print("]")
# 오른쪽 정렬
print("[", end="")
print(ss.rjust(10), end="")
print("]")

print(ss.zfill(10))
print(ss.rjust(10, "-"))

