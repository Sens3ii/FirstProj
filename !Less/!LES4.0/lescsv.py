import csv
filename = 'user_settings.csv'
with open(filename, newline='') as myfile:
    reader = csv.reader(myfile)
    for row in reader:
        print(row)
