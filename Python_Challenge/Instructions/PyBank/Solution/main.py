import os
import csv
import math

# Path to collect data from the Resources folder
csvpath = os.path.join('Instructions','PyBank','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    #Read and delimit the data
    csvreader=csv.reader(csvfile,delimiter=',')


    # Sum of Rows
    rows=[r for r in csvreader]
    
    #Initialize Variable
    month_n=0
    revenue=0
    delta_rev = 0
    delta_all = []
    delta_sum=0
    date = []
    delta_inc = 0
    delta_dec = 999999999
    inc_index = 0
    dec_index = 0
    inc_date = 0
    dec_date = 0
   
    #Using the FOR loop
    for i in range(1,len(rows)):
        
        month_n=month_n + 1
        row=rows[i]
        revenue= int(row[1]) + revenue
        
        #Will need it when collecting the greatest increase and decrease in profits
        date.append(row[0])
          
        #Skipping Header Row
        if i > 1:
            delta_rev=(int(row[1])-int(rows[i-1][1])) 
            delta_sum = delta_rev + delta_sum
            delta_all.append(delta_rev)

#Find the greatest increase and decrease of profit and its dates
inc_profit = max(delta_all)
dec_profit = min(delta_all)

inc_date = date[delta_all.index(inc_profit)+1]
dec_date = date[delta_all.index(dec_profit)+1]


#Calculating Average and Average Change in Revenue
average= round((delta_sum /(month_n-1)),2)

# print summary to user
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_n}")
print(f"Total Revenue: ${revenue}")
print(f"Average Revenue Change: ${average}")
print(f"Greatest Increase in Profits: {inc_date} (${inc_profit})")
print(f"Greatest Decrease in Profits: {dec_date} (${dec_profit})")


# save summary to txt
save_file = "financial_results.txt"
filepath = os.path.join('Instructions','PyBank','Solution',save_file)
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {month_n}" + "\n")
    text.write(f"Total Revenue: ${revenue}" + "\n")
    text.write(f"Average Revenue Change: ${average}" + "\n")
    text.write(f"Greatest Increase in Profits: {inc_date} (${inc_profit}" + ")\n")
    text.write(f"Greatest Decrease in Profits: {dec_date} (${dec_profit}" + ")\n")
