#WE WILL MAKE A CALCULATOR WHICH WILL PRINT WRONG ANSWERS FOR SOME QUESTION GIVEN IN README
first_input = float(input("Enter the first number:"))
second_input = float(input("Enter the second number:"))
 
Operator = """Please type the following operator: 
    1.)Addition(A)
    2.)Subtraction(S)
    3.)Division(D)
    4.)Multiplication(M)"""
print(Operator)
c_operator = str(input(""))

#now we have take the input and lets start with the calculation
if c_operator == "A":
    if  first_input == 558 and second_input == 8: 
        print("Please learn for exams and dont cheat")
    else: 
        calculation = (first_input + second_input)
        print(calculation)
elif c_operator == "a":
    print('Please use capital letters(A)')
elif c_operator == "S":
    calculation = first_input - second_input
    print(calculation)
elif c_operator == "s":
    print('Please use capital letters(S)')
elif c_operator == "D":
    if first_input == 678 and second_input == 3:
        print('Please dont cheat in exams')
    else:
        calculation = first_input / second_input
        print(calculation)
elif c_operator == "d":
    print("Please use capital letter(D)")
elif c_operator == "M":
    if first_input == 45 and second_input == 3:
        print("Please dont cheat in exams")
    else:
        calculation = first_input * second_input
        print(calculation)
elif c_operator == "m":
    print("Please use capital letters (M)")

