import json

newdata = []

with open('/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as/dataset/edic_train_dev_dataset.json', 'r') as file:
    data = json.load(file)
    
for row in data:
    newdata.append(row)


# Load JSON from a file
with open('/media/nas_mount/shaina_mehta/osdvd/osdvd_train_data.json', 'r') as file:
    data2 = json.load(file)
    
for row in data2:
    newdata.append(row)

print(len(newdata))
with open('osdvd_edic_train_dev_dataset.json', 'w') as file:
    json.dump(newdata, file, indent=4)