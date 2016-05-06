import csv

with open("/home/khamm/repos/kirk-data/POST0316.txt", "rb") as file_pipe:
    reader_pipe = csv.reader(file_pipe, delimiter='|')
    with open("/home/khamm/repos/kirk-data/POST0316.csv", 'wb') as file_comma:
        writer_comma = csv.writer(file_comma, delimiter=',')
        for row in reader_pipe:
            writer_comma.writerow(row)