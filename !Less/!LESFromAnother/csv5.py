import csv
csv_file = open('names.csv', 'r', encoding='utf-8')
csv_reader = csv.DictReader(csv_file)

new_file = open('new_names.csv', 'w', encoding='utf-8')
fieldnames = ['#','id','Name','Surname','MName','Spec']
csv_writer = csv.DictWriter(new_file,fieldnames = fieldnames, delimiter=' ')

csv_writer.writeheader()

for line in csv_reader:
    csv_writer.writerow(line)