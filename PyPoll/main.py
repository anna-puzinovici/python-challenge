
# import module to read csv file
import os
import csv

# path to open csv file
csvpath = os.path.join("Resources", "election_data.csv")

# text file storage
output_path = os.path.join("Resources", "election_analysis.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Assign variables
total_number_votes = 0
candidates_votes = {} # curly bc its dictionary 
percentagevotes_candidate = 0
total_votes_percandidate = 0
winner_percentage = 0
winner_count = 0

#variable for candidate nominees as a list 
candidates_nominees = []

# open the csv file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # remove header and first row
    csv_header = next(csvreader)
    

 
    for row in csvreader:
        total_number_votes += 1 # keeps adding one every time loop iterates 
        candidate_name = row[2] #every time we iterate the candidate name is stored in this variable 
       
       # conditional statement for the list of candidates 
        if candidate_name not in candidates_nominees:
           candidates_nominees.append(candidate_name)
           candidates_votes[candidate_name] = 0 # candidate name is going in the dictionary, and reseting the vote to 0 so it starts counting again 

        candidates_votes[candidate_name] += 1
    
    
    output = (
        f"Election Results \n"
        f"----------------- \n"
        f"Total Votes: {total_number_votes}\n"
        f"------------------\n"
    )
    print(output)

with open(output_path, 'w') as txtfile:
    txtfile.write(output)

    # txtfile.write(output2)

    #percentage calculation 
    for x in candidates_nominees:
        vote = candidates_votes[x]    # getting name from list and putting it back in the di
        percentage = (vote/total_number_votes)*100
        output1 = (
            f"{x}: {percentage}% ({vote})\n"
        )
        print(output1)
        txtfile.write(output1)
      
        if vote > winner_count:
            winner_count = vote
            winner_percentage = percentage 
            winner = x 

    output2 = (
        f"Winner: {winner}\n"
    )
    print(output2)
    txtfile.write(output2)
        

    

       

