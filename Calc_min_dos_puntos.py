def calcular_minimo(a, b):
    # Compara los dos valores y devuelve el menor
    if a < b:
        minimo = a
    else:
        minimo = b

    return minimo


print(calcular_minimo(1, 2))   # 1
print(calcular_minimo(8, 1))   # 1