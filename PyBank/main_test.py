# Modules
import statistics
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
        profit_losses.append(row[1])

    # Determine total number of months
    total_months = 0
    for month in dates:
        total_months += 1

    # Determine net total amount
    net_total = 0
    for row in profit_losses:
        net_total += int(row)

    # Determine monthly change
    for i in range(len(net_total)):
        monthly_change.append(net_total[i+1]-net_total[i])
        
# print(range(len(net_total)))
print("Financial Analysis\n")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
# print(dates)
# print(profit_losses)