# put your python code here
first_number = float(input())
second_number = float(input())
oper = input()

if oper == "mod":
    if second_number == 0:
        print("Division by 0!")
    else:
        print(first_number % second_number)
elif oper == "div":
    if second_number == 0:
        print("Division by 0!")
    else:
        print(first_number // second_number)
elif oper == "/":
    if second_number == 0:
        print("Division by 0!")
    else:
        print(first_number / second_number)
elif oper == "+":
    print(first_number + second_number)
elif oper == "-":
     print(first_number - second_number)
elif oper == "*":
    print(first_number * second_number)
elif oper == "pow":
    print(first_number ** second_number)







