### Retos ###

""" 
Fizz Buzz
"""

def fizzbuzz ():
    for index in range (1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print ("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)
 
fizzbuzz()

"""
Es un anagrama
"""

def anagrama (word_one, word_two):
    if word_one.lower() == word_two.lower():
       return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(anagrama("amor", "roma"))

# fibonacci

def fibonacci():

    prev = 0
    next = 1
    for i in range (0, 51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
           
fibonacci()

#numeros primos

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in range(1, 101):
    if es_primo(num):
        print(num)

# La función es_primo(num) es una función auxiliar que determina si un número es primo o no.
# La primera línea de la función es_primo(num) verifica si num es menor que 2. Si es así, devuelve False, ya que los números menores que 2 no son primos.
# La línea for i in range(2, num): itera a través de los números desde 2 hasta num - 1.
# La línea if num % i == 0: verifica si num es divisible por i. Si es así, significa que num no es primo y se devuelve False.
# Si el bucle for se completa sin encontrar un número que num sea divisible, significa que num es primo y se devuelve True.
# La segunda parte del código, for num in range(1, 101):, itera a través de los números del 1 al 100.
# La línea if es_primo(num): llama a la función es_primo(num) para verificar si num es primo.
# Si num es primo, se imprime en la consola con la línea print(num).
# En resumen, este código utiliza una función auxiliar es_primo(num) para determinar si un número es primo o no, y luego itera a través de los números del 1 al 100 para imprimir aquellos que son primos.