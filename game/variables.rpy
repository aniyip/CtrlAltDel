
label initialize_var():

    $ difficulty = "Easy"
    $ stage="At Home"
    $ end_scenario = "Out of Time"
    $ end_scenario_subcategory = "None"
    $ day = 1
    $ cash_on_hand = 0

    # following variables are set when choosing difficulty level in choices.rpy
    $ money_amt_left = 0
    $ packing_time_left = 0

    $ chance_baby_sick = 0
    $ chance_email_lockedout = 0
    $ chance_being_found = 0

    $ cost_of_gas = 0
    $ cost_of_food = 0
    $ cost_of_toiletries = 0
    $ cost_of_medication = 0
    $ cost_of_diapers = 0
    $ cost_of_motel_normal = 0
    $ cost_of_motel_crammed = 0
    $ cost_of_motel_sketchy = 0
    $ cost_of_motel_unclean = 0
    $ cost_of_hospital_bill = 0
    
    # following variables hold importance in story 
    
    ### needed for winning, in adddition to having enough money
    $ kids_coralled = False
    $ dogs_coralled = False
    $ have_car_keys = False
    $ have_passport = False
    
    ### affects scenarios requiring spending money
    $ have_toiletries = False
    $ have_diapers = False
    $ have_medication = False
    $ have_teddy_bear = False
    $ have_credit_card = False

    ### affects chance of being found
    $ todo_reset_phone = False
    $ todo_logoff_email = False
    $ todo_clear_cache = False
    $ used_credit_card = False
    
    # following variables help track visted areas of home
    $ visited_under_bed = False
    $ reviewed_book = False
    $ picked_up_book = False

    # teen phones not reset
    # can track

    # need to use credit card - joint

    #abusrs montior ; chance that abuser catches up