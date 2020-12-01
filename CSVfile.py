class CSVfile() : #creazione della classe#

    def __init__(self, name):
        self.name = name
    
        if not type(name) == str:
            raise Exception('non e una stringa')

    def get_data(self, start=None, end=None):
        
        values = []   
        try:
            my_file = open('shampoo_sales.csv')
        except Exception as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None
            
        for line in my_file :
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

mio_file = CSVfile(name = 'shampoo_sales.csv') #inizializzazione
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data())) 
