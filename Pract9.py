import csv
import json

# Read data from the CSV file
with open("students.csv", "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Write data to the JSON file
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")