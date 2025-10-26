


def addition(a,b):
    print(a+b)


def subtraction(a,b):
    print(a-b)


def multiplication(a,b):
    print(a*b)


def division(a,b):
    if b==0:
        print("please choose a different number from 0")
    else:
        #c = a/b
        print(a/b)

###############

problem_solve = int(input("what is the problem you wanna do?(1- addition, 2- subtraction, 3- multiplication, 4- division, 0- Exit): "))

a = int(input("enter first number: "))
b = int(input("enter second number: "))

while problem_solve != 0:

    if problem_solve == 1:

        addition(a,b)

    elif problem_solve == 2:
        subtraction(a,b)

    elif problem_solve == 3:
        multiplication(a,b)

    elif problem_solve == 4:
        division(a,b)

    else:
        print("please select one of the listed options")

    problem_solve = int(input("what is the problem you wanna do?(1- addition, 2- subtraction, 3- multiplication, 4- division, 0- Exit): "))

    a = int(input("enter first number: "))
    b = int(input("enter second number: "))









#problem_solve = int(input("what is the problem you wanna do?(1- addition, 2- subtraction, 3- multiplication, 4- division, 0- Exit): "))
"""
if problem_solve == "addition":
    print("The sum is: ", a+b)
elif problem_solve == "subtraction":
    print("The subtraction is: ", a-b)
elif problem_solve == "multiplication":
    print("The multiplication is: ", a*b)
elif problem_solve == "division":
    if b==0:
        print("Infinite Number")
    else:    
          print("The division is: ", a/b)
else:
     print("Insert one of the options")
"""
"""""
while problem_solve != 0:
    if problem_solve == 1:
        def addition(a,b):
            return a + b
        c = a+b
        print(c)
        addition
    elif problem_solve == 2:
        def subtraction(a,b):
            return a-b
        c = a-b
        print(c)

        subtraction
    elif problem_solve == 3:
        def multiplication(a,b):
            return a*b
        c = a*b
        print(c)

        multiplication
    elif problem_solve == 4:
        def division(a,b):
            return a/b
        if b==0:
            print("please choose a different number")
        else:
            c = a/b
            print(c)

        division
    else:
        print("please choose one of the options.")


    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    
    problem_solve = int(input("what is the problem you wanna do?(1- addition, 2- subtraction, 3- multiplication, 4- division, 0- Exit):"))
    
   # a = int(input("enter first number: "))
    #b = int(input("enter second number: "))


    c=addition(a,b)

def addition(a,b):
            return a + b
    """