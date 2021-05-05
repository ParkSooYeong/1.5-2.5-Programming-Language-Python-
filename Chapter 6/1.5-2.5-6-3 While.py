### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 6 , Number 3 ###

# while

customer = "토르"
index = 5

while index >= 1:

    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))

    index -= 1

    if index == 0:
        print("주문하신 커피가 폐기처분되었습니다.")

'''
customer = "아이언맨"
index = 1

while True:
    print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
    index += 1
'''

customer = "캡틴아메리카"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("성함이 어떻게 되세요? : ")
