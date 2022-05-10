# Josh Thiessen
def get_retail_item_description():
    """Return the return item description from the user"""
    desc = input("enter retail item description:")
    return desc


def get_number_of_items_purchased():
    """ Returns the number of items purchased from the user"""
    num_items = input("enter quantity purchased:")
    return int(num_items)


def get_price_per_unit():
    """ Returns the price of the unit purchased"""
    price_per_unit = float(input("enter price per unit"))
    return price_per_unit


def get_tax_rate():
    """ Returns the tax rate entered by the user"""
    tax_rate = float(input("enter tax: "))
    return tax_rate


def calculate_subtotal(price, quantity):
    """ Returns the subtotal amount"""
    subtotal = price * quantity
    return subtotal


def calculate_tax(subtotal, tax):
    """ Returns the calculated tax on the purchase"""
    tax_amount = subtotal * tax
    return tax_amount


def calculate_total(subtotal, tax):
    """ Returns the total purchase price"""
    return subtotal + tax


def main():
    item_description = get_retail_item_description()
    num_items = get_number_of_items_purchased()
    price_per_unit = get_price_per_unit()
    tax_rate = get_tax_rate()

    print("Sales Receipt:")
    print("Item Description", item_description)
    print("Number of Purchased Items:", num_items)
    print("Unit Price:", price_per_unit)
    print("Tax Rate:", tax_rate)

    subtotal = calculate_subtotal(price_per_unit, num_items)
    print("Subtotal:", subtotal)

    tax = calculate_tax(subtotal, tax_rate)
    print("Tax:", tax)

    total = calculate_total(subtotal, tax)
    print("Total:", total)


if __name__ == "__main__":
    main()
