### Excepciones ###
"""Manejo de errores"""

numberOne, numberTwo = 5, 1
numberTwo = "4"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:   #opcional
    #se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:   #opcional
    #Se ejecuta siempre
    print("la ejecucion continua")

# tipos de excepciones

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Error 506")
except ValueError:
    print("Error 102")
except ZeroDivisionError:
    print("Error 1002")

# Captura de la informacion de la excepion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as e:
    print(e)
    