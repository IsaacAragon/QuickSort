# Complejidad temporal del mejor caso

import time

tamanos = [10000, 12000, 14000, 16000, 18000]
resultados = []

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    izq, centro, der = [], [], []
    pivote = lista[len(lista)//2]

    for n in lista:
        if n < pivote:
            izq.append(n)
        elif n == pivote:
            centro.append(n)
        else:
            der.append(n)

    return quicksort(izq) + centro + quicksort(der)

for n in tamanos:
    lista = list(range(1, n+1))
    inicio = time.perf_counter()
    quicksort(lista)
    fin = time.perf_counter()
    tiempo = fin - inicio
    resultados.append((n, tiempo))

print("Tamaños\t Tiempo")
for n, tiempo in resultados:
    print(f"{n}\t {tiempo:.6f}")
