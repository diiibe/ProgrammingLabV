
name = ('shampoo_sales.csv')

def count(name):
    num_lines = sum(1 for line in open(name))
    return num_lines
        
        
print('numero righe: {}'.format(count(name)) )



