# csv file
import csv
a = {"type": "A", "field1": "value1", "field2": "value2"}
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)
