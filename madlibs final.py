import random
intro_input = input("Are you ready to play? type Y or N\n").lower()
if intro_input == "y":
    print("""Great! Let me briefly introduce you the game. No time to introduce  
We have prepared 3 stories for you. Just choose one and say nothing """)

else:
    print("Get back when you want to play. Bye")
    quit()
print("""1. The one in a hospital 
2. The one in hiking adventures
3. The one lost in woods""")
choice_input = input("Type 1, 2 or 3 to choose the respective story OR you can type R to choose randomly\n").lower()
#first story below

if choice_input == "r":
    r = random.randint(1, 3)
    choice_input = str(r)
    #print(r)
if choice_input == "1":
    print("""Good choice, now in the field below I need you to write a list
of required elements to generate your story """)
    while True:
        input_first_1 = input("""Type here 3 comma separated Adjectives (make sure you typed 3)\n""")
        f1 = input_first_1.split(",")
        if len(f1) != 3:
            print("I said 3, do you understand, threee")
            continue
        else:
            break
    print("Good job, now...")
    while True:
        input_first_2 = input("Type here comma separated 2 numbers, a measure of time(years, days etc) "
                              "and any transportation type\n")
        f2 = input_first_2.split(",")
        if len(f2) != 4 or not f2[0].isdigit() or not f2[1].isdigit():
            print("Try again...Probably you missed something or put a space after comma ")
            continue
        print("Working on your story...Bare with me, I need more details")
        while True:
            input_first_3 = input("Now I need comma separated 4 nouns, a verb, "
                                      "a part of the body and some silly word\n")
            f3 = input_first_3.split(",")
            if len(f3) != 7:
                print("You missed something")
                continue
            else:
                break
        print("Working on the last part...")
        while True:
            input_first_4 = input("Type here comma separated color, part of the body and a verb\n")
            f4 = input_first_4.split(",")
            if len(f4) != 3:
                print("Something went wrong, try again")
                continue
            else:
                break
        first_story = f"""
                    It was about {f2[0]} {f2[2]} ago when I arrived at the hospital in a 
                    {f2[3]}. The hospital is a/an {f1[0]} place, there are a lot of {f1[1]}
                    {f3[0]} here. There are nurses here who have {f4[0]} {f3[5]}. If someone wants to come 
                    into my room I told them that they have to {f3[4]} first. I’ve decorated my room with {f2[1]} {f3[1]}.
                    Today I talked to a doctor and they were wearing a {f3[2]} on their {f4[1]}. 
                    I heard that all doctors {f4[2]} {f3[3]} every day for breakfast. The most {f1[2]} thing about 
                    being in the hospital is the {f3[6]} {f3[0]}!"""
        print(first_story)
        break
#second story below
if choice_input == "2":
    print("""Excellent, now in the field below I need you to write a list
of required elements to generate your story """)
    while True:
        input_second_1 = input("""Type here 2 comma separated Nouns, 2 Verbs and 2 colors \n""")
        s1 = input_second_1.split(",")
        if len(s1) != 6:
            print("You missed something, try again")
            continue
        print("Good job, now...")
        while True:
            input_second_2 = input("Type here comma separated 2 adjectives, 2 feelings and 2 animal names \n")
            s2 = input_second_2.split(",")
            if len(s2) != 6:
                print("You missed something, try again")
                continue
            else:
                print("Working on your story...Bare with me, I need more details")
                break
        while True:
            input_second_3 = input("Now I need comma separated 1 Verb (ending in ing), 1 Adverb (ending in ly) and 2 ""numbers \n")
            s3 = input_second_3.split(",")
            ing = s3[0]
            if ing[-3:] != "ing":
                print("You missed something, try again")
                continue
            else: 
                break
        print("Working on the last part...")
        input_second_4 = input("Type here comma separated 1 silly word, measure of time, adjective and Person's name \n")
        s4 = input_second_4.split(",")
        second_story = f"""
        This weekend I am going camping with {s4[2]} {s4[3]}. 
        I packed my lantern, sleeping bag, and {s1[0]}. I am so {s2[0]} {s2[3]} 
        to {s1[2]} in a tent. I am {s2[1]} {s2[4]} we might see a(n) {s2[5]}, 
        I hear they’re kind of dangerous. While we’re camping, we are going to hike, 
        fish, and {s1[3]}. I have heard that the {s1[4]} lake is great for {s3[0]}. 
        Then we will {s3[1]} hike through the forest for {s3[2]} {s4[1]}. 
        If I see a {s1[5]} {s2[5]} while hiking, I am going to bring it home as a pet! At night we will 
        tell {s3[3]} {s4[0]} stories and roast {s1[1]} around the campfire!!
"""
        print(second_story)
        break
#third story below
if choice_input == "3":
    print("""Good choice, now in the field below I need you to write a list
of required elements to generate your story """)
    while True:
# big, small, loud, quiet, bright
        input_third_1 = input("""Type here 5 comma separated Adjectives \n""")
        t1 = input_third_1.split(",")
        if len(t1) != 5:
            print("You missed something make sure you typed 5 adjectives")
            continue
        else:
            break
    print("Good job, now...")
#cat, dog, bird, trees, mountains, years
    while True:
        input_third_2 = input("Type here comma separated 5 nouns 3 singular 2 plural and "
                              "measure of time(year,day etc.)\n")
        t2 = input_third_2.split(",")
        if len(t2) != 6:
            print("You missed something")
            continue
        else:
            break
    print("Working on your story...Bare with me, I need more details")
#Tiger, Australia, red, living room
    while True:
        input_third_3 = input("Now I need comma separated animal name, country, any color and room name in a House \n")
        t3 = input_third_3.split(",")
        if len(t3) != 4:
            print("Something went wrong, try again")
            continue
        else:
            break
    print("You have really tough patience...")
#Running, unicorns, dragons, 7
    while True:
        input_third_4 = input("Type here comma separated Verb (ending in ing), "
                              "2 magical creatures(plural) and a number\n")
        t4 = input_third_4.split(",")
        if len(t4) != 4:
            print("Something went wrong, try again")
            continue
        else:
            break
    print("Working on the last part")
    while True:
        input_third_5 = input("Type here comma separated Adjective and a Person's name \n")
        t5 = input_third_5.split(",")
        if len(t5) != 2:
            print("Something went wrong, try again")
            continue
        else:
            break
    third_story = f"""Dear {t5[0]} {t5[1]}, I am writing to you from a {t1[0]} castle in an
        enchanted forest. I found myself here one day after going for a ride on a {t3[2]} {t3[0]} in {t3[1]}. 
        There are {t1[1]} {t4[1]} and {t1[2]} {t4[2]} here! 
        In the {t3[3]} there is a pool full of {t2[0]}. I fall asleep each night on a {t2[1]} of 
        {t2[3]} and dream of {t1[3]} {t2[4]}. It feels as though I have lived here for 
        {t4[3]} {t2[5]}. I hope one day you can visit, although the only way to get here now is 
        {t4[0]} on a {t1[4]} {t2[2]}!!                
"""
    print(third_story)

