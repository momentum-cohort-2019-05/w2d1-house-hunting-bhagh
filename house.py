annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("Enter the cost of your dream home: ")

portion_down_payment = float(total_cost) * 0.25
monthly_income = float(annual_salary) / 12
monthly_investment = float(monthly_income) * float(portion_saved)

current_savings = 0
months = 0
r = .04

while current_savings < portion_down_payment:
    interest = float(current_savings * r / 12)
    current_savings += interest
    current_savings +=  float(monthly_investment)
    months += 1
print("Number of months: ", months)






