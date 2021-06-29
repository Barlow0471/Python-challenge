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

    unique_candidates = ["Khan", "Correy", "Li", "O\'Tooley"]

    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    khan_votes = 0
    for vote in candidate:
        if vote == "Khan":
            khan_votes += 1
        elif vote == "Li":
            li_votes += 1
        elif vote == "O\'Tooley":
            otooley_votes += 1
        else:
            correy_votes += 1

print(otooley_votes)
print(correy_votes)
print(li_votes)            
print(khan_votes)
print(unique_candidates)
print(f"Election Results\n")
print(f"Total Votes: {total_votes}")