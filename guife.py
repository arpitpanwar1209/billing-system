import tkinter as tk
from tkinter import messagebox

# Products with prices
products = {
    "Apple": 30,
    "Banana": 10,
    "Milk": 50,
    "Bread": 40,
    "Eggs": 60,
    "Rice": 70
}

cart = {}
discount_applied = False

def update_cart():
    cart_display.delete("1.0", tk.END)
    total = 0
    for item, qty in cart.items():
        price = products[item]
        item_total = price * qty
        cart_display.insert(tk.END, f"{item} x {qty} = ₹{item_total}\n")
        total += item_total
    
    if discount_applied:
        discount = int(total * 0.10)
        total -= discount
        cart_display.insert(tk.END, f"\n🎉 Promo Applied: -₹{discount}")
    
    total_label.config(text=f"Total: ₹{total}")

def add_to_cart():
    product = product_var.get()
    qty = quantity_entry.get()

    if not product:
        messagebox.showerror("Error", "Please select a product.")
        return

    try:
        quantity = int(qty)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter valid quantity.")
        return

    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

    quantity_entry.delete(0, tk.END)
    update_cart()
    messagebox.showinfo("Added", f"{quantity} x {product} added to cart.")

def remove_from_cart():
    product = product_var.get()

    if product not in cart:
        messagebox.showerror("Error", f"{product} not in cart.")
        return

    try:
        quantity = int(quantity_entry.get())
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter valid quantity.")
        return

    if quantity >= cart[product]:
        del cart[product]
        messagebox.showinfo("Removed", f"All {product} removed from cart.")
    else:
        cart[product] -= quantity
        messagebox.showinfo("Removed", f"{quantity} x {product} removed from cart.")

    quantity_entry.delete(0, tk.END)
    update_cart()

def clear_cart():
    global discount_applied
    cart.clear()
    discount_applied = False
    update_cart()
    messagebox.showinfo("Cleared", "Cart has been cleared.")

def apply_promo():
    global discount_applied
    code = promo_entry.get().strip().lower()
    if code == "save10":
        if discount_applied:
            messagebox.showinfo("Already Applied", "Promo code already used.")
        else:
            discount_applied = True
            update_cart()
            messagebox.showinfo("Success", "10% discount applied!")
    else:
        messagebox.showerror("Invalid", "Invalid promo code.")

# GUI
root = tk.Tk()
root.title("🛒 Full Billing System")
root.geometry("430x600")
root.config(bg="#f8f8f8")

tk.Label(root, text="🧾 Billing System", font=("Arial", 16, "bold"), bg="#f8f8f8").pack(pady=10)

# Product Selection
tk.Label(root, text="Select Product:", bg="#f8f8f8").pack()
product_var = tk.StringVar(value="Apple")
product_menu = tk.OptionMenu(root, product_var, *products.keys())
product_menu.pack()

# Quantity Entry
tk.Label(root, text="Quantity:", bg="#f8f8f8").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Add/Remove Buttons
tk.Button(root, text="Add to Cart", command=add_to_cart, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Remove from Cart", command=remove_from_cart, bg="#f44336", fg="white").pack(pady=5)
tk.Button(root, text="Clear Cart", command=clear_cart, bg="#9E9E9E", fg="white").pack(pady=5)

# Cart Display
tk.Label(root, text="Cart:", bg="#f8f8f8").pack()
cart_display = tk.Text(root, height=10, width=40)
cart_display.pack()

# Promo Code
tk.Label(root, text="Promo Code:", bg="#f8f8f8").pack()
promo_entry = tk.Entry(root)
promo_entry.pack()
tk.Button(root, text="Apply Promo", command=apply_promo, bg="#2196F3", fg="white").pack(pady=5)

# Total Label
total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 14, "bold"), bg="#f8f8f8")
total_label.pack(pady=10)

update_cart()

root.mainloop()
