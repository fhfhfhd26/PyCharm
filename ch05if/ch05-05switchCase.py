def sf1():
    print("첫번째")


def sf2():
    print("두번째")


def sf3():
    print("세번째")


def switch(key):
    return {"1": sf1, "2": sf2, "3": sf3}.get(key, '잘못 된 선택')


# 함수를 가져와서 result에 저장한다.
result = switch("1")
print(result) # <function sf1 at 0x02D9D778>
# print(result())
result() # 첫번째
switch("2")() # 두번째
print(switch("4")) # 잘못 된 선택

