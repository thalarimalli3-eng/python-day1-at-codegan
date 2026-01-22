#loop control statments
#break
for i in range (1,6):
    if i==5:
        break
    print(i)
else:
    print("program is done")

#continue
    for i  in range(1,6):
        if i == 5:
            continue
        print(i)
        print("program is done")
#sum of two numbers
        n1=int(input("enter first number:"))
        n2=int(input("enter second number:"))
        sum=n1 + n2
        print(f"sum of two numbers {n1} and {n2} is {sum}")

#sum of two number using functions def sum_of_two_numbers (n1, n2):
def sum_of_two_numbers(n1, n2):
    s=n1+n2
    return s
result=sum_of_two_numbers (10,20)
print(result)

#simple calcuator using functions method 1
def calculator (num1, num2, operator):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    elif operator=='/':
        return num1 / num2
    else:
        return "invalid operator"
    result=calculator(10,20,'+')
    print(result)
    result=calculator(10,20,'-')
    print(result)
    result=calculator(10,20, '*')
    print(result)
    result=calculator (10,20, '/')
    print(result)
    result=calculator(10,20, '%')
    print(result)

#simple calcuator using functions method 2

def addition (a, b):
    return a+b
def subtraction (a, b) :
    return a-b
def multiplication(a, b):
    return a*b
def division (a, b) :
    if b== 0:
        return "division by zero not possible"
    return a/b
               
