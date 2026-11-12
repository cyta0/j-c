# This project is about converting data from a file with .CSV format to a onw with .JSON format and vice versa.
# The 'file.csv, file0.csv, file.json, file0.json' in the code below are only for testing the code. Feel free to set your own path for your files.

import csv
import json

# In the code below we are restoring a list of dictionaries in the 'new_' variable.
# new_ = []
# with open("../tests/file.csv", mode='r', newline='', encoding='utf-8') as open_ :
#     reader_ = csv.DictReader(open_)
#     for i in reader_ :
#         new_.append(i)
    

# with open("../tests/file.json", mode='w', newline='', encoding='utf-8') as file_ :
#     json.dump(new_, file_, indent=4)

# Alternative to the code above is to store the data of the csv file as dictionaries inside a dictionary.
# Another modification in the code below is that we are registering the data which should be registered as integers to be integers rather than strings.

new_file = {}

with open("../tests/file.csv", mode='r', newline='', encoding='utf-8') as opening :
    reader_ = csv.DictReader(opening)
    for row in reader_:
        row["id"] = int(row["id"])
        row["age"] = int(row["age"])

        new_file[row["id"]] = row

with open("../tests/file0.json", mode='w', newline='', encoding='utf-8') as closing :
    json.dump(new_file, closing, indent=4)


# Below, I will be reading the file0.json file and convert it into appropriate data for file0.csv


data_ = {}

with open("../tests/file0.json", mode='r', newline='', encoding='utf-8') as input_file :
    data_ = json.load(input_file)

    # In this line we are deriving the necessary headers for our csv file's header 
    fieldnames = next(iter(data_.values())).keys()
with open("../tests/file0.csv", mode='w', newline='', encoding='utf-8') as output_file :
    writer_ = csv.DictWriter(output_file, fieldnames = fieldnames)

    writer_.writeheader()
    writer_.writerows(data_.values())
