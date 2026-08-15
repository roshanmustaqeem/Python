menu = {
    "whey protein": 2499,
    "creatine": 899,
    "Peanut Butter": 350,
    "Oats": 120,
    "Protein Bar": 150
}

for k, v in menu.items():
    print(f"{k} : {v}")

print("--menu--")

order = []
total = 0

while True:
    cart = input("enter your order (q to quit): ").lower()

    if cart == "q":
        break
    elif menu.get(cart) is not None:
        order.append(cart)

print("--your order--")

for cart in order:
    print(cart, end=" ")
    total = total + menu.get(cart)

print()
print(f"total is $: {total}")