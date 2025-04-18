def calculate_discount(price, discount_percent):
    if discount_percent >= 20: 
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price 
    else:
        return price

# User input 
original_price = float(input("Enter the original price of the item: ")) 
discount_percent = float(input("Enter the discount percentage: "))  

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Display result
if discount_percent >= 20:
    print(f"After applying a {discount_percent}% discount, the final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {original_price:.2f}")
    