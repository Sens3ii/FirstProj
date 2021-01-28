import csv
csv_file = open('names.csv', 'r', encoding='utf-8')
csv_reader = csv.DictReader(csv_file)

new_file open('new_names.csv','w')
# for line in csv_reader:
#     print(line['Name'])

