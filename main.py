
#This list will supply the randomly generated vacation destinations.

destination_list = ["New York City", "Boston", "St Augustine,Florida"]
#These next three lists will pertain to our fist destination on our list New York City.

nyc_restaurant_list = ["Carmine's Italian Restaurant", "STK Steakhouse Midtown NYC","La Grande Boucherie"]
nyc_transportation_list = ["Taxi Cab", "Subway", "Uber XL"]
nyc_entertainment_list = ["Broadway", "Top of The Rock: Observation Deck", "Madame Tussauds New York"]

#These next three lists will pertain to our second destination. St Augustine, Florida.

florida_restaurant_list = ["Salt Life", "Harry's Seafood Bar & Grille","Prohibition Kitchen"]
florida_transportation_list =["Old Town Trolley Tours St Augustine", "Taxi Cab", "Salty Seas Transportation"]
florida_entertainment_list = ["Castillo de San Marcos National Monument", "Ripley's Believe It or Not!", "Ponce de Leon's Fountain of Youth Archaeological Park","Lightner Museum"]

#These three lists will pertain to our final destination. Boston.

boston_restaurant_list = ["Del Frisco's Double Eagle Steakhouse", "Bostonia Public House", "Buttermilk & Bourbon"]
boston_transportation_list =["Uber Xl", "Taxi Cab", "Bus"]
boston_entertainment_list =["Boston Crime Tour", "Samuel Adams Brewery Tour", "Fenway Park", "Whale Watching boat tour", "Boston Aquarium"]


import random
random_dest = random.choice(destination_list)

# NYC Destination function, including .pop() function(s) when destination needs to be changed.
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
            elif random_dest_pop == "Boston":
              print(f'{random_dest_pop} is your final destination option. If you would like to continue with the generator, please choose "y" in the following input. ')
              are_you_happy = input(f'{random_dest_pop} is the final destination choice, if you would like to continue with the vacation generator type "y".')
              if are_you_happy == "y":
                random_dest = random_dest_pop_florida
                print(f'Great! you will be going to {random_dest_pop}!')
# Boston destination functions. Including .pop() function(s) for when destination needs to be changed. 
        
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
             if are_you_happy == "y":
                random_dest = random_dest_pop_florida
                print(f'Great! you will be going to {random_dest_pop_florida}!')

    
# St Augustine Florida destination function. Including .pop() function(s) for when the destination needs to be changed.

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
                    random_dest_pop_boston = random_dest
                    print(f'Great, you are going to {random_dest_pop_boston}!')


 # New York City Restaurant List Functions   
if random_dest == "New York City":
    random_rest_nyc = random.choice(nyc_restaurant_list)

    if random_rest_nyc == "Carmine's Italian Restaurant":
         are_you_happy = input(f'Are you happy with {random_rest_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! you will be dining at {random_rest_nyc}')
         elif are_you_happy == "n":
            remove_carmines = nyc_restaurant_list.pop(0)
            random_rest_pop_nyc = random.choice(nyc_restaurant_list)
            print(f'You are now going to use a {random_rest_nyc}!')
            are_you_happy = input(f'Are you happy with dining at {random_rest_nyc} (y/n) ')
            if are_you_happy == "y":
                random_rest_nyc = random_rest_pop_nyc
                print(f'Youn are now going to dine at {random_rest_nyc}!')
            elif are_you_happy == "n":
                 if random_rest_nyc == "STK Steakhouse Midtown NYC":
                    remove_stk = nyc_restaurant_list.pop(1)
                    random_rest_pop_nyc = random.choice(nyc_restaurant_list)
                    print(f'You are now going to dine at {random_rest_pop_nyc}.')
                    are_you_happy = input(f'Are you happy dining at {random_rest_pop_nyc}? (y/n) ')
                    if are_you_happy == "y":
                        random_rest_nyc = random_rest_pop_nyc
                        print(f'Great! you will be eating at {random_rest_pop_nyc}!')
                    elif are_you_happy == "n":
                        if random_rest_pop_nyc == "La Grande Boucherie":
                            print(f'We are going to use a {random_rest_pop_nyc} as your choice of restaurant, because it is the last option.')
                            are_you_happy = input(f'{random_rest_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_rest_pop_nyc
                                print(f'Great! you will be dining at {random_rest_pop_nyc}!')


    elif random_rest_nyc == "STK Steakhouse Midtown":
         are_you_happy = input(f'Are you happy with {random_rest_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! you will be dining at {random_rest_nyc}')
         elif are_you_happy == "n":
            remove_stk = nyc_restaurant_list.pop(1)
            random_rest_pop_nyc = random.choice(nyc_restaurant_list)
            print(f'You are now going to use a {random_rest_nyc}!')
            are_you_happy = input(f'Are you happy with dining at {random_rest_nyc} (y/n) ')
            if are_you_happy == "y":
                random_rest_nyc = random_rest_pop_nyc
                print(f'Youn are now going to dine at {random_rest_nyc}!')
            elif are_you_happy == "n":
                 if random_rest_nyc == "Carmine's Italian Restaurant":
                    remove_stk = nyc_restaurant_list.pop(0)
                    random_rest_pop_nyc = random.choice(nyc_restaurant_list)
                    print(f'You are now going to dine at {random_rest_pop_nyc}.')
                    are_you_happy = input(f'Are you happy dining at {random_rest_pop_nyc}? (y/n) ')
                    if are_you_happy == "y":
                        random_rest_nyc = random_rest_pop_nyc
                        print(f'Great! you will be eating at {random_rest_pop_nyc}!')
                    elif are_you_happy == "n":
                        if random_rest_pop_nyc == "La Grande Boucherie":
                            print(f'We are going to use a {random_rest_pop_nyc} as your choice of restaurant, because it is the last option.')
                            are_you_happy = input(f'{random_rest_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_rest_pop_nyc
                                print(f'Great! you will be dining at {random_rest_pop_nyc}!')


    elif random_rest_nyc == "La Grande Boucherie":
         are_you_happy = input(f'Are you happy with {random_rest_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! you will be dining at {random_rest_nyc}')
         elif are_you_happy == "n":
            remove_boucherie = nyc_restaurant_list.pop(2)
            random_rest_pop_nyc = random.choice(nyc_restaurant_list)
            print(f'You are now going to use a {random_rest_nyc}!')
            are_you_happy = input(f'Are you happy with dining at {random_rest_nyc} (y/n) ')
            if are_you_happy == "y":
                random_rest_nyc = random_rest_pop_nyc
                print(f'Youn are now going to dine at {random_rest_nyc}!')
            elif are_you_happy == "n":
                 if random_rest_nyc == "STK Steakhouse Midtown NYC":
                    remove_stk = nyc_restaurant_list.pop(1)
                    random_rest_pop_nyc = random.choice(nyc_restaurant_list)
                    print(f'You are now going to dine at {random_rest_pop_nyc}.')
                    are_you_happy = input(f'Are you happy dining at {random_rest_pop_nyc}? (y/n) ')
                    if are_you_happy == "y":
                        random_rest_nyc = random_rest_pop_nyc
                        print(f'Great! you will be eating at {random_rest_pop_nyc}!')
                    elif are_you_happy == "n":
                        if random_rest_pop_nyc == "Carmine's Italian Restaurant":
                            print(f'We are going to use a {random_rest_pop_nyc} as your choice of restaurant, because it is the last option.')
                            are_you_happy = input(f'{random_rest_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_rest_pop_nyc
                                print(f'Great! you will be dining at {random_rest_pop_nyc}!')

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
                random_trans_nyc = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
            elif are_you_happy == "n":
                if random_trans_pop_nyc == "Subway":
                  remove_subway = nyc_transportation_list.pop(0)
                  random_trans_pop_nyc = random.choice(nyc_transportation_list)
                  print(f'You are now going to use a {random_trans_pop_nyc}!')
                  are_you_happy = input(f'Are you happy with this location? (y/n) ')
                  if are_you_happy == "y":
                   random_trans_nyc = random_trans_pop_nyc
                   print(f'Youn are now going to {random_trans_pop_nyc}!')
            elif are_you_happy == "n":
                if random_trans_pop_nyc == "Uber Xl":
                 print(f'{random_trans_pop_nyc} is the last option, so we will use this as your form of transportation!')
                 are_you_happy = input(f'Are you happy with this location? (y/n) ')
                 if are_you_happy == "y":
                  random_trans_nyc = random_trans_pop_nyc
                  print(f'Youn are now going to {random_trans_pop_nyc}!')

    elif random_trans_nyc == "Subway":
          are_you_happy = input(f'Are you happy with {random_trans_nyc}? ')
          if are_you_happy == "y":
             print(f'Great! thats good to hear!')
          elif are_you_happy == "n":
            remove_subway = nyc_transportation_list.pop(1)
            random_trans_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to use a {random_trans_pop_nyc}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_nyc} (y/n) ')
            if are_you_happy == "y":
                random_trans_nyc = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
            elif are_you_happy == "n":
                if random_trans_pop_nyc == "Uber Xl":
                   remove_uber = random_trans_nyc.pop(1)
                   random_trans_pop_nyc = random.choice(nyc_transportation_list)
                   print(f'You are now going to to use {random_trans_pop_nyc} as transportation.')
                   are_you_happy = input(f'Are you happy using {random_trans_pop_nyc} as a form of transportation? (y/n) ')
                   if are_you_happy == "y":
                        random_trans_nyc = random_trans_pop_nyc
                        print(f'Great! you will be using {random_trans_pop_nyc} to get around!')
                   elif are_you_happy == "n":
                        if random_trans_pop_nyc == "Taxi Cab":
                            print(f'We are going to use a {random_trans_pop_nyc} as your form of transportation because it is the last option.')
                            are_you_happy = input(f'{random_trans_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_trans_pop_nyc
                                print(f'Great! you will be using {random_trans_pop_nyc} to get around!')
            
    elif random_trans_nyc == "Uber XL":
         are_you_happy = input(f'Are you happy with {random_trans_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! your transportation method will be {random_trans_nyc}')
         elif are_you_happy == "n":
            remove_uber = nyc_transportation_list.pop(2)
            random_trans_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to use a {random_trans_pop_nyc}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_nyc} (y/n) ')
            if are_you_happy == "y":
                random_trans_nyc = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
            elif are_you_happy == "n":
                 if random_trans_pop_nyc == "Subway":
                    remove_subway = random_trans_nyc.pop(1)
                    random_trans_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to use {random_trans_pop_nyc} as transportation.')
                    are_you_happy = input(f'Are you happy using {random_trans_pop_nyc} as a form of transportation? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_nyc = random_trans_pop_nyc
                        print(f'Great! you will be using {random_trans_pop_nyc} to get around!')
                    elif are_you_happy == "n":
                        if random_trans_pop_nyc == "Taxi Cab":
                            print(f'We are going to use a {random_trans_pop_nyc} as your form of transportation because it is the last option.')
                            are_you_happy = input(f'{random_trans_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_trans_pop_nyc
                                print(f'Great! you will be using {random_trans_pop_nyc} to get around!')


# New York Entertainment Functions

if random_dest == "New York City":
    random_ent_nyc = random.choice(nyc_entertainment_list)

    if random_ent_nyc == "Broadway":
         are_you_happy = input(f'Are you happy with {random_ent_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! you will be going to {random_ent_nyc}!')
         elif are_you_happy == "n":
            remove_broadway = nyc_entertainment_list.pop(0)
            random_ent_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to {random_ent_pop_nyc}!')
            are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
            if are_you_happy == "y":
                random_ent_nyc = random_ent_pop_nyc
                print(f'Youn are now going to {random_ent_pop_nyc}!')
            elif are_you_happy == "n":
                 if random_ent_pop_nyc == "Top of The Rock: Observation Deck":
                    remove_top_of_the_rock = nyc_entertainment_list.pop(1)
                    random_ent_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to {random_ent_pop_nyc}.')
                    are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
                    if are_you_happy == "y":
                        random_ent_nyc = random_ent_pop_nyc
                        print(f'Great! you will be going to {random_ent_pop_nyc}!')
                    elif are_you_happy == "n":
                        if random_ent_pop_nyc == "Madam Tussauds New York":
                            print(f'We are going to use a {random_ent_pop_nyc} as your form of entertainment because it is the last option.')
                            are_you_happy = input(f'{random_ent_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_ent_nyc = random_ent_pop_nyc
                                print(f'Great! you will be going to {random_ent_pop_nyc}!')

                            
    if random_ent_nyc == "Top of The Rock: Observation Deck":
         are_you_happy = input(f'Are you happy with {random_ent_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! you will be going to {random_ent_nyc}!')
         elif are_you_happy == "n":
            remove_top_of_the_rock = nyc_entertainment_list.pop(1)
            random_ent_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to {random_ent_pop_nyc}!')
            are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
            if are_you_happy == "y":
                random_ent_nyc = random_ent_pop_nyc
                print(f'Youn are now going to {random_ent_pop_nyc}!')
            elif are_you_happy == "n":
                 if random_ent_pop_nyc == "Broadway":
                    remove_top_of_the_rock = nyc_entertainment_list.pop(0)
                    random_ent_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to {random_ent_pop_nyc}.')
                    are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
                    if are_you_happy == "y":
                        random_ent_nyc = random_ent_pop_nyc
                        print(f'Great! you will be going to {random_ent_pop_nyc}!')
                    elif are_you_happy == "n":
                        if random_ent_pop_nyc == "Madam Tussauds New York":
                            print(f'We are going to use a {random_ent_pop_nyc} as your form of entertainment because it is the last option.')
                            are_you_happy = input(f'{random_ent_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_ent_nyc = random_ent_pop_nyc
                                print(f'Great! you will be going to {random_ent_pop_nyc}!')
                            

   if random_ent_nyc == "Madam Tussauds New York":
         are_you_happy = input(f'Are you happy with {random_ent_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! you will be going to {random_ent_nyc}!')
         elif are_you_happy == "n":
            remove_tussauds = nyc_entertainment_list.pop(2)
            random_ent_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to {random_ent_pop_nyc}!')
            are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
            if are_you_happy == "y":
                random_ent_nyc = random_ent_pop_nyc
                print(f'Youn are now going to {random_ent_pop_nyc}!')
            elif are_you_happy == "n":
                 if random_ent_pop_nyc == "Top of The Rock: Observation Deck":
                    remove_top_of_the_rock = nyc_entertainment_list.pop(1)
                    random_ent_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to {random_ent_pop_nyc}.')
                    are_you_happy = input(f'Are you happy going to {random_ent_pop_nyc}? (y/n) ')
                    if are_you_happy == "y":
                        random_ent_nyc = random_ent_pop_nyc
                        print(f'Great! you will be going to {random_ent_pop_nyc}!')
                    elif are_you_happy == "n":
                        if random_ent_pop_nyc == "Broadway":
                            print(f'We are going to use a {random_ent_pop_nyc} as your form of entertainment because it is the last option.')
                            are_you_happy = input(f'{random_ent_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_ent_nyc = random_ent_pop_nyc
                                print(f'Great! you will be going to {random_ent_pop_nyc}!')
                             


# Boston List Functions
elif random_dest == "Boston":
      random_rest_boston = random.choice(boston_restaurant_list)

      if random_trans_nyc == "Uber XL":
         are_you_happy = input(f'Are you happy with {random_trans_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! your transportation method will be {random_trans_nyc}')
         elif are_you_happy == "n":
            remove_uber = nyc_transportation_list.pop(2)
            random_trans_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to use a {random_trans_pop_nyc}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_nyc} (y/n) ')
            if are_you_happy == "y":
                random_trans_nyc = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
            elif are_you_happy == "n":
                 if random_trans_pop_nyc == "Subway":
                    remove_subway = random_trans_nyc.pop(1)
                    random_trans_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to use {random_trans_pop_nyc} as transportation.')
                    are_you_happy = input(f'Are you happy using {random_trans_pop_nyc} as a form of transportation? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_nyc = random_trans_pop_nyc
                        print(f'Great! you will be using {random_trans_pop_nyc} to get around!')
                    elif are_you_happy == "n":
                        if random_trans_pop_nyc == "Taxi Cab":
                            print(f'We are going to use a {random_trans_pop_nyc} as your form of transportation because it is the last option.')
                            are_you_happy = input(f'{random_trans_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_trans_pop_nyc
                                print(f'Great! you will be using {random_trans_pop_nyc} to get around!')

      elif random_trans_nyc == "Uber XL":
            are_you_happy = input(f'Are you happy with {random_trans_nyc}? ')
            if are_you_happy == "y":
              print(f'Great! your transportation method will be {random_trans_nyc}')
            elif are_you_happy == "n":
              remove_uber = nyc_transportation_list.pop(2)
              random_trans_pop_nyc = random.choice(nyc_transportation_list)
              print(f'You are now going to use a {random_trans_pop_nyc}!')
              are_you_happy = input(f'Are you happy with taking {random_trans_pop_nyc} (y/n) ')
              if are_you_happy == "y":
                random_trans_nyc = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
              elif are_you_happy == "n":
                 if random_trans_pop_nyc == "Subway":
                    remove_subway = random_trans_nyc.pop(1)
                    random_trans_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to use {random_trans_pop_nyc} as transportation.')
                    are_you_happy = input(f'Are you happy using {random_trans_pop_nyc} as a form of transportation? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_nyc = random_trans_pop_nyc
                        print(f'Great! you will be using {random_trans_pop_nyc} to get around!')
                    elif are_you_happy == "n":
                        if random_trans_pop_nyc == "Taxi Cab":
                            print(f'We are going to use a {random_trans_pop_nyc} as your form of transportation because it is the last option.')
                            are_you_happy = input(f'{random_trans_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_trans_pop_nyc
                                print(f'Great! you will be using {random_trans_pop_nyc} to get around!')

      if random_trans_nyc == "Uber XL":
         are_you_happy = input(f'Are you happy with {random_trans_nyc}? ')
         if are_you_happy == "y":
             print(f'Great! your transportation method will be {random_trans_nyc}')
         elif are_you_happy == "n":
            remove_uber = nyc_transportation_list.pop(2)
            random_trans_pop_nyc = random.choice(nyc_transportation_list)
            print(f'You are now going to use a {random_trans_pop_nyc}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_nyc} (y/n) ')
            if are_you_happy == "y":
                random_trans_nyc = random_trans_pop_nyc
                print(f'Youn are now going to {random_trans_pop_nyc}!')
            elif are_you_happy == "n":
                 if random_trans_pop_nyc == "Subway":
                    remove_subway = random_trans_nyc.pop(1)
                    random_trans_pop_nyc = random.choice(nyc_transportation_list)
                    print(f'You are now going to to use {random_trans_pop_nyc} as transportation.')
                    are_you_happy = input(f'Are you happy using {random_trans_pop_nyc} as a form of transportation? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_nyc = random_trans_pop_nyc
                        print(f'Great! you will be using {random_trans_pop_nyc} to get around!')
                    elif are_you_happy == "n":
                        if random_trans_pop_nyc == "Taxi Cab":
                            print(f'We are going to use a {random_trans_pop_nyc} as your form of transportation because it is the last option.')
                            are_you_happy = input(f'{random_trans_pop_nyc} is your last option. Please type "y" to continue using the vacation generator. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_nyc = random_trans_pop_nyc
                                print(f'Great! you will be using {random_trans_pop_nyc} to get around!')

# Boston Transportation Functions
      if random_dest == "Boston":
         random_trans_boston = random.choice(boston_transportation_list)

      if random_trans_boston == "Uber Xl":
           are_you_happy = input(f'Are you happy taking a {random_trans_boston}? (y/n) ')
           if are_you_happy == "y":
            print(f'Great, you will be using the {random_trans_boston} to get around!')
           elif are_you_happy == "n":
            remove_uber = boston_transportation_list.pop(0)
            random_trans_pop_boston = random.choice(boston_transportation_list)
            print(f'You are now going to {random_trans_pop_boston}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_boston}? (y/n) ')
            if are_you_happy == "y":
                random_trans_boston = random_trans_pop_boston
                print(f'Great, you will be taking {random_trans_pop_boston} to get around!')
            elif are_you_happy == "n":
                if random_dest_pop_boston == "Bus":
                    remove_bus = boston_transportation_list.pop(1)
                    random_trans_pop_boston = random.choice(boston_transportation_list)
                    print(f'You are now going to use {random_dest_pop_boston} for transportation!')
                    are_you_happy = input (f'Are you happy with taking the {random_dest_pop_boston} to get around? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_boston = random_trans_pop_boston
                        print(f'Great! you will be using the {random_dest_pop_boston} to get around!')
                    elif are_you_happy == "n":
                        if random_dest_pop_boston == "Taxi Cab":
                            print(f'We will use {random_dest_pop_boston} as your mode of transportation, being that it is the final option!')
                            are_you_happy = input(f'This is the final option. Select "y" if you would like to continue to select vacation details. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_boston = random_trans_pop_boston
                                print(f'Great, you will be using {random_dest_pop_boston} to get around!')


      elif random_trans_boston == "Taxi Cab":
           are_you_happy = input(f'Are you happy taking a {random_trans_boston}? (y/n) ')
           if are_you_happy == "y":
            print(f'Great, you will be using the {random_trans_boston} to get around!')
           elif are_you_happy == "n":
            remove_taxi = boston_transportation_list.pop(1)
            random_trans_pop_boston = random.choice(boston_transportation_list)
            print(f'You are now going to {random_trans_pop_boston}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_boston}? (y/n) ')
            if are_you_happy == "y":
                random_trans_boston = random_trans_pop_boston
                print(f'Great, you will be taking {random_trans_pop_boston} to get around!')
            elif are_you_happy == "n":
                if random_dest_pop_boston == "Bus":
                    remove_bus = boston_transportation_list.pop(2)
                    random_trans_pop_boston = random.choice(boston_transportation_list)
                    print(f'You are now going to use {random_dest_pop_boston} for transportation!')
                    are_you_happy = input (f'Are you happy with taking the {random_dest_pop_boston} to get around? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_boston = random_trans_pop_boston
                        print(f'Great! you will be using the {random_dest_pop_boston} to get around!')
                    elif are_you_happy == "n":
                        if random_dest_pop_boston == "Uber Xl":
                            print(f'We will use {random_dest_pop_boston} as your mode of transportation, being that it is the final option!')
                            are_you_happy = input(f'This is the final option. Select "y" if you would like to continue to select vacation details. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_boston = random_trans_pop_boston
                                print(f'Great, you will be using {random_dest_pop_boston} to get around!')


      elif random_trans_boston == "Bus":
           are_you_happy = input(f'Are you happy taking a {random_trans_boston}? (y/n) ')
           if are_you_happy == "y":
            print(f'Great, you will be using the {random_trans_boston} to get around!')
           elif are_you_happy == "n":
            remove_bus = boston_transportation_list.pop(2)
            random_trans_pop_boston = random.choice(boston_transportation_list)
            print(f'You are now going to {random_trans_pop_boston}!')
            are_you_happy = input(f'Are you happy with taking {random_trans_pop_boston}? (y/n) ')
            if are_you_happy == "y":
                random_trans_boston = random_trans_pop_boston
                print(f'Great, you will be taking {random_trans_pop_boston} to get around!')
            elif are_you_happy == "n":
                if random_dest_pop_boston == "Taxi Cab":
                    remove_bus = boston_transportation_list.pop(1)
                    random_trans_pop_boston = random.choice(boston_transportation_list)
                    print(f'You are now going to use {random_dest_pop_boston} for transportation!')
                    are_you_happy = input (f'Are you happy with taking the {random_dest_pop_boston} to get around? (y/n) ')
                    if are_you_happy == "y":
                        random_trans_boston = random_trans_pop_boston
                        print(f'Great! you will be using the {random_dest_pop_boston} to get around!')
                    elif are_you_happy == "n":
                        if random_dest_pop_boston == "Uber Xl":
                            print(f'We will use {random_dest_pop_boston} as your mode of transportation, being that it is the final option!')
                            are_you_happy = input(f'This is the final option. Select "y" if you would like to continue to select vacation details. (y/n) ')
                            if are_you_happy == "y":
                                random_trans_boston = random_trans_pop_boston
                                print(f'Great, you will be using {random_dest_pop_boston} to get around!')
                                

        
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
          print(f'Okay great! {random_rest_florida} is the restaurant you will be eating at ')
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
     print(f'Congratulations on confirming your vacation details. You will be going to {random_dest}. Once there, you will be using {random_trans_nyc} to get to {random_ent_nyc}. Once there, you will enjoy one of {random_dest}s many attractions. After {random_ent_nyc} you will take a {random_trans_nyc} to {random_rest_nyc} where you will enjoy a great meal!')


if random_dest == "Boston":
    confirm_trip_boston = input(f'Are you happy with all of your vacation details? (y/n) ')
    if confirm_trip_boston == "y":
        print(f'Congratulations on planning your vacation! You will be going to {random_dest}. Once there, you will use {random_trans_boston} to get to {random_ent_boston}. Once you finish at {random_ent_boston}, you will head over to {random_rest_boston} in a {random_trans_boston}. Thank you for using the vacation generator!  ')


if random_dest == "St Augustine,Florida":
    confirm_trip = input(f'Are you happy with all of your vacation details? (y/n) ')
    if confirm_trip == "y":
     print(f'Congratulations on confirming your vacation details. You will be going to {random_dest}. Once there, you will be using {random_trans_florida} to get to {random_ent_florida}. Once there, you will enjoy one of {random_dest}s many attractions. After {random_ent_florida} you will take a {random_trans_florida} to {random_rest_florida} where you will enjoy a great meal!')
