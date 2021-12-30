import random
num = random.randint(01, 99)
guess = ""
guess_count = 0

while guess != num:
      guess=int(input("guess a 2 digit number:"))
    guess_count +=1
    if guess==num:
    print("your guess is correct. You guessed it in:",guess_count)
   break
elif guess>num:
print("Guess is high")
elif guess<num:
print("Guess is low")
