### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 8 , Number 4 ###

import pickle

profile_file = open("profile.pickle", "wb")
profile = {"이름" : "박명수", "나이" : 50, "취미" : ["축구", "골프", "코딩"]}

print(profile)

pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()


profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기

print(profile)

profile_file.close()
