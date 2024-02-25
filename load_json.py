from pymongo import MongoClient
import json


client = MongoClient("mongodb+srv://user599:qwerty123@cluster0.vprpbbg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['Hw08']

authors_collection = db["authors"]

authors_json = "C:/project_py/hw/py_web/hw08/authors.json"

with open(authors_json, "r") as f:
    authors_data = json.load(f)
    authors_collection.insert_many(authors_data)

quotes_collection = db["quotes"]

quotes_json_file_path = "C:/project_py/hw/py_web/hw08/quotes.json"

with open(quotes_json_file_path, "r") as f:
    quotes_data = json.load(f)
    quotes_collection.insert_many(quotes_data)

print("Succesfull")
