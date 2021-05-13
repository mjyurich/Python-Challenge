#import modules to bring csv file over
import os
import csv

#Create path for resources get data
csvpath = os.path.join(".", "resources", "budget_data.csv")

#Variables/Lists parameters needed
months = []
revenue_list = []
total_months = 0
net_total = 0
revenue_last = 0



#Open and read the data
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read header row first
    csvheader = next(csvreader) 

    for row in csvreader:
        
        #Find the totals of months and net profits/losses
        total_months = total_months + 1
        net_total = net_total + int(row[1])

       #Determine the changes in Profits/Losses
        revenue_change = int(row[1]) - revenue_last
        revenue_last = int(row[1])
        revenue_list = revenue_list + [revenue_change]

        #Calculate the Average revenue change
        revenue_average = sum(revenue_list) / len(revenue_list)

        







