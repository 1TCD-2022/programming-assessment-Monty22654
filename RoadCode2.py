"""
Filename: RoadCode2.py
Author: Monty Davidson
Date: 07/2022
Description: The purpose of this program is to help people study the New Zealand road code.
             Real Questions from the new zealand road code will be used.
             Make your way through this program and test your knowledge!  
"""
answers_valid_input = False
menu_option_valid_input = False
run_road_code_test = False

#this loop is to validate the users chouice of menu option.
while not menu_option_valid_input:
    try:
        menu_option = int(input(""" \nWelcome to Montys road code test, Please choose an option from below, either 1 or 2 
1. Get 5 questions to answer all from the New Zealand Road Code
2. Exit
Enter a number: """))
        if menu_option == 1 or menu_option == 2:
            menu_option_valid_input = True
        
    except:
        print("Please enter 1 or 2: ")
            
if menu_option == 1:
    run_road_code_test = True

#this is so that if the user chooses to exit the code it will skip asking all the questions and just farewell the user.
if run_road_code_test == True:
    while not answers_valid_input:
        try:
            question_1 = int(input("""\nYou are driving past a line of parked cars. You notice a ball bouncing out onto the road ahead. What do you do?

    1 - Keep driving at the same speed
    2 - Keep driving at the same speed and flash the vehicles headlights
    3 - Slow down and be prepared to stop for children
    4 - Slow down and move to the right-hand side of the road.

    Answer, 1,2,3,4: """))
            if question_1 == 3:
                print ("Correct!")
                answers_valid_input = True
            elif question_1 in [1,2,4]:
                print("\nIncorrect")
                answers_valid_input = True
                
         

        except ValueError:
            print("\nInvalid entry, Please enter 1, 2, 3, or 4")

#reset answers_valid_input to false so that the next question can be put into a loop making it that the try, except code works
    answers_valid_input = False

    
    while not answers_valid_input:    
        try:
            question_2 = int(input(""" \nWhen passing a horse and rider, you should:
    1 - Warn the rider by sounding the horn on your vehicle.
    2 - Slow down and give them as much room as you can.
    3 - Speed up.
    4 - Warn the rider by turning your vehicle headlights on.

    Answer, 1,2,3,4: """))
            if question_2 == 2:
                print ("Correct!")
                answers_valid_input = True
            elif question_2 in [1,3,4]:
                print("\nIncorrect")
                answers_valid_input = True

        except ValueError:
            print("\nInvalid entry, Please enter 1, 2, 3, or 4")

                
















    if question_2.lower() == "b":
        print ("\nCorrect!")
    else:
        print ("""\nIncorrect!, the answer was "b" """)

    question_3 = input("""\n You can be fined if your vehicle is on a road and not up to warrent of fitness standard:
    True or False?

    Answer T or F: """)

    if question_3.lower() == "t":
        print ("\nCorrect!")
    else:
        print ("""\n Incorrect, the answer was "T" """)
else:
    print ("Have a nice day")
