stringa = "fragola"
letter = stringa[1]
print(letter)

print("la prima lettera è ", stringa[0])
print("l'ultimo carattere è ", stringa[-1])
print(stringa[1:5])
print(stringa[4:])
length = len(stringa)
print(length)
stringa2 = "Zagabria"

if stringa < stringa2:
    print("fragola viene prima di Zagabria")
else:
    print("Zagabria viene prima di fragola")

print(dir(stringa))
print(help(str.upper))
string_upper = stringa.upper()
print(string_upper)
print(stringa.replace("a","e"))
