def multi_return():
    return 100, 200


# main
a, b = 10, 20
print(a, b)

# 2개의 리턴값 2개의 변수에 각각 넣을 수 있다.
a, b = multi_return()
print(a, b)


# 파라메터 값이 2개 또는 4개 등을 전달 받을 수 있는 함수
def para_func(v1, v2, v3=0):
    return v1 + v2 + v3


print(para_func(10, 20))
print(para_func(10, 20, 3))

