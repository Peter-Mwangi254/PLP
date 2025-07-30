def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    else:
        return price
        
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)
print("Final price:",final_price)