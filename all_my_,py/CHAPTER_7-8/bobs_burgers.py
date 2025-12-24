# BOBS BURGER

class Restaurant:
    name = ''
    category = ''
    rating = 0.0 
    delivery = False
    
bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))


PAPA_JOHN = Restaurant()

PAPA_JOHN.name = 'PAPA JOHN'
PAPA_JOHN.category = 'PIZZA'
PAPA_JOHN.rating = 4.0
PAPA_JOHN.delivery = True

print(vars(PAPA_JOHN))

Momas_pie = Restaurant()

Momas_pie.name = 'Momas_pie'
Momas_pie.category = 'CAEKE'
Momas_pie.rating = 4,8
Momas_pie.delivery = False 

print(vars(Momas_pie))

