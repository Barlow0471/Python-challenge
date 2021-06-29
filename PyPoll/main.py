# Import CSV
import os
import csv

# Set path for file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    csv_reader = next(csvreader, None)

     # Create empty lists
    voter_id = []
    county = []
    candidate = []

    # Create loop for separate lists
    for row in csvreader:

        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # Determine total number of months
    total_votes = 0
    for vote in voter_id:
        total_votes += 1
print(f"Election Results\n")
print(f"Total Votes: {total_votes}")