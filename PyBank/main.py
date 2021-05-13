#import modules to bring csv file over
import os
import csv

#Create path for resources get data
csvpath = os.path.join(".", "resources", "budget_data.csv")

#Variables needed 
months = []
total_months = 0
net_total = 0
total_change = 0

#Open and read the data
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read header row first
    csvheader = next(csvreader) 

    for row in csvreader:
        
        #Find the totals of months and net profits/losses
        total_months = total_months + 1
        net_total = net_total + int(row[1])

        

        







