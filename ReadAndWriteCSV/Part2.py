# importing csv module
import csv
import collections

# csv file name
filename = "UFOSightings.csv"

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

    # get total number of ufo sightings
    print("Total no. of UFO sightings: %d" % csvreader.line_num)

# printing the field names
print('Field names are:' + ', '.join(field for field in fields) + f'\nThere are {len(fields) - 1} total indexes.')

# printing all ufo sightings in 2010
print(f'There have been {len(list(filter(lambda x: "2010" in x[0], rows)))} UFO sightings in 2010.')

# printing the total number of shapes
print(f'There are {len(set(row[4] for row in rows))} different shapes sighted so far.')


# had to make this a function since there were dates mixed in in with tha latitudes :)
def get_certain_lats(x: list) -> bool:
    try:
        return 45 >= int(float(x[9])) >= 40
    except ValueError:
        pass  # if its a date mixed in it doesnt matter ignore it so we pass


# printing How many sightings are between latitude 40 and 45
print(f'There are {len(list(filter(get_certain_lats, rows)))} sightings between latitude 40 and 45.')

# Number of sightings in MN
print(f'There have been {len(list(filter(lambda x: "mn" in x[2], rows)))} UFO sightings in Minnesota')

# write to csv file total of sightings for each state
write_fields = ['State', 'Total Sightings']

counter = collections.Counter()  # use counter to count each time each state is reported to have a sighting

for row in rows:
    counter[row[2]] += 1  # increase number of sightings each time the counter finds the states in the data

states = set(row[2] for row in rows)  # create a set for the states to get each unique state reported

write_rows = list(list(tuple((s, counter[s]))) for s in states)  # create rows

filename = 'NumberOfSightingsAcrossStates.csv'

# write to file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(write_fields)

    csvwriter.writerows(write_rows)

print(f'Created file {filename}')
