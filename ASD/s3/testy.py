lista = {'r': 1, 'o': 1, 'a': 1, 'k': 2, 'p': 1}
ind = {'k': 2, 'a': 1, 'r': 1, 'o': 1}

klucze_do_usuniecia = [key for key in lista if key not in ind]

for key in klucze_do_usuniecia:
    del lista[key]

print(lista)