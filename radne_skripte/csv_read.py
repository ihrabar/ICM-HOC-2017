import csv


# Napisi ime .csv file-a iz kojih ces citati podatke
filename='csv_redci.csv'

podaci=[]
# otvori csv file
with open(filename, 'r') as csv_file:
    # otvori .csv file u notebook-u i pogledaj koji delimiter se koristi
    wr = csv.reader(csv_file, delimiter=',')
    # zapisi podatke u .csv
    for row in wr:
        podaci.append(row)

# promjena liste stringova u listu floatova
vrijeme=list(map(float,podaci[0]))
mjerenja=list(map(float,podaci[1]))

print(vrijeme)
print(mjerenja)
