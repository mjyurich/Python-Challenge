#import modules to bring csv file over
import os
import csv

#Create path for resources get data
csvpath = os.path.join(".", "resources", "budget_data.csv")
file_output = os.path.join(".", "analysis", "budget_analysis.txt")

#Variables/Lists parameters needed
months = []
revenue_list = []
total_months = 0
net_total = 0
revenue_last = 0
month_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 999999999999]

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
        month_change = month_change +  [row[0]]


        #Calculate the Average revenue change
        revenue_average = sum(revenue_list) / len(revenue_list)

        #calculate greatest increase in profits(dates included)
        if (revenue_change > greatestIncrease[1]):
            greatestIncrease[1] = revenue_change
            greatestIncrease[0] = row[0]

        #Calculate greatest decrease in profits(dates included)
        if (revenue_change < greatestDecrease[1]):
            greatestDecrease[1] = revenue_change
            greatestDecrease[0] = row[0]

#Generate Output Summary
output = (
        f"/nFinancial Analysis/n"
        f"------------------------/n"
        f"Total Months: {total_months}/n"
        f"Total Revenue: ${net_total}/n"
        f"Average Revenue Change: ${revenue_average}/n"
        f"Greatest Increase in Revenue: {greatestIncrease[0]} (${greatestIncrease})/n"
        f"Greatest Decrease in Revenue: {greatestDecrease[0]} (${greatestDecrease})/n"
        )

print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${revenue_average}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")


#Export the results to text file
with open(file_output, "w") as txt_file:
    txt_file.write(output)





