### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 8 , Number 1 ###

print("Python", "Java")
print("Python", "Java", sep = ",")
print("Python", "Java", sep = " vs ")
print("Python", "Java", "JavaScript", sep = " vs ")
print("Python", "Java", sep = ",", end = "?")
print("무엇이 더 재밌을까요?")

import sys

print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)


# 시험 성적
scores = {"수학":99, "영어":66, "코딩":33}

for subject, score in scores.items():

    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")


# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):

    print("대기번호 : " + str(num).zfill(3))


answer = input("아무 값이나 입력하세요. : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
