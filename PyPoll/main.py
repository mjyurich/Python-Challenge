# Import Dependecies
import os 
import csv

#Creates path for resources to get data
csvpath = os.path.join("..", "Resources", "election_data.csv")
file_output = os.path.join(".", "analysis", "election_analysis.txt")

# Variables needed 
total_votes = 0
winner_votes = 0
total_candidates = 0
most_votes = 0
candidate_running = []
candidate_votes = {}
names_list = []

#Open and Read the data
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read header row first
    csvheader = next(csvreader)

    for row in csvreader:

        #Find the total number of votes
        total_votes = total_votes + 1
        
        #Find candidate names
        candidate_name = row[2]
        
        #Add list of candidates in the running
        if candidate_name not in candidate_running:
            candidate_running.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #Add votes to each candidates name
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    #Calculating the percentage of votes
    for candidates in candidate_votes:

        #Need vote count for each candidate
        votes = candidate_votes.get(candidates)
        vote_percentage = int(votes) / int(total_votes) * 100

        #Find the candidar with the most votes
        if votes > most_votes:
            most_votes = votes
            winning_candidate = candidates

        #Put all the candidate in analysis form with vote percentage and total votes
        voter_number = f"{candidates}: {vote_percentage: .2f}% ({votes})\n"
        print(voter_number)
        names_list.append(voter_number)

print(names_list)

#Get output data and analysis
output = (
         f"\nElection Results\n"
         f"----------------------------\n"
         f"Total Votes: {total_votes}\n"
         f"--------------------------------\n")
for data in names_list:
    output = output + data
output = output + (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n")

print(output)

with open(file_output, "w") as text_file:
    text_file.write(output)






