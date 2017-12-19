
"""
unit test for db/mongo.py

TODO:
    read
    update
    delete
"""

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

class TestBaseCreate(unittest.TestCase):
    def setUp(self):
        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.obj = db.mongo.Base(mongo_client=self.client, collection=CLIENT_COLLECTION, db=CLIENT_DB) 
        self.schema = {
                'name' : {
                    'type' : 'string',
                    'required' : True
                    },
                'email' : {
                    'type' : 'email',
                    'required' : True
                    }
                } 
    def tearDown(self):
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.mongo_client.close()
        self.client.close()

    def test_create_one_no_validator(self):
        query = {
                'name' : 'abc',
                'email' : 'qq@ww.com'
                }
        with self.assertRaises(db.mongo.MongodbValidationError):
            self.obj.create_one(query)

    def test_create_one_with_validator(self):
        validator = db.mongo.DefaultValidator(self.schema)
        query = {
                'name' : 'abc',
                'email' : 'qq@ww.com'
                }
        self.obj.validator_create = validator
        result = self.obj.create_one(query)
        result = json.loads(result)
        ret_id = result['id'] 
        result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'name' : 'abc'})
        ret = []
        for doc in result:
            ret.append(doc)
        self.assertEqual(1, len(ret))
        self.assertEqual(ret_id, str(ret[0]['_id']))
        self.assertTrue('created_at' in ret[0])
        self.assertTrue('updated_at' in ret[0])


    def test_create_multiple_with_validator(self):
        validator = db.mongo.DefaultValidator(self.schema)
        query = [
                    {
                        'name' : 'abc',
                        'email' : 'qq@ww.com'
                    } for i in range(3)
                ]
        self.obj.validator_create = validator
        result = self.obj.create_multiple(query)
        result = json.loads(result)
        self.assertEqual(3, len(result))

        
        ret_result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'name' : 'abc'})
        ret = []
        for doc in ret_result:
            ret.append(doc)
            self.assertTrue('updated_at' in doc)
            self.assertTrue('created_at' in doc)
        self.assertEqual(3, len(ret))
    
    def test_create_multiple_with_broken_query(self):
        validator = db.mongo.DefaultValidator(self.schema)
        query = [
                    {
                        'name' : 'abc',
                        'email' : 'qq@ww.com'
                    },
                    {
                        'name' : 'abc',
                        'email' : 'qq@ww.com'
                    },
                    {
                        'name' : 'abc',
                        'email' : 'qq@ww.com',
                        'created_at' : 'wow'
                    }
                ]
        self.obj.validator_create = validator
        with self.assertRaises(db.mongo.MongodbValidationError):
            result = self.obj.create_multiple(query)


class TestBaseRead(unittest.TestCase):
    def setUp(self):
        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.obj = db.mongo.Base(mongo_client=self.client, collection=CLIENT_COLLECTION, db=CLIENT_DB) 
        self.schema = {
                'name' : {
                    'type' : 'string',
                    'required' : True
                    },
                'email' : {
                    'type' : 'email',
                    'required' : True
                    }
                } 
    def tearDown(self):
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.mongo_client.close()
        self.client.close()

    def test_read_one_no_validator(self):
        query = {
                'name' : 'abc',
                'email' : 'qq@ww.com'
                }
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_one(query)
        
        with self.assertRaises(db.mongo.MongodbValidationError):
            self.obj.read_one(query)
    
    def test_read_one_with_validator(self):
        query = {
                'name' : 'abc',
                'email' : 'qq@ww.com',
                'what' : 'isthat'
                }
        validator = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_read = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_one(query)
        with self.assertRaises(db.mongo.MongodbValidationError):
            self.obj.read_one(query)
        query = {
                'name' : 'abc',
                'email' : 'qq@ww.com'
                } 
        result = json.loads(self.obj.read_one(query))
        self.assertEqual(query['name'], result['name'])

    def test_read_multiple_with_validator(self):
        query = [
                    {
                        'name' : 'abc',
                        'email' : 'qq@ww.com'
                    } for i in range(3)
               ]
        validator = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_read = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_many(query)
        r_query = {'name' : 'abc'}
        with self.assertRaises(db.mongo.MongodbValidationError):
            result = self.obj.read_multiple(r_query)
        r_query['email'] = 'qq@ww.com'
        result = self.obj.read_multiple(r_query)
        result = json.loads(result)
        self.assertEqual(len(result), 3)


class TestBaseUpdate(unittest.TestCase):
    def setUp(self):
        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.obj = db.mongo.Base(mongo_client=self.client, collection=CLIENT_COLLECTION, db=CLIENT_DB) 
        self.schema = {
                'name' : {
                    'type' : 'string'
                    },
                'email' : {
                    'type' : 'email'
                    }
                } 
    def tearDown(self):
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.mongo_client.close()
        self.client.close()

    def test_update_one_no_validator(self):
        query = {
            'name' : 'abc',
            'email' : 'qq@ww.com'
            }
        # validator = db.mongo.defaultvalidator(self.schema)
        # self.obj.validator_update = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_one(query)
        query_update = {
                'filter' : {'name' : 'abc'},
                'update' : {'$set' : {'email' : 'updated@updated.com'}}
                }
        with self.assertRaises(db.mongo.MongodbValidationError):
            self.obj.update_one(query_update) 
    
    def test_update_one_with_validator(self):
        query = {
            'name' : 'abc',
            'email' : 'qq@ww.com'
            }
        validator = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_update = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_one(query)
        query_update = {
                'filter' : {'name' : 'abc'},
                'update' : {'$set' : {'email' : 'updated@updated.com'}}
                }
        self.obj.update_one(query_update) 
                    
        result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'name' : 'abc'})
        ret = []
        for doc in result:
            ret.append(doc)
        self.assertEqual(1, len(ret))


        result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'email' : 'qq@ww.com'})
        ret = []
        for doc in result:
            ret.append(doc)
        self.assertEqual(0, len(ret))
    

class TestBaseDelete(unittest.TestCase):
    def setUp(self):
        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.obj = db.mongo.Base(mongo_client=self.client, collection=CLIENT_COLLECTION, db=CLIENT_DB) 
        self.schema = {
                'name' : {
                    'type' : 'string'
                    },
                'email' : {
                    'type' : 'email'
                    }
                }
        
    def tearDown(self):
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.mongo_client.close()
        self.client.close()

    def test_delete_no_validator(self):
        query = {
            'name' : 'abc',
            'email' : 'qq@ww.com'
            }
        # validator = db.mongo.DefaultValidator(self.schema)
        # self.obj.validator_delete = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_one(query)
        with self.assertRaises(db.mongo.MongodbValidationError):
            self.obj.delete_multiple(query)           
        # result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'name' : 'abc'})
        # ret = []
        # for doc in result:
        #     ret.append(doc)
        # self.assertEqual(0, len(ret))

    def test_delete_with_validator(self):
        query = {
            'name' : 'abc',
            'email' : 'qq@ww.com'
            }
        validator = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_delete = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_one(query)
        query = {
            'name' : 'abc',
            'email' : 'qq@ww.com'
            }
        self.obj.delete_multiple(query)           
        result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'name' : 'abc'})
        ret = []
        for doc in result:
            ret.append(doc)
        self.assertEqual(0, len(ret))


    def test_delete_multiple_with_validator(self):
        query = [{
            'name' : 'abc',
            'email' : 'qq@ww.com'
            } for i in range(3)]
        validator = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_delete = validator
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].insert_many(query)
        query = {
            'name' : 'abc',
            'email' : 'qq@ww.com'
            }
        result = self.obj.delete_multiple(query)
        result = json.loads(result)
        self.assertEqual(3, result['deleted_count'])
        result = self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].find({'name' : 'abc'})
        ret = []
        for doc in result:
            ret.append(doc)
        self.assertEqual(0, len(ret))

class TestIntegratedCase(unittest.TestCase):

    def setUp(self):
        self.mongo_client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.client = MongoClient(CLIENT_HOST, CLIENT_PORT)
        self.obj = db.mongo.Base(mongo_client=self.client, collection=CLIENT_COLLECTION, db=CLIENT_DB) 
        self.schema = {
                'name' : {
                    'type' : 'string'
                    },
                'email' : {
                    'type' : 'email'
                    }
                }
        self.schema_create = {
                'name' : {
                    'type' : 'string',
                    'required' : True
                    },
                'email' : {
                    'type' : 'email',
                    'required' : True
                    }
                }
        self.obj.validator_create = db.mongo.DefaultValidator(self.schema_create)
        self.obj.validator_read = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_update = db.mongo.DefaultValidator(self.schema)
        self.obj.validator_delete = db.mongo.DefaultValidator(self.schema)
        
    def tearDown(self):
        self.mongo_client[CLIENT_DB][CLIENT_COLLECTION].delete_many({})
        self.mongo_client.close()
        self.client.close()

    def test_integration(self):
        query = []
        from random import randint
        a = randint(30, 40)
        for i in range(0 , a):
            q = { 
                    'name' : str(i),
                    'email' : str(i) + '@test.com'
                    }
            query.append(q)
        create_result = json.loads(self.obj.create_multiple(query))
        self.assertEqual(a, len(create_result))

        target = randint(0, a)
        delete_result = json.loads(self.obj.delete_multiple({'name' : str(target)}))
        self.assertEqual(1, delete_result['deleted_count'])
        read_result = json.loads(self.obj.read_multiple({}))
        self.assertEqual(a - 1, len(read_result))
        target = (target + 1) % a
        self.obj.update_one({
                                'filter' : {'name' : str(target)},
                                'update' : {
                                    '$set' : {
                                        'email' : 'update@test.com'
                                        }
                                    }
                            })

        read_result = json.loads(self.obj.read_multiple({'email' : 'update@test.com'}))
        self.assertEqual(1, len(read_result))

 

if __name__ == '__main__':
    unittest.main()








