from pymongo import MongoClient

class MongoDBPayloadRetriever:
    def __init__(self, connection_string, database_name):
        self.connection_string = connection_string
        self.database_name = database_name

    def retrieve_payloads(self):
        # Connect to MongoDB
        client = MongoClient(self.connection_string)
        db = client[self.database_name]

        # Get a list of all collection names
        collection_names = db.list_collection_names()
        sensor_data = {}
        # Iterate over each collection
        for collection_name in collection_names:
            collection = db[collection_name]

            # Retrieve the payload field from each document in the collection
            documents = collection.find()
            for document in documents:
                payload = document.get("payload")
                if isinstance(payload, dict):
                    for field_name in payload.keys():
                        field_value = payload[field_name]
                        if field_name != "timestamp" and field_name != "topic":
                            if field_name not in sensor_data:
                                sensor_data[field_name] = [field_value]
                            else:
                                sensor_data[field_name].append(field_value)

        client.close()

        return sensor_data


