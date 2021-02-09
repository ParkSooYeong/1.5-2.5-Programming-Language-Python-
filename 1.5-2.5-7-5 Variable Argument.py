### SKU CoE ITE - ParkSooYoung ###
### Grade 1.5 , Semester 2.5 , Chapter 7 , Number 5 ###

'''
 def profile(name, age, lang1, lang2, lang3, lang4, lang5):

    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    print(lang1, lang2, lang3, lang4, lang5)
'''

def profile(name, age, *language):

    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")

    for lang in language:
        print(lang,  end = " ")

    print()

profile("유재석", 45, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
