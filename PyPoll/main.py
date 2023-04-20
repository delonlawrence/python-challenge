import os
import csv

csvpath = os.path.join("resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}
winner = ""
winner_votes = 0



# Open the CSV file and read in the data
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop through each row in the CSV file
    # to calculate total votes
    for row in csvreader:
        total_votes += 1

        candidate = row[2]   

        #to populate list of candidates
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 0

        #calculate the votes per candidate
        votes_per_candidate[candidate] += 1


# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through each candidate and calculate their percentage of the vote
for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = round((votes / total_votes) * 100, 2)
    print(f"{candidate}: {percentage}% ({votes})")

    # Check if this candidate has more votes than the current winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("election_results.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate in candidates:
        votes = votes_per_candidate[candidate]
        percentage = round((votes / total_votes) * 100, 2)
        text_file.write(f"{candidate}: {percentage}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")

