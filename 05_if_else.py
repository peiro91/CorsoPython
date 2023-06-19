età = 15 
if età > 17:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

numero1 = 10 
numero2 = 15

if numero1 > numero2:
    print("Vero")
else:
    print("Falso")

if numero1 >= numero2:
    print("Vero")
else:
    print("Falso")

if numero1 < numero2:
    print("Vero")
else:
    print("Falso")

if numero1 <= numero2:
    print("Vero")
else:
    print("Falso")

if numero1 == numero2:
    print("Vero")
else:
    print("Falso")

if numero1 != numero2:
    print("Vero")
else:
    print("Falso")

num = int(input("Inserisci numero tra 5 e 10\n"))

if num < 5 or num > 10:
    print("Il numero non è valido")
else:
    print("il numero è valido")

if num >= 5 and num <= 10:
    print("il numero è valido")
else:
    print("Il numero non è valido")
