
class Pokemon:
    def __init__(self,entry,name,types,description,is_caught):
     self.entry = entry
     self.name = name
     self.types = types
     self.description = description
     self.is_caught =  is_caught
     
    def speak(self):
        print(f"This pokemon makes this sound {self.name} {self.name}")
        
    def display_details(self):
        print(f'Entry Number:{self.entry}')
        print(f'Name:{self.name}')
        print(f'Type:{self.types}')
        print(f'Description:{self.description}')
        if self.is_caught == True:
            print(f"{self.name} has already been caught! ")
        else:
            print(f"{self.name} can be caught")








Bulbasaur = Pokemon(1,'Bulbasaur',['Grass','poison'],'Bulbasaur carries a seed on its back that grows as it absorbs sunlight. It can store energy for battle and growth through photosynthesis',True)      
        
Charmander = Pokemon(4,'Charmander',['fire'],'Charmander has a flame burning at the tip of its tail. The flame shows its life force and burns brighter when it is excited or angry.',False)

Squirtle = Pokemon(7,'Squirtle',['water'],'Squirtle protects itself by hiding in its shell. It sprays water with strong pressure to defend itself or attack opponents.',True)

Bulbasaur.speak()

Charmander.display_details()
Squirtle.display_details()