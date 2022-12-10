text = input("Ingresa un texto: ")

firstLetter = input("Ingresa 1 letra a elección: ")
secondLetter = input("Ingresa 2 letra a elección: ")
thirdLetter = input("Ingresa 3 letra a elección: ")

arrayOfLetters = [firstLetter, secondLetter, thirdLetter]

countFirstletter = text.lower().count(arrayOfLetters[0].lower())
countSecondletter = text.lower().count(arrayOfLetters[1].lower())
countThirdletter = text.lower().count(arrayOfLetters[2].lower())
print(text)

textInArray = text.split(" ")

numberTextinArray = len(textInArray)

firstLetterInTheText = textInArray[0][0]

lastLetterInTheText = textInArray[-1][-1]

textInArray.reverse()
textReverse = " ".join(textInArray)

findPython = text.lower().find("python")


print("")
print("--------------Resumen------------------------")
print("")
print(f"1. Total de palabras encontradas: {numberTextinArray}")
print(f"2. Para tu primera letra encontramos {countFirstletter} coindidencias\n2. Para tu segunda letra encontramos {countSecondletter} coindidencias\n2. Para tu tercera palabra encontramos {countThirdletter} coindidencias")
print(f"3. Primera letra de texto: {firstLetterInTheText}")
print(f"3. Ultima letra del texto: {lastLetterInTheText}")
print(f"4. Texto invertido: {textReverse}")
if findPython >= 0:
    print("5. La palabra Python esta en el texto")
else:
    print("5. La palabra Python no esta en el texto")
    
