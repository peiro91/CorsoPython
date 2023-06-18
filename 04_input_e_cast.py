numero1 = 3.99
print(int(numero1))

stringa2 = "10"

print(type(stringa2))

numero2 = int(stringa2)

print(type(numero2))

float1=float(stringa2)

print(type(float1))
print(float1)

stringa3 = str(float1)
print(type(stringa3))
numero3=0
bool_t = bool(numero1)
bool_f = bool(numero3)
print(bool_t,bool_f)

nome = input("Come ti chiami?\n")
print ("Benvenuto", nome)

anno_corrente = 2023
anno_nascita = int(input("Qual è il tuo anno di nascita?"))
età = anno_corrente - anno_nascita
print ("La tua età è", età)
