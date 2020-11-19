values = []   # inizializzo lista per prezzi
shampoolist = open("shampoo_sales.csv", "r") # apro file e lo leggo riga per riga

for line in shampoolist :
    elements = line.split(",") # faccio li split sulla virgola

    if elements [0] != "Date":
        date = elements [0]
        value = elements [1]

values.append(float(value)) # creo lista con prezzi

def somma(values): # sommo tutti i prezzi 
    totale = 0
    for item in values:
        totale += item 
    return totale
print("Totale: {}".format(somma(values)))