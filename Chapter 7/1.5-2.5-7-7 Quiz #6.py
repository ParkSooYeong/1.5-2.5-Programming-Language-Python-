### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 7 , Number 7 ###

'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)

남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.35kg 입니다.
'''

def std_weight(height, gender):

    if gender == "남자":
        weight = height * height * 22 # return height * height * 22
        std = str(weight)
        print("키 {0}cm 남자의 표준 체중은 {1}.{2}kg 입니다.".format(height, std[0:2], std[3:5]))
    elif gender == "여자":
        weight = height * height * 21
        std = str(weight)
        print("키 {0}cm 여자의 표준 체중은 {1}.{2}kg 입니다.".format(height, std[0:2], std[3:5]))
    else:
        print("다시 입력해주세요.")

gender = str(input("성별을 입력해주세요.(남자 or 여자) : "))
height = int(input("키를 입력해주세요.(cm) : "))

std_weight(height, gender)
