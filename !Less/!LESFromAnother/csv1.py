import csv
with open('names.csv','r',encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)