
# import module to read csv file
import os
import csv

# path to open csv file
csvpath = os.path.join("Resources", "budget_data.csv")


os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Track various financial parameters
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
month_count = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # remove header and first row
    csv_header = next(csvreader)
    first_row = next(csvreader)

    month_count += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    for row in csvreader:
        month_count += 1
        total_net += int(row[1])

    # calculate the The changes in "Profit/Losses" over the entire period, and then the average of those changes
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        
        # calculate the greatest increase and decrease 
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change 

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change 
avg = sum(net_change_list)/len(net_change_list)
output = (
        f"Financial analysis\n"
        f"-------------------\n"
        f"total_months: {month_count}\n"
        f"total: {total_net}\n"
        f"average_change: {avg:.2f}\n"
        f"greatest_increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"greatest_decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

print(output)


        

        


        
        

        

        
      

