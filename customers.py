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
