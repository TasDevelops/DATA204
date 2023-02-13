import pymongo

try:
    client = pymongo.MongoClient()
    print("Connected successfully!")
except:
    print("Could not connect to MongoDB")
db = client['starwars']

characters = db.characters.find({})

"""character_names = db.characters.find({"species.name":"Droid"}, {"name":1,"species.name":1, "_id":0})

for person in character_names:
    print(person)"""

"""luke = db.characters.find_one({"name":"Luke Skywalker"})
print (luke)"""

"""Find the height of Darth Vader, only return results for the name and the height.
Find all characters with yellow eyes, only return results for the names of the characters.
Find male characters. Limit your results to only show the first 3.
Find the names of all the humans whose homeworld is Alderaan."""


"""character_names = db.characters.find({"name":"Darth Vader"},{"name":1,"height":1, "_id":0})

for person in character_names:
    print(person)


yellow = db.characters.find({"eye_color":"yellow"}, {"name":1, "_id":0})

for y in yellow:
    print(y)

male = db.characters.find({"gender":"male"}, {"name":1, "_id":0}).limit(3)

for m in male:
    print(m)


home = db.characters.find({"homeworld.name":"Alderaan", "species.name":"Human"}, {"name":1, "_id":0})
for h in home:
    print(h)"""

#removing unknown heights
#db.characters.update_many({"height":"unknown"}, {"$unset":{"height":""}})

#getting rid of unknown mass
#db.characters.update_many({"mass":"unknown"}, {"$unset":{"mass":""}})

#changing to Integer
#db.characters.update_many({},[{"$set": {"height":{"$toInt": "$height"}}}])

#sorting out comma problem in data
#db.characters.update_many({"mass":"1,358"}, {"$set":{"mass": "1358"}})

#coverting mass to double
#db.characters.update_many({},[{"$set":{"mass": {"$toDouble": "$mass"}}}])


#all_characters = db.characters.find({}, {"height":1, "mass":1, "_id":0})

#average height for female characters (done with $match)
#get female heights
#$avg to find average
#put in list because it containes pipline STAGES ($match, $sort, $group, $project)

#counting particular documents
#count = db.characters.count_documents({"mass":None})
#print(count)

avg_f_height = db.characters.aggregate([{"$match":{"gender":"female"}},{"$group":{"_id":"$gender", "avg_height":{"$avg":"$height"}}}])

for f in avg_f_height:
    print(f)
