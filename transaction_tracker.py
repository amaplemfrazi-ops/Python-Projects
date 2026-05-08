# Transaction Tracker
# Tracks purchases, running total, and budget

transactions = []
budget = float(input("What is your budget for today? $"))
print(f"\nBudget set to ${budget:.2f}")
print("Let's start tracking your transactions!\n")
while True:
    print("Enter a transaction or type 'done' to finish.")
    description = input("Description:  ").strip()
    if description.lower() == 'done':
        break
    try:
        amount = float(input(f"Amount for {description}: $").strip())
        transactions.append({"description": description, "amount": amount})
        total = sum(t['amount'] for t in transactions)
        print(f"\nAdded: {description} - ${amount:.2f}")
        print(f"Running total: ${total:.2f} of ${budget:.2f}")
        
        if total > budget:
            print(f"⚠️ WARNING: You are ${total - budget:.2f} over your budget! Consider reviewing your transactions.")
        else:
            print(f"Remaining budget: ${budget - total:.2f}")
    except:
        print("Invalid input. Please enter a valid amount.")
print("\n-- Transaction Summary --")
print(f"Total transactions: {len(transactions)}")
for t in transactions:
    print(f" {t['description']} - ${t['amount']:.2f}")
print(f"\nTotal spent: ${total:.2f}")
print(f"Budget: ${budget:.2f}")

if total > budget:
    print(f"You went ${total - budget:.2f} over budget!")
else:
    print(f"You stayed under budget by ${budget - total:.2f}. Great job!")
    