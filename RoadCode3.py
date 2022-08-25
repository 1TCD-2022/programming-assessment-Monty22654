"""
Filename: RoadCode3.py
Author: Monty Davidson
Date: 07/2022
Description: The purpose of this program is to help people
             study the New Zealand road code.
             Real Questions from the new zealand road code will be used.
             Make your way through this program and test your knowledge!  
"""
#set constants
answers_valid_input = False
menu_option_valid_input = False
run_road_code_test = False
question_number = 0
score = 0

questions = ["You are driving past a line of parked cars. You notice a ball bouncing out onto the road ahead. What do you do?"
             ,"When passing a horse and rider, you should:"
             ,"What is the closest distance your vehicle may be parked to a vehicle entrance?"
             ,"What lights should you use if your vehicle has broken down and is being towed?"
             ,"When coming up to a pedestrian crossing without a raised traffic island, what must you do?"
             ,"What should you do when you are coming up to traffic signals and the signals change from green to yellow?"
             ,"What may you do at traffic signals if there is a green arrow pointing to the right and a red light showing at the same time?"
             ,"If you have a learner licence can you carry passengers?"
             ,"Are you allowed to drive a vehicle towing a trailer with a load that is not tied on properly?"
             ,"When may you park your vehicle over a fire hydrant?"]


answers = [[ "1 - Keep driving at the same speed.",
             "2 - Keep driving at the same speed and flash the vehicles headlights.",
             "3 - Slow down and be prepared to stop for children.",
             "4 - Slow down and move to the right-hand side of the road."]
           
           ,["1 - Warn the rider by sounding the horn on your vehicle."
             ,"2 - Slow down and give them as much room as you can."
             ,"3 - Speed up."
             ,"4 - Warn the rider by turning your vehicle headlights on."]
           
           ,["1 - 0.5 meters."
             ,"2 - 1 meter."
             ,"3 - 1.5 meter."
             ,"4 - 2 meter."]

           ,["1 - Headlights."
             ,"2 - Hazard lights."
             ,"3 - Brake lights."
             ,"4 - Reversing lights."]

           ,["1 - Only stop if the pedestrians are on your side of the road."
             ,"2 - Go straight through as the pedestrians have to give way to you."
             ,"3 - Stop if the pedestrians are at any part of the crossing."
             ,"4 - Only stop if its during the weekend"]

           ,["1 - Speed through before it turns red."
             ,"2 - Slow to a stop."
             ,"3 - Drive through if the coast is clear."
             ,"4 - Drive through if your birthday is in january."]

           ,["1 - Turn right only."
             ,"2 - Go straight through."
             ,"3 - Whatever you want."
             ,"4 - Turn left."]

           ,["1 - Yes."
             ,"2 - Only if you drive carefully."
             ,"3 - Only if your supervisor takes responsibility for them."
             ,"4 - Only if they are older than 18."]

           ,["1 - As long as you drive slowly."
             ,"2 - Yes if it doesnt fall off."
             ,"3 - No, never."
             ,"4 - You can if you put an orange flag on the back."]

           ,["1 - When a Mobility card is displayed on the front window."
             ,"2 - When you aren't leaving it unattended for more than 10 minutes."
             ,"3 - When there is someone with the vehicle who can move it."
             ,"4 - If your vehicle breaks down."]]

correct_answer = [3,2,2,2,3,2,1,3,3,3]
incorrect_answer = [[1,2,4],[1,3,4],[1,3,4],[1,3,4],[1,2,4],[1,3,4],[2,3,4],[1,2,4],[1,2,4],[1,2,4]]

#this loop is to validate the users chouice of menu option.
while not menu_option_valid_input:
    try:
        menu_option = int(input(""" \nWelcome to Montys road code test, Please choose an option from below, either 1 or 2 
1. Get 5 questions to answer all from the New Zealand Road Code
2. Exit
Enter a number: """))
        if menu_option in [1,2]:
            menu_option_valid_input = True
        
    except:
        print("Please enter 1 or 2: ")
            
if menu_option == 1:
    run_road_code_test = True

#this is so that if the user chooses to exit the code it will skip asking all the questions and just farewell the user.
if run_road_code_test:
    while not answers_valid_input:
        try:
            if question_number != (10):
                print()
                print(questions[question_number])
                for ans in answers[question_number]:
                    print (ans)
                question = int(input("\nAnswer 1,2,3,4: "))

                if question in (incorrect_answer[question_number]):
                    print("\nIncorrect")
                    question_number = question_number + 1
                    print("\nYour score is",score)
                
                elif question in [correct_answer[question_number]]:
                    print ("\nCorrect!")
                    question_number = question_number + 1
                    score = score + 1
                    print("\nYour score is",score)
                    
                    
                


            
            else:
                print("Thankyou for playing.")
                answers_valid_input = True
                
                
#This bit makes it so that if the user doesnt enter an integer theyll be asked again                
        except ValueError:
            print("\nInvalid entry, Please enter 1, 2, 3, or 4")

else:
    print ("Have a nice day")
