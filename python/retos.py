# Enunciado
#           El objetivo de este trabajo será usar sentencias condicionales y funciones para validar una fecha
#   dada como argumento de entrada, y así determinar si corresponde a una fecha existente o no.
#   Por ejemplo:

#           24/5/2008 es una fecha válida.
#           31/9/2018 no es una fecha válida porque Septiembre no tiene un día 31.
#           29/2/2000 es una fecha válida porque 2000 es bisiesto y Febrero tiene un día 29.
#           29/2/1900 no es una fecha válida porque 1900 no es bisiesto y Febrero no tiene un día 29.
#           Nota: no utilice la entrada de datos por teclado (con input) en ninguna parte del código.

# Descomposición del problema

#   Para resolver el ejercicio deberá escribir varias funciones con el objetivo de descomponer el problema
#   y luego usar esas funciones para implementar la solución completa. Es recomendable que escriba
#   cada función en el orden presentado aquí y pruebe cada una antes de pasar a la siguiente.
#   Todas las funciones deberán implementarse en un único archivo .py que luego deberá subir al entorno con el formato TP1_NombreApellido.py.
#   Las tres primeras funciones no producirán ninguna sentencia print, más bien producirán un resultado (con return). Puede usar print dentro de estas funciones para visualizar y/o corregir errores,
#   pero para la entrega final deberá comentar esas líneas o eliminarlas.

# 1. Escriba la función es_mes_valido(mes). La función deberá retornar True si el mes es válido,
#   y False de lo contrario. Necesitará al menos 3 casos de prueba para asegurarse de que funciona
#   correctamente. Por ejemplo:
#           5 es un mes válido.
#           -5 no es un mes válido.
#           15 no es un mes válido.
# 
# 2. Escriba la función es_año_bisiesto(año). La función deberá retornar True si el año es un año
#   bisiesto, y False de lo contrario. Un año es bisiesto si es divisible por 4, excepto los años de comienzo
#   de siglo (terminados en 00) que no sean divisibles por 400. Necesitará al menos 4 casos de prueba
#   para asegurarse de que funciona correctamente. Por ejemplo:

#           2020 es un año bisiesto.
#           2013 no es un año bisiesto.
#           2000 es un año bisiesto.
#           1900 no es un año bisiesto.

# 3. Escriba la función es_dia_valido(dia, mes, año). La función deberá retornar True si el día es
#   válido dentro del mes, y False de lo contrario. Las reglas son:
#       Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre tienen 31 días.
#       Abril, Junio, Septiembre y Noviembre tienen 30 días.
#       Febrero tiene 28 días, excepto en años bisiestos que tiene 29 días (por eso se incluye el argumento año en la función).
#    Necesitará al menos 6 casos de prueba para asegurarse de que funciona correctamente:

#           5 es un día válido en cualquier mes.
#           -5 no es un día válido en ningún mes.
#           35 no es un día válido en ningún mes.
#           31 es un día válido en algunos meses pero inválido en otros.
#           29 es un día válido en Febrero sólo si es un año bisiesto.

# 4. Escriba la función es_fecha_valida(dia, mes, año). Esta función deberá recibir como argumentos el día, el mes y el año, y deberá mostrar un mensaje en pantalla (usando print). En esta
#   función deberá llamar a las funciones anteriores para determinar la validez de la fecha y probar los
#   resultados (usando sentencias if/else).

#           Si la fecha es válida (por ejemplo, la fecha 24/5/2008), la función deberá mostrar el texto:
#   24/5/2008 es una fecha válida.
#           Y si la fecha es inválida (por ejemplo, la fecha 31/9/2018), la función deberá mostrar el texto:
#   31/9/2018 no es una fecha válida.


"""Resolucion"""
def es_mes_valido (mes):
    if (mes < 0 or mes > 12):
        return False
    else:
        return True

# print(es_mes_valido (5)) 

#los año comienzo de siglo que NO sean divisibles por 400

#un año es biciesto si es divisible por 4 y por 100 y no es divisible por 400

def es_año_bisiesto (año):
    if (año % 4 == 0 and (año % 100 == 0 and año % 400 != 0)): 
        return True
    else:
        return False

# print(es_año_bisiesto(1900))

# las funciones tienen que ser inicializadas con ( ) y tenes q pasarle el parametro que te pide. Si lleva 1 parametro, le pasas 1 parametro. 

def es_dia_valido (dia, mes, año): #estas usando 1 solo parametro y hay 3 

    if (es_año_bisiesto(año) == True):

        if ((mes in (1,3,5,7,8,10,12)) and (dia <= 31 and dia > 0)):
            return True

        elif ((mes in (4, 6, 9, 11)) and (dia <= 30 and dia > 0)):
            return True

        elif ((mes == 2) and (dia <= 29 and dia > 0)):
            return True

        else:
            return False

    #esto se inicia si el año biciesto es False
    else:

        if ((mes in (1,3,5,7,8,10,12)) and (dia <= 31 and dia > 0)): 
            return True

        elif ((mes in (4, 6, 9, 11)) and (dia <= 30 and dia > 0)): 
            return True
              
        elif ((mes == 2) and (dia <= 28 and dia > 0)): 
            return True

        else:
            return False


# print(es_dia_valido (12, 9, 2023))
# print(es_dia_valido (48, 2, 2023)) 

def es_fecha_valida (dia, mes, año):
    if ((es_mes_valido(mes) == True) and (es_dia_valido(dia, mes, año) == True)):
        print("Es una fecha valida")
    else: 
        print("Es una fecha invalida")

es_fecha_valida (24, 5, 2008)
es_fecha_valida (32, 2, 2018)
es_fecha_valida (-3, 12, 2015)
es_fecha_valida (3, 6, 2011)
es_fecha_valida (29, 2, 2023)
es_fecha_valida (29, 2, 1900)


### Enunciado 2 ###


# print("Desorden")
# mi_lista = ("Santa", "Fe")
# d1 =(mi_lista[0][:3])
# d2 =(mi_lista[1][:1])
# t1 =(mi_lista[0][3:])
# t2 =(mi_lista[1][1:])
# x = d1 + d2 + t1 + t2
# print(x)


# def desorden (text):
#     print(str.split(text[:3]))
# desorden("asgrfd")

