
#This list will supply the randomly generated vacation destinations.

destination_list = ["New York City", "Boston", "St Augustine,Florida"]
#These next three lists will pertain to our fist destination on our list New York City.

nyc_restaurant_list = ["Carmine's Italian Restaurant", "STK Steakhouse Midtown NYC","La Grande Boucherie"]
nyc_transportation_list = ["Taxi Cab", "Subway", "Uber XL"]
nyc_entertainment_list = ["Broadway", "Top of The Rock: Observation Deck", "Madame Tussauds New York"]

#These next three lists will pertain to our second destination. St Augustine, Florida.

florida_restaurant_list = ["Salt Life", "Harry's Seafood, Bar & Grille","Prohibition Kitchen"]
florida_transportation_list =["Old Town Trolley Tours St Augustine", "Taxi Cab", "Salty Seas Transportation"]
florida_entertainment_list = ["Castillo de San Marcos National Monument", "Ripley's Believe It or Not!", "Ponce de Leon's Fountain of Youth Archaeological Park","Lightner Museum"]

#These three lists will pertain to our final destination. Boston.

boston_restaurant_list = ["Del Frisco's Double Eagle Steakhouse", "Bostonia Public House", "Buttermilk & Bourbon"]
boston_transportation_list =["Uber Xl", "Taxi Cab", "Bus"]
boston_entertainment_list =["Boston Crime Tour", "Samuel Adams Brewery Tour", "Fenway Park", "Whale Watching boat tour", "Boston Aquarium"]


import random

random_dest = random.choice(destination_list)
if random_dest == "New York City":
    are_you_happy = input(f'Are you happy with {random_dest}? (y/n) ')
    if are_you_happy == "y":
        print(f'Great, we will figure out where you will go eat!')
    elif are_you_happy == "n":
        remove_ny = destination_list.pop(0)
        random_dest_pop = random.choice(destination_list)
        print(f'You are now going to {random_dest_pop}!')
        are_you_happy = input(f'Are you happy with this location? (y/n) ')
        if are_you_happy == "y":
         random_dest = random_dest_pop
         print(f'You are now going to {random_dest}!')
        elif are_you_happy == "n":
         if random_dest_pop == "St Augustine,Florida":
            remove_florida = destination_list.pop(1)
            random_dest_pop_florida = random.choice(destination_list)
            print(f'You are now going to {random_dest_pop_florida}!')
            are_you_happy = input(f'Are you happy with this location? (y/n) ')
            if are_you_happy == "y":
                random_dest = random_dest_pop_florida
                print(f'Youn are now going to {random_dest_pop_florida}!')
         
elif random_dest == "Boston":
     are_you_happy = input(f'Are you happy with {random_dest}? (y/n) ')
     if are_you_happy == "y":
        print(f'Great, we will figure out where you will go eat!')
     elif are_you_happy == "n":
        remove_boston = destination_list.pop(1)
        random_dest_pop_boston = random.choice(destination_list)
        print(f'You are now going to {random_dest_pop_boston}!')
        are_you_happy = input(f'Are you happy with this location? (y/n) ')
        if are_you_happy == "y":
         random_dest = random_dest_pop_boston
         print(f'You are now going to {random_dest}!')
        elif are_you_happy == "n":
         if random_dest_pop_boston == "St Augustine,Florida":
            remove_florida = destination_list.pop(1)
            random_dest_pop_florida = random.choice(destination_list)
            print(f'You are now going to {random_dest_pop_florida}!')
            are_you_happy = input(f'Are you happy with this location? (y/n) ')
            if are_you_happy == "y":
                random_dest = random_dest_pop_florida
                print(f'Youn are now going to {random_dest_pop_florida}!')
        elif random_dest_pop_boston == "New York City":
             print(f'{random_dest} is your last destination choice!')
             are_you_happy = input(f'Are you happy with {random_dest}? ')
    

elif random_dest == "St Augustine,Florida":
     are_you_happy = input(f'Are you happy with {random_dest}? (y/n) ')
     if are_you_happy == "y":
        print(f'Great, we will figure out where you will go eat!')
     elif are_you_happy == "n":
        remove_florida = destination_list.pop(2)
        random_dest_pop_florida = random.choice(destination_list)
        print(f'You are now going to {random_dest_pop_florida}!')
        are_you_happy = input(f'Are you happy with this location? (y/n) ')
        if are_you_happy == "y":
         random_dest = random_dest_pop_florida
         print(f'You are now going to {random_dest}!')
        elif are_you_happy == "n":
         if random_dest_pop_florida == "Boston":
            remove_boston = destination_list.pop(1)
            random_dest_pop_boston = random.choice(destination_list)
            print(f'You are now going to {random_dest_pop_boston}!')
            are_you_happy = input(f'Are you happy with this location? (y/n) ')
            if are_you_happy == "y":
                random_dest = random_dest_pop_boston
                print(f'Youn are now going to {random_dest_pop_boston}!')
            elif are_you_happy == "n":
                 if random_dest_pop_boston == "New York City":
                    print(f'There are no more options! So we will keep this last one!')
                    random_dest_pop_boston == random_dest

        elif random_dest_pop_florida == "New York City":
             print(f'{random_dest} is your last destination choice!')
             are_you_happy = input(f'Are you happy with {random_dest}? ')
    
    
if random_dest == "New York City":
    random_rest = random.choice(nyc_restaurant_list)

    if random_rest == "Carmine's Italian Restaurant":
      are_you_happy = input(f'Are you happy with {random_rest}? (y/n) ')
      if are_you_happy =="y":
        print("Okay , great!")
      elif are_you_happy == "n":
        print("we will figure that out")

    elif random_rest == "La Grande Boucherie":
      are_you_happy = input(f'Are you happy with {random_rest}? (y/n) ')
      if are_you_happy == "y":
        print("Great! that sounds good!")
      elif are_you_happy == "n":
        print("Wait a dang second!")

    elif random_rest =="STK Steakhouse Midtown NYC":
      are_you_happy = input(f'Are you okay with {random_rest} as a selection? (y/n) ')
      if are_you_happy == "y":
        print(f'Great! you will be going to {random_rest}, now lets figure out what kind of transportation you will be using.')
      elif are_you_happy == "n":
        print("Give me a minute!")

# New York Transportation Functions
    if random_dest == "New York City":
     random_trans_nyc = random.choice(nyc_transportation_list)

     if random_trans_nyc == "Taxi Cab":
        are_you_happy = input(f'Are you happy with taking a {random_trans_nyc}? (y/n) ')
        if are_you_happy == "y":
           print(f'Great! You will be taking a {random_trans_nyc} to get around. Now lets find out where you will be eating.')
        elif are_you_happy == "n":
            remove_taxi = nyc_transportation_list.pop(0)
            random_trans_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to use a {random_trans_pop_nyc}!')
            are_you_happy = input(f'Are you happy with this location? (y/n) ')
            if are_you_happy == "y":
                random_dest = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
     elif random_trans_nyc == "Subway":
          print(f'{random_trans_nyc} is your last destination choice!')
          are_you_happy = input(f'Are you happy with {random_trans_nyc}? ')
          if are_you_happy == "y":
             print(f'Great! thats good to hear!')
          elif are_you_happy == "n":
            remove_subway = nyc_transportation_list.pop(1)
            random_trans_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to use a {random_trans_pop_nyc}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_nyc (y/n)} ')
            if are_you_happy == "y":
                random_dest = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
    
# New York Entertainment Functions
     if random_dest == "New York City":
         random_ent_nyc = random.choice(nyc_entertainment_list)

         if random_ent_nyc == "Broadway":
            are_you_happy = input(f'Are you happy with going to {random_ent_nyc}? (y/n) ')
            if are_you_happy == "y":
                print(f'Great! You will be going to the world famous {random_ent_nyc}!')
            elif are_you_happy == "n":
                remove_broadway = nyc_entertainment_list.pop(0)
                random_ent_pop_nyc = random.choice(nyc_entertainment_list)
                print(f'You are now going to {random_ent_pop_nyc}')
                are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
                if are_you_happy == "y":
                    random_ent_nyc = random_ent_pop_nyc
                    print(f'You are now going to {random_ent_pop_nyc}!')
         elif random_ent_nyc == "Top of The Rock: Observation Deck":
              are_you_happy = input(f'Are you happy with going to {random_ent_nyc}? (y/n) ')
              if are_you_happy == "y":
                 print(f'Great! You will be going to the world famous {random_ent_nyc}!')
              elif are_you_happy == "n":
                remove_broadway = nyc_entertainment_list.pop(0)
                random_ent_pop_nyc = random.choice(nyc_entertainment_list)
                print(f'You are now going to {random_ent_pop_nyc}')
                are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
                if are_you_happy == "y":
                    random_ent_nyc = random_ent_pop_nyc
                    print(f'You are now going to {random_ent_pop_nyc}!')



# Boston List Functions
elif random_dest == "Boston":
     random_rest_boston = random.choice(boston_restaurant_list)

     if random_rest_boston == "Del Frisco's Double Eagle Steakhouse":
         are_you_happy = input(f'Are you happy with {random_rest_boston}? (y/n) ')
         if are_you_happy =="y":
          print("Okay , great!")
         elif are_you_happy == "n":
          print("we will figure that out")

     elif random_rest_boston == "Bostonia Public House":
          are_you_happy = input(f'Are you happy with {random_rest_boston}? (y/n) ')
          if are_you_happy == "y":
            print("Great! that sounds good!")
          elif are_you_happy == "n":
            print("Wait a dang second!")

     elif random_rest_boston == "Buttermilk & Bourbon":
          are_you_happy = input(f'Are you happy with {random_rest_boston}? (y/n) ')
          if are_you_happy == "y":
            print("Great! that sounds good!")
          elif are_you_happy == "n":
            print("Wait a dang second!")

# Boston Transportation Functions
     if random_dest == "Boston":
      random_trans_boston = random.choice(boston_transportation_list)

     if random_trans_boston == "Uber Xl":
      are_you_happy = input(f'Are you happy using {random_trans_boston} for transportation? (y/n) ')
      if are_you_happy == "y":
        print(f'Great! you will be using {random_trans_boston} to get around!')
      elif are_you_happy == "n":
        print()
        
# Boston Entertainement Functions
     if random_dest == "Boston":
      random_ent_boston = random.choice(boston_entertainment_list)



#ST Augustine, Florida
# St Augustine,Florida Restaurant List Functions
     if random_dest == "St Augustine,Florida":
      random_rest_florida = random.choice(florida_restaurant_list)

      if random_rest_florida == "Salt Life":
       are_you_happy = input(f'Are you happy with {random_rest_florida}? (y/n) ')
       if are_you_happy =="y":
        print("Okay , great!")
      elif are_you_happy == "n":
        print("we will figure that out")

      elif random_rest_florida == "Harry's Seafood, Bar & Grille":
       are_you_happy = input(f'Are you happy with {random_rest_florida}? (y/n) ')
       if are_you_happy == "y":
        print("Great! that sounds good!")
       elif are_you_happy == "n":
        print("Wait a dang second!")

      elif random_rest_florida == "Prohibition Kitchen":
       are_you_happy = input(f'Are you happy with {random_rest_florida}? (y/n) ')
       if are_you_happy == "y":
        print("Great! that sounds good!")
       elif are_you_happy == "n":
        print("Wait a dang second!")

# St Augustine,Florida Transportation Functions
     if random_dest == "St Augustine,Florida":
       random_trans_florida = random.choice(florida_transportation_list)

# St Augustine,Florida Entertainement Functions
     if random_dest == "St Augustine,Florida":
       random_ent_florida = random.choice(florida_entertainment_list)



if random_dest == "New York City":
    confirm_trip = input(f'Are you happy with all of your vacation details? (y/n) ')
    if confirm_trip == "y":
     print(f'Congratulations on confirming your vacation details. You will be going to {random_dest}. Once there, you will be using {random_trans_nyc} to get to {random_ent_nyc}. Once there, you will enjoy one of {random_dest}s many attractions. After {random_ent_nyc} you will take a {random_trans_nyc} to {random_rest} where you will enjoy a great meal!')
