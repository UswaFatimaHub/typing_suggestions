from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

# Read values from environment variables
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "traction-stage")  # Default value fallback
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "articles")


client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
