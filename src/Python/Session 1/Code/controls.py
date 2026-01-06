from User_Data import USER_DATA

class Controls:
    def change_name (self):
        ver_pass = input ("Please Enter Your Password to Continue: ").strip()
        if ver_pass != USER_DATA ["password"]:
            print("❌ Incorrect password! Username change cancelled.")
            return USER_DATA ["username"]
        
        while True:
            x = input ("Enter The New Username: ").strip().lower()
            if not x:
                print("❌ Username cannot be empty!")
                continue
            else:
                ver_x = input ("Verify The New Username: ").strip().lower()
                if x == ver_x:
                    confirm = input (f"Change username from '{USER_DATA ["username"]}' to '{ver_x}'? (yes/no): ").strip().lower()
                    if confirm in ["yes", "y"]:
                        USER_DATA ["username"] = ver_x
                        print ("✅ Username Changed Successfuly.")
                        return ver_x
                        break
                    else:
                        print("❌ Username change cancelled.")
                        return USER_DATA ["username"]
                        break
                else:
                    print ("❌ WRONGE Username !! Please Enter The Username again.")
            break

    def change_pass (self):
        ver_pass_2 = input ("Please Enter Your Password to Continue: ").strip()
        if ver_pass_2 != USER_DATA ["password"]:
            print("❌ Incorrect password! Password change cancelled.")
            return USER_DATA ["password"]
        
        while True:
            x_2 = input ("Enter The New Password: ").strip()
            if not x_2:
                print("❌ Password cannot be empty!")
                continue
            else:
                ver_x_2 = input ("Verify The New Pasword: ").strip()
                if x_2 == ver_x_2:
                    confirm = input ("Change Password? (yes/no): ").strip().lower()
                    if confirm in ["yes", "y"]:
                        USER_DATA["password"] = ver_x_2
                        print ("✅ Password Changed Successfuly.")
                        return ver_x_2
                        break
                    else:
                        print("❌ Password change cancelled.")
                        return USER_DATA ["password"]
                        break
                else:
                    print ("❌ WRONGE Password !! Please Enter The Password again.")
            break