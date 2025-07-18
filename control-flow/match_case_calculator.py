number1 = float(input("enter the first number : "))
number2 = float(input("enter the second number : "))
operator = input("enter the operator you want ( + , - , * , /  ) : ")
match operator:
    case '+':
        number3 = number1 + number2
    case '-':
        number3 = number1 - number2
    case '*':
        number3 = number1 * number2
    case '/':
        number3 = number1 / number2
print(number3)