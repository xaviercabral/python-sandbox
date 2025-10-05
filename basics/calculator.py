a = int(input("enter first number: "))
b = int(input("enter second number: "))

problem_solve = input("what is the problem you wanna do?(addition, subtraction, multiplication, division): ")

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


    