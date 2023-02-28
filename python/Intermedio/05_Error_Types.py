### Tipos de Errores ###

#Syntax Error
# print "hola gente" #Error
print("Hola gente")

# Name Error
name = "pedro" #Comentar para Error
print(name)

#Index Error
my_list = [2, 5, 6, 7, 9]
print(my_list[0])
print(my_list[3])
#print(my_list[5]) #descomentar para error

#ModuleNotFoundError
#import maths #Descomentar para error
import math

#AttributeError
#print(math.PI) #Descomentar para Error
print(math.pi)

#Key Error
my_dict = {
    "Nombre" : "Pedro", 
    "Apellido" : "Niello", 
    "Age" : 17,
    "Lenguajes" : {"python", "Java", "c#"},
    1: "1,79"
    }
print(my_dict["Nombre"])
#print(my_dict["Nomvre"]) #Descomentar para error

#Type Error
#print(my_list["Nombre"]) #Descomentar para error
print(my_list[0])

#Import Error
#from math import PI #Descomentar para error
from math import pi
print(pi)

# Value Error
#my_int = int("10 años") #Descomentar para error
my_int = int("10")
print(type(my_int))

#ZeroDivisionError
#print(4/0) #Descomentar para error
print(4/2)