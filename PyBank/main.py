#paths across opperating system
import os

#module for reading csv file
import csv

# Initialize variables
num_rows = 0
total_months = 0
total_sum = 0
Average_change = 0
previous_month = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0


csvpath = os.path.join('resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # to specify delimeter
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #read header row first
    csv_header = next(csvreader) 
    print(csv_header)
    
    #calculating months
    for row in csvreader:
        num_rows += 1
    print(f'Total months: {num_rows}')
    
    # Task 3: Calculate Total profit and losses
    csvfile.seek(0)  # Reset the file pointer to the beginning
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_sum += float(row[1])
    print(f"Total: {total_sum}")
    
    #Calculate Avg change in profits and losses
    csvfile.seek(0)
    next(csvreader) 
    previous_profit = 0
    for row in csvreader:
        current_profit = float(row[1])
        if previous_profit !=0:
            change_in_profit = current_profit - previous_profit
            total_change += change_in_profit
        previous_profit = current_profit
    average_change = total_change / (num_rows - 1)
    print(f'Average Change: {average_change: .2f}')
    
# Calculate changes in profit and keep track of greatest increase and decrease
    csvfile.seek(0)
    next(csvreader) 
    for row in csvreader:
        current_profit = float(row[1])
        if previous_profit != 0:
            change_in_profit = current_profit - previous_profit
            total_change += change_in_profit
            if change_in_profit > greatest_increase:
                greatest_increase = change_in_profit
                greatest_increase_month = row[0]
            elif change_in_profit < greatest_decrease:
                greatest_decrease = change_in_profit
                greatest_decrease_month = row[0]
        previous_profit = current_profit
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

