# This code calculates the monthly savings and projects the annual savings with interest.
# It prompts the user for their monthly income and expenses, calculates the savings, and then projects
# the annual savings assuming a 5% interest rate on the savings.
# The formula used is: annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate).

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = income - expenses
annual_savings = (savings * 12) + (savings * 12 * 0.05)  # Assuming a 5% annual interest rate on savings
print(f"Your monthly savings are ${savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")