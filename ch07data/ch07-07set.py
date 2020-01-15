mySet1 = {1,2,3,4,4,4,3}
print(mySet1)

saleList = ['삼김', '바나나', '삼김', '도시락', '삼김', '도시락', '라면', '삼김']
set(saleList)

print(set(saleList))

for i in set(saleList):
    print("%s 의 주문 횟수는 : %d " % (i, saleList.count(i)))

mySet1 = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7}
print(mySet1 & mySet2) # 교집합
print(mySet1 | mySet2) # 합집합
print(mySet1 - mySet2) # 차집합
print(mySet1 ^ mySet2) # 대칭 차집합


list1 = [1, 2, 3, 4, 5]
list2 = []

for i in range(1,101):
    list2.append(i)
print("list2 = %s " % list2)

list3 = [num for num in range(1, 5+1)]

print("list3 = %s" % list3)


# 1 ~ 10 사이 3의 배수로 리스트 만들기 -> [3, 6, 9]
# for i in range(1,10+1)
#    if i % 3 == 0:
#       list2.append(i)

list4 = [num for num in range(1, 10+1) if num % 3 == 0]
print("list4 = %s" % list4)

# 1 ~ 5 의 데이터 제곱을 구해서 리스트를 만들어라
list5 = [num*num for num in range(1, 5+1)]
print("list5 = %s" % list5)

foods = ["떡볶이", "짜장면", "라면", "피자"]
sides = ["오뎅", "단무지", "김치"]

for food, side in zip(foods, sides):
    print(food, "-->", side)

print('while')
i = 0

while True:
    if bool(foods[i] != '') & bool(sides[i] != ''):
        print(foods[i], "-->", sides[i])
        i += 1
    else:
        break
