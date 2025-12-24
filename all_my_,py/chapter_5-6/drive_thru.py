#


def get_item(option):
   if  option == 1:
       return('🍔 Cheeseburger')
   elif option == 2:
       return('🍟 Fries')
   elif option == 3:
       return('🥤 Soda')
   elif option == 4:
       return('🍦 Ice Cream')
   elif option == 5:
       return('🍪 Cookie')
   else:
       return(f'Sorry, {option} is not available.')
    
  




def welcome():
    print("Hello this is are menu today:") 
    print('1🍔 Cheeseburger')
    print('2🍟 Fries')
    print('3🥤 Soda')
    print('4🍦 Ice Cream')
    print('5🍪 Cookie')
        
    
welcome()

option = int(input('What would you like to order? '))
print(get_item(option))

