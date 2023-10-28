text = input("Введите текст: ")
text = text.split(" ")
print(type(text))

reservedWords = []

while len(reservedWords) < 5:
    reservedWords.append(input("Введите зарезервированные слова(5 штук): "))
print(reservedWords)

for i in range(len(text)):
    for j in range(len(reservedWords)):
        if text[i].lower() == reservedWords[j].lower():
            text[i] = text[i].upper()
print(text)
