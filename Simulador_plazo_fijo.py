monto = float(input("Ingrese su monto inicial: "))
monto_extra_agregado_cada_30_dias = float(input("Ingrese algún monto extra ingresado cada mes: "))
interes_anual = float(input("Ingrese el interés anual: "))
dias = float(input("Ingrese la duración del palzo fijo: "))

def simular_plazo_fijo(monto, monto_extra_agregado_cada_30_dias, interes_anual, dias):
    interes_mensual = interes_anual/12
    meses = int(dias//30)
    for mes in range(meses):
        monto += (monto*interes_mensual/100 + monto_extra_agregado_cada_30_dias)
    return int(monto)

print(f"Su plazo fijo le retornaría un aproximado de {simular_plazo_fijo(monto, monto_extra_agregado_cada_30_dias, interes_anual, dias)} pesos.")
