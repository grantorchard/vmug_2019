ages = {
    "Grant": 40,
    "Elizabeth": None,
    "Audrey": 8,
    "Ewan": 4
}


def find_age_by_name(name):
    for k, v in ages.items():
        if k == name:
            print(v)
        else:
            print("No-one with that name found.")


def main():
    find_age_by_name("Grant")

if __name__ == '__main__':
    main()
