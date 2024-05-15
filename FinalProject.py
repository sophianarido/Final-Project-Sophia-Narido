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
                    print("Please enter a positive number.")
                else: daily_spendings.append(spending)
                break
            except ValueError:
                print("Invalid input. Please eneter a number.")