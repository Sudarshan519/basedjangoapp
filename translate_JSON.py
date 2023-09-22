import csv
import json
# Open the TSV file for reading
with open('translate.tsv', 'r', newline='', encoding='utf-8') as tsvfile:
    # Create a CSV reader with tab as the delimiter
    reader = csv.DictReader(tsvfile, delimiter='\t')

    # Initialize an empty list to store the data
    data_list = []

    # Iterate through each row in the TSV file
    for row in reader:
        # Append each row (represented as a dictionary) to the list
        data_list.append(row)

 
filename = "eng.json"
file2name="jap.json"
eng={}
jap={}
# python_list = json.loads(json_data)
for data in (data_list):
 
    value=data['English']
    japvalue=data['Japanese']
 
    eng[value]=value
    jap[value]=japvalue
 

print(eng)
# Write the JSON data to the file
with open(filename, 'w', encoding='utf-8') as json_file:
    json.dump(eng, json_file, indent=4, ensure_ascii=False)
with open(file2name, 'w', encoding='utf-8') as json_file:
    json.dump(jap, json_file, indent=4, ensure_ascii=False)

# Optionally, you can also use json.dumps() to get the JSON string and write it to the file
# json_data = json.dumps(data, indent=4, ensure_ascii=False)
# with open(filename, 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)

print(f"Data has been written to {filename}")
 
 

print(f"Data has been written to {file2name}")


