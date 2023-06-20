semaforo = input("inserisci colore del semaforo, verde, giallo o rosso\n")

if semaforo == "verde":
    print("passa")
else:
    if semaforo == "giallo":
        print("rallenta")
    else:
        print("fermati")

numero1 = int(input("inserisci il primo numero\n"))
numero2 = int(input("inserisci il secondo numero\n"))
operazione = input("inserisci l'operazione desiderata a scelta tra +,-,*,/\n")

if operazione == "+":
    print(numero1 + numero2)
elif operazione == "-":
    print(numero1 - numero2)
elif operazione == "*":
    print(numero1 * numero2)
elif operazione == "/":
    print(numero1 / numero2)
else:
    print("operazione non valida")
