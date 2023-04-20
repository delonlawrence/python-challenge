# python-challenge

    for Pypoll this part of the code is from chat. Its the code for exporting the data to txt.
    
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


