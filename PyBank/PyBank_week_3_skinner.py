#Python_Challenge homework week 3 skinner
# PyBank
#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)


#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv

# Store the file path associated with the file (note the backslash may be OS specific)
file = 'Resources/03-Python_Homework_PyBank_Resources_budget_data.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "month_data"
with open(file, 'r') as month_data:

    # Store all of the text inside a variable called "lines"
    lines = csv.reader(month_data)

    # Print the contents of the text file
    TotalMonths = 0
    NetProfitLosses = 0

    #to skip header row 1
    next(lines)
    
    #for looping through each row except header to Count months in data set

    for line in lines: 
        
        TotalMonths +=1
    
        NetProfitLosses +=int(line[1])


    print(TotalMonths)
    print(NetProfitLosses)

    #Count months in data set







