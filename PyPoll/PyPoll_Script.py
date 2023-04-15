# Modules
import os
import csv

ballotID = []
county = []
candidate = []
cand1 = 0
cand2 = 0
cand3 = 0

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
    # Removing the Header
   csv_header = next(csvreader)
   #print(f"CSV Header: {csv_header}")

    # Getting the Net Total of Profit/Loss
   for row in csvreader:
      ballotID.append(row[0])
      county.append(row[1])
      candidate.append(row[2])

    # Test print for List
   #print(ballotID)
   #print(county)
   #print(candidate)

    # Getting the Total Votes
   total_votes = len(list(ballotID))  

   # Complete List of Candidates who received votes
   for row in candidate:
      if row == 'Charles Casper Stockham':
         cand1 += 1
      elif row == 'Diana DeGette':
         cand2 += 1
      else:
         cand3 += 1

   # Determining the percentage
   percent1 = "{:.3%}".format(cand1/int(total_votes))
   percent2 = "{:.3%}".format(cand2/int(total_votes))
   percent3 = "{:.3%}".format(cand3/int(total_votes))
 
   # Placing Result in lists
   result_name = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
   result_number = [cand1, cand2, cand3]

   # Determining the winner
   winner = max(result_number)
   winner_index = result_number.index(winner)
   winner_name = result_name[winner_index]
   
   # Printing the winner

   print("")
   print("Election Results")
   print("")
   print("----------------------------")
   print("")
   print(f"Total Votes: {total_votes}")
   print("")
   print("----------------------------")
   print("")
   print(f"Charles Casper Stockham: {percent1} ({cand1})")
   print("")
   print(f"Diana DeGette: {percent2} ({cand2})")
   print("")
   print(f"Raymon Anthony Doane: {percent3} ({cand3})")
   print("")
   print("----------------------------")
   print("")
   print(f"Winner: {winner_name}")
   print("")
   print("----------------------------")

   # save the output file path
   output_file = os.path.join("analysis","output.txt")

   with open(output_file, 'w') as csvfile:

      csvwriter = csv.writer(csvfile, delimiter=',')
      csvwriter.writerow([])
      csvwriter.writerow(["Election Results"])
      csvwriter.writerow([])
      csvwriter.writerow(["----------------------------"])
      csvwriter.writerow([])
      csvwriter.writerow([f"Total Votes: {total_votes}"])
      csvwriter.writerow([])
      csvwriter.writerow(["----------------------------"])
      csvwriter.writerow([])
      csvwriter.writerow([f"Charles Casper Stockham: {percent1} ({cand1})"])
      csvwriter.writerow([])
      csvwriter.writerow([f"Diana DeGette: {percent2} ({cand2})"])
      csvwriter.writerow([])
      csvwriter.writerow([f"Raymon Anthony Doane: {percent3} ({cand3})"])
      csvwriter.writerow([])
      csvwriter.writerow(["----------------------------"])
      csvwriter.writerow([])
      csvwriter.writerow([f"Winner: {winner_name}"])
      csvwriter.writerow([])
      csvwriter.writerow(["----------------------------"])