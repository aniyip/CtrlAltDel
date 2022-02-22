# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define police = Character('Police', color='#3366CC')
define aunt = Character('Aunt May', color='#8D539A')
define dr = Character('Doctor', color='#2A7FBA')
define b_patrol = Character('Border Patrol', color='3366CC')
define cen = Character(None, what_xalign=0.5, what_text_align=0.5)



# The game starts here.

label start:

    call initialize_var from _call_initialize_var

    # Select Difficulty Level

    jump cm_set_difficulty # cm stands for choice menu; see choices.rpy
    

label story_crossborder_escape:

    # Opening Story

    "{color=#FFFF8F} {i} I didn't know it'd happen to me..."
    
    "{color=#FFFF8F} {i} But it did."

    # Scenario #1

    police "We hear your concerns about your partner threatening to hit you and your children, but nothing has happened and we cannot arrest unless there is probable cause. If anything does happen, though, please call us back."

    "*click*"

    "{color=#FFFF8F} {i} But by then it'd be too late."

    "{color=#FFFF8F} {i} What's more, there are other types of abuse besides being hit."

    "{color=#FFFF8F} {i} Abuse through fear and coercive control is a criminal offense."
    
    "{color=#FFFF8F} {i} I know it because I've lived through it." 
    
    "{color=#FFFF8F} {i} If only police could recognize it more readily—"

    "{color=#FFFF8F} {i} I need to reset my life."
    
    "{color=#FFFF8F} {i} I need to leave now."

    ##########################################################################################
    # Scenario #1 : Morning Phase 
    ##########################################################################################
    
    play music "audio/bgm_story_wakeUp.mp3" fadein 1.0 volume 0.25 # music loops by default

    #####################################
    # Back story
    #####################################

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg story_bedroom.png" or "bg story_bedroom.jpg") to the
    # images directory to show it.

    scene bg story_bedroom
    with fade

    aunt "Oh dear! Of course, you can come live with us while you make the transition."

    aunt "It's a long journey, though, since we live across the border."

    aunt "Remember to bring your {color=#D10E33}passport{/color}."

    aunt "It'll also be rough to bring {color=#D10E33}4 children and 2 dogs.{/color}"

    aunt "Will {color=#D10E33}lil' Casey{/color} be alright? Poor child - having to deal with a chronic condition at such an early age."

    aunt "Make sure to pack {color=#D10E33}more{/color}, just in case."

    aunt "I know you don't have much time before your partner comes home."   

    aunt "Here's a prepaid Visa gift card to help you make the 1000+ mile drive here."   

    aunt "Please stay safe!"

    "*received $[money_amt_left]*"   

    ############################################################
    # Decisions : explore house to pack what you need and leave
    ############################################################

    jump places_to_explore

    #####################################
    # Story On The Road
    #####################################

    label on_the_road():

        $ stage="On the Road"
        $ end_scenario = "Out of Money"

        stop music fadeout 1.0
        scene bg story_car_driveaway
        with fade

        if day == 1:

            play music "audio/bgm_story_onTheGo.mp3" fadein 1.0 volume 0.25 

            "You successfully packed up and are off to {color=#8D539A}Aunt May{/color}'s!"
            
            "But you haven't escaped just yet."

            ############################################
            # fill up gas tank
            ############################################

            scene bg story_gasstop01
            with fade

            "One of the first stops you make is to the gas station so that you can fill up your tank."
            
            $ money_amt_left -= cost_of_gas
            "You pay with your prepaid gift card, so you now have $[money_amt_left]."

            ############################################
            # reset phone to default factory settings 
            ############################################

            scene bg story_phonereset
            with fade

            if todo_reset_phone == True:
                "While at the gas station, you remember your note about resetting everyone's phone to default factory settings."

                "After all, cell phones can be a beacon, tracking your exact location in real-time."

                "Perpetrators can also retrieve call and text history with the right info about you."

                "You reset everyone's phone and breathe a sigh of relief that you won't be as easily tracked by your phone GPS and apps."

            else:
                $ chance_being_found += 20
                "You grab your phone to look up your next destination."

            if chance_being_found > renpy.random.randint(1,100):
                $ end_scenario = "Was Found"
                $ end_scenario_subcategory = "Bad Luck"                
                jump game_over

            ############################################
            # purchase supplies 
            ############################################    

            scene bg story_store
            with fade

            "After hours of driving, you find a general purpose store and stop in to double check that you have all the supplies you need for this trip."

            if have_toiletries:
                "Toiletries? Already have some."
            else:
                $ money_amt_left -= cost_of_toiletries
                "Toiletries? We'll need some for tonight."

            if have_medication:
                "Medication? Check!"
            else:
                $ money_amt_left -= cost_of_medication
                "Medication? We can't forget that."

            if have_diapers:
                "Diapers? Got some already!"
            else:
                $ money_amt_left -= cost_of_diapers
                "Diapers? Why do they have to be so expensive?"
            
            "That's all you need for now. You can always stop by another store later if need be."

            "After checkout, you have $[money_amt_left]. By now everyone's famished - time to eat!"

            ############################################
            # pay for food 
            ############################################    

            scene bg story_restaurant
            with fade

            "You enjoy your meal and go to pay the bill."

            if todo_logoff_email == False:
                $ chance_email_lockedout = 50
                $ chance_being_found += 20 
            else: 
                $ chance_email_lockedout = 0 

            if chance_email_lockedout > renpy.random.randint(1,100):

                "You try to pay via the prepaid Visa gift card Aunt May sent you virtually, but you can no longer access your account."

                "{color=#FFFF8F} {i} Ugh... I must've forgotten to log out of my account somewhere."

                if cash_on_hand == 0:

                    if have_credit_card == False:
                        $ end_scenario_subcategory = "Locked Out of Email"                
                        jump game_over
                    else: 
                        $ used_credit_card = True
                        $ chance_being_found += 10 
                        "Although you don't have any cash on hand, you remember you have a credit card so you charge the cost."

                else:
                    if money_amt_left > cash_on_hand:
                        $ money_amt_left = cash_on_hand

                    $ money_amt_left -= cost_of_food

                    "Thank goodness you still have some cash on hand!"

                    "You proceed to pay for the food and now have $[money_amt_left] remaining."
                    
            else:

                "You now have $[money_amt_left]."

            "The last to do for the day is to find lodging."

            if chance_being_found > renpy.random.randint(1,100):
                
                "Before you headed off, you hear footsteps from behind you."

                $ end_scenario = "Was Found"
                $ end_scenario_subcategory = "Bad Luck"                
                jump game_over


            ############################################
            # Decisions : pay for accomodations 
            ############################################  

            jump cm_on_the_road

        elif day == 2:
            
            play music "audio/bgm_story_onTheGo.mp3" fadein 1.0 volume 0.25 
            
            "You start driving off again."

            ############################################
            # trip to hospital  
            ############################################    
            
            if chance_baby_sick > renpy.random.randint(1,100):

                "An hour into the drive, {color=#D10E33}lil' Casey{/color} starts crying so you switch directions and head towards the hospital." 
            
                scene bg story_hospital
                with fade

                $ money_amt_left -= cost_of_hospital_bill

                dr "Your child is medically fragile and could not tolerate the rough conditions yesterday."

                dr "While you could help avoid this scenario by ensuring that {color=#D10E33}lil' Casey{/color} is in a clean environment, it's hard to completely avoid the hospital."

                dr "Here's a prescription to help {color=#D10E33}lil' Casey{/color} get over this challenge."
                
                if money_amt_left < 1:

                    if have_credit_card == False:
                        $ end_scenario_subcategory = "Hospital Bill"                
                        jump game_over
                    else: 
                        $ used_credit_card = True
                        $ chance_being_found += 10 
                        "Because you didn't have enough cash on hand, you charge the rest on your credit card."

                else:
                    
                    "You now have $[money_amt_left]."

                "Off you go again--"

            if chance_being_found > renpy.random.randint(1,100):
                $ end_scenario = "Was Found"
                $ end_scenario_subcategory = "Bad Luck"                
                jump game_over

            # food
            # gas

            ############################################
            # border patrol  
            ############################################    

            scene bg story_border
            with fade

            "The finish line is almost in sight!"

            if have_passport == False:

                scene bg end_border_uturn
                with fade

                b_patrol "Can you show me your passport please?"

                "You fumble around the vehicle and realize you forgot to bring the necessary documents."

                b_patrol "Sorry, we can't let you cross."

                b_patrol "I'm receiving a call right now. Can you wait here?"

                $ end_scenario = "Reported Kidnapping"                
                jump game_over

            else:

                "With passport in hand, you pass through border patrol without issues."

                $ end_scenario = "You Win"
                jump game_over

#####################################
# Game Over Scenarios
#####################################

label game_over():

    stop music fadeout 1.0
    play music "audio/bgm_story_endgame.mp3" fadein 1.0 volume 0.25 
            
    jump game_over_scenarios

label end_ask():

    "While this was a game for you, this was a real journey for one family, with details changed to respect privacy."

    "It took $500 for them to escape successfully, thanks to assistance from a nonprofit organization called {a=https://dvcontrolaltdelete.org/?ref=dvgame}Control Alt Delete{/a}"

    scene bg end_donate
    with fade

    "98 percent of domestic abuse victims suffer financial abuse, and this is the #1 reason why domestic violence victims stay with their abusers."
    
    "Abusers control money, which leaves victims with no available financial resources to escape the relationship."

    cen "Will you help {a=https://dvcontrolaltdelete.org/donate/?ref=dvgame}fund someone's escape or part of their escape?{/a}"


    jump end_game

label end_game():

    # This ends the game.

    return
