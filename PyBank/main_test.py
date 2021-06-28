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

    dates = []
    profit_losses = []

    for row in csvreader:
        money = row[1]
        date = row[0]

        dates.append(date)
        profit_losses.append(money)
    'Determine total number of months'
    total_months = 0
    for month in dates:
        total_months += 1

    'Determine net total amount'
    net_total = 0
    for row in profit_losses:
        net_total += int(row)

print(statistics.mean(profit_losses))
print(net_total)
print(total_months)
# print(dates)
# print(profit_losses)