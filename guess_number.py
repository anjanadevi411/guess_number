from random import randint

answer = randint(1,10)

guess = int(input("Guess a number between 1 to 10: "))

if guess == answer:
    print("guessed correctly")
else:
    if guess < answer:
        print("Nope, it's higher")
    else:
        print("Nope, it's lower")

print(f"The number was: {answer}")
