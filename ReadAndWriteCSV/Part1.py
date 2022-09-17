# importing csv module
import csv

# csv file name
filename = "simple.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % csvreader.line_num)

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing Employees with gmail accounts
print(f'Employees with Gmail Accounts: {list(filter(lambda s: "@gmail" in s[2], rows))}')

# printing Employee names and salaries
print(f'Employee Name and Salary: {[[row[1] + "," + row[3]] for row in rows]}')

# printing employee names who ids start with M
print(f'Employee Names with IDS starting with M: {[i[1] for i in (list(filter(lambda s: "M" in s[0][0], rows)))]}')

# printing employee salaries
print(f'Employee salaries: {[row[3] for row in rows]}')

