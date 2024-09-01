# Author: Adrian Melchi
# Application Name: Dean's List or Honor Roll? (Can't think of a good name for the app)
# Purpose: The purpose of this program is to take a students first name, last name, and GPA, and to decide whether they are on the dean's list or honor roll.

#While true loop to keep student collection going
while True:
    lastName = input("Please enter student's last name, or ZZZ to quit.") # collects student last name or tests for break condition
    if lastName == "ZZZ": # if loop to break away from loop at user request
        break
    firstName = input("Please enter student's first name.") # collect student last name
    gpa = float(input("Please enter student's GPA.")) # collect student GPA
    if gpa >= 3.5: #if loop to determine deans list
        print("Student has made the Dean's List.")
        
    elif gpa >= 3.25: # determines honor roll
        print("Student has made the Honor Roll.")

    else: # message if student does not hit either honor roll or deans list criteria
        print("Student is not on Dean's List or Honor Roll")
        
