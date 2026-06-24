# Usage of loops in Python

import time

# The "for" loop

for i in range(10):
    time.sleep(1)
    print(f"Countdown: {10 - i}")
print("Blast off!")

time.sleep(1)

print("Liftoff!")

time.sleep(1)

# The "while" loop

lives = 3

while lives > 0:
    time.sleep(1)
    print(f"You have {lives} lives left.")
    lives -= 1
print("Game over!")

time.sleep(1)

# The usage of loops in real-life scenarios

name = input("Enter your name: ")
times = int(input("How many times do you want to be greeted? "))

for _ in range(times):
    print(f"Hello, {name}!")

time.sleep(1)

# The "break" statement

while True:
    command = input("Enter a command (type 'exit' to quit): ")
    if command == "exit":
        print("Exiting the program.")
        break
    else:
        print(f"You entered: {command}")
