from User_Data import USER_DATA
import random
from controls import Controls
from display_prod import Display_Products
from product_database import Products

con = Controls ()

choices = """ 
Action List:
cu   : Change Username
cp   : Change Password
shd  : Show The Products Database
exit : EXIT
"""
def Login_UI ():
    while True:
        x = input ("Please Enter Your Username: ").lower ().strip ()
        if x == USER_DATA ["username"]:
            x_2 = input ("Please Enter Your Password: ").strip ()
            if x_2 == USER_DATA ["password"]:
                ran = random.randrange (10000, 99999)
                print (f"Your Verivication is >> {ran}")
                while True:
                    ver = int (input ("Enter Your Verification Code: "))
                    try:
                        if ver == ran:
                            print ("Logged in **Successfully** to The Database.", choices)
                            action = input ("Please Choose The action from the list: ").strip().lower()
                            try:
                                if action == "cu":
                                    con.change_name ()
                                    break
                                elif action == "cp":
                                    con.change_pass ()
                                    break
                                elif action == "shd":
                                    Display_Products (Products)
                                    break
                                elif action == "exit":
                                    break
                            except ValueError:
                                print("❌ Invalid action! Please choose from the list.")
                                continue_option = input("Type 'exit' to logout or Type 'continue' to continue: ").lower ().strip ()
                                if continue_option.lower() == 'exit':
                                    break
                                elif continue_option.lower() == 'continue':
                                    continue
                    except ValueError:
                        print ("Wronge Verification Code, Please Try Again !!!")
                        continue
                ex = input ("Do You Want To Choose Other Action? (yes / no)").lower ().strip ()
                if ex in ["yes", "y"]:
                    continue
                else:
                    break
            else:
                print ("Wronge Password, Please Try Again !!!")
                break
        else:
            print ("Wronge Username, Please Try Again !!!")
            break