### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 5 , Number 2 ###

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 새 손님
print(cabinet2)
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호"
print(cabinet2)

# 간 손님
del cabinet2["A-3"]
print(cabinet2)

# key 들만 출력
print(cabinet2.keys())

# Value 들만 출력
print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet2.items())

# 목욕탕 폐점
cabinet2.clear()
print(cabinet2)
