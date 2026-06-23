 # My first python script to test buglem and to test my python skills

import time

score = 3

print("hello buglem, this is a script to test that buglem is working correctly")
print("while answering the questions, please never use uppercase letters")

time.sleep(3)

buglem = input("are you ready to start the test? (yes/no): ")
if buglem != "yes":
    print("ok, maybe next time")
    exit()
elif buglem == "yes":
    print("great! let's start the test")

time.sleep(3)

name = "emir"
lastname = "karakaya"

print("first question: what is my full name?")
answer1 = input("your answer: ")
if answer1 != name + " " + lastname:
    print(f"wrong answer, the correct answer is: {name} {lastname}")
    score -= 1
else:
    print("correct answer, well done!")

time.sleep(3)

fullbirthday = "2010-08-30"
print("second question: what is my birthday? (format: yyyy-mm-dd)")
answer2 = input("your answer: ")
if answer2 != fullbirthday:
    print(f"wrong answer, the correct answer is: {fullbirthday}")
    score -= 1
else:
    print("correct answer, well done!")

time.sleep(3)

favoritecolor = "red"

print("third question: what is my favorite color?")
answer3 = input("your answer: ")
if answer3 != favoritecolor:
    print(f"wrong answer, the correct answer is: {favoritecolor}")
    score -= 1
else:
    time.sleep(3)
    print(f"The rose is red, the violet's blue, " \
    f"The honey's sweet, and so are you.")

time.sleep(3)

print("test completed!")
print(f"your final score is: {score}")
print("thank you for taking the test, have a great day!")
