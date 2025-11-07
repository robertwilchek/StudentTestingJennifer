import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# read students.csv and print out file

# sort by last name

# send sorted records to new file