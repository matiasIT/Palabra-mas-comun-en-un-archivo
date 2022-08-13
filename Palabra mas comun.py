"""
Programa que crea una tupla con el conteo de las veces que aparece cada palabra contenida en el archivo
"""

"""
Se abre el archivo en el que se itera por linea y palabras para contarlas almacenandolas en un diccionario
"""

archive = open("mbox-short.txt")
counts = dict()
for line in archive:        
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

"""
Se itera el diccionario y se crea una lista con los valores y las claves para poder ordenarlas de mayor a menor
"""

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

"""
Y por ultimo se vuelve a iterar por la lista ya ordenada de mayor a menor el conteo de cada palabra mostrandose en formato de tupla
en un top 10
"""

for val, key in lst [:10]:
    print(key, val)
