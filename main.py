phrase1 = input()
phrase2 = phrase1[0].lower() + phrase1[1:]
for character in phrase2:
    if character.isupper():
        phrase2 = phrase2.replace(character,"_" + character.lower())
        phrase2 = phrase2.lower()
print(phrase2)




