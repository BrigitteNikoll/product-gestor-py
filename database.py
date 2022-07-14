import sys
sys.path.append("./venv/lib/python3.10/site-packages")

from pymongo import MongoClient
import certifi

MONGO_URI ='mongodb+srv://brixs:ZisMPzZ6hmXjv7HZ@cluster0.tk5raxj.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db

    