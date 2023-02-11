
def calculadora(operacion, numeros):
    if operacion == "suma":
        resultado = sum(numeros)
    elif operacion == "resta":
        resultado = numeros[0] - sum(numeros[1:])
    elif operacion == "multiplicacion":
        resultado = 1
        for num in numeros:
            resultado *= num
    elif operacion == "division":
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado /= num
    else:
        resultado = "Operación no válida"
    return resultado

print(calculadora("suma", [1, 2, 3]))
print(calculadora("resta", [10, 5, 2]))
print(calculadora("multiplicacion", [1, 2, 3, 4]))
print(calculadora("division", [10, 5, 2]))
