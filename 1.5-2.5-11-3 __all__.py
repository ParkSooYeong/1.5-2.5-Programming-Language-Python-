### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 11 , Number 3 ###


'''
# thailand.py
class ThailandPackage:

    def detail(self):

        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원)")

# vietnam.py
class VietnamPackage:

    def detail(self):

        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")

# __init__.py
__all__ = ["vietnam", "thailand"]
'''


import travel.thailand
# import travel.thailand.ThailandPackage
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
