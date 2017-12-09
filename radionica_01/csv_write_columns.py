# da pise u stupce umjesto u redke

import csv

mjerenja=[2,5,6,4,2,3,]
vrijeme=[1,2,3,4,5,6]

# napisi ime .csv file-a u koji ce se spremiti podaci
filename = "csv_stupci.csv"

length=len(vrijeme)
# otvori csv file
with open(filename, 'w', newline='') as csv_file:
    wr = csv.writer(csv_file)
    for i in range(length):
    	this_row=[vrijeme[i], mjerenja[i]]
    	wr.writerow(this_row)
