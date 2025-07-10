# Complejidad temporal del peor caso

import time
import random
import sys

sys.setrecursionlimit(20000)

tamanos = [10000, 100000, 1000000, 10000000, 100000000]

resultados = []

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    izq, centro, der = [], [], []
    pivote = lista[0]

    for n in lista:
        if n < pivote:
            izq.append(n)
        elif n == pivote:
            centro.append(n)
        else:
            der.append(n)

    return quicksort(izq) + centro + quicksort(der)

for n in tamanos:
    lista = list(range(n, 0, -1))
    inicio = time.perf_counter()
    quicksort(lista)
    fin = time.perf_counter()
    tiempo = fin - inicio
    resultados.append((n, tiempo))

print("Tamaños\t Tiempo")
for n, tiempo in resultados:
    print(f"{n}\t {tiempo:.6f}")
