
#find out what they want to calculate  

print('==================')
print('Area Calculator 📐')
print('==================')
print('')
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print("")
Waht_are_wecaluating = 0
Waht_are_wecaluating = int(input("which shape "))  
print("")

if Waht_are_wecaluating == 1:
    side = int(input("Type the side length of the square "))
    print("")
    sqaure = side * side 
    print(f"the square area is {sqaure}")
elif Waht_are_wecaluating == 2:
    lenght = int(input(" What is the length of your rectangle ? " ))
    print("")
    width = int(input( "what is the width of your rectangle ? "))
    print("")
    Rectangle = lenght * width 
    print(f"The Rectangle area is {Rectangle}")
elif Waht_are_wecaluating == 3:
    height = int(input("what is the height of your triangle ? "))
    print("")
    base = int(input(" waht is the base of your triangle ? "))
    print("")
    Triangle = base * height / 2 
    print(f" The Triangle area is {Triangle}")
elif Waht_are_wecaluating == 4:
    radius = int(input(" what is the radius of your circul ?"))
    print(" ")
    Circle = 3.14 * radius ** 2 
    print(f"The area of your circel is {Circle}")
else:
    print("please enter one of the nummbers 1-4")

