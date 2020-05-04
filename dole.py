'''
Python script for monitoring staffs temperature
'''

NotAllowableTemp = float(37.6)

# first I'm going to check your teperature
a = input("Please input your temperature: ")

# convert the data from "a" in to float
StaffTemp = float(a)

# test the condition
if StaffTemp < NotAllowableTemp:

    print("You are allowed to enter the building.")

    # Accomplish visitor's checklist? <- what is this?
    # Let the Guard/Personnel on the lobby check if you are at the list
    a = input("Do you have an appointment? ") # Yes/No Only

    # convert the answer to string
    Answer = str(a)

    # test the condition
    if Answer == "Yes":
        print("You can enter the building.")
    else:
        print("You better go home.")

else:
    print("You better go home.")
