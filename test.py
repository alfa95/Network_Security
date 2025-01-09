from pymongo.mongo_client import MongoClient
uri = "mongodb://localhost:27017"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected to MongoDB")
except Exception as e:
    print("Error in connection to MongoDB", e)