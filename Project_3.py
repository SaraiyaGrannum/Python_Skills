
def calc_item_total(price, quantity):
    return price * quantity


def calc_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)


def print_receipt(items, prices, quantities, tax_rate):
    print("\n--- RECEIPT ---")
    subtotal = 0.0
    for i in range(len(items)):
        item_total = calc_item_total(prices[i], quantities[i])
        subtotal += item_total
        print(f"{items[i]} (x{quantities[i]}): ${item_total:.2f}")

    tax = calc_tax(subtotal, tax_rate)
    total = subtotal + tax
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate}%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

def main():
        tax_rate = float(input("Enter tax rate (%): "))
        items, prices, quantities = [], [], []
        more_items = "y"
        while more_items.lower() == "y":
            items.append(input("Item name: "))
            prices.append(float(input("Item price: $")))
            quantities.append(int(input("Item quantity: ")))
            more_items = input("Add another item? (y/n): ")
        print_receipt(items, prices, quantities, tax_rate)

if __name__ == "__main__":
    main()