
d = {'chiave': 10, 'altro': 11, 'nonesiste': 12}

try:
    # accedo a una proprietà che non c'è
    print(d['nonesiste'])
    a = 0 / 1
    print(a)    
except KeyError as ke:
    print(ke)
except ZeroDivisionError as ze:
    print(ze)
except Exception as err:
    print('errore generico')
    print(err)