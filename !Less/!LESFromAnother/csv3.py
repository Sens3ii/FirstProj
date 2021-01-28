import csv
csv_file = open('names.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file)
new_file = open('new_names.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(new_file, delimiter=',')

for line in csv_reader:
    csv_writer.writerow(line)
csv_file.close()
new_file.close()
