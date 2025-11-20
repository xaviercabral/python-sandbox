
def menu():

    print("___Xavier's calculator___")
    print("")
    print("")
    print("Calculator options:___")
    print("")
    print("")
    print("1- addition")
    print("2- subtraction")
    print("3- multiplication")
    print("4- division")
    print("0- Exit/Off")

def operations():
    problem_solve=-10
    while problem_solve not in [0,1,2,3,4]:
        try:
            problem_solve = int(input("Which of the options would you like to chose?: "))
            return problem_solve
        except ValueError:
            print("please insert a number.")
            continue
    print("")



def numbers():
    while 1==1:
        try:
            a = int(input("enter first number: "))
        except ValueError:
            print("please insert a number.")
            continue
        break
    print("")

    while 1==1:
        try:
            b = int(input("enter second number: "))
        except ValueError:
            print("please insert a number.")
            continue
        break

    print("")

    return a,b

def addition(a,b):
    return a+b 



def subtraction(a,b):
    return a-b


def multiplication(a,b):
    return a*b


def division(a,b):
    if b==0:
        print("please choose a different number from 0")
    else:
        return a/b

###############

operator=1

while operator != 0:
    
    menu()

    operator=operations()


    a,b=numbers()

    if operator == 1:

        result=addition(a,b)

    elif operator == 2:
        result=subtraction(a,b)

    elif operator == 3:
        result=multiplication(a,b)

    elif operator == 4:
        result=division(a,b)

    else:
        print("please select one of the listed options")

    print(result)
    wait_click=input("Click any key to continue")
    print("")
    
