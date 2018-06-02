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

# 7.Try statement
while True:
    try:
        x = int(input('Please enter a number:'))
        break
    #     if we don`t specify type of error, project will never stop
    except ValueError:
        print('That`\s not a valid number! Try again')
    except KeyboardInterrupt:
        print('\n No input taken')
    finally:
        print('\n Attempted Input')


# 8. Party cookies example
def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered that 0 people will be attending.")
        print("Please enter a good number of people for this big party.")

    return (num_each, leftovers)


# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")
