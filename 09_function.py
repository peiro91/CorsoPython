def saluta():
    print("Ciao amici youtubers!")

saluta()
saluta()

def operazione(n1,n2):
    print("la somma è ", n1 + n2)
    print("il prodotto è ", n1 * n2)

operazione(3,4)
operazione(8,10)
operazione(7,6)

def moldiv(n):
    return n * 2/10

risultato = moldiv(30)
print (risultato)

def molquad(n):
    moltiplicazione = n * 2
    quadrato = n ** 2
    return moltiplicazione,quadrato

molt, quad = molquad(3)

print ("la moltiplicazione per due è ", molt)
print ("il prodotto è ", quad)

def colore():
    colore = input("inserisci un colore\n")
    if colore == "rosso":
        print("Fermati")
        return
    print ("Hia scelto il ",colore)

colore()
