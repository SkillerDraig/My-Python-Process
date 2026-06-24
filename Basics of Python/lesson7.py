# Usage of list and for loop in Python

import time

favoritemovies = ["Inception", "Seven", "Prisoners", "Fight Club", "Snatch"]
guess = input("guess one of my favorite movies: ")

time.sleep(2)

if guess in favoritemovies:
    print("correct")
else:
    print("wrong")
    print("my favorite movies are: ")
    for movie in favoritemovies:
        print(movie)
        time.sleep(1)

print("thank you for taking the test, have a great day!")
