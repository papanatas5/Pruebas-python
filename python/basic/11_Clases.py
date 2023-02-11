### Classes ###
#Una clase es un objeto

class MyEmptyPerson:
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname): #init es un constructor
        self.name = name
        self.surname = surname
    #el nombre y el apellido son definidos por fuera

my_person = Person("Pedro","Niello")
print(f"{my_person.name} {my_person.surname}")

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  #Propiedad publcia
        self.__name= name
        self.__surname= name #al poner __ lo definis como privada

    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} Esta Caminando")

my_person = Person ("Pedro", "Niello")
print(my_person.full_name) 
print(my_person.get_name)
my_person.walk()

my_other_person = Person("Ricardo", "Rodriguez", "Riri")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Esteban Uzumaki (El gran ninja de la cuarta guerra)"
print(my_other_person.full_name)

my_other_person.full_name = 666     #Como es un lenguaje debil, podemos cambiar y romper como si nada
print(my_other_person.full_name)
