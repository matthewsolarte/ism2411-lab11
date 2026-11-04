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


# Exercise 5: Lookup table
print("\n=== Exercise 5 ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
discount = tier_discounts.get(customer["tier"], 0)
purchase = 200
final_price = purchase * (1 - discount)
print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of dicts
print("\n=== Exercise 6 ===")
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 1250.00},
    {"name": "Brian", "tier": "silver", "ytd_spend": 480.00},
    {"name": "Carla", "tier": "bronze", "ytd_spend": 95.00},
]
purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount on ${purchase}: ${discount_amount:.2f}")


# Exercise 7: Nested catalog
print("\n=== Exercise 7 ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")
