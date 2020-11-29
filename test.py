
class CSVfile() : #creazione della classe#

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        

        if not type(name) == str:
            raise Exception('non e una stringa')


    def count(self, name):
        num_lines = sum(1 for line in open(self.name))
        return num_lines

        self.lines = num_lines
        


    def get_data(self, num_lines, start=None, end=None):

        if not type(start) == int and type(end) == int: 
            raise Exception('non sono righe')

        if not end < num_lines:
            raise Exception('non ci sono abbastanza righe')


        values = []   
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None

        lines = my_file.readlines()
        linesf = lines[self.start:self.end]



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

        def total(values):   
            total = 0
            for item in values:
                total += item 
            return total


mio_file = CSVfile(name = 'shampoo_sales.csv', start = 8 ,end = 59) #inizializzazione
print('Nome del file: "{}"\n'.format(mio_file.name))
print('Numero righe: "{}"\n'.format(mio_file.count(mio_file.name)))
print('\nDati contenuti nel file: "{}"'.format(mio_file.get_data(mio_file.num_lines)))
print("Totale: {}".format(mio_file.total(mio_file.values)))