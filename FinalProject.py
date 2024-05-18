# Final Project Assignment - Sophia Narido

def calculate_monthly_budget():
    total_days = 30 
    daily_spendings = []

#Input how much you spent 
    for day in range(1, total_days + 1):
        while True:
            try:
                spending = float(input(f"Enter how much you spent for day {day}: $"))
                if spending < 0:
                    print("Please enter a number.")
                else: daily_spendings.append(spending)
                break
            except ValueError:
                print("Invalid input. Please eneter a positive number.")
#Calculate total spending for the month 
total_spending = sum(daily_spendings)

#Calculate average daily spending
average_daily_spending = total_spending / total_days

#Calculate monthly budget
monthly_budget = 0
if total_spending < 0:
    monthly_budget = "Invalid input. Totaly spending cannot be negative."
else: 
    monthly_budget = total_spending - (average_daily_spending * total_days)

#To use the function and display the results
monthly_budget, average_daily_spending = calculate_monthly_budget()
print(f"Total spending for the month: ${monthly_budget:.2f}")
print(f"Average daily spending: ${average_daily_spending:.2f}")

#Determine if the budget was met or not 
if total_spending > monthly_budget:
        budget_status = "over budget"
elif total_spending < monthly_budget:
        budget_status = "under budget"
else:
        budget_status = "on budget"