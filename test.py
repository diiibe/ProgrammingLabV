
class CSVfile() : #creazione della classe#

    def __init__(self, name):
        self.name = name
        self.num_lines = 0
        self.tot = 0.0

        if not type(name) == str:
            raise Exception('non e una stringa')


    def count(self):
        self.num_lines = sum(1 for line in open(self.name))
        return self.num_lines

        
    def get_data(self, start = None, end = None):

        if not type(start) == int and type(end) == int: 
            raise Exception('non sono righe')

        if end > self.num_lines:
            raise Exception('non ci sono abbastanza righe')

        values = []   
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None

        lines = my_file.readlines()
        linesf = lines[start:end]

        for line in linesf :
            elements = line.split(',')          
            if elements[0] != 'Date':                                  
                date  = elements[0]
                value = elements[1]                                
                try:
                    value = float(value)
                except Exception as e:                                     
                    print('Errore nela conversione a float: "{}"'.format(e))  
                    continue               
                values.append(value)              
        my_file.close()               
        return values

    
    def total(self, values):   
        self.tot = sum(values)
        return self.tot


        



# corpo principale dello script
mio_file = CSVfile(name = 'shampoo_sales.csv') #inizializzazione
mio_file.count() # conto righe

#print('Nome del file: "{}"\n'.format(mio_file.name))
print('Numero righe: "{}"\n'.format(mio_file.count()))
#print('\nDati contenuti nel file: "{}"'.format(mio_file.get_data(start = 8, end = 27)))

lista = mio_file.get_data(start = 8, end = 27)
print(mio_file.total(lista))
