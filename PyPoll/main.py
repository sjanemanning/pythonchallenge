import os
import csv
import sys
sys.stdout = open('solutions_pypoll.txt' , 'w' )

pypoll_path = os.path.join('Resources','election_data.csv')

countofvotes=0
candidate = ''
candidatelist = {}
votepercent = {}
mostvotes = 0
winner = ''



with open(pypoll_path,'r', newline="") as pypollcsv:
    csvreader = csv.reader(pypollcsv , delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        countofvotes = countofvotes + 1
        candidate = row[2]
        if candidate in candidatelist:
            candidatelist[candidate] = candidatelist[candidate] + 1
        else:
            candidatelist[candidate] = 1

for person, votecount in candidatelist.items():
    votepercent[person] = '{0:.0%}'.format(votecount / countofvotes)
    if votecount > mostvotes:
        mostvotes = votecount
        winner = person



print("Election Results")
print(f"Total Votes: {countofvotes}")
for person, votecount in candidatelist.items():
    print(f"{person}: {votepercent[person]} ({votecount})")
print(f"Winner: {winner}")



    


