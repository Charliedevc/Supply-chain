# Supply Chain Inventory & Order Tracker
# This program manages product inventory, updates stock levels,
# alerts for low stock, and generates reports.

# Initialize the inventory dictionary to store products
inventory = {}

def add_product(id, name, stock, reorder_level):
    """
    Add a new product to the inventory with given stock and reorder level.
    Parameters:
    id (int): Unique product identifier
    name (str): Product name
    stock (int): Initial stock quantity
    reorder_level (int): Stock level to trigger reorder alert
    """
    inventory[id] = {
        'name': name,
        'stock': stock,
        'reorder_level': reorder_level
    }
    print(f"Product {name} added with stock {stock} and reorder level {reorder_level}.")

def update_stock(id, quantity_change):
    """
    Update stock quantity for an existing product.
    Positive quantity_change adds stock, negative reduces stock.
    If stock falls below reorder level, alerts user.
    """
    if id in inventory:
        inventory[id]['stock'] += quantity_change
        print(f"Updated stock for {inventory[id]['name']}: {inventory[id]['stock']} units.")
        # Check if stock is below reorder level and alert
        if inventory[id]['stock'] < inventory[id]['reorder_level']:
            print(f"ALERT: Stock low for product '{inventory[id]['name']}'! Reorder needed.")
    else:
        print("Product not found in inventory.")

def print_inventory_report():
    """
    Prints a summary report of all products with current stock levels,
    indicating if reorder is needed.
    """
    print("\nInventory Report:")
    print("-----------------")
    for id, product in inventory.items():
        status = "OK"
        if product['stock'] < product['reorder_level']:
            status = "REORDER NEEDED"
        print(f"ID: {id} | Name: {product['name']} | Stock: {product['stock']} | Status: {status}")

def main():
    """
    Main loop providing a menu-driven interface to interact with inventory.
    User can add products, update stock, view reports, or exit.
    """
    while True:
        print("\nMenu:")
        print("1. Add product")
        print("2. Update stock")
        print("3. Print inventory report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                stock = int(input("Enter initial stock quantity: "))
                reorder = int(input("Enter reorder level: "))
                add_product(id, name, stock, reorder)
            except ValueError:
                print("Invalid input. Please enter numeric values for ID, stock, and reorder level.")
        elif choice == '2':
            try:
                id = int(input("Enter product ID to update: "))
                qty = int(input("Enter quantity to add/remove (use negative for removal): "))
                update_stock(id, qty)
            except ValueError:
                print("Invalid input. Please enter numeric values for ID and quantity.")
        elif choice == '3':
            print_inventory_report()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# If this script is run directly, start the main program loop
if __name__ == "__main__":
    main()
