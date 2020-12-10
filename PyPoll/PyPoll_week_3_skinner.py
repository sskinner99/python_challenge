#PyPoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
  
#    You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.
#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import Dependencies
import os
import csv
import pandas as pd
import numpy as nd

# Make a reference to the election_data.csv file path
full_path = r'C:\Users\Sue\code\PythonStuff\python_challenge\PyPoll\Resources\03-Python_Homework_PyPoll_Resources_election_data (2).csv'
csv_path = os.path.normpath(full_path)

candidate_votes = dict()

with open(csv_path) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    print(header)

    for row in reader:
        voter_id = row[0]
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# # Count the total number of votes cast
Total_Votes = candidates_only_df["Voter ID"].count()
Total_Votes


    

    # for key, value in candidate_votes.items():
    #     print(f'Candidate "{key}" has {str(value)} votes')






# Import the election_data.csv file as a dataframe
# election_data_df = pd.read_csv(csv_path, encoding="utf-8")
# election_data_df.head()
 
# candidates_only_df = election_data_df["Candidate", "Voter ID"]
# candidates_only_df.head()
 
# # Complete a list of candidates who recieved votes
# votes_received = candidates_only_df["Candidate"].value_counts()
# votes_received.head()
 
# # Count the total number of votes cast
# Total_Votes = candidates_only_df["Voter ID"].count()
# Total_Votes
 
# # calculate the percentage of votes each candidate won
# election_results_df = candidates_only_df["Candidate"].value_counts()/Total_Votes
# election_results_df.head()

