from pymongo import MongoClient

import db.mongo

CLIENT_HOST = 'server-mongo'
CLIENT_PORT = 27017
CLIENT_DB = 'default'
CLIENT_COLLECTION = 'page'

class Pages(db.mongo.Base):

    def connect(self):

        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.collection = CLIENT_COLLECTION
        self.db = CLIENT_DB

        self.schema = {
            'page_name': {
                'type': 'string'
                },
            'articles': {
                'type': 'list',
                'schema': {
                	'type': 'integer'
                }
            }
        }
                
        self.schema_create = {
            'page_name': {
                'type': 'string',
                'required': True
                },
            'articles': {
                'type': 'list',
                'schema': {
                	'type': 'integer'
                }
            }
        }

        self.validator_read = db.mongo.DefaultValidator(self.schema)
        self.validator_update = db.mongo.DefaultValidator(self.schema)
        self.validator_delete = db.mongo.DefaultValidator(self.schema)
        self.validator_create = db.mongo.DefaultValidator(self.schema_create)

    def close(self):
        self.mongo_client.close()


