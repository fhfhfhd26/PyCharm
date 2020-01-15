# 1. 리스트의 갯수를 출력
def func1(aa):
    print("1. 리스트의 갯수 : %d" % len(aa))


# 2. 리스트의 데이터를 바꾸지 않으면서 정렬해서 출력
def func2(aa):
    print("2. 리스트의 정렬 : %s" % sorted(aa))


# 3. 90 데이터의 위치를 출력
def func3(aa):
    a = aa.index(90)+1
    print("3. 90데이터의 위치 : %d" % a)


# 4. 마지막 데이터를 꺼내오면서 제거해 보세요
def func4(aa):
    print("4. aa의 마지막 데이터 출력후 삭제 : %d" % aa.pop())


# 5. bb라는 리스트에 동일한 데이터를 가지도록 처리해 보세요
def func5(aa):
    bb = aa
    print("5. bb에 동일데이터 만들기 : %s" % bb)


# 6. aa 리스트에서 값이 100인 것을 지운다.
def func6(aa):
    aa.remove(100)
    print("6. aa에 100지우기 : %s" % aa)


# 7. aa 리스트 값을 지운다.
def func7(aa):
    aa.clear()
    print("7. aa 리스트 삭제 : %s" % aa)


aa = [85, 100, 90, 70, 95, 90]
func1(aa)
func2(aa)
func3(aa)
func4(aa)
func5(aa)
func6(aa)
func7(aa)

