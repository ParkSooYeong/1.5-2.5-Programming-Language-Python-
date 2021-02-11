### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 9 , Number 11 ###


'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass
'''


class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):

        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):

        print("{0} {1} {2} {3} {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        # print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# house = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")


class Gangnam(House):

    def __init__(self):

        House.__init__(self, "강남", "아파트", "매매", "10억", 2010)


class Mapo(House):

    def __init__(self):

        House.__init__(self, "마포", "오피스텔", "전세", "5억", 2007)


class Songpa(House):

    def __init__(self):

        House.__init__(self, "송파", "빌라", "월세", "500/50", 2000)


G = Gangnam()
M = Mapo()
S = Songpa()

# house.append(house1)
# house.append(house2)
# house.append(house3)

print("총 3대의 매물이 있습니다.") # print("총 {0}대의 매물이 있습니다.".format(len(houses)))

House.show_detail(G)
House.show_detail(M)
House.show_detail(S)

# for house in houses:
#     house.show_detail()
