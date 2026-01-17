
Options = """ 
        Choose The Operation:
        1) Sum
        2) Subtract
        3) Multiply
        4) Divide
        5) EXIT
    """

class Calculator:
    result = 0

    def __init__(self):
        self.result = Calculator.result
    
    def summ (self):
        try:
            num_1 = float (input ("Enter The FIRST Number: "))
            num_2 = float (input ("Enter The SECOND Number: "))
        except ValueError:
            print ("Please Enter Valide Number !!!")
        else:
            x = num_1 + num_2
            print (f"The result is: {x}")

    def substract (self):
        try:
            num_1 = float (input ("Enter The FIRST Number: "))
            num_2 = float (input ("Enter The SECOND Number: "))
        except ValueError:
            print ("Please Enter Valide Number !!!")
        else:
            x = num_1 - num_2
            print (f"The result is: {x}")  

    def multiply (self):
        try:
            num_1 = float (input ("Enter The FIRST Number: "))
            num_2 = float (input ("Enter The SECOND Number: "))
        except ValueError:
            print ("Please Enter Valide Number !!!")
        else:
            x = num_1 * num_2
            print (f"The result is: {x}")

    def divide (self):
        try:
            num_1 = float (input ("Enter The FIRST Number: "))
            num_2 = float (input ("Enter The SECOND Number: "))
        except ValueError:
            print ("Please Enter Valide Number !!!")
        else:
            if num_2 == 0:
                print ("Can't divide on ZERO !!!!")
            else:
                x = num_1 / num_2
                print (f"The result is: {x}")  
                   


def calculate ():
    while True:
        print (Options)
        try:
            ms = int (input ("Please Choose Operation: "))
        except ValueError:
            print ("Please enter valid number !!")
        else:
            if ms == 1:
                Calculator().summ ()
                continue
            elif ms == 2:
                Calculator().substract ()
                continue
            elif ms == 3:
                Calculator().multiply ()
                continue
            elif ms == 4:
                Calculator().divide ()
                continue
            elif ms == 5:
                while True:
                    ms = input ("Are you sure to EXIT? (yes / no)")
                    if ms.lower().strip() in ["yes", "y"]:
                        print ("Thank You, Best Wishes.")
                        return
                    elif ms.lower().strip() in ["no", "n"]:
                        break
                    else:
                        print ("Wrong Choice !!!")
                        continue
                continue
            else:
                print ("Wrong Choice !!!")
                continue


if __name__ == "__main__":
    calculate ()