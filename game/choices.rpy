label cm_set_difficulty():
    menu:
        "Easy":
 
            $ difficulty = "Easy"
            $ money_amt_left = 1000
            $ packing_time_left = renpy.random.randint(15,20)
            $ chance_baby_sick = renpy.random.randint(0,10)
            $ chance_email_lockedout = renpy.random.randint(10,20)
            $ chance_being_found = renpy.random.randint(0,10)

            $ cost_of_gas = 30
            $ cost_of_food = 50
            $ cost_of_toiletries = 50
            $ cost_of_medication = 50
            $ cost_of_diapers = 30
            $ cost_of_motel_normal = renpy.random.randint(15,18)*10
            $ cost_of_motel_crammed = renpy.random.randint(12,15)*10
            $ cost_of_motel_sketchy = renpy.random.randint(5,8)*10
            $ cost_of_motel_unclean = renpy.random.randint(15,18)*10
            $ cost_of_hospital_bill = renpy.random.randint(4,5)*50

            jump story_crossborder_escape

        "Intermediate":

            $ difficulty = "Intermediate"
            $ money_amt_left = 800
            $ packing_time_left = renpy.random.randint(10,15)
            $ chance_baby_sick = renpy.random.randint(10,20)
            $ chance_email_lockedout = renpy.random.randint(20,50)
            $ chance_being_found = renpy.random.randint(10,20)

            $ cost_of_gas = 30
            $ cost_of_food = 60
            $ cost_of_toiletries = 50
            $ cost_of_medication = 100
            $ cost_of_diapers = 30
            $ cost_of_motel_normal = renpy.random.randint(15,20)*10
            $ cost_of_motel_crammed = renpy.random.randint(12,18)*10
            $ cost_of_motel_sketchy = renpy.random.randint(5,8)*10
            $ cost_of_motel_unclean = renpy.random.randint(10,12)*10
            $ cost_of_hospital_bill = renpy.random.randint(4,6)*50

            jump story_crossborder_escape
        
        "Hard":

            $ difficulty = "Hard"
            $ money_amt_left = 500
            $ packing_time_left = renpy.random.randint(8,12)
            $ chance_baby_sick = renpy.random.randint(20,30)
            $ chance_email_lockedout = renpy.random.randint(50,80)
            $ chance_being_found = renpy.random.randint(20,30)

            $ cost_of_gas = 30
            $ cost_of_food = 60
            $ cost_of_toiletries = 50
            $ cost_of_medication = 100
            $ cost_of_diapers = 30
            $ cost_of_motel_normal = renpy.random.randint(15,20)*10
            $ cost_of_motel_crammed = renpy.random.randint(12,18)*10
            $ cost_of_motel_sketchy = renpy.random.randint(5,8)*10
            $ cost_of_motel_unclean = renpy.random.randint(10,12)*10
            $ cost_of_hospital_bill = renpy.random.randint(4,6)*50

            jump story_crossborder_escape


#############################################################################################################

label cm_explore_house():

    $ stage="At Home"
    $ end_scenario = "Out of Time"

    menu places_to_explore: 

        "Where will you go?"
        # "print: [packing_time_left] & [money_amt_left]"

        "Children bedroom":

            scene bg story_cbedroom
            with fade

            if kids_coralled == False:
                $ packing_time_left -= 1
                $ kids_coralled = True
                "You rounded up the {color=#D10E33}kids{/color} and carried {color=#D10E33}Lil' Casey{/color} in your arms."
                jump explore_cbedroom
            else:

                menu explore_cbedroom: 

                    "Need to check anything?"
                    
                    "Changing Table":
                        $ packing_time_left -= 1

                        if have_diapers == True:
                            "There's nothing else to see here."
                        else: 
                            $ have_diapers = True
                            "You grabbed some {color=#D10E33}diapers{/color}!"                        

                        if packing_time_left < 1:
                            jump game_over
                        else: 
                            jump explore_cbedroom

                    "On the Bed":
                        $ packing_time_left -= 1

                        if have_teddy_bear == True:
                            "There's nothing else to see here."
                        else:                            
                            $ have_teddy_bear = True
                            "{color=#D10E33}Lil' Casey{/color} points at most favorite teddy bear, so you grab it."

                        if packing_time_left < 1:
                            jump game_over
                        else: 
                            jump explore_cbedroom

                    "Under the Bed":
                        $ packing_time_left -= 1

                        if visited_under_bed == True:
                            "There's nothing else to see here."
                        else:                            
                            $ visited_under_bed = True
                            $ money_amt_left += 250
                            $ cash_on_hand += 250
                            "You reach under the bed to find your hidden cash stash - just for emergencies like this."
                            "*Received additional $250*"
                        
                        if packing_time_left < 1:
                            jump game_over
                        else: 
                            jump explore_cbedroom

                    "Back":
                        scene bg story_bedroom
                        with fade
                        jump places_to_explore

        "Master bedroom":

            scene bg story_mbedroom
            with fade

            menu explore_mbedroom: 

                "Need to check anything?"

                "Closet":
                    $ packing_time_left -= 1

                    "{color=#FFFF8F}{i}I can buy clothes along the way as needed."

                    if packing_time_left < 1:
                        jump game_over
                    else: 
                        jump explore_mbedroom

                "Drawers":
                    $ packing_time_left -= 1

                    if have_car_keys == True:
                        "There's nothing else to grab here."
                    else: 
                        $ have_car_keys = True
                        "{color=#FFFF8F}{i}Thank goodness I have a spare copy of the {color=#D10E33}car keys{/color} that I keep here."
                        "*Obtained car keys*"

                    if packing_time_left < 1:
                        jump game_over
                    else: 
                        jump explore_mbedroom

                "Side Table":
                    $ packing_time_left -= 1

                    if have_passport == True:
                        "There's nothing else to grab here."
                    else: 
                        $ have_passport = True
                        "You open the inner compartment to find your {color=#D10E33}passport{/color} and grab it to go."

                    if packing_time_left < 1:
                        jump game_over
                    else: 
                        jump explore_mbedroom

                "Computer":

                    if todo_logoff_email == False:

                        $ packing_time_left -= 1
                        $ todo_logoff_email = True
                        $ chance_email_lockedout = 0

                        "{color=#FFFF8F}{i}Wow, thank goodness I checked! Leaving while logged onto my email wouldn't have turned out well..."
                        "*Logged out of email*"
                        
                        jump todo_on_computer

                    else:

                        menu todo_on_computer: 

                            "What would you like to do on the computer?"

                            "Surf the Web for information":
                                $ packing_time_left -= 1
                                "{color=#FFFF8F}{i}It's going to be sunny for the next few days. While it makes the drive easier for us, it also makes it easy for us to be caught."

                                if packing_time_left < 1:
                                    jump game_over
                                else: 
                                    jump todo_on_computer

                            "I know I'm forgetting something...":
                                $ packing_time_left -= 1
                                $ todo_clear_cache = False
                                "{color=#FFFF8F}{i}Ah, that's right. I need to clear the cache and history on this machine to avoid leaving clues more readily. Nothing's private on a computer after all."
                                "*Clears cache and history on machine*"

                                if packing_time_left < 1:
                                    jump game_over
                                else: 
                                    jump todo_on_computer
                            "Back":                            
                                jump explore_mbedroom

                    if packing_time_left < 1:
                        jump game_over
                    else: 
                        jump explore_mbedroom
                        
                "Back":
                    scene bg story_bedroom
                    with fade
                    jump places_to_explore
            
        "Living room":

            scene bg story_livingroom
            with fade

            if dogs_coralled == False:
                $ packing_time_left -= 1
                $ dogs_coralled = True
                "You rounded up your dogs, {color=#D10E33}Toto{/color} and {color=#D10E33}Benji{/color}!"

                "{color=#FFFF8F}{i}I was doing some late night research yesterday... now where did I put my notes again?"

                jump explore_livingroom

            else:

                "Need to check anything?"

                menu explore_livingroom:

                    "On the Table":
                        $ packing_time_left -= 1

                        if picked_up_book == True:
                            "There's nothing else to see here."

                        elif reviewed_book == True:
                            $ picked_up_book = True
                            $ todo_reset_phone = True
                            "{color=#FFFF8F}{i}Ah, that's right. I was almost caught writing down some to do's."
                            "*picks up book and finds note underneath*"
                            "{color=#FFFF8F}{i}Note to self: {color=#D10E33}reset phone to factory settings{/color}."

                        else: 
                            $ reviewed_book = True
                            "{color=#FFFF8F}{i}Room by Emma Donoghue... The scenes seared into my memory include the son’s attempted escape, and those moments when he was trapped within a rolled carpet."                        

                            "{color=#FFFF8F}{i}Harrowing just thinking about it— but why is this book here again?"                        

                        if packing_time_left < 1:
                            jump game_over
                        else: 
                            jump explore_livingroom

                    "In the bookcase":
                        $ packing_time_left -= 1

                        "There's nothing to see here except for books. Most of them are detective novels..."

                        if packing_time_left < 1:
                            jump game_over
                        else: 
                            jump explore_livingroom
                            
                    "Under the Rug":
                        $ packing_time_left -= 1

                        if have_credit_card == True:
                            "There's nothing else to grab here."
                        else:
                            $ have_credit_card = True
                            "Yippee! You found one of your old credit cards that you secretly stashed away for times like this, so you take it with you."
                        
                        if packing_time_left < 1:
                            jump game_over
                        else: 
                            jump explore_livingroom

                    "Back":
                        scene bg story_bedroom
                        with fade
                        jump places_to_explore
    
        "Bathroom":

            scene bg story_bathroom
            with fade

            menu explore_bathroom: 

                "Need to check anything?"

                "Medicine Cabinet":
                    $ packing_time_left -= 1

                    if have_medication == True:
                        "You've already packed up medication."
                    else:
                        $ have_medication = True
                        "{color=#FFFF8F}{i}You grab {color=#D10E33}medicine{/color} for {color=#D10E33}Lil' Casey{/color}."

                    if packing_time_left < 1:
                        jump game_over
                    else: 
                        jump explore_bathroom

                "Sink":
                    $ packing_time_left -= 1
                    
                    if have_toiletries == True:
                        "You've packed what you can for toiletries."
                    else:
                        $ have_toiletries = True
                        "You pack up {color=#D10E33}toiletries{/color}!"

                    if packing_time_left < 1:
                        jump game_over
                    else: 
                        jump explore_bathroom

                "Back":
                    scene bg story_bedroom
                    with fade
                    jump places_to_explore

        "Hop into the car":
            $ packing_time_left -= 1

            if packing_time_left < 1:
                $ end_scenario_subcategory = "Car"
                jump game_over
            elif kids_coralled == False:
                "Oh my! How can I forget my {color=#D10E33}babies{/color}?!"
                jump places_to_explore
            elif dogs_coralled == False:
                play sound "audio/sound_dogs_barking.mp3"
                "*woof woof!*"
                "Oh my! We can't leave {color=#D10E33}Toto{/color} and {color=#D10E33}Benji{/color}."
                jump places_to_explore
            elif have_car_keys == False:
                "Oh my! I can't drive without the {color=#D10E33}car keys{/color}."
                jump places_to_explore
            else: 
                jump on_the_road

#############################################################################################################

label cm_on_the_road():

    scene bg story_motelsign
    with fade

    menu stop_by_motel: 

        "While you've driven far out, who knows how far your partner will go to find you? It costs $[cost_of_motel_normal] to stay here for the night, and you currently have $[money_amt_left]. Will you stay at this motel?"

        
        "Stay at this motel":

            scene bg story_motelstay
            with fade

            $ money_amt_left -= cost_of_motel_normal
            $ chance_being_found += 10
            "You now have on hand $[money_amt_left] left."

            jump pay_for_lodging

        "Find another place":

            scene bg story_motelstay
            with fade

            $ money_amt_left -= cost_of_motel_unclean
            $ chance_baby_sick += 50 

            "You drive on for a while, there weren't that many great options along the way, and it's getting very late."
            
            "You take what you can get and stop at the next one on the road. It costs $[cost_of_motel_unclean], leaving you with $[money_amt_left] left."

            "When you check into the room, you quickly realize how bad it is."

            "Some cockroaches scattered upon you opening the door and the room and blankets smelled of cigars."

            "It's pretty gross, but you suck it up because of the circumstances."

            jump pay_for_lodging

label pay_for_lodging():
    $ day += 1
    jump on_the_road

