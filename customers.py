# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Matthew Solarte
#
# Reflection 1:
# I would use .get() when a key might not be there, like an optional field such as
# a phone number or email that some customers never gave us. Bracket notation is
# better when the key has to exist, because if it is missing I want the program to
# fail loudly so I find the bad data. My rule of thumb is .get() for optional data
# and brackets for required data.
#
# Reflection 2:
# Building a summary dictionary with a loop is a lot like a SUMIF or a pivot table in
# Excel, where you total sales by region. The Python version is more useful for large
# datasets because it can handle millions of rows without slowing down or crashing,
# and the same script can be rerun on new data every week without redoing the steps.


# Exercise 1: One customer
print("=== Exercise 1 ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and add
print("\n=== Exercise 2 ===")
customer["phone"] = "813-555-0142"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)


# Exercise 3: Safe lookup
print("\n=== Exercise 3 ===")
email = customer.get("email", "no email on file")
print("Using .get():", email)
try:
    print(customer["email"])
except KeyError as error:
    print("Using brackets raised a KeyError:", error)


# Exercise 4: Iterate
print("\n=== Exercise 4 ===")
for key, value in customer.items():
    print(f"{key}: {value}")

print("Without .items():")
for key in customer:
    print(key)
# Looping over the dict without .items() only gives the keys.
# With .items() you get each key and its value together as a pair,
# so you do not have to look up customer[key] to get the value.
