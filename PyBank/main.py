#import modules to bring csv file over
import os
import csv

#Create path for resources get data
csvpath = os.path.join(".", "resources", "budget_data.csv")
file_output = "analysis/budget_analysis.txt"

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

        #calculate greatest increase in profits(dates included)
        profit_increase = max(revenue_change)
        #find month of greatest increase
        mon = revenue_change.index(profit_increase)
        month_inc = month[mon + 1]

        #Calculate greatest decrease in profits(dates included)
        profit_decrease = min(revenue_change)
        #find month of greatest decrease
        date = revenue_change.index(profit_decrease)
        month_dec = month[date +1]

#Generate Output Summary
output = (
        f"/nFinancial Analysis/n"
        f"------------------------/n"
        f"Total Months: {total_months}/n"
        f"Total Revenue: ${net_total}/n"
        f"Average Revenue Change: ${revenue_average}/n"
        f"Greatest Increase in Revenue: {mon_inc} (${profit_increase})"
        f"Greatest Decrease in Revenue: {mon_dec} (${profit_decrease})"
        )
print(output)

#Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)





