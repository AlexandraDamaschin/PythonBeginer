# 1. Calculate cylinder_volume
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(2, 3))


# 2. Print vs. Return in Functions
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)


# this returns something
def add_ten(num):
    return (num + 10)


print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('This function returned: {}'.format(return_value_2))
