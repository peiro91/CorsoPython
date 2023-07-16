#16/07/23 - Pierporz
# Questo programma ha lo scopo di leggere un file di testo e contare le occorrenze di un determinato carattere, per poi stamparlo su un un  altro file.

#1. Chiedere all'utente il nome del file di input, il nome del file di output e il carattere da cercare
file_input = input("Inserisci il nome file da leggere\n")
file_output = input("Inserisci il nome file dove salvare il risultato\n")
carattere = input("Inserisci il carattere da cercare\n")[0]
#2. aprire il file in modalità lettura
with open(file_input,'r') as file_i:
    #3. Leggere il file e salvare il contenuto in una stringa 
    contenuto = file_i.read()
#4. Utilizzare il ciclo for per scorrere ogni carattere all'interno della stringa
contatore = 0
for e in contenuto:
    #5. Controllare se il carattere è uguale a quello richiesto dall'utente ed incrementare un contatore
    if e == carattere:
        contatore += 1
#6. Aprire il file di output in modalità scrittura.
with open (file_output,'w') as file_o:
    #7. Scrivere il contatore nel file creato
    risultato = "All'interno del file, il carattere " +carattere +" compare " +str(contatore) +" volte"
    file_o.write(risultato)
