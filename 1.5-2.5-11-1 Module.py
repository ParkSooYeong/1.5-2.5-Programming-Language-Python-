### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 11 , Number 1 ###


# 일반 가격
def price(people):

    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조 할인 가격
def price_morning(people):

    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):

    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))


'''
import 1.5-2.5-11-1 Module # 실제 사용 시 모듈명 변경 필요

1.5-2.5-11-1 Module.price(3) # 3명이서 영화 보러 갔을 때 가격
1.5-2.5-11-1 Module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
1.5-2.5-11-1 Module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

import 1.5-2.5-11-1 Module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from 1.5-2.5-11-1 Module import * # from random import *
price(3)
price_morning(4)
price_soldier(5)

from 1.5-2.5-11-1 Module import price, price_morning
price(5)
price_morning(4)
# price_soldier(3)

from 1.5-2.5-11-1 Module import price_soldier as price
price(5)
'''
