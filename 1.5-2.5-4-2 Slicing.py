### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 4 , Number 2 ###

jumin = "980414-1234567"

print("성별 : " + jumin[7])
print("생년 : " + jumin[0:2]) # 0 ~ 2 직전까지 (0,1)
print("생월 : " + jumin[2:4])
print("생일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("후속정보 : " + jumin[7:]) # 7 부터 끝까지
print("후속정보(reverse) : " + jumin[-7:]) # 맨 뒤, 7번째부터 끝까지
