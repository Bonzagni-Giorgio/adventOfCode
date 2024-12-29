# Nome del file da cui leggere i dati
file_name = "liste.txt"

# Liste vuote per salvare i dati
lista1 = []
lista2 = []

# Apertura e lettura del file
with open(file_name, "r") as file:
    # Leggi riga per riga
    for riga in file:
        # Dividi ogni riga in base al separatore (spazio o tab)
        valori = riga.strip().split()
        
        # Aggiungi il primo valore alla prima lista e il secondo alla seconda lista
        lista1.append(int(valori[0]))
        lista2.append(int(valori[1]))
lista1.sort()
lista2.sort()


'''
diffTot = 0
for i in range(len(lista1)):
    valore1 = lista1[i]
    valore2 = lista2[i]
    diff=abs(valore1 - valore2)
    diffTot=diffTot+diff
print (diffTot)
'''
conta = 0
moltiplica = 0
finale = 0
for valore1 in lista1:
    conta = lista2.count(valore1)  # Conta quante volte valore1 è presente in lista2
    print("il numero ",valore1," è presente ",conta, " volte")
    moltiplica=valore1*conta
    finale=finale+moltiplica
print(finale)
# Stampa per verifica
#print("Lista 1:", lista1)
#rint("\n\n")
#print("Lista 2:", lista2)