# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')

month_year = []
profits = []
difference = []
average_changes2 = []

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
     # Read the header row first (skip this step if there is no header)
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
     # Read the header row first (skip this step if there is no header)

    for column in csvreader:
        month_year.append(column[0])
        profits.append(int(column[1]))

    print("Financial Analysis")
    print("____________________")   
    #Find the Total amount of months
    Total_Months = (len(month_year))
    print(f"Total Months: {Total_Months}")
    #Find the Total amount of profits or losses
    Total_Profits = (sum(profits))
    print(f"Total profits = ${Total_Profits}")
    #Find the percentage change
    for column in range (0,len(profits)-1):
        difference.append(int(profits[column+1])-int(profits[column]))
        average_changes1 = sum(difference) / len(difference)
        
    print(f"Average Change: (${average_changes1})")
    # Find the greatest increase and greatest decrease in profits
    Greatest_positive_change = max(difference) 
    Greatest_negative_change = min(difference) 
     #Find the months with respective greatest increase and greatest decrease
    Greatest_increase_month = month_year[difference.index(Greatest_positive_change)+ 1]
    Greatest_decrease_month = month_year[difference.index(Greatest_negative_change)+ 1]
    print(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_positive_change})")
    print(f"Greatest Decrease in Profits: {Greatest_decrease_month} (${Greatest_negative_change})")

output_path = os.path.join("bank.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Total Months: {Total_Months}")
    txtfile.write(f"Total: ${Total_Profits}")
    txtfile.write(f"Average Change: ${average_changes1}")
    txtfile.write(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_positive_change})")
    txtfile.write(f"Greatest Decrease in Profits: {Greatest_decrease_month} (${Greatest_negative_change})")
    txtfile.close()