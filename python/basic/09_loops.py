### Loops ###

# while

my_condition = 0

while my_condition < 10:
    print (my_condition)
    my_condition += 2
else:   # Opcional
    print ("La ejecucion termino")

print ("La ejecucion continua")

# Break #
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print ("Mi condicion es 15 se acabo bro")
        break

    print (my_condition)

print ( "La ejecucion continua")

# For # Bucle para los elementos en las listas, tuplas, sets y dict

my_list =  [ 17, 24, 52, 30, 30, 35, 100]

for  element  in  my_list:
    print(element)

my_tuple = ( 17, 1.79, "Pedro", "Niello")
for  element  in  my_tuple:
    print(element)

my_set = {"Pedro", "Niello", 17}
for  element  in  my_set:
    print(element)

my_dict = {"Nombre" : "Pedro", "Apellido" : "Niello", "Age" : 17, "Lenguajes" : {"python", "Java", "c#"}, 1: "1,79"}

for  element  in my_dict:
    print(element)
    if element == "Age":
        break   #termina el for y sigue con lo siguiente 
    print ("Se ejecuta")
else:
    print("El bucle for para diccionario ah finalizado")

print ( "La ejecucion continua")

# Continue # aplicable en el while

for  element  in my_dict:
    print(element)
    if element == "Age":
        continue    #Salta a lo siguiente o toma un pequeño break / No Aconsejable
    print ("Ejecucion")
else:
    print("El bucle for para diccionario ah finalizado")

# Range #
"""The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range"""
# syntax
# for iterator in range(start, end, step):

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

#Ejemplo para que en los dict tengas la clave y el valor

person = {
    'first_name: ':'Asabeneh',
    'last_name: ':'Yetayeh',
    'age: ':250,
    'country: ':'Finland',
    'is_marred: ':True,
    'skills: ':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address: ':{
        'street: ':'Space street',
        'zipcode: ':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop') 

#Imprimiendo valor especifico#
person = {
    'first_name': 'Asabeneh',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# Pass #
"""In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors"""
for number in range(6):
    pass
