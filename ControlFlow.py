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
