import csv
import os

# Assign a variable for the file to load and the path.  Use os method to join folder to file.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read file
# Method of opening and then closing
# election_data = open(file_to_load,"r")

# Method with with. No need for closing file after. -Have to indent next actions-
with open(file_to_load) as election_data:

    # To do: read and perform analysis
    #print(election_data)

    # Read the file with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    #for row in file_reader:
        #print(row)

    # Print the header row
    headers = next(file_reader)
    print(headers)

# Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# outfile.write("Hello World")
# outfile.close()

# Using with to write open file
with open(file_to_save,"w") as txt_file:
    # Write to file
    #txt_file.write("Arapahoe, Denver, Jefferson")  #same line
    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")   #different lines

# 1. Cast all votes
# 2. Make list of candidates
# 3. Count votes for each candidate
# 4. Calculate percentage of votes for each candidate
# 5. Determine winning candidate

# Close file
# election_data.close()