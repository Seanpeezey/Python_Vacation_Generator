#This list will supply the randomly generated vacation destinations.
 
destination_list = ["New York City", "Boston", "St Augustine, Florida"]
# no_florida = ["New York City", "Boston"]
# no_boston = ["New York City", "St Augustine, Florida"]
#These next three lists will pertain to our fist destination on our list New York City.

nyc_restaurant_list = ["Carmine's Italian Restaurant", "STK Steakhouse Midtown NYC","La Grande Boucherie"]
nyc_transportation_list = ["Taxi Cab", "Subway", "Uber XL", "Horse & Carriage"]
nyc_entertainment_list = ["Broadway", "Top of The Rock: Observation Deck", "Madame Tussauds New York"]

#These next three lists will pertain to our second destination. St Augustine, Florida.

florida_restaurant_list = ["Salt Life", "Harry's Seafood, Bar & Grille", "Columbia Restaurant", "Prohibition Kitchen"]
florida_transportation_list =["Old Town Trolley Tours St Augustine", "Taxi Cab", "Salty Seas Transportation"]
florida_entertainment_list = ["Castillo de San Marcos National Monument", "Ripley's Believe It or Not!", "Ponce de Leon's Fountain of Youth Archaeological Park","Lightner Museum"]

#These three lists will pertain to our final destination. Boston.

boston_restaurant_list = ["Del Frisco's Double Eagle Steakhouse", "Bostonia Public House", "Buttermilk & Bourbon"]
boston_transportation_list =["Uber Xl", "Taxi Cab", "Bus"]
boston_entertainment_list =["Boston Crime Tour", "Samuel Adams Brewery Tour", "Fenway Park", "Whale Watching boat tour", "Boston Aquarium"]


import random
random_dest = random.choice(destination_list)

if random_dest == "New York City":
    print("You are going to New York City!")

    are_you_happy = input("Are you happy with this selection? (y/n)")
    if are_you_happy == "y":
        print("Great, you are going to NYC, now lets find out what restaurant you will be going to.")
        random_rest_nyc = random.choice(nyc_restaurant_list)

        if random_rest_nyc == "Carmine's Italian Restaurant":
            print("You are you going to Carmine's Italian Restaurant!")
            restaurant_choice_nyc = input("Are you happy with this option? (y/n) ")
            if restaurant_choice_nyc == "y":
                print("Great! you are going to Carmine's Italian Restaurant, now lets figure out what kind of transportation you will be using.")
            elif restaurant_choice_nyc == "n":
                print('Sorry!')
#Must fill these with .pops statements to return diferet results
        elif random_rest_nyc == "STK Steakhouse Midtown NYC":
            print("You are going to STK Steakhouse Midtown NYC!")
            restaurant_choice_nyc = input("Are you happy witht this option? (y/n) ")

            if restaurant_choice_nyc == "y":
                print("Great, STK Steakhouse it is!")

            elif restaurant_choice_nyc =="n":
                print("Lets chnage that up!")

        elif random_rest_nyc == "La Grande Boucherie":
            print("You are going to La Grande Boucherie")

            restaurant_choice_nyc = input("Are you happy with this option?")

            if restaurant_choice_nyc == "y":
                print("Great! You are going to La Grande Boucherie")

            elif restaurant_choice_nyc == "n":
                print("Oh well!")
            
        random_trans_nyc = random.choice(nyc_transportation_list)

        if random_trans_nyc == "Taxi Cab":
            print("The Cabs Smell")

        elif random_trans_nyc == "Subway":
            print("Whatch out for the empty subway cars")

        elif random_trans_nyc == "Uber XL":
            print("Nice and cozy ride around the big city!")

        elif random_trans_nyc == "Horse & Carriage":
            print("I feel bad for the horse's , but it is a historic form of travel.")

        elif random_trans_nyc == "Bike & Carriage":
            print("Time to take a ride around town.")

        random_ent_nyc = random.choice(nyc_entertainment_list)
        print(random_ent_nyc)

        if random_ent_nyc == "Broadway":
            print("Broadway has some of the best plays in the country!")

        elif random_ent_nyc == "Top of The Rock: Observation Deck":
            print("What a beautiful place to view the city skyline!")

        elif random_ent_nyc == "Madame Tussauds New York":
            print("Come checkout the wax creations and replicas of celebrities!")

    
        
    # if are_you_happy =="n":
    #    destination_list.pop(0)
    #    print(random_dest)

# if random_dest == "Boston":
#     print("You are going to Boston!")
#     are_you_happy = input("Are you happy with this selection? (y/n)")
#     if are_you_happy == "y":
#         print("Great, you are going to NYC, now lets find out what restaurant you will be going to.")
#     if are_you_happy =="n":
#        remove_ny = destination_list.pop(1)
#        print(random_dest)

if random_dest == "St Augustine, Florida":
    print("You are going to St Augustine, Florida!")

    are_you_happy = input("Are you happy with this selection? (y/n) ")

    if are_you_happy == "y":
        print("Great, you are going to NYC, now lets find out what restaurant you will be going to.")

    if are_you_happy =="n":
       remove_ny = destination_list.pop(2)
       random_dest_pop = random.choice(destination_list)
       print(f'You are now going to {random_dest_pop}!')

       are_you_happy = input("Are you happy with this selection? (y/n) ")

       if are_you_happy == "y":
        print(f'Great, you are going to {random_dest_pop}!')

       elif are_you_happy == "n":
        remove_boston = destination_list.pop(1)
        random_dest_pop_boston = random.choice(destination_list)
        print(f'This is our final option, I hope you will like {random_dest_pop_boston}')
        are_you_happy = input("Are you happy with this option? (y/n) ")

        if are_you_happy == "y":
            print(f'Great, You will be going to {random_dest_pop_boston}, now lets figure out where you will go eat!')
        if are_you_happy == "n":
            print("I am sorry, but there arent any more options!")
