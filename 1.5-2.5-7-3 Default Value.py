### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 7 , Number 3 ###

def profile(name, age, main_lang):

    print("이름 : {0}\t나이 : {1}\t,주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 45, "파이썬")
profile("김태호", 40, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

def profile2(name, age = 17, main_lang = "파이썬"):

    print("이름 : {0}\t나이 : {1}\t,주 사용 언어 : {2}".format(name, age, main_lang))

profile2("유재석")
profile2("김태호")
