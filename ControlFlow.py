# 1. IF condition
phone_balance = 3
bank_balance = 100

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

# 2. IF ELIF ELSE
season = "summer"
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

# 3. Odd and Even numbers
number = 146
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

# 4. Bus ride cost
age = 12
# ages types
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
# set the bus fares
concession_ticket = 1.25
adult_ticket = 2.50
# ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

# 5. Prizes
points = 174
if points <= 50:
    result = "wooden rabbit"
    print("Congratulations! You won a " + result)
elif points <= 150:
    result = "no prize"
    print("Congratulations! You won a " + result)
elif points <= 180:
    result = "wafer-thin mint"
    print("Congratulations! You won a " + result)
elif points <= 200:
    result = "penguin"
    print("Congratulations! You won a " + result)
else:
    print("Oh dear, no prize this time. ")

# 6. Guess the number
answer = 12
guess = 23
# logic implemented
if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"
print(result)

# 7. States taxes
state = "CA"
purchase_amount = 100

if state == "CA":
    tax_amount = .075
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY":
    tax_amount = .089
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

# 8. Air traffic control program
altitude = 10000
speed = 250
propulsion = "Propeller"

print(altitude < 1000 and speed > 100)
print((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000)
print(not (speed > 400 and propulsion == "Propeller"))
print((altitude > 500 and speed > 100) or not propulsion == "Propeller")

# 9. Prizes
points = 174
prize = None

if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)

# 10. For loops
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

# 11. Range
for i in range(3):
    print("Hello!")

# 12. modify a list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    print(capitalized_cities)

# 13. Replace " " with "_"
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)

# 14.Modify usernames with Range
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)

# 15. Count in a list
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)

# 16. Iterating through html items
items = ['first string', 'second string']
html_str = "<ul>\n"

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

# 17. Iterating Through Dictionaries with For Loops
cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# 18. Count by iterating through the list
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))

# 19. Fruit or not fruit
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} items that are not fruits.".format(fruit_count, not_fruit_count))

# 20. While loops
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())
    print(hand)

# 21. Print characters diveided
print_str = "Water falls"
i = 0
while i < len(print_str):
    print(print_str[i])
    i = i + 1

# 22. Factorials with While Loops
number = 6
factorial = 1
while number > 1:
    factorial = factorial * number
    number = number - 1
print(factorial)

# 23. Factorials with For Loops
for i in range(1, number + 1):
    factorial = factorial * i
print(factorial)

# 24. Count by
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)

# 25. Count by check
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops!  Looks like your start value is greater than the end value.  Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num
print(result)

# 26.Nearest Square
limit = 40
num = 0
while (num + 1) ** 2 < limit:
    num += 1
nearest_square = num ** 2
print(nearest_square)

# 27. METHOD 1
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
# breaks from the loop when weight reaches or exceeds limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# 28.METHOD 2
# skips an iteration when adding an item would make weight exceed limit
# breaks from the loop if weight reaches exactly the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# 29. Break the string
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

# 30. Zip
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# 31. Enumerate
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
