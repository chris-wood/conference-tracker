import json

conferences = json.loads(open("./db/conferences.json").read())
print conferences

for conference in conferences:
    print conference["title"]
    for topic in conference["topics"]:
        print topic
