# 1. sum numbers
print((23 + 32 + 64) / 3)

# 2.order is important
print((17 * 6) - ((9 * 7) + (5 * 7)))

# 3.variables name need to contain _
mv_population = 12345
mv_area = 11.23
mv_density = mv_population / mv_area
print(mv_density)

# 4.decrease by 10%
mv_population *= 0.9

# 5.decrease by 5%
mv_population *= 0.95

# 6.print type of inputted value
print(type(4.0))

# 7.convert int to float
print(int(2.3))

# 8.boolean example
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population / sf_area
rio_de_janeiro_pop_density = rio_population / rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)

# 9.strings
welcome = 'Hello world'
print(welcome)

# 10.length of a string
welcome_length = len(welcome)
print(welcome_length)

# 11.index into strings
print(welcome[1])

# 12.write a sentence
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

print(username + " accessed the site " + url + " at " + timestamp + ".")

# 13.calculate length of a sentence
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

full_name = (given_name + " " + middle_names + " " + family_name)

name_length = len(full_name)

# Now we check to make sure that the name fits within the driving license character limit
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# 14.Sales example
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

mon_sales = int(mon_sales)
tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)
total_sales = (mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales)
print("This week's total sales: " + str(total_sales))

# 15.count fish
print("One fish, Two fish, Red FISH, blue Fish".count("fish"))

# 16. Build in types
print('01\t012\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234'.expandtabs(4))
print('Py' in 'Python')
print("The sum of 1 + 2 is {0}".format(1 + 2))
print('   spacious   '.lstrip())
print('www.example.com'.lstrip('cmowz.'))
print('1,2,3'.split(','))

# 17. negative indexes
months = ['JAN', 'FEB', 'MARCH', 'APRIL', 'MARCH', 'JUN', 'JUL']
print(months[-1])

# 18. slices of indexes
q3 = months[3:5]
print(q3)

first_half = months[:3]
print(first_half)

second_half = months[3:]
print(second_half)

# 19. membership operators
print('isa' in 'this is a string')
print(5 not in [1, 2, 3, 4, 6])

# 20. Month days
month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month
num_days = days_in_month[7]

print(num_days)

# 21. Print last 3
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

print(eclipse_dates[-3:])

# 22. Max in a string prints last event after being ordinated alphabetical.
variables = {'a', 'b', 's', 'w', 'e', 'i'}
print(max(variables))

# 23. Join
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["García", "O'Kelly"])
print(name)

# 24. Append
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

# 25. Tuples
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

# 26. Sets remove duplicates
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

# 27. Dictionaries
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print(elements)
print("carbon" in elements)  # check if carbon is in elements
print(elements.get("dilithium"))  # get value of dilithium from elements
