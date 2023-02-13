import pymongo
import json
import requests

try:
    client = pymongo.MongoClient()
    print("Connected successfully!")
except:
    print("Could not connect to MongoDB")
db = client['starwars']
print("Retrieving original search results")


# scraping all pages at once

def scrape():
    starship_pages=[]
    response = requests.get("https://swapi.dev/api/starships/")
    data = response.json()
    while data['next'] is not None:
        print("retrieving next page", data["next"])
        response = requests.get(data["next"])
        data = response.json()
        for i in data["results"]:
            starship_pages.append(i["url"])
    return starship_pages


# Extracting the starship URLs about pilots.

def replace():
    starship_info = []
    for i in scrape():
        for elements in i:
            starship_info.append(requests.get(elements["url"]).json()["result"]["properties"])



#getting properties for all the starships and changing the pilot urls to pilot names

    replaced_info = []
    for s in starship_info:
        list_of_pilots = []
        for pilot in s["pilots"]:
            # Find the pilot's name and search characters db to find their ObjectID.
            name = requests.get(pilot).json()["result"]["properties"]["name"]
            pilot_id = db.characters.find_one({"name": name}, {"_id": 1})
            list_of_pilots.append(pilot_id)
        s.update({'pilots': list_of_pilots})
        replaced_info.append(s)
    return replaced_info




db.drop_collection("starships")
db.create_collection("starships")  #creating starships collection


for r in replace():
    db.starships.insert_one(r)

print('All starships have been now added')
