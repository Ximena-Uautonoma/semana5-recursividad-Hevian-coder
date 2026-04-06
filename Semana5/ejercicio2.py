"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    y = n
    x = 1
    while y != 1:
        n = n + x
        x = x + 1
        y = y-1
    return print(n)
    



def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)

suma_ciclo(5)
print("recursiva: ")
print(suma_recursiva(5))