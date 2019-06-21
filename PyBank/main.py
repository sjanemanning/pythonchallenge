import os
import csv
import sys
sys.stdout = open('solutions_pybank.txt' , 'w' )

pybank_path = os.path.join('Resources','budget_data.csv')


countofmonths = 0
nettotal = 0
averagechange = 0
currentmonth =  0
lastmonth = 0
monthchange = 0 
month = []
monthlychanges = []

with open(pybank_path,'r', newline="") as pybankcsv:
    csvreader = csv.reader(pybankcsv, delimiter=",")

    next(csvreader,None)

    for row in csvreader:
        month.append(row[0])
        countofmonths = countofmonths + 1
        currentmonth = int(row[1])
        nettotal = currentmonth + nettotal
        if countofmonths > 1:
            monthchange = currentmonth - lastmonth
            monthlychanges.append(monthchange)

        lastmonth = currentmonth

change = sum(monthlychanges)
averagechange  = round(change/(countofmonths - 1),2)
maxchangevalue = max(monthlychanges)
#print(maxchangevalue)
maxmonthloc = monthlychanges.index(maxchangevalue)
#print(maxmonthloc)
maxmonth = month[maxmonthloc]
#print(maxmonth)
minchangevalue = min(monthlychanges)
minmonthloc = monthlychanges.index(minchangevalue)
minmonth = month[minmonthloc]

print('Financial Analysis')
print(f"Total Months: {countofmonths}")
print(f"Total: ${nettotal}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase: ${maxchangevalue}, {maxmonth}")
print(f"Greatest Decrease: ${minchangevalue}, {minmonth}")



