annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("Enter the cost of your dream home: ")

portion_down_payment = float(total_cost) * float(.25)
monthly_income = float(annual_salary) / 12
monthly_investment = float(monthly_income) * float(portion_saved)

current_savings = 0
months = 0
r = .04

while current_savings < portion_down_payment:
    months += 1
    current_savings +=  monthly_investment
    interest = current_savings * r / 12
    current_savings += interest
print("Number of months: ", months)





