for x in range (1,100):
  print(x)
  if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")     
  elif x % 3 == 0:
    print("Fizz")
  elif x % 5 == 0:    
    print("Buzz")
