from pymongo import MongoClient

import db.mongo

CLIENT_HOST = 'server-mongo'
CLIENT_PORT = 27017
CLIENT_DB = 'default'
CLIENT_COLLECTION = 'articles'

class Articles(db.mongo.Base):

    def connect(self):

        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.collection = CLIENT_COLLECTION
        self.db = CLIENT_DB

        self.schema = {
            'title': {
                'type': 'string'
            },
            'body': {
                'type': 'string'
            },
            'article_id': {
                'type': 'integer'
            },
            'creator_id': {
                'type': 'integer'
            },
            'comments': {
                'type': 'list',
                'schema' : {
                    'type' : 'string'
                }
            },
            'irc_id': {
                'type': 'integer'
            }
        }

        self.schema_create = {
            'title': {
                'type': 'string',
                'required': True
            },
            'body': {
                'type': 'string',
                'required': True
            },
            'article_id': {
                'type': 'integer',
                'required': True
            },
            'creator_id': {
                'type': 'integer',
                'required': True
            },
            'comments': {
                'type': 'list',
                'schema' : {
                    'type' : 'string'
                }
            },
            'irc_id': {
                'type': 'integer',
                'required': True
            }
        }

        self.validator_read = db.mongo.DefaultValidator(self.schema)
        self.validator_update = db.mongo.DefaultValidator(self.schema)
        self.validator_delete = db.mongo.DefaultValidator(self.schema)
        self.validator_create = db.mongo.DefaultValidator(self.schema_create)

    def close(self):
        self.mongo_client.close()
