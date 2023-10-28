myStr = input("Введите строку: ")
newStr = myStr[::-1]

for i in myStr:
    myStr = myStr.replace(" ", "")
    myStr = myStr.lower()
print(myStr)

for i in newStr:
    newStr = newStr.replace(" ", "")
    newStr = newStr.lower()
print(newStr)

for i in range(len(myStr)):
    if myStr[i] != newStr[i]:
        print("Строка не является палиндромом")
        break
    elif i == len(myStr) - 1 and myStr[i] == newStr[i]:
        print("Строка является палиндромом")
