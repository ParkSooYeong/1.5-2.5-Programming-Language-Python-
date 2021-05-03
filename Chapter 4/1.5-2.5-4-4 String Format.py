### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 4 , Number 4 ###

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 24)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
# %s
print("나는 %s살입니다." % 24)
print("나는 %s색과 %s색을 좋아해요." % ("푸른", "멋진"))

# 방법 2
print("나는 {}살입니다.".format(24))
print("나는 {}색과 {}색을 좋아해요.".format("푸른", "멋진"))
print("나는 {0}색과 {1}색을 좋아해요.".format("푸른", "멋진"))
print("나는 {1}색과 {0}색을 좋아해요.".format("푸른", "멋진"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 24, color = "멋진"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "멋진", age = 24))

# 방법 4 (v3.6 이상 ~)
age = 24
color = "멋진"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
