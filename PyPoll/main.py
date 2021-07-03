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

    # Create complete list of candidates
    unique_candidates = ["Khan", "Correy", "Li", "O\'Tooley"]

    # Determine total number of votes each candidate won
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

    # Create a list of all the votes
    votes = [khan_votes, correy_votes, li_votes, otooley_votes]

    # Zip candidates into a dictionary with votes
    dict_candidates_and_votes = dict(zip(unique_candidates, votes))

    # Use max function to determine winner
    winner = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

    # Create function to return percentage of votes
    def percentage(part, whole):
         return 100 * (part)/(whole)

# Print relevant data
print(f"Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print("------------------")
print(f"Khan: {int(percentage(khan_votes, total_votes))}% ({khan_votes})")
print(f"Correy: {int(percentage(correy_votes, total_votes))}% ({correy_votes})")
print(f"Li: {int(percentage(li_votes, total_votes))}% ({li_votes})")
print(f"O\'Tooley: {int(percentage(otooley_votes, total_votes))}% ({otooley_votes})")
print("------------------")
print(f"Winner: {winner}")

# Print analysis to text document
f = open("PyPoll.txt", "w")
f.write(f"Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("-------------------------\n")
f.write(f"Khan: {int(percentage(khan_votes, total_votes))}% ({khan_votes})\n")
f.write(f"Correy: {int(percentage(correy_votes, total_votes))}% ({correy_votes})\n")
f.write(f"Li: {int(percentage(li_votes, total_votes))}% ({li_votes})\n")
f.write(f"O\'Tooley: {int(percentage(otooley_votes, total_votes))}% ({otooley_votes})\n")
f.write("-------------------------\n")
f.write(f"Winner: {winner}\n")