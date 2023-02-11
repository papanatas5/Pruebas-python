### lambdas ###

suma = lambda first_value, second_value: first_value + second_value

print(suma (1, 1))

def sum_three_values (value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
