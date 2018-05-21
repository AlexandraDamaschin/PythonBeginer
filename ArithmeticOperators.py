# sum numbers
print((23 + 32 + 64) / 3)

# order is important
print((17 * 6) - ((9 * 7) + (5 * 7)))

# variables name need to contain _
mv_population = 12345
mv_area = 11.23
mv_density = mv_population / mv_area
print(mv_density)

# decrease by 10%
mv_population *= 0.9

# decrease by 5%
mv_population *= 0.95

# print type of inputted value
print(type(4.0))

# convert int to float
print(int(2.3))

# boolean example
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population / sf_area
rio_de_janeiro_pop_density = rio_population / rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
