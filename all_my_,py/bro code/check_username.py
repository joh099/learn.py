

name = input("Enter your unsername:")

name = name.upper()

if len(name) > 12:
    print(' your user name cant be over 12 characters')
elif not name.find(' ') == -1:
    print('you cant have spaces ')
elif  not name.isalpha():
    print("you can only use Letters")
else:
    print(f'welcome{name}')