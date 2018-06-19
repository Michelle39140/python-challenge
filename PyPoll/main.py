# Target:  create a Python script that analyzes the votes and calculates each of the following:
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# Data: a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID (int)`, `County(str)`, and `Candidate(str)`
import csv
import os

# 1. open csv file
input_file_path=os.path.join('..','..','Instructions','PyPoll','Resources','election_data.csv')

with open(input_file_path,newline='') as input_file:
    csviterator=csv.reader(input_file,delimiter=",")
    header = next(csviterator)
    #print(header)

    # 2. loop thru rows and calculate:
    candidates ={} # store candidate name and vote counts in a library, key = candidate name, value = count of votes
    total_votes=0

    for rows in csviterator:
    #   * The total number of votes cast = number of rows
        total_votes +=1
    #   * A complete list of candidates who received votes -> if name not in the candidate list, add in
    #   * The total number of votes each candidate won = sum of votes
        if rows[2] not in candidates.keys():
            candidates[rows[2]]=1
        else: candidates[rows[2]]+=1 # count number of votes

    
    # 3. print out results
    results = (f"Election Results\n\
--------------------------\n\
Total Votes: {total_votes}\n\
--------------------------\n") # initialize the result string
    
    max_vote = 0
    keylist=candidates.keys() # get the key list of the library
    for ikey in keylist:
        if candidates[ikey] > max_vote: #find who has the most vote and store his/her name
            max_vote = candidates[ikey]
            max_vote_name = ikey
        results += (f"{ikey}: {candidates[ikey]/total_votes*100:.3f}% ({candidates[ikey]})\n") # add the results needed to be print to the result string

    results += (f"--------------------------\n\
Winner:{max_vote_name}\n\
--------------------------")

    print(results)

    # 4. export result in txt file
    result_file_path="PyPoll_results.txt" 
    with open(result_file_path,"w+") as result_file:
        result_file.write(results)
