### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 4 , Number 6 ###

# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부븐은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#                 (nav)                (5)             (1)         (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"

# url = "http://daum.net"
# url = "http://google.com"
# url = "http://youtube.com"

temp = url[7:12] # temp = url.replace("http://", "") # 규칙1

# temp = temp[:temp.index(".")] # temp[0:5] -> 0 ~ 5 직전까지 (0,1,2,3,4) # 규칙2

# password = temp[:3] + str(len(temp)) + str(temp.count("e")) + "!"

print("생성된 비밀번호 : " + temp[:3] + str(len(temp)) + str(temp.count("e")) + "!")

# print("{0}의 비밀번호는 {1}입니다.".format(url, password))
