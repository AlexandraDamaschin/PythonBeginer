# 1. Snakes example
how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""

print(snake_string * how_many_snakes)

# 2. Input string
name = input('Please, Enter a name:')
print('Hello', name.title())

# 3. Input int
number = int(input('Please, Enter a number'))
print(number)

# 4. Input int
num = float(input('Please, Enter a number'))
print(num)

# 5.Input float transformed to int
numb = int(float(input('Please, Enter a number')))
print(numb)

# 6. Input expression
x = eval(input('Enter an expression: '))
print(x)
