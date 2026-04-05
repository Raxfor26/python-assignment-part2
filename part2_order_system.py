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



#Task 1


# (Assuming the 'menu' dictionary is already defined at the top of your script)

# --- Part 1: Print Menu Grouped by Category ---

# Dynamically extract all unique categories from the menu
# Using a set ensures we don't get duplicates
categories = []
for details in menu.values():
    if details["category"] not in categories:
        categories.append(details["category"])

# You could also hardcode categories = ["Starters", "Mains", "Desserts"] 
# to enforce a specific order, but dynamic extraction is safer for future updates.

for category in categories:
    print(f"===== {category} =====")
    for item_name, details in menu.items():
        if details["category"] == category:
            # Determine the string for availability
            status = "Available" if details["available"] else "Unavailable"
            
            # Format: Left-align name (16 chars), format price to 2 decimals
            print(f"{item_name:<16} ₹{details['price']:>6.2f}   [{status}]")
    print() # Add a blank line between categories for readability


# --- Part 2: Compute and Print Statistics ---

# Total number of items
total_items = len(menu)

# Total number of available items
# We loop through just the values() since we don't need the item names for this count
available_items = sum(1 for details in menu.values() if details["available"])

# Find the most expensive item
highest_price = 0
expensive_item = ""

for item_name, details in menu.items():
    if details["price"] > highest_price:
        highest_price = details["price"]
        expensive_item = item_name

# Find all items under ₹150
cheap_items = []
for item_name, details in menu.items():
    if details["price"] < 150:
        cheap_items.append((item_name, details["price"]))

# Print the final statistics
print("--- Menu Statistics ---")
print(f"Total menu items: {total_items}")
print(f"Available items: {available_items}")
print(f"Most expensive item: {expensive_item} (₹{highest_price:.2f})")
print("Items priced under ₹150:")
for item, price in cheap_items:
    print(f"  - {item} (₹{price:.2f})")



#Task 2

# Starting with an empty cart as requested
cart = []

# --- 1. Cart Logic Functions ---

def add_to_cart(item_name, qty):
    # Check if item exists in menu
    if item_name not in menu:
        print(f"❌ Failed: '{item_name}' does not exist on the menu.")
        return
    
    # Check if item is available
    if not menu[item_name]["available"]:
        print(f"❌ Failed: '{item_name}' is currently unavailable.")
        return
    
    # Check if item is already in the cart to update quantity
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            print(f"✓ Updated '{item_name}' quantity to {entry['quantity']}")
            return
            
    # If we reach here, it's a valid new item. Add it to the cart list.
    cart.append({
        "item": item_name, 
        "quantity": qty, 
        "price": menu[item_name]["price"]
    })
    print(f"✓ Added {qty}x '{item_name}' to the cart.")


def remove_from_cart(item_name):
    # Enumerate allows us to get the index (i) to delete the item securely
    for i, entry in enumerate(cart):
        if entry["item"] == item_name:
            del cart[i]
            print(f"🗑️ Removed '{item_name}' completely from the cart.")
            return
            
    print(f"⚠️ Warning: '{item_name}' is not in the cart to remove.")


def update_quantity(item_name, new_qty):
    for entry in cart:
        if entry["item"] == item_name:
            if new_qty <= 0:
                remove_from_cart(item_name) # If qty is 0, just remove it entirely
            else:
                entry["quantity"] = new_qty
                print(f"🔄 Quantity for '{item_name}' set to {new_qty}.")
            return
            
    print(f"⚠️ Warning: '{item_name}' is not in the cart to update.")


# --- 2. The Simulation Sequence ---
print("\n--- Simulation Steps ---")

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


# --- 3. Order Summary Generation ---
print("\n========== Order Summary ==========")
subtotal = 0

for entry in cart:
    # Calculate the total price for this specific line item
    line_total = entry["quantity"] * entry["price"]
    subtotal += line_total
    
    # Format: left-align name(18 chars), left-align qty(4 chars), right-align price
    print(f"{entry['item']:<18} x{entry['quantity']:<4} ₹{line_total:>7.2f}")

print("-" * 36)

# Calculate taxes
gst = subtotal * 0.05
total_payable = subtotal + gst

print(f"{'Subtotal:':<25} ₹{subtotal:>7.2f}")
print(f"{'GST (5%):':<25} ₹{gst:>7.2f}")
print(f"{'Total Payable:':<25} ₹{total_payable:>7.2f}")
print("====================================")




#Task 3

import copy

# (Assuming 'inventory' is defined from the provided data)
# Recreating the final cart from Task 2 for this simulation
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# --- 1. The Deep Copy & Demonstration ---
print("--- Deep Copy Test ---")
inventory_backup = copy.deepcopy(inventory)

# Manually change a value in the active inventory to prove they are separate
inventory["Paneer Tikka"]["stock"] = 999

print(f"Modified Active Inventory (Paneer Tikka): {inventory['Paneer Tikka']['stock']}")
print(f"Untouched Backup Inventory (Paneer Tikka): {inventory_backup['Paneer Tikka']['stock']}")

# Restore the inventory to its original state using the backup before proceeding
inventory = copy.deepcopy(inventory_backup)
print("✓ Inventory restored to original state.\n")


# --- 2. Order Fulfillment Simulation ---
print("--- Fulfilling Order ---")
for entry in cart:
    item_name = entry["item"]
    qty_ordered = entry["quantity"]
    
    # Check if the item is in the inventory
    if item_name in inventory:
        current_stock = inventory[item_name]["stock"]
        
        # Check if we have enough stock
        if current_stock >= qty_ordered:
            inventory[item_name]["stock"] -= qty_ordered
            print(f"✓ Deducted {qty_ordered}x '{item_name}'. Remaining stock: {inventory[item_name]['stock']}")
        else:
            # Insufficient stock logic
            print(f"⚠️ Warning: Insufficient stock for '{item_name}'. Ordered {qty_ordered}, but only {current_stock} available.")
            print(f"   Deducting remaining {current_stock} units.")
            inventory[item_name]["stock"] = 0


# --- 3. Reorder Alerts ---
print("\n--- Inventory Alerts ---")
alerts_triggered = False

for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")
        alerts_triggered = True

# (Note: Based on the Task 2 cart, Paneer Tikka drops to 7, which is > 3, so you 
# may not see an alert naturally. This acts as a fallback message.)
if not alerts_triggered:
    print("✓ All items are currently above their reorder levels.")


# --- 4. Deep Copy Proof (Final State) ---
print("\n--- Deep Copy Proof (Final State) ---")
# Printing just a few relevant items to keep the output clean, rather than the whole dictionary
print("Active Inventory (Paneer Tikka):", inventory["Paneer Tikka"])
print("Backup Inventory (Paneer Tikka):", inventory_backup["Paneer Tikka"])




#Task 4


# --- 1. Reusable Function for Revenue Stats ---
def print_revenue_stats(log_data):
    highest_revenue = 0
    best_day = ""
    
    print("Revenue Per Day:")
    for date, orders in log_data.items():
        # Calculate the sum of all 'total' values in the day's orders
        daily_total = sum(order["total"] for order in orders)
        print(f"  {date}: ₹{daily_total:.2f}")
        
        # Track the best day
        if daily_total > highest_revenue:
            highest_revenue = daily_total
            best_day = date
            
    print(f"\nBest-Selling Day: {best_day} (₹{highest_revenue:.2f})\n")

print("--- Initial Sales Data ---")
print_revenue_stats(sales_log)


# --- 2. Find the Most Ordered Item ---
item_counts = {}

# Loop through every day, then every order, then every item
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            # .get() safely adds 1, defaulting to 0 if the item isn't in the dict yet
            item_counts[item] = item_counts.get(item, 0) + 1

# Find the item with the highest count
most_ordered_item = max(item_counts, key=item_counts.get)
print(f"Most Ordered Item: {most_ordered_item} ({item_counts[most_ordered_item]} occurrences)\n")


# --- 3. Add New Day and Reprint ---
print("--- Adding Data for 2025-01-05 ---\n")
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("--- Updated Sales Data ---")
print_revenue_stats(sales_log)


# --- 4. Numbered List Using Enumerate ---
print("--- All Orders (Numbered List) ---")

# First, we flatten the dictionary into a single list of tuples: (date, order_dictionary)
# This allows us to use enumerate() cleanly across the entire dataset
flat_orders = []
for date, orders in sales_log.items():
    for order in orders:
        flat_orders.append((date, order))

# Now we use enumerate, starting the count at 1
for i, (date, order) in enumerate(flat_orders, start=1):
    # .join() elegantly turns the list of items into a comma-separated string
    items_joined = ", ".join(order["items"])
    
    print(f"{i}.  [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items_joined}")


#Output
"""
===== Starters =====
Paneer Tikka     ₹180.00   [Available]
Chicken Wings    ₹220.00   [Unavailable]
Veg Soup         ₹120.00   [Available]

===== Mains =====
Butter Chicken   ₹320.00   [Available]
Dal Tadka        ₹180.00   [Available]
Veg Biryani      ₹250.00   [Available]
Garlic Naan      ₹ 40.00   [Available]

===== Desserts =====
Gulab Jamun      ₹ 90.00   [Available]
Rasgulla         ₹ 80.00   [Available]
Ice Cream        ₹110.00   [Unavailable]

--- Menu Statistics ---
Total menu items: 10
Available items: 8
Most expensive item: Butter Chicken (₹320.00)
Items priced under ₹150:
  - Veg Soup (₹120.00)
  - Garlic Naan (₹40.00)
  - Gulab Jamun (₹90.00)
  - Rasgulla (₹80.00)
  - Ice Cream (₹110.00)

--- Simulation Steps ---
✓ Added 2x 'Paneer Tikka' to the cart.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}]

✓ Added 1x 'Gulab Jamun' to the cart.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

✓ Updated 'Paneer Tikka' quantity to 3
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

❌ Failed: 'Mystery Burger' does not exist on the menu.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

❌ Failed: 'Chicken Wings' is currently unavailable.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}, {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}]

🗑️ Removed 'Gulab Jamun' completely from the cart.
Current Cart: [{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}]


========== Order Summary ==========
Paneer Tikka       x3    ₹ 540.00
------------------------------------
Subtotal:                 ₹ 540.00
GST (5%):                 ₹  27.00
Total Payable:            ₹ 567.00
====================================
--- Deep Copy Test ---
Modified Active Inventory (Paneer Tikka): 999
Untouched Backup Inventory (Paneer Tikka): 10
✓ Inventory restored to original state.

--- Fulfilling Order ---
✓ Deducted 3x 'Paneer Tikka'. Remaining stock: 7

--- Inventory Alerts ---
✓ All items are currently above their reorder levels.

--- Deep Copy Proof (Final State) ---
Active Inventory (Paneer Tikka): {'stock': 7, 'reorder_level': 3}
Backup Inventory (Paneer Tikka): {'stock': 10, 'reorder_level': 3}
--- Initial Sales Data ---
Revenue Per Day:
  2025-01-01: ₹790.00
  2025-01-02: ₹560.00
  2025-01-03: ₹960.00
  2025-01-04: ₹570.00

Best-Selling Day: 2025-01-03 (₹960.00)

Most Ordered Item: Garlic Naan (5 occurrences)

--- Adding Data for 2025-01-05 ---

--- Updated Sales Data ---
Revenue Per Day:
  2025-01-01: ₹790.00
  2025-01-02: ₹560.00
  2025-01-03: ₹960.00
  2025-01-04: ₹570.00
  2025-01-05: ₹750.00

Best-Selling Day: 2025-01-03 (₹960.00)

--- All Orders (Numbered List) ---
1.  [2025-01-01] Order #1  — ₹220.00 — Items: Paneer Tikka, Garlic Naan
2.  [2025-01-01] Order #2  — ₹210.00 — Items: Gulab Jamun, Veg Soup
3.  [2025-01-01] Order #3  — ₹360.00 — Items: Butter Chicken, Garlic Naan
4.  [2025-01-02] Order #4  — ₹220.00 — Items: Dal Tadka, Garlic Naan
5.  [2025-01-02] Order #5  — ₹340.00 — Items: Veg Biryani, Gulab Jamun
6.  [2025-01-03] Order #6  — ₹260.00 — Items: Paneer Tikka, Rasgulla
7.  [2025-01-03] Order #7  — ₹570.00 — Items: Butter Chicken, Veg Biryani
8.  [2025-01-03] Order #8  — ₹130.00 — Items: Garlic Naan, Gulab Jamun
9.  [2025-01-04] Order #9  — ₹300.00 — Items: Dal Tadka, Garlic Naan, Rasgulla
10.  [2025-01-04] Order #10  — ₹270.00 — Items: Paneer Tikka, Gulab Jamun
11.  [2025-01-05] Order #11  — ₹490.00 — Items: Butter Chicken, Gulab Jamun, Garlic Naan
12.  [2025-01-05] Order #12  — ₹260.00 — Items: Paneer Tikka, Rasgulla"""    