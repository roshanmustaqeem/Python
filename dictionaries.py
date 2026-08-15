cars = {
    "name": "lamborghini",
    "model": "2025",
    "prices": ["251", "301", "45"]
}

ke = cars.keys()

for k in ke:
    print(k)

ke = cars.values()

for k in ke:
    print(k)

print(cars.get("name"))

ke = cars.items()

for k, v in ke:
    print(f"{k}: {v}")