#no inputs

sum = 0
mult = 0

action = input("Укажите действие сложение или умножение: ")

if action == "сложение":
    sum = firstNumber + secondNumber + thirdNumber
    print(sum)
elif action == "умножение":
    mult = firstNumber * secondNumber * thirdNumber
    print(mult)
else:
    print("такое действие не предусмотрено")