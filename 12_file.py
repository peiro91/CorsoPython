file1 = open("divina_commedia.txt","r")

print(dir(file1))
contenuto = file1.read(10)
print(contenuto)
file1.close()

file1 = open("esempio_write.txt","w")
file1.write("Questo è il mio primo file\nSeguite Pierporz!")
file1.close()
file1 = open("esempio_write.txt","a")
file1.write("\nIl canale di Pierporz è il migliore")
file1.close()

with open("esempio_with.txt","w") as file1:
    file1.write("esempio cosrutto with")
