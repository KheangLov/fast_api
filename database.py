import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.fast_api

user = database.get_collection("users")
