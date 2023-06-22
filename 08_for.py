stringa = "Ciao!"
for numero in 1,2,3,4,5:
    print(stringa)

for n in range(4):
    print(n)

for n in range(2,5):
    print(n)

for n in range(2,8,2):
    print(n)   

stringa = "pierporz"

for n in stringa:
    print ("il mio canale preferito!")
    print(n)

for n in range(10):
    if n>5 or n<8:
        continue
    print(n)

for n in range(10):
    if n>5 and n<8:
        continue
    print(n)
