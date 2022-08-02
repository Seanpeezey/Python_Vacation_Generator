welcome = "Welcome to Day Trip Generator"
print(welcome)

import random
# Destination List 
destinations_list = ['New York', 'Florida', 'Maryland', 'California', 'Texas']
destination = random.choice(destinations_list)

transportations_list = ['Car', 'Train', 'Plane', 'Motorcycle', 'Bike']
transportation = random.choice(transportations_list)

entertainments_list = ['Beach', 'Museum', 'Sport Stadium', 'Club', 'Park']
entertainment = random.choice(entertainments_list)

restaurants_list = ['Shake Shak', 'Pizza Hut', 'McDonalds', 'Chipotle', 'Five Guys']
restaurant = random.choice(restaurants_list)




user_response = input('Do you want to go? Yes or No: ')

if user_response == "Yes":
   print(f"Awesome! We chose {destination}!")
   user_response = input(f'Are you okay going to {destination}? Yes or No ')
   if user_response == "Yes":
    print(f'Thats great! you will love {destination}.')
   elif user_response == "No":
    print("Well, let's see if this next one makes you happy... Let's try again!")
    destination = random.choice(destinations_list)
    print(f'How does {destination} sound? ')
    user_response  = input(f'Are you happy with {destination}? Yes or No')
    
        
#Transportation Selection
transportation = random.choice(transportations_list)
print(f'We will be using {transportation} to get around!')
user_response = input(f'Are you okay with using {transportation} to get around? Yes or No: ')

if user_response == "Yes":
    print(f'Thats great! you will be using {transportation} to get around!')
elif user_response == "No":
    transportation = random.choice(transportations_list)
    print(f'Im Sorry you didnt like our transportation choice. We have chosen {transportation} for you.')
    user_response = input(f'Would you like to go to {transportation}? Yes or No ')
    if user_response == "Yes":
        print(f'Great! You will now be going to {transportation}!')
    elif user_response == "No":
         transportation = random.choice(transportations_list)
         print(f'Im Sorry you didnt like our transportation choice. We have chosen {transportation} for you.')
         user_response = input(f'Would you like to go to {transportation}? Yes or No ')

# Entertainment Selection
entertainment = random.choice(entertainments_list)
print(f'For your entertainment, we have chosen {entertainment}!')
user_response = input(f'Are you okay with {entertainment}?  Yes or No: ')

if user_response == "Yes":
    print(f'Thats great! you will enjoy your night at {entertainment}!')
elif user_response == "No":
    entertainment = random.choice(entertainments_list)
    print(f'Im Sorry you didnt like our entertainment choice. We have chosen {entertainment} for you.')
    user_response = input(f'Would you like to go to {entertainment}? Yes or No ')
    if user_response == "Yes":
        print(f'Great! You will now be going to {entertainment}!')
    elif user_response == "No":
         entertainment = random.choice(entertainments_list)
         print(f'Im Sorry you didnt like our entertainment choice. We have chosen {entertainment} for you.')
         user_response = input(f'Would you like to go to {entertainment}? Yes or No ')

# Restaurant Selection
restaurant = random.choice(restaurants_list)
print(f'For your restaurant, you will be going to {restaurant}!')
user_response = input(f'Are you okay with going to {restaurant}? Yes or No ')

if user_response == "Yes":
    print(f'Thats great! You will be going to {restaurant}!')
elif user_response == "No":
    restaurant = random.choice(restaurants_list)
    print(f'Im Sorry you didnt like our restaurant choice. We have chosen {restaurant} for you.')
    user_response = input(f'Would you like to go to {restaurant}? Yes or No ')
    if user_response == "Yes":
        print(f'Great! You will now be going to {restaurant}!')
    elif user_response == "No":
         restaurant = random.choice(restaurants_list)
         print(f'Im Sorry you didnt like our restaurant choice. We have chosen {restaurant} for you.')
         user_response = input(f'Would you like to go to {restaurant}? Yes or No ')


confrim_trip = input('Are you happy with your day trip details? Yes or No ')
if confrim_trip == "Yes":

 print(f'Great! So lets go over your trip! You will be going to {destination}. Once there you will be using {transportation} to get to your reservation at {restaurant}. After you have enjoyed your meal, you will take {transportation} to {entertainment} where you will enjoy the remainder of your day! Thank you for using the day trip generator.') 

"""
So i pretty much deleted my entire code. I realized the code I was typing up was very ineficient and sloppy. 
I was having a hard time organizing and structuring the code for it to work.

Even this is somewhat a broken code and im sure there are tools ive been taught that I have not implemented correctly in this project. 
I will study more on Defining functions as well as While statements. I think If i had a better understanding of these, this project would
have been done on time and correctly. 

"""