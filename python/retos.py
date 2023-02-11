def es_mes_valido (mes):
    if (mes < 0 or mes > 12):
        message = ("No es valido")
    else:
        message = ("Es valido")
    return message

print(es_mes_valido (5))

def es_año_bisiesto (año):
    if (año % 4 == 0 and (año % 100 == 0 and año % 400 != 0)):
        message = ("Es un año bisiesto")
    else:
        message = ("No es un año bisiesto")
    return message

print(es_año_bisiesto(1900))

def es_dia_valido (dia, mes, año):
    if es_año_bisiesto == True:
        if es_mes_valido == (1,3,5,7,8,10,12):
            if dia <= 31 or dia > 0:
                message = ("es valido")
        elif es_mes_valido == (4, 6, 9, 11):
                if dia <= 30 or dia > 0:
                    message = ("es valido")
        elif es_mes_valido == 2:
            if  dia < 29 or dia > 0:
                message = ("Es valido")
        else:
            message = ("no es valido")
        return message
    else:
        if es_mes_valido == (1,3,5,7,8,10,12):
            if dia <= 31 and dia > 0:
                message = ("es valido")
        elif es_mes_valido == (4, 6, 9, 11):
                if dia <= 30 or dia > 0:
                    message = ("es valido")
        elif es_mes_valido == 2:
            if  dia < 28 or dia > 0:
                message = ("Es valido")
        else:
            message = ("no es valido")
        return message

print(es_dia_valido (12, 9, 2023))
print(es_dia_valido (48, 2, 2023))



def es_dia_valido (dia, mes, año):
    if (año % 4 == 0 and año % 100 == 0 or año % 400 != 0):
        if mes == (1,3,5,7,8,10,12):
            if dia <= 31 or dia > 0:
                message = ("es valido")
        elif mes == (4, 6, 9, 11):
                if dia <= 30 or dia > 0:
                    message = ("es valido")
        elif mes == 2:
            if  dia < 29 or dia > 0:
                message = ("Es valido")
        else:
            message = ("no es valido")
        return message
    else:
        if mes == (1,3,5,7,8,10,12):
            if dia <= 31 or dia > 0:
                message = ("es valido")
        elif mes == (4, 6, 9, 11):
                if dia <= 30 or dia > 0:
                    message = ("es valido")
        elif mes == 2:
            if  dia <= 28 or dia > 0:
                message = ("Es valido")
        else:
            message = ("no es valido")
        return message     



## esto te lo mando yo pa ##

def es_mes_valido (mes):
    if (mes < 0 or mes > 12):
        message = ("No es valido")
    else:
        message = ("Es valido")
    return message

# print(es_mes_valido (5)) 

#los año comienzo de siglo que NO sean divisibles por 400

#un año es biciesto si es divisible por 4 y por 100 y no es divisible por 400

def es_año_bisiesto (año):
    if (año % 4 == 0 and (año % 100 == 0 and año % 400 != 0)): 
        message = ("Es un año bisiesto")
    else:
        message = ("No es un año bisiesto")
    return message

# print(es_año_bisiesto(1900))

# las funciones tienen que ser inicializadas con ( ) y tenes q pasarle el parametro que te pide. Si lleva 1 parametro, le pasas 1 parametro. 

def es_dia_valido (dia, mes, año): #estas usando 1 solo parametro y hay 3 
    message = "Error"

    if (es_año_bisiesto(año) == True):

        if ((mes in (1,3,5,7,8,10,12)) and (dia <= 31 and dia > 0)):
            message = "Es valido"

        elif ((mes in (4, 6, 9, 11)) and (dia <= 30 and dia > 0)):
            message = "Es valido"

        elif ((mes == 2) and (dia <= 29 and dia > 0)):
            message = "Es valido"

        else:
            message = "No es valido"

        return message

    #esto se inicia si el año biciesto es False
    else:

        if ((mes in (1,3,5,7,8,10,12)) and (dia <= 31 and dia > 0)): 
            message = "Es valido"

        elif ((mes in (4, 6, 9, 11)) and (dia <= 30 and dia > 0)): 
            message = "Es valido" 
              
        elif ((mes == 2) and (dia <= 28 and dia > 0)): 
            message = "Es valido"

        else:
            message = "No es valido"

        return message

print(es_dia_valido (12, 9, 2023))
print(es_dia_valido (48, 2, 2023)) 

