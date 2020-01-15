# 별개의 새로운 리스트를 만든다. 예전에 데이터를 그대로 사용
oldlist = ["짜장면"]
# newlist = oldlist # 주소값 복사
# newlist = oldlist.copy() # 데이터값 복사
newlist = oldlist[:] # 데이터값 복사

print("oldlist : %s" % oldlist)
print("newlist : %s" % newlist)

oldlist.append("탕수육")

print("oldlist : ", oldlist)
print("newlist : ", newlist)

