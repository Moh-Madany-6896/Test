from User_Data import USER_DATA
import random
from controls import Controls

con = Controls ()

choices = """ 
Action List:
cu  : Change Username
cp  : Change Password
shd : Show Your Database
"""
def Login_UI ():
    while True:
        x = input ("Please Enter Your Username: ")
        if x == USER_DATA ["username"]:
            x_2 = input ("Please Enter Your Password: ")
            if x_2 == USER_DATA ["password"]:
                ran = random.randrange (10000, 99999)
                print (f"Your Verivication is >> {ran}")
                while True:
                    ver = int (input ("Enter Your Verification Code: "))
                    if ver == ran:
                        print ("Logged in **Successfully** to The Database.", choices)
                        action = input ("Please Choose The action from the list: ").strip().lower()
                        if action == "cu":
                            con.change_name ()
                            break
                        elif action == "cp":
                            con.change_pass ()
                            break
                        # elif action == "shd":
                        else:
                            print("❌ Invalid action! Please choose from the list.")
                            continue_option = input("Type 'exit' to logout or press Enter to continue: ")
                            if continue_option.lower() == 'exit':
                                break
                    else:
                        print ("Wronge Verification Code, Please Try Again !!!")
                        continue
                continue
            else:
                print ("Wronge Password, Please Try Again !!!")
                break
        else:
            print ("Wronge Username, Please Try Again !!!")
            break
