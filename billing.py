products = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "eggs": 60,
    "rice": 70
}

cart = {}

def show_products():
    print("\n🛒 Available Products:")
    for product, price in products.items():
        print(f" - {product.title()} : ₹{price}")

def add_to_cart():
    product = input("Enter product name to add to cart: ").lower()
    if product in products:
        try:
            quantity = int(input(f"Enter quantity of {product.title()}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
            else:
                if product in cart:
                    cart[product] += quantity
                else:
                    cart[product] = quantity
                print(f"✅ {quantity} x {product.title()} added to cart.")
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print("❌ Product not found. Please try again.")

def show_cart():
    if not cart:
        print("\n🛒 Your cart is empty.")
        return

    print("\n🧾 Your Cart:")
    total = 0
    for item, qty in cart.items():
        price = products[item]
        item_total = price * qty
        print(f" - {item.title()} x {qty} = ₹{item_total}")
        total += item_total
    print(f"\n💰 Total Bill: ₹{total}")

def billing_system():
    while True:
        print("\n========= ONLINE BILLING =========")
        print("1. Show Products")
        print("2. Add Product to Cart")
        print("3. Show Cart & Total Bill")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            show_cart()
        elif choice == '4':
            print("👋 Thank you for shopping with us!")
            show_cart()
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")


billing_system()
