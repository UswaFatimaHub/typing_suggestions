from pymongo import MongoClient

MONGO_URI ="mongodb+srv://muhammadawais:vkl1Phd92yEJLHOR@cluster0.0wi6ueg.mongodb.net/"
DB_NAME = "traction-stage"
COLLECTION_NAME = "articles"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
