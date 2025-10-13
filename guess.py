guess = 0
tries = 0
while guess != 6 and tries < 7:
  guess = int(input("Guess the number:  "))
  tries += 1

if guess == 6:
  print("You guessed it!")  

else:
  print("Sorry, you lose!")