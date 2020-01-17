#  문자 사이의 공백을 하나로 만드는 함수
def blankwithword(s):
    s = s.strip()
    while s.find("  ") >= 0:
        s = s.replace("  ", " ")
    return s


ss = "   파    이    썬   "
# 앞 뒤 공백을 없애서 출력
print("[", end="")
print(ss, end="")
print("]")
print("[", end="")
print(ss.rstrip(), end="")
print("]")
print("[", end="")
print(ss.lstrip(), end="")
print("]")
print("[", end="")
print(ss.strip(), end="")
print("]")
# 글자 사이의 공백을 하나만 남긴다.
print("[", end="")
print(blankwithword(ss), end="")
print("]")

