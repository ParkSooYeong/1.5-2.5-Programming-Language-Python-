### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 5 , Number 6 ###

"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
"""

from random import *

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # users = range(1, 21) # 1부터 20까지 숫자를 생성

# users = list(users)

shuffle(lst)
temp = sample(lst, 4) # 1명 뽑고 3명을 뽑으려하였으나 4명을 동시에 뽑는것이 중복 방지면에서 효율적

print("-- 당첨자 발표--")
print("치킨 당첨자 : " + str(temp[0])) # print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : " + str(temp[1:4])) # print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
