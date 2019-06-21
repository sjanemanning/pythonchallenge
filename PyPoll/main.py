import os
import csv

pypoll_path = os.path.join('Resources','election_data.csv')

countofvotes=0
candidate = ''
candidatevotes = {}


with open(pypoll_path,'r', newline="") as pypollcsv:
    csvreader = csv.reader(pypollcsv , delimiter=',')
    
    next(csvreader, None)

    for row in csvreader:
        countofvotes = countofvotes + 1
        candidate = row[2]
        if candidate in candidatevotes:
            candidatevotes[candidate] = candidatevotes[candidate] + 1
        else:
            candidatevotes[candidate] = 1



print(countofvotes)
print(candidate)
print(candidatevotes)

