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


# 3. Population Density Function
def population_density(population, land_area):
    """Calculate the population density of an area.
    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.
    OUTPUT:
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# 4. Return how many weeks and days mean an inputted int
def readable_timedelta(days):
    """ Return a string of the number of weeks and days included in days.
    Parameters:
    days -- number of days to convert (int)
    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)


# test your function
print(readable_timedelta(10))

# 5.Lambda Expressions
multiply = lambda x, y: x * y
print(multiply(4, 7))

# 6.  Lambda with Map
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

# function
# def mean(num_list):
#    return sum(num_list) / len(num_list)
# lambda expresion 1
# mean= lambda num_list: sum(num_list)/len(num_list)
# lambda expresion 2
# averages = list(map(mean, numbers))
averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

# 7.Lambda with filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
# funtionc
# def is_short(name):
#   return len(name) < 10

# short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)


# 8. Iterators And Generators
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1


for x in my_range(5):
    print(x)

# 9. Implement  generator function that works like the built-in function enumerate
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# 10. Chunker
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))

# 11.Generator Expressions
sq_list = [x ** 2 for x in range(10)]  # this produces a list of squares
print(sq_list)
sq_iterator = (x ** 2 for x in range(10))  # this produces an iterator of squares
print(sq_iterator)
