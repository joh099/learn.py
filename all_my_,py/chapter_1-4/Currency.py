# MY code 

Peso_to_USD = int(input("how many peso do you have "))

Peso_to_USD =  Peso_to_USD * 0.00025

reais_to_USD = int(input("how many real do you have"))


reais_to_USD = reais_to_USD * 0.18 

peruvian_to_USD = int(input("how many sol do you have")) 

peruvian_to_USD = peruvian_to_USD * 0.29 

final_abount = Peso_to_USD + reais_to_USD + peruvian_to_USD 
print(" in $")
print(final_abount)
print( "________________________________")
print(' this is how much you still have')



# The best way to code it 
# Currency 💵
# Codédex

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = pesos * 0.00025 + soles * 0.28 + reais * 0.21

print(total)
