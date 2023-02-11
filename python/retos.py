
## esto te lo mando yo pa ##

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
