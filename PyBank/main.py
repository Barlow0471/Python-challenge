# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    csv_reader = next(csvreader)

    # Set up loop for months
    month_counter = 0
    total_counter = 0
    for row in csvreader:
        total_counter += float(row[1])
        month_counter += 1
    
    print("Total Months: " + str(month_counter))
    print("The total is ${}" .format(total_counter))
    # total_counter = 0
    # for i in csvreader:
    #     total_counter += 1
    # print(total_counter)
