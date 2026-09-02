
class Companion:
    def __init__(self, name, evol_type, power):
        self.name = name
        self.evol_type = evol_type
        self.power = int(power)

    def __str__(self):
        return "Name: %-8s | Evol: %-8s | Power Level: %d" % (
            self.name, self.evol_type, self.power
        )

def main():
    print("=== Deepspace Hunter Database ===")
    database = {
        "Xavier": Companion("Xavier", "Light", 4200),
        "Zyane": Companion("Zyane", "Ice", 4500)
    }

    while True:
        print("\nMenu: [1] View All  [2] Add  [3] Search  [4] Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            for companion in database.values():
                print(companion)

        elif choice == "2":
            name = input("Enter Companion Name: ")
            evol = input("Enter Evol Type (Fire/Light/etc.): ")
            power = input("Enter Power Level: ")

            database[name] = Companion(name, evol, power)
            print("Successfully added %s!" % name)

        elif choice == "3":
            search_name = input("Enter Name to search: ")
            if search_name in database:
                print("Found: %s" % database[search_name])
            else:
                print("No record found for '%s'." % search_name)

        elif choice == "4":
            print("Logging off. Good luck on your hunts!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
