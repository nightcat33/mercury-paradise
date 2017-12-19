import unittest
import re
import json
from pymongo import MongoClient
from cerberus import Validator
from bson import ObjectId
from datetime import datetime
import copy
import bcrypt
import string
import random
import os
import sys
sys.path.insert(0, os.path.abspath('../src/'))

import db.mongo

CLIENT_HOST = '127.0.0.1'
CLIENT_PORT = 27017
CLIENT_DB = 'default_test'
CLIENT_COLLECTION = 'test'

class UserProfile(db.mongo.Base):
    def connect(self):

        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.collection = CLIENT_COLLECTION
        self.db = CLIENT_DB

        self.schema = {
            'user_id': {
                'type': 'integer'
            },
            'bio':{
                'type': 'string'
            }
        }

        self.schema_create = {
            'user_id': {
                'type': 'integer',
                'required' : True
            },
            'bio':{
                'type': 'string'
                'required': True
            }
        }

        self.validator_read = db.mongo.DefaultValidator(self.schema)
        self.validator_update = db.mongo.DefaultValidator(self.schema)
        self.validator_delete = db.mongo.DefaultValidator(self.schema)
        self.validator_create = db.mongo.DefaultValidator(self.schema_create)

    def close(self):
        self.mongo_client.close()
