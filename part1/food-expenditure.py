times_eat = float(input("How many times a week do you eat at the student cafeteria?"))
price_of_lunch = float(input("The price of a typical student lunch?"))
money_spent_groceries = float(input("How much money do you spend on groceries in a week?"))


money_spent_weekly = (times_eat*price_of_lunch) + money_spent_groceries
daily_spending = money_spent_weekly/7


print("Average food expenditure:")
print("Daily: ", daily_spending, "euros")
print("Weekly: ", money_spent_weekly, "euros")