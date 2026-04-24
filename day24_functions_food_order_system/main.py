print("\n--- ORDER SUMMARY ---")
def place_order(customer_name,bill_amount,*items,delivery_charge=40,**details):
    print("\nCustomer:",customer_name)
    print("\nItems ordered:")
    for item in items:
        print(item)
    print("\nDetails:")
    for key,value in details.items():
        print(key,":",value)
    print("\nTotal items:", len(items))
    print("\nDelivery Charge:", delivery_charge)
    print("\nBill Amount: ₹", bill_amount)
    print("\nTotal Amount: ₹", bill_amount + delivery_charge)
place_order("Jeni",560,"Fried Rice","Chilly Chicken","Mango Juice",phone=4523,city="Thrissur")