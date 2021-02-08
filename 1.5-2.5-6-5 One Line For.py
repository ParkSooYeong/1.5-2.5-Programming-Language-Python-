### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 6 , Number 5 ###

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]

print(students)

students = [i + 100 for i in students]

print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Captain America", "Thor"]
students = [len(i) for i in students]

print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Captain America", "Thor"]
students = [i.upper() for i in students]

print(students)
