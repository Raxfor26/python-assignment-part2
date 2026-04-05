menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# Task 1

# first collect all the unique categories from the menu
categories = []
for details in menu.values():
    if details["category"] not in categories:
        categories.append(details["category"])

# print each category and the items under it
for category in categories:
    print("===== " + category + " =====")
    for item_name in menu:
        details = menu[item_name]
        if details["category"] == category:
            if details["available"] == True:
                status = "Available"
            else:
                status = "Unavailable"
            print(f"{item_name:<16} Rs.{details['price']:>6.2f}   [{status}]")
    print("")

# count total items in menu
total_items = len(menu)

# count how many items are available
available_count = 0
for item_name in menu:
    if menu[item_name]["available"] == True:
        available_count = available_count + 1

# find the most expensive item
highest_price = 0
expensive_item = ""
for item_name in menu:
    if menu[item_name]["price"] > highest_price:
        highest_price = menu[item_name]["price"]
        expensive_item = item_name

# find all items under 150
cheap_items = []
for item_name in menu:
    if menu[item_name]["price"] < 150:
        cheap_items.append((item_name, menu[item_name]["price"]))

print("--- Menu Statistics ---")
print("Total menu items: " + str(total_items))
print("Available items: " + str(available_count))
print("Most expensive item: " + expensive_item + " (Rs." + str(highest_price) + ")")
print("Items priced under Rs.150:")
for item, price in cheap_items:
    print("  - " + item + " (Rs." + str(price) + ")")




# Task 2

cart = []

def add_to_cart(item_name, qty):
    # check if the item is even on the menu
    if item_name not in menu:
        print("Failed: " + item_name + " does not exist on the menu.")
        return

    # check if the item is available right now
    if menu[item_name]["available"] == False:
        print("Failed: " + item_name + " is currently unavailable.")
        return

    # check if the item is already in the cart
    # if yes just increase the quantity
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = entry["quantity"] + qty
            print("Updated " + item_name + " quantity to " + str(entry["quantity"]))
            return

    # if we get here the item is new so add it
    new_entry = {
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    }
    cart.append(new_entry)
    print("Added " + str(qty) + "x " + item_name + " to the cart.")


def remove_from_cart(item_name):
    # find the item in the cart by going through each entry
    index_to_remove = -1
    for i in range(len(cart)):
        if cart[i]["item"] == item_name:
            index_to_remove = i
            break

    if index_to_remove == -1:
        print("Warning: " + item_name + " is not in the cart.")
    else:
        del cart[index_to_remove]
        print("Removed " + item_name + " from the cart.")


def update_quantity(item_name, new_qty):
    for entry in cart:
        if entry["item"] == item_name:
            if new_qty <= 0:
                # if new qty is 0 or less just remove it
                remove_from_cart(item_name)
            else:
                entry["quantity"] = new_qty
                print("Quantity for " + item_name + " set to " + str(new_qty))
            return

    print("Warning: " + item_name + " is not in the cart.")


print("")
print("--- Simulation Steps ---")

add_to_cart("Paneer Tikka", 2)
print("Current Cart:", cart, "\n")

add_to_cart("Gulab Jamun", 1)
print("Current Cart:", cart, "\n")

add_to_cart("Paneer Tikka", 1)
print("Current Cart:", cart, "\n")

add_to_cart("Mystery Burger", 1)
print("Current Cart:", cart, "\n")

add_to_cart("Chicken Wings", 1)
print("Current Cart:", cart, "\n")

remove_from_cart("Gulab Jamun")
print("Current Cart:", cart, "\n")

# print the order summary
print("")
print("========== Order Summary ==========")

subtotal = 0
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    subtotal = subtotal + line_total
    print(f"{entry['item']:<18} x{entry['quantity']:<4} Rs.{line_total:>7.2f}")

print("-" * 36)

gst = subtotal * 0.05
total_payable = subtotal + gst

print(f"{'Subtotal:':<25} Rs.{subtotal:>7.2f}")
print(f"{'GST (5%):':<25} Rs.{gst:>7.2f}")
print(f"{'Total Payable:':<25} Rs.{total_payable:>7.2f}")
print("====================================")




# Task 3

import copy

# use the cart from task 2 result
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# make a deep copy of inventory so we have a backup
print("--- Deep Copy Test ---")
inventory_backup = copy.deepcopy(inventory)

# change a value to prove the backup is separate
inventory["Paneer Tikka"]["stock"] = 999

print("Modified Active Inventory (Paneer Tikka): " + str(inventory["Paneer Tikka"]["stock"]))
print("Untouched Backup Inventory (Paneer Tikka): " + str(inventory_backup["Paneer Tikka"]["stock"]))

# restore inventory from backup
inventory = copy.deepcopy(inventory_backup)
print("Inventory restored to original state.")
print("")

# now fulfill the order by deducting from inventory
print("--- Fulfilling Order ---")
for entry in cart:
    item_name = entry["item"]
    qty_ordered = entry["quantity"]

    if item_name in inventory:
        current_stock = inventory[item_name]["stock"]

        if current_stock >= qty_ordered:
            inventory[item_name]["stock"] = inventory[item_name]["stock"] - qty_ordered
            print("Deducted " + str(qty_ordered) + "x " + item_name + ". Remaining stock: " + str(inventory[item_name]["stock"]))
        else:
            # not enough stock, deduct whatever is left
            print("Warning: Not enough stock for " + item_name + ". Ordered " + str(qty_ordered) + " but only " + str(current_stock) + " available.")
            print("Deducting remaining " + str(current_stock) + " units.")
            inventory[item_name]["stock"] = 0

# check if any item has gone below its reorder level
print("")
print("--- Inventory Alerts ---")
found_alert = False
for item_name in inventory:
    stock = inventory[item_name]["stock"]
    reorder = inventory[item_name]["reorder_level"]
    if stock <= reorder:
        print("Reorder Alert: " + item_name + " - Only " + str(stock) + " unit(s) left (reorder level: " + str(reorder) + ")")
        found_alert = True

if found_alert == False:
    print("All items are currently above their reorder levels.")

print("")
print("--- Deep Copy Proof (Final State) ---")
print("Active Inventory (Paneer Tikka):", inventory["Paneer Tikka"])
print("Backup Inventory (Paneer Tikka):", inventory_backup["Paneer Tikka"])




# Task 4

# a function to print revenue stats for any sales log we pass in
def print_revenue_stats(log_data):
    highest_revenue = 0
    best_day = ""

    print("Revenue Per Day:")
    for date in log_data:
        orders = log_data[date]

        # add up all the totals for this day
        daily_total = 0
        for order in orders:
            daily_total = daily_total + order["total"]

        print("  " + date + ": Rs." + str(daily_total))

        if daily_total > highest_revenue:
            highest_revenue = daily_total
            best_day = date

    print("")
    print("Best-Selling Day: " + best_day + " (Rs." + str(highest_revenue) + ")")
    print("")


print("--- Initial Sales Data ---")
print_revenue_stats(sales_log)

# count how many times each item appears across all orders
item_counts = {}

for date in sales_log:
    orders = sales_log[date]
    for order in orders:
        for item in order["items"]:
            if item in item_counts:
                item_counts[item] = item_counts[item] + 1
            else:
                item_counts[item] = 1

# find the item with the highest count
most_ordered = ""
highest_count = 0
for item_name in item_counts:
    if item_counts[item_name] > highest_count:
        highest_count = item_counts[item_name]
        most_ordered = item_name

print("Most Ordered Item: " + most_ordered + " (" + str(highest_count) + " occurrences)")
print("")

# add a new day to the sales log
print("--- Adding Data for 2025-01-05 ---")
print("")
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("--- Updated Sales Data ---")
print_revenue_stats(sales_log)

# print all orders with a number in front
print("--- All Orders (Numbered List) ---")

# first flatten everything into one big list
all_orders = []
for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

# now print each one with a number
number = 1
for date, order in all_orders:
    items_joined = ""
    for i in range(len(order["items"])):
        if i == 0:
            items_joined = order["items"][i]
        else:
            items_joined = items_joined + ", " + order["items"][i]

    print(str(number) + ".  [" + date + "] Order #" + str(order["order_id"]) + "  - Rs." + str(order["total"]) + " - Items: " + items_joined)
    number = number + 1






#Output

"""
===== Starters =====
Paneer Tikka     Rs.180.00   [Available]
Chicken Wings    Rs.220.00   [Unavailable]
Veg Soup         Rs.120.00   [Available]

===== Mains =====
Butter Chicken   Rs.320.00   [Available]
Dal Tadka        Rs.180.00   [Available]
Veg Biryani      Rs.250.00   [Available]
Garlic Naan      Rs. 40.00   [Available]

===== Desserts =====
Gulab Jamun      Rs. 90.00   [Available]
Rasgulla         Rs. 80.00   [Available]
Ice Cream        Rs.110.00   [Unavailable]

--- Menu Statistics ---
Total menu items: 10
Available items: 8
Most expensive item: Butter Chicken (Rs.320.0)
Items priced under Rs.150:
  - Veg Soup (Rs.120.0)
  - Garlic Naan (Rs.40.0)
  - Gulab Jamun (Rs.90.0)
  - Rasgulla (Rs.80.0)
  - Ice Cream (Rs.110.0)

--- Simulation Steps ---
Added 2x Paneer Tikka to the cart.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}]

Added 1x Gulab Jamun to the cart.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

Updated Paneer Tikka quantity to 3
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

Failed: Mystery Burger does not exist on the menu.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

Failed: Chicken Wings is currently unavailable.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

Removed Gulab Jamun from the cart.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}]


========== Order Summary ==========
Paneer Tikka       x3    Rs. 540.00
------------------------------------
Subtotal:                 Rs. 540.00
GST (5%):                 Rs.  27.00
Total Payable:            Rs. 567.00
====================================
--- Deep Copy Test ---
Modified Active Inventory (Paneer Tikka): 999
Untouched Backup Inventory (Paneer Tikka): 10
Inventory restored to original state.

--- Fulfilling Order ---
Deducted 3x Paneer Tikka. Remaining stock: 7

--- Inventory Alerts ---
All items are currently above their reorder levels.

--- Deep Copy Proof (Final State) ---
Active Inventory (Paneer Tikka): {'stock': 7, 'reorder_level': 3}
Backup Inventory (Paneer Tikka): {'stock': 10, 'reorder_level': 3}
--- Initial Sales Data ---
Revenue Per Day:
  2025-01-01: Rs.790.0
  2025-01-02: Rs.560.0
  2025-01-03: Rs.960.0
  2025-01-04: Rs.570.0

Best-Selling Day: 2025-01-03 (Rs.960.0)

Most Ordered Item: Garlic Naan (5 occurrences)

--- Adding Data for 2025-01-05 ---

--- Updated Sales Data ---
Revenue Per Day:
  2025-01-01: Rs.790.0
  2025-01-02: Rs.560.0
  2025-01-03: Rs.960.0
  2025-01-04: Rs.570.0
  2025-01-05: Rs.750.0

Best-Selling Day: 2025-01-03 (Rs.960.0)

--- All Orders (Numbered List) ---
1.  [2025-01-01] Order #1  - Rs.220.0 - Items: Paneer Tikka, Garlic Naan
2.  [2025-01-01] Order #2  - Rs.210.0 - Items: Gulab Jamun, Veg Soup
3.  [2025-01-01] Order #3  - Rs.360.0 - Items: Butter Chicken, Garlic Naan
4.  [2025-01-02] Order #4  - Rs.220.0 - Items: Dal Tadka, Garlic Naan
5.  [2025-01-02] Order #5  - Rs.340.0 - Items: Veg Biryani, Gulab Jamun
6.  [2025-01-03] Order #6  - Rs.260.0 - Items: Paneer Tikka, Rasgulla
7.  [2025-01-03] Order #7  - Rs.570.0 - Items: Butter Chicken, Veg Biryani
8.  [2025-01-03] Order #8  - Rs.130.0 - Items: Garlic Naan, Gulab Jamun
9.  [2025-01-04] Order #9  - Rs.300.0 - Items: Dal Tadka, Garlic Naan, Rasgulla
10.  [2025-01-04] Order #10  - Rs.270.0 - Items: Paneer Tikka, Gulab Jamun
11.  [2025-01-05] Order #11  - Rs.490.0 - Items: Butter Chicken, Gulab Jamun, Garlic Naan
12.  [2025-01-05] Order #12  - Rs.260.0 - Items: Paneer Tikka, Rasgulla"""