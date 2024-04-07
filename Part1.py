def calculate_amount(food_charge):
    tip_amount = food_charge * 0.18
    tax_amount = food_charge * 0.07
    total_amount = food_charge + tip_amount + tax_amount
	
    return tip_amount, tax_amount, total_amount

def main():
    try:
        food_charge = float(input("Enter the charge for the food: $"))
        
        if food_charge < 0:
            raise ValueError("Food charge cannot be negative.")
        
        tip_amount, tax_amount, total_amount = calculate_amount(food_charge)

        print(f"Tip amount (18% of food charge): ${tip_amount:.2f}")
        print(f"Tax amount ( 7% of food charge): ${tax_amount:.2f}")
        print(f"Total amount: ${total_amount:.2f}")
    except ValueError as ve:
        print("Invalid input:", ve)

if __name__ == "__main__":
    main()