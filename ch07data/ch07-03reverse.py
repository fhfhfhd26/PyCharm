aa = [10, 20, 30, 40, 50]

print(aa)

# 리스트 aa의 값의 순서를 거꾸로 정렬하여 출력하시오
aa = aa[::-1]
print(aa)

aa.reverse()
print(aa)

# 일부 데이터의 변경
# aa 리스트 데이터 중 3번째 30을 300으로 변경
aa[2] = 300
print(aa)

# 1번째 100으로 2번째는 200으로 변경
aa[0:2] = [100, 200]
print(aa)

aa[1:3] = [700]
print(aa)

aa[1] = [1000, 2000]
print(aa)

print(aa[0], type(aa[0]))
print(aa[1], type(aa[1]))

# 리스트의 데이터 삭제
aa[2:] = []
print(aa)

