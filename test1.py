import csv

p = ['1','2','3']

with open('names.csv', 'w') as new_file:
    for p in p:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow([p])
