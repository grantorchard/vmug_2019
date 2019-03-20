ages = {
    "Grant": 40,
    "Elizabeth": None,
    "Audrey": 8,
    "Ewan": 4,
    "Cody": 1
}

print(ages.keys())
print(ages.values())
print(ages.items())

for k, v in ages.items():
    if k == "Grant":
        print(v)
