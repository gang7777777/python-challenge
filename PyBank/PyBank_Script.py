# Modules
import os
import csv
import statistics

data = []
dates = []
difference = []
change = 0
initial = 0
# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Removing the Header
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Getting the Net Total of Profit/Loss
    for row in csvreader:
        dates.append(row[0])
        data.append(int(row[1]))
        net = sum(data)

        change = float(row[1]) - initial
        difference.append(change)
        initial = float(row[1])
    del difference[0]

    # Test print for List
    # print(data)
    # print(dates)

    # Getting the Total Number of Months
    months = len(list(data))

    # Getting the Average Change
    average = float(sum(difference)/(months-1))

    # Getting the Greatest Increase and Date

    increase = max(difference)
    increase_index = difference.index(increase)
    increase_date = dates[increase_index+1]

    # Getting the Greatest Decrease and Date

    decrease = min(difference)
    decrease_index = difference.index(decrease)
    decrease_date = dates[decrease_index+1]

    # Printing Final Results
    print("Financial Analysis")
    print("")
    print("----------------------------")
    print("")
    print(f"Total Months: {months}")
    print("")
    print(f"Total: ${net}")
    print("")
    print(f"Average Change: ${average:.2f}")
    print("")
    print(f"Greatest Increase in Profits: {increase_date} (${increase:.0f})")
    print("")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease:.0f})")

    # save the output file path
    output_file = os.path.join("analysis","output.csv")

    with open(output_file, 'w') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([])
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow([])
        csvwriter.writerow(["----------------------------"])
        csvwriter.writerow([])
        csvwriter.writerow([f"Total Months: {months}"])
        csvwriter.writerow([])
        csvwriter.writerow([f"Total: ${net}"])
        csvwriter.writerow([])
        csvwriter.writerow([f"Average Change: {average:.2f}"])
        csvwriter.writerow([])
        csvwriter.writerow([f"Greatest Increase in Profits: {increase_date} (${increase:.0f})"])
        csvwriter.writerow([])
        csvwriter.writerow([f"Greatest Decrease in Profits: {decrease_date} (${decrease:.0f})"])
        