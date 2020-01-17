ss = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠."

print(ss, type(ss))
print(ss.count("공부"))
print("공부글자 위치:", ss.find("공부"), "  오른쪽(끝)에서 공부글자의 위치:", ss.rfind("공부"))
print(ss.find("5번째 글자 뒤의 공부", 5), ss.find("없다"))

print("공부글자 위치:", ss.index("공부"), "  오른쪽(끝)에서 공부글자의 위치:", ss.rindex("공부"))

print("파이썬이란 글자로 시작:", ss.startswith("파이썬"))
print("공부이란 글자로 시작:", ss.startswith("공부"))
print(".으로 끝나는가:", ss.endswith("."))
