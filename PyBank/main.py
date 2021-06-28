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

    # Set up loop for months
    month_counter = 0
    total_counter = 0
    
    for row in csvreader:
        # greatest_increase = float(row[1])
        total_counter += int(row[1])
        month_counter += 1
                
        
    print(float(total_counter / month_counter))
    print("Financial Analysis\n")
    print("Total Months: " + str(month_counter))
    print("Total: ${}" .format(total_counter))
    # total_counter = 0
    # for i in csvreader:
    #     total_counter += 1
    # print(total_counter)
