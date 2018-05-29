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
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)


# test your function
print(readable_timedelta(10))
