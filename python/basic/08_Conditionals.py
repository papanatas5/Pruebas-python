### Condicionales ###

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True
    print ("Se ejecuta la condicion del if")


my_condition = 5*5

if my_condition == 10:  
    print ("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20: #aqui debe cumplir dos condiciones / se usan operadores   
    print ("es mayor que 10 y menor que 20")
elif my_condition == 25:
        print ("es 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print ("La ejecucion continua")

my_string = ""

if  not my_string:
    print ("mi cadena de texto esta vacía")

if my_string == "mi cadena de textoooo":
    print ( " estas cadenas de texto coinciden")

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

enter_your_age = 17
if enter_your_age >=18:
    print("You are old enough to learn to drive")
elif enter_your_age == 17:
    print("you need 1 more year to learn to drive")
elif enter_your_age == 16:
    print("you need 2 more year to learn to drive")
elif enter_your_age == 15:
    print("you need 3 more year to learn to drive")
elif enter_your_age == 14:
    print("you need 4 more year to learn to drive")
elif enter_your_age == 13:
    print("you need 5 more year to learn to drive")
elif enter_your_age == 12:
    print("you need 6 more year to learn to drive")
else:
    print("Come back in the next few years")



jessica = 95
naruto = 60
itadori = 72
sasuke = 53
steven = 47

if steven >=90 and steven <=100:
    print("You have A")
if steven >=70 and steven <=89:
    print("You have B")
if steven >=60 and steven <=69:
    print("You have C")
elif steven >=50 and steven <= 59:
    print("You have D")
else:
    print("You have F") 

#jessica = 95
if jessica >=90 and jessica <=100:
    print("You have A")
if jessica >=70 and jessica <=89:
    print("You have B")
if jessica >=60 and jessica <=69:
    print("You have C")
if jessica >=50 and jessica <= 59:
    print("You have D")
if jessica >=0 and jessica <=49:
    print("You have F") 

#naruto = 60
if naruto >=90 and naruto <=100:
    print("You have A")
if naruto >=70 and naruto <=89:
    print("You have B")
if naruto >=60 and naruto <=69:
    print("You have C")
elif naruto >=50 and naruto <= 59:
    print("You have D")
else:
    print("You have F") 

#itadori = 75
if itadori >=90 and itadori <=100:
    print("You have A")
if itadori >=70 and itadori <=89:
    print("You have B")
if itadori >=60 and itadori <=69:
    print("You have C")
if itadori >=50 and itadori <= 59:
    print("You have D")
if itadori >=0 and itadori <=49:
    print("You have F") 

#sasuke = 53
if sasuke >=90 and sasuke <=100:
    print("You have A")
if sasuke >=70 and sasuke <=89:
    print("You have B")
if sasuke >=60 and sasuke <=69:
    print("You have C")
elif sasuke >=50 and sasuke <= 59:
    print("You have D")
else:
    print("You have F")