import csv

mjerenja=[2,5,6,4,2,3,]
vrijeme=[1,2,3,4,5,6]


#napuni varijable mjerenja i vrijeme random vrijednostima#




##########################################################

# napisi ime .csv file-a u koji ce se spremiti podaci
filename = "csv_redci.csv"

# otvori csv file
with open(filename, 'w', newline='') as csv_file:
    wr = csv.writer(csv_file)
    # zapisi podatke u .csv
    wr.writerow(vrijeme)
    wr.writerow(mjerenja)
