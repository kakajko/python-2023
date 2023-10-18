import json
with open('body.json', 'r') as file:
    data = json.load(file)
prospech = {}
for jmeno, body in data.items():
    if body >= 60:
        prospech[jmeno] = "Pass"
    else:
        prospech[jmeno] = "Fail"

with open('prospech.json', 'w') as file:
    json.dump(prospech, file)
