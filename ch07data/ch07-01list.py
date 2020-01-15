# aa = [0, 0, 0, 0]
aa = []
hap = 0

# print(aa)
print(len(aa))

for i in range(0, 4):
    aa.append(int(input(str(i + 1)+"번째 숫자:")))
# aa[i] = int(input(str(i+1)+"번째 숫자:"))
'''
aa[0] = int(input("첫번째 숫자 : "))
aa[1] = int(input("두번째 숫자 : "))
aa[2] = int(input("세번째 숫자 : "))
aa[3] = int(input("네번째 숫자 : "))
'''

# index 값을 증가하면서 합계 구함
# for i in range(0, len(aa)):
#     hap += aa[i]
# hap = aa[0] + aa[1] + aa[2] + aa[3]

# 리스트에 있는 데이터를 하나씩 꺼내와서 합계 구함
for i in aa:
    hap += i

print(aa)
print(aa[0])
print("합계 : %d" % hap)

