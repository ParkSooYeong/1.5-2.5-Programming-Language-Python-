### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 6 , Number 6 ###

'''
Quiz) 당신은 KaKao 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[O] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 명
'''

from random import *

index = 0 # 총 탑승 승객 수

for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)

    j = randrange(5, 51) # my answer : int((random() * 50) + 5)

    if 5 <= j <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, j))
        index += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, j))

print("총 탑승 승객 : {0}명".format(index)) # my answer : if i == 50: print("총 탑승 승객 : {0}명".format(index))
