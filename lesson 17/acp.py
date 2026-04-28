# Program to calculate customer due amount

def calculate_due():
    try:
        # Input: Total bill amount and amount paid
        total_bill = float(input("Enter the total bill amount: "))
        amount_paid = float(input("Enter the amount paid by the customer: "))

        # Calculation
        due_amount = total_bill - amount_paid

        # Output logic
        if due_amount > 0:
            print(f"Remaining balance due: {due_amount:.2f}")
        elif due_amount < 0:
            print(f"Overpayment! Change to return: {abs(due_amount):.2f}")
        else:
            print("Bill paid in full. No amount due.")
            
    except ValueError:
        print("Please enter valid numerical values.")

# Run the program
calculate_due()
