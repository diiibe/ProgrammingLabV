class CSVfile() : #creazione della classe

    def __init__(self, name):
        self.name = name

    def get_data(self):
        
        values = []   
        file = open(self.name, "r") 

        for line in file :
            elements = line.split(",") 

            if elements [0] != "Date":
                date = elements [0]
                value = elements [1]
                values.append(float(value)) 
            return values

pass

myfile = CSVfile(name = 'shampoo_sales.csv') #inizializzazione
print(myfile.name)
print(myfile.get_data()) 