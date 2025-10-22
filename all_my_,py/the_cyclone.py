height = int(input(" waht is your height in cm "))
credits = int(input("how many credits do you have "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride ")
elif height < 137 and credits >= 10:
       print("You are not tall enough to ride ") 
elif height >= 137 and credits < 10: 
         print("your dont have enough credits")
else :
    print(" you have not met the requirements to ride ")