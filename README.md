# Election Audit

## Overview of Election Audit
A Colorado Board of Election employee asked us the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calclate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winer of the election based on popular vote.

## Resources
- Data source: The audit was performed on the file "election_results.cvs" provided by the Colorado Board of Election. The following image shows the structure of the file.

    ![CSV file analyzed](/Resources/CSV_file.png)

- Software use to perform the analysis: Python 3.7.6, Visual Studio Code 1.63.2

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The breakdown of votes per county is the following:
    - Jefferson: 10.51% (38,855)
    - Denver: 82.78% (306,055)
    - Arapahoe: 6.71% (24,801)
- The county that had the largest number of votes was:
    - **Denver** with **306,055 votes**
- The breakdown of votes for each candidate are:
    - Charles Casper Stockham: 23.05% (85,213)
    - Diana DeGette: 73.81% (272,892)
    - Raymon Anthony Doane: 3.14% (11,606)
- The winner of the election was:
    - Winner: **Diana DeGette from Jefferson**
    - Winning Vote Count: **272,892**
    - Winning Percentage: **73.81%**

- These results are printed to the termina where the program is run and also  saved to the file "election_results.txt" as the following images shows:
    - Results printed in command line:
        ![Terminal output with audit results](/Resources/Terminal_output.png)
    
    - Results written in text file:
    
        ![Text file with audit results](/Resources/Txt_output.png)

## Electon Audit Summary

Given that the file analyzed contained all the election results for a local congressional election in Colorado, the audit was performed with a python code in under 3 seconds.  The code shows the election results by candidate and by County, giving the number of votes as well the percentage of votes for each case, resulting in determining the winner.  With this kind of audit, larger public elections can be audited within seconds of having the results file to be analyzed, even for state or federal elections.

The following are modifications that could be implemented in other type of elections:
- Include data for different types of positions being elected: Governor, Lieutenant Governor, Secretary of State, and Attorney General, State Supreme Court Justices, Comptroller, Treasurer, State Senators, and State Legislators.
- Information about voters could be include to categorize by age, gender, zip codes, etcetera.
