# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    csv_reader = next(csvreader, None)

    # Create empty lists
    dates = []
    profit_losses = []
    monthly_change = []

    # Create loop for separate lists
    for row in csvreader:

        dates.append(row[0])
        profit_losses.append(int(row[1]))

    # Determine total number of months
    total_months = 0
    for month in dates:
        total_months += 1

    # Determine net total amount
    net_total = 0
    for row in profit_losses:
        net_total += int(row)

    # Determine monthly change
    for i in range((len(profit_losses)-1)):
        monthly_change.append(int(profit_losses[i+1])-int(profit_losses[i]))
        
print("Financial Analysis")
print("---------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
monthly_change_round = (sum(monthly_change))/len(monthly_change)
print(f"Average Change: ${monthly_change_round:.2f}")
# print(dates)
# print(profit_losses)