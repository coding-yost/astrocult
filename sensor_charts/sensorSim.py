import csv
from time import sleep

#reader
with open('testData1.csv', newline='') as reader_file:
    reader = csv.reader(reader_file, delimiter=',', quotechar='|')
    for row in reader:
        with open('data.csv', 'a', newline='') as writer_file:
            writer = csv.writer(writer_file, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(row)
            writer_file.close()
        sleep(1)
