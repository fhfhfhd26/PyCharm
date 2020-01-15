# list는 데이터 변경 가능 [] , tuple은 데이터 변경이 불가능 ()

tt = (10, 20, 30)

print(tt, type(tt))

print(tt[2])

# tt[2] = 300
# tt.append(40)

tt1 = tt

print(tt, type(tt))

print(tt1)

print(tt1+tt)

print(tt*3)

# tuple -> (10, 20, 30) -> (10, 200, 30)

# tuple -> list -> 수정 -> tuple

tt2 = list(tt)

print(tt2, type(tt2))

tt2[1] = 200

print(tt2)

tt = tuple(tt2)

print(tt, type(tt))