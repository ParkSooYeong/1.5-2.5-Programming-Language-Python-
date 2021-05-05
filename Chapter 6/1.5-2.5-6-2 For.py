### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 6 , Number 2 ###

'''
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
'''

for waiting_number in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_number))

for waiting_number in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_number))

for waiting_number in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_number))
    
starbucks = ["아이언맨", "캡틴아메리카", "토르"]

for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
