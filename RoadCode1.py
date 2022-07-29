"""
Filename: RoadCode1.py
Author: Monty Davidson
Date: 07/2022
Description: The purpose of this program is to help people study the New Zealand road code.
             Real Questions from the new zealand road code will be used.
             Make your way through this program and test your knowledge!  
"""
question_1 = "start"
answer_1 = False
while question_1.lower() != "c" :
    question_1 = input(""" You are driving past a line of parked cars. You notice a ball bouncing out onto the road ahead. What do you do?
    A - Keep driving at the same speed
    B - Keep driving at the same speed and flash the vehicles headlights
    C - SLow down and be prepared to stop for children
    D - Slow down and move to the right-hand side of the road.

    Answer, A,B,C,D: """)

    while not answer_1:
        if question_1.lower() == "a":
            print("""\nIncorrect!, the answer was "c" """)
            answer_1 = True
        elif question_1.lower() == "b":
            print("""\nIncorrect!, the answer was "c" """)
            answer_1 = True
        elif question_1.lower() == "c":
            print("\nCorrect!")
            answer_1 = True
        elif question_1.lower() == "d":
            print("""\nIncorrect!, the answer was "c" """)
            answer_1 = True
        else:
            question_1 = input("Please enter a,b,c or d: ")
            answer_1 = False


question_2 = input(""" \nWhen passing a horse and rider, you should:
A - Warn the rider by sounding the horn on your vehicle.
B - Slow down and give them as much room as you can.
C - Speed up.
D - Warn the rider by turning your vehicle headlights on.

Answer, A,B,C,D: """)


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
