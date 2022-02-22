label game_over_scenarios():

    if end_scenario == "Out of Time":

        scene bg end_outoftime
        with dissolve

        if end_scenario_subcategory == "Car":
            "Your partner approaches, stands in front of the driver side car door, and says there's no need to make a trip anywhere." 
        else: 
            "You hear the front door creak open. Alas, your partner came back, sensed some suspicious behavior, and immediately started questioning you." 

        "You missed the opportunity to get away, and now your partner is guarding you like a hawk." 

        "It will be at least several months before you have an opportunity like this again." 

    elif end_scenario == "Was Found":

        scene bg end_found
        with dissolve

        if end_scenario_subcategory == "Bad Luck":

            "Alas, even with all the planning you put into this escape, sometimes they're one step ahead."

            if todo_reset_phone == False:
                
                "It didn't help that you forgot to reset everyone's phone to factory settings."

            if todo_logoff_email == False:
                
                "Forgetting to log off email on your shared computer gave your partner access to information and power to lock you out of your account."
                
            if todo_clear_cache == False:

                "Not clearing cache on the computer before leaving provided your partner clues as to your whereabouts."

            if todo_clear_cache == False:

                "Unknowingly, using your credit card helped provide some location leads."
                
                "Your partner had found your credit card a long time ago, successfully applied for a joint account, and hid mail from you."

            "You may have had bad luck this time. Hopefully you will have another chance to escape later."

    elif end_scenario == "Out of Money":

        show bg background_black
        with dissolve

        "Alas, you ran out of money."
        
        if end_scenario_subcategory == "Locked Out of Email":
            scene bg end_moneyburn
            with fade

            "If your only way to pay is blocked, it's game over."

        elif end_scenario_subcategory == "Hospital Bill":
            scene bg end_moneyburn
            with fade

            "You can't keep sickness at bay. When it happens, it happens."

            "In the meantime, all you can do is to minimize the chance of a relapse by doing things like keeping a clean environment."

        else:
            scene bg end_car_brokedown
            with fade

            "At that point, you didn't have enough money to pay for gas."


        "You had to call the police to help, and they helped reconnect you with your partner, who had reported you were missing."

        "After \"reuniting\", you realize the locks were changed and you no longer have keys."

        "{color=#FFFF8F} {i} Four walls. Trapped. And nowhere to go."

    elif end_scenario == "Reported Kidnapping":
        
        scene bg end_arrested
        with fade

        "You were taken into custody because your partner reported that you kidnapped the children."

        "They took you back to where you started."

        "So close, yet so far."

        "{color=#FFFF8F} {i} Four walls. Trapped. And nowhere to go."

    else:

        # winning scenario
        scene bg end_freedom
        with dissolve

        "You finally arrive at Aunt May's - hooray!"
        
        "{color=#FFFF8F} {i} This was the reset I was looking for."

    jump end_ask