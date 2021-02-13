### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 11 , Number 4 ###


'''
# thailand.py
class ThailandPackage:

    def detail(self):

        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원)")

if __name__ == "__main__":

    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")

    trip_to = ThailandPackage()
    trip_to.detail()

else:

    print("Thailand 외부에서 모듈 호출")
'''

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
