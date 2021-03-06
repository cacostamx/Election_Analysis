import csv
import os

# Assign a variable for the file to load and the path.  Use os method to join folder to file.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_results.txt")

# 1. Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
candidate_dict = {}
winner = ""
txt_results = ""

# Open the election results and read file
# Method of opening and then closing
# election_data = open(file_to_load,"r")

# Method with with. No need for closing file after. -Have to indent next actions-
with open(file_to_load) as election_data:

    # To do: read and perform analysis
    #print(election_data)

    # Read the file with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        #print(row)
        # 2. Add votes to counter
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:  # checkk if name is not in options to add it 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_dict[candidate_name] = row[1]
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Using with to write open file
with open(file_to_save,"w") as txt_file:
    
    election_results = (
        f"\nElection Results\n" +
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)
        #print(f"{candidate_name}: received {vote_percentage:.2%} of the vote.")
        
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        candidate_results = (f"{candidate_name}: {vote_percentage:.2%} ({votes:,})\n") 
        print(candidate_results)
        # write results to file
        txt_file.write(candidate_results)


# print(f"Total votes: {total_votes:,}")
# print(candidate_options)
# print(candidate_votes)

    winner = (
        f"-------------------------\n"
        f"Winner: {winning_candidate} from {candidate_dict[winning_candidate]}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2%}")
    print(winner)
    # Save winner to txt_file
    txt_file.write(winner)

# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# outfile.write("Hello World")
# outfile.close()

# Using with to write open file
#with open(file_to_save,"w") as txt_file:
    # Write to file
    #txt_file.write("Arapahoe, Denver, Jefferson")  #same line
    #txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")   #different lines

# 1. Cast all votes
# 2. Make list of candidates
# 3. Count votes for each candidate
# 4. Calculate percentage of votes for each candidate
# 5. Determine winning candidate

# Close file
# election_data.close()