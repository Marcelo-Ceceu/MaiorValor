Entrada1 = float (input("Escreva 1º Valor: "))

while True:
    Entrada2 = float (input("Escreva 2º Valor: "))
    if Entrada2 != Entrada1:
        break
    else:
        print("Os valores precisão ser diferentes, digite novamente:")

if Entrada2 == Entrada1:
   print("Entrada invalida")
   Entrada2 = float (input("Escreva um novo número: "))

if Entrada2 > Entrada1:
    print("Valor Maior", Entrada2)
else:
    print (f"Valor Maior: {Entrada1}")