hotelmenu = {
    'chicken biryani': 300,
    'beef biryani'   : 600,
    'chinese rice'   : 400,
    'mutton kharai'  : 1200,
    'chicken handi'  : 900,
    'delicious qorma': 750,
    'tikka boti'     : 450, 
}

print("Welcome to The PYTHON Hotel !")
print("We are delighted to serve you. Here is our hotelmenu:\n")
for item, price in hotelmenu.items():
    print(f"{item.capitalize()}: Rs. {price}")

order_total = 0
while True:
    item = input("\nEnter the name of the item you want to order (or 'done' to finish): ").strip().lower()

    if item == 'done':
        break
    
    if item in hotelmenu:
        order_total += hotelmenu[item]
        print(f"{item.capitalize()} has been added to your order.")
    else:
        print(f"Sorry but this, {item.capitalize()} is not available yet!")

print(f"\nThe total amount of your order is Rs. {order_total}")
print("Thankyou for ordering from The PYTHON Hotel ! Have a great day!")