### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 8 , Number 5 ###

import pickle

with open("profile.pickle", "rb") as profile_file:

    print(pickle.load(profile_file))

with open("study.txt", "w", encoding = "utf8") as study_file:

    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding = "utf8") as study_file:

    print(study_file.read())
