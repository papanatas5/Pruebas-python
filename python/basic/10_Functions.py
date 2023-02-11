### Funciones ###

def my_function ():
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
    print (first_value + second_value)

sum_two_values (5, 8) 
sum_two_values (467185, 47855)
sum_two_values ("5", "7")
sum_two_values (1.5, 5.8)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values (1.4, 5.2)
print (my_result)   #curiosidad, esto devuelve none, por que no retorna nada

my_result = sum_two_values_with_return(10, 5)
print(my_result)

## PARAMETROS ##

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Dos parametros # 
def print_name (name, surname):
    print(f"{name} {surname}")  #F de Formateo

print_name(surname = "Niello", name = "Pedro")

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


# Parametro por defecto #
def print_name_with_default (name, surname, alias = "Sin alias"):
     print(f"{name} {surname} {alias}") 

print_name_with_default("Pedro","Niello")
print_name_with_default("Pedro","Niello", "Pepe")

#Poder pasar textos infinitos en un parametro, un parametro dinamico
def print_texts (*text):
    print(text)

print_texts ("Hola", "Python", "Java")
print_texts ("hola")

# Parametro por defecto y numeros arbitrario de parametros
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

#Con For
def print_texts (*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts ("Hola", "Python", "Java")
print_texts ("hola")

# Devolviendo un booleano
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

#Devolviendo una lista
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

#Function as a Parameter of Another Function#

#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
