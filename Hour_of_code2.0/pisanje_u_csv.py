import csv


mjerenja=[1,2,3]
vrijeme=[2,3,4]


#napuni varijable mjerenja i vrijeme random vrijednostima#






##########################################################

# napisi ime .csv file-a u koji ce se spremiti podaci
filename = "13.csv"

# otvori csv file
with open(filename, 'w', newline='') as csv_file:
    wr = csv.writer(csv_file)
    # zapisi podatke u .csv
    wr.writerow(mjerenja)
    wr.writerow(vrijeme)