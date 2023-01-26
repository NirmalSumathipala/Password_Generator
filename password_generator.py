import random

print('''

   ▄███████▄    ▄████████    ▄████████    ▄████████  ▄█     █▄   ▄██████▄     ▄████████ ████████▄          ▄██████▄     ▄████████ ███▄▄▄▄      ▄████████    ▄████████    ▄████████     ███      ▄██████▄     ▄████████ 
  ███    ███   ███    ███   ███    ███   ███    ███ ███     ███ ███    ███   ███    ███ ███   ▀███        ███    ███   ███    ███ ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
  ███    ███   ███    ███   ███    █▀    ███    █▀  ███     ███ ███    ███   ███    ███ ███    ███        ███    █▀    ███    █▀  ███   ███   ███    █▀    ███    ███   ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
  ███    ███   ███    ███   ███          ███        ███     ███ ███    ███  ▄███▄▄▄▄██▀ ███    ███       ▄███         ▄███▄▄▄     ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀   ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
▀█████████▀  ▀███████████ ▀███████████ ▀███████████ ███     ███ ███    ███ ▀▀███▀▀▀▀▀   ███    ███      ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
  ███          ███    ███          ███          ███ ███     ███ ███    ███ ▀███████████ ███    ███        ███    ███   ███    █▄  ███   ███   ███    █▄  ▀███████████   ███    ███     ███     ███    ███ ▀███████████ 
  ███          ███    ███    ▄█    ███    ▄█    ███ ███ ▄█▄ ███ ███    ███   ███    ███ ███   ▄███        ███    ███   ███    ███ ███   ███   ███    ███   ███    ███   ███    ███     ███     ███    ███   ███    ███ 
 ▄████▀        ███    █▀   ▄████████▀   ▄████████▀   ▀███▀███▀   ▀██████▀    ███    ███ ████████▀         ████████▀    ██████████  ▀█   █▀    ██████████   ███    ███   ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
                                                                             ███    ███                                                                    ███    ███                                       ███    ███ 

                                                        _   _   _   _   _   _   _     _   _      _   _   _   _   _   _     _   _   _   _   _   _   _   _   _   _   _  
                                                        / \ / \ / \ / \ / \ / \ / \   / \ / \    / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
                                                        ( c | r | e | a | t | e | d ) ( b | y )  ( N | i | r | m | a | l ) ( S | u | m | a | t | h | i | p | a | l | a )
                                                        \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/    \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  

''')

#Assigning Upper Letters , Lower Letters , Numbers and Symbols To Lists.
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers       = [1,2,3,4,5,6,7,8,9,0]
symbols       = ["!" , "@" , "#" , "$" , "%" , "&" , "(" , ")" ]

#Taking user inputs as integer values.
user_lower      = int(input("How many lower letters do you want ? "))
user_upper      = int(input("How many upper letters do you want ? "))
user_numbers    = int(input("How many numbers do you want       ? "))
user_symbols    = int(input("How many symbols do you want       ? "))

#Using 'random.choices' function picking random lower letters , upper letters , numbers and symbols from the above lists
lower_pw = random.choices(lower_letters,k=user_lower)
upper_pw = random.choices(upper_letters,k=user_upper)
numbers_pw = random.choices(numbers,k=user_numbers)
symbols_pw = random.choices(symbols,k=user_symbols)

#Testing the code
# print(lower_pw)
# print(upper_pw)
# print(numbers_pw)
# print(symbols_pw)

#Assigning above random choices to a list
password_list = lower_pw + upper_pw + numbers_pw + symbols_pw

#Testing the code
#print(password_list)

#Using 'random.shuffle' function we can shuffle a list
random.shuffle(password_list)

#Testing the code
#print(password_list)

#Convert list in to a string
password_string = ''.join(map(str,password_list))

#Printing the generated password to the console
print("************************************************")
print(f"Your generated password is: {password_string}")
