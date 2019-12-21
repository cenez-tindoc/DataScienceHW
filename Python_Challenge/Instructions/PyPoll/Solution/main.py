import csv
import os 

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    #Read and delimit the data
    csvreader=csv.reader(csvfile,delimiter=',')

    next(csvreader)

    #Initialize Variable
    candidates = []
    num_votes = 0
    vote_counts = []
    
    # Process the votes
    for row in csvreader:

        # Add to total number of votes
        num_votes = num_votes + 1

        # The candidate voted for
        candidate = row[2]

        # If the candidate has other votes then add to vote total
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        # Else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

    # Create variables for calculations
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = round((vote_counts[count]/num_votes*100),3)
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            max_index = count
    winner = candidates[max_index]

    # Round decimal
    percentages = [round(i,3) for i in percentages]

# Print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
print("--------------------------")

for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# save summary to txt
save_file = "poll_results.txt"
filepath = os.path.join('Solution',save_file)
with open(filepath,'w') as text:
    text.write("Election Results")
    text.write("--------------------------")
    text.write(f"Total Votes: {num_votes}")
    text.write("--------------------------")

    for count in range(len(candidates)):
        text.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")

    text.write("---------------------------")
    text.write(f"Winner: {winner}")
    text.write("---------------------------")

