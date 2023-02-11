### Dictionaries ###

my_dict = dict ()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre" : "Pedro", 
    "Apellido" : "Niello", 
    "Age" : 17,
    1 : "python"}

my_dict = {
    "Nombre" : "Pedro", 
    "Apellido" : "Niello", 
    "Age" : 17,
    "Lenguajes" : {"python", "Java", "c#"},
    1: "1,79"}

print(my_other_dict)
print(my_dict)

#Como trata la longitud#
print(len(my_other_dict))
print(len(my_dict))

#impresion#
print(my_dict["Nombre"])

print(my_dict.get("Nombre")) # Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method.

#Cambiar dato#
my_dict["Nombre"] = "Brais"
print(my_dict["Nombre"])

print(my_dict[1])

#agregar dato#
my_dict["calle"] = "25 de mayo"
print(my_dict)

#Borrar un dato#
del my_dict ["calle"]
print(my_dict)

#Comprobar un dato, se comprueba por la clave no por el valor#
print("Niello" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items()) #Item
print(my_dict.keys()) #Claves
print(my_dict.values()) #Valores

#FromKeys#
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict)) #Aca es como que hace una copia de un dict sin sus valores para poder llenarlos luego
my_new_dict = dict.fromkeys (my_dict, "Pedro")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict)) 

#The items() method changes dictionary to a list of tuples.
print(my_dict.items())
print(type(my_dict))

#clear a dictionary
print(my_dict.clear())

#copy dict
print(my_dict.copy)

#ejercicio#
dog = { "Name" : "Homero",
    "color" : "Brown", 
    "age" : 2,
    "breed" : "Akita japonés",
    "legs" : 3
  }
student = {"First Name" : "Pepe",
    "Last Name" : "Rodriguez",
    "Gender" : "Other",
    "Age" : 45,
    "Status Marital" : "Solitarie",
    "Skills" : "none",
    "Country" : "Poland",
    "City" : "Varsovia",
    "Adress" : "No Exist"
    } #GG

print(len(student)) #GG

print(student["Skills"])
print(type(student.get("Skills")))
print(type(student["Skills"])) #G

student["Skills"] = "Sleep", "Eat"
print(student) #GG?

print(student.keys()) #GG
print(student.values()) #GG

student_list = list(student.items( ))
print(type(student_list)) #GG

del student ["Adress"]
print (student) #GG

print(student.clear()) #GG