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

#Declare variable for greatest increase and decrease       
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)

#Determine months for greatest increase and decrease
greatest_increase_month = monthly_change.index(greatest_increase)+1
greatest_decrease_month = monthly_change.index(greatest_decrease)+1

# Print analysis to terminal
print(greatest_increase_month)
print(greatest_decrease_month)
print(greatest_decrease)
print(greatest_increase)
print("Financial Analysis")
print("---------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
monthly_change_round = (sum(monthly_change))/len(monthly_change)
print(f"Average Change: ${monthly_change_round:.2f}")
print(f"Greatest Increase in Profits: {dates[greatest_increase_month]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {dates[greatest_decrease_month]} (${greatest_decrease})")

# Export file as a text file
f = open("PyBank.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${net_total}\n")
f.write(f"Average Change: ${monthly_change_round:.2f}\n")
f.write(f"Greatest Increase in Profits: {dates[greatest_increase_month]} (${greatest_increase})\n")
f.write(f"Greatest Decrease in Profits: {dates[greatest_decrease_month]} (${greatest_decrease})")