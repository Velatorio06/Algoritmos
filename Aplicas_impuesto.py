def calcular_precio_con_impuesto(precio_base, porcentaje_impuesto):
    # Calcula el impuesto
    impuesto = precio_base * (porcentaje_impuesto / 100)

    # Calcula el precio final
    precio_final = precio_base + impuesto

    return precio_final


print(calcular_precio_con_impuesto(100, 21))   # 121.0
print(calcular_precio_con_impuesto(50, 10))    # 55.0
