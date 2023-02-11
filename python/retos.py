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
