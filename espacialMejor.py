# Complejidad espacial del mejor caso

import tracemalloc

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
    tamano_enteros = n * 28
    tamano_lista = 64 + n * 8
    total_bytes = tamano_enteros + tamano_lista
    teorico_kb = total_bytes / 1024

    picos_memoria = []
    for _ in range(5):
        lista = list(range(1, n+1))
        tracemalloc.start()
        quicksort(lista)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        picos_memoria.append(peak)
    
    promedio_peak_kb = (sum(picos_memoria) / len(picos_memoria)) / 1024

    resultados.append((n, teorico_kb, promedio_peak_kb))

print("Tamaño\t Espacio teórico (B) \t\t Espacio teórico (KB) \t\t Espacio real (B) \t\t Espacio real (KB)")
for n, teorico, real in resultados:
    print(f"{n}\t {teorico * 1024} B\t\t\t {teorico:.1f} KB\t\t\t {real * 1024} B\t\t\t {real:.1f} KB")
