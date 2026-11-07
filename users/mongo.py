from django.conf import settings
from pymongo import MongoClient
from pymongo.errors import PyMongoError


def get_user_sessions(user_id):
    client = MongoClient(
        settings.MONGODB_URI,
        serverSelectionTimeoutMS=2000,
    )
    try:
        database = client[settings.MONGODB_DB_NAME]
        collection = database[settings.MONGODB_SESSIONS_COLLECTION]
        cursor = collection.find({"user_id": user_id}).sort("created_at", -1)
        return list(cursor)
    except PyMongoError:
        return []
    finally:
        client.close()
