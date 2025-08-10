import os
import motor.motor_asyncio

MONGO_URI = os.getenv("MONGO_URI", "mongodb://root:root@mongo:27017/")
DB_NAME = os.getenv("MONGO_DB_NAME", "game_db")

_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = _client[DB_NAME]
campaigns_collection = db["campaigns"]
