#input for the sorting hat

Gryffindor = 0 
Ravenclaw = 0 
Hufflepuff = 0 
Slytherin = 0 

dawn_or_Dusk = int(input("type 1 for dawn and 2 for Dusk"))
Good_Great_Wise_Bold = int(input("When I’m dead, I want people to remember me as type 1 for good type 2 for great type 3 for wise type 4 for Bold"))
What_instrument = int(input(" Which kind of instrument most pleases your ear? type   1) The violin 2 The trumpet 3 The piano 4 The drum "))

if dawn_or_Dusk == 1: 
  Gryffindor += 1
  Ravenclaw += 1
 
elif dawn_or_Dusk == 2:
  Hufflepuff += 1 
  Slytherin  += 1 
  
else:
   print("Wrong input")


if Good_Great_Wise_Bold == 1: 
  Hufflepuff += 2 
 
elif Good_Great_Wise_Bold == 2:
 Slytherin  += 2 

elif Good_Great_Wise_Bold == 3: 
 Ravenclaw += 2

elif Good_Great_Wise_Bold == 4:
 Gryffindor += 2
else:
   print("Wrong input")



if Good_Great_Wise_Bold == 2: 
  Hufflepuff += 4 
 
elif Good_Great_Wise_Bold == 1:
 Slytherin  += 4 

elif Good_Great_Wise_Bold == 3: 
 Ravenclaw += 4

elif Good_Great_Wise_Bold == 4:
 Gryffindor += 4
else:
   print("Wrong input")

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
