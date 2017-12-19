# -*- coding: utf-8 -*-
"""
This module is used to connect with mongodb. This module contains base classes and functions to integrate mongodb.

We use the cerberus package as our validator framework. And we have extended it use validate email, username and id by default.

Generally, to interact with MongoDB, you should inherit from the Base object, set validator_create, validator_update, validator_read, and validator_delete accordingly. See test/test_db_mongo.py for detailed implementation.

"""
import re
import json
from pymongo import MongoClient, ReturnDocument
from cerberus import Validator
from bson import ObjectId
from datetime import datetime
import copy
import bcrypt
import string
import random

EMAIL_REGEX = re.compile(r"^[_]*([a-z0-9]+(\.|_*)?)+@([a-z][a-z0-9-]+(\.|-*\.))+[a-z]{2,6}$")
"""Email regex for validator"""

URL_REGEX = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
"""url regex for validator"""

USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9_.-]+$")
"""user name regex for validator"""

PASSWORD_REGEX = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
"""password regex for validator"""

KEYS_FORBIDDEN_TO_MODIFY = ["_id", "id", "created_at", "updated_at"]
"""keys that are forbidden to exist in create and update queries"""

KEYS_LIMITED_IN_UPDATE = ["filter", "update"]

ACTIONS_ALLOWED_IN_UPDATE_ACTION = ['$set']

class MongodbValidationError(Exception):
    """Error raised when there is a validation error"""
    pass

class DefaultValidator(Validator):
    """The Default Validator to be used and inherited in this module"""
    def _validate_type_email(self, value):
        if EMAIL_REGEX.match(value):
           return True 
    
    def _validate_type_url(self, value):
        if URL_REGEX.match(value):
            return True

    def _validate_type_id(self, value):
        if len(value) == 24:
            return True

    def _validate_type_username(self, value):
        if USERNAME_REGEX.match(value):
            return True




class Base(object):
    """The base object to be inherited by data models
        
    """
    def __init__(self,
                mongo_client=None,
                schema=None,
                collection=None,
                db=None,
                ):
        """
        Args:
            mongo_client (pymongo.MongoClient): The mongodb client
            schema (dict): A schema for cerberus.Validator
            collection (str): the name of the collection
            db (str): the name of the db
        """
        self.mongo_client = mongo_client
        self.schema = schema
        self.validator_update = None
        self.validator_delete = None
        self.validator_create = None
        self.validator_read = None
        self.collection = collection
        self.db = db

    def validate_query(self, query, validator):
        """ Preprosess the query and return the preprocessed result
        Args:
            query (JSON): the raw query of the data
            validator (cerberus.Validator): the validator used to validate this query

        Raises:
            MongodbValidationError: The query does not pass the validator


        """
        if validator is None:
            raise MongodbValidationError("Validator is None")
        if not validator.validate(query):
            error_msg = "forwarded error message:\n" + str(validator.errors)
            raise MongodbValidationError(error_msg)

    def create_one(self, query):
        """ Create method for one entry
        
        Returns: 
            str: A json string

        
        """
        self.preprocess_create_one_default(query)
        result = self.mongo_client[self.db][self.collection].insert_one(query)
        ret_id = result.inserted_id
        ret = {'id' : str(ret_id)}
        return ret
    
    def create_multiple(self, query):
        """ Create method for multiple entries
        
        Returns: 
            str: A json string
        
        returned format::

        """
        
        self.preprocess_create_multiple_default(query)
        result = self.mongo_client[self.db][self.collection].insert_many(query)
        ret_ids = result.inserted_ids
        ret = [{'id' : str(ret_id)} for ret_id in ret_ids]
        return ret


    def read_one(self, query):
        """ Read method for one entry
        
        Returns: 
            str: A json string
        
        """
        self.preprocess_read_one_default(query) 
        result = self.mongo_client[self.db][self.collection].find_one(query)
        if '_id' in result:
            result['_id'] = str(result['_id'])
        return result

    def read_multiple(self, query):
        """ Read method for multiple entries
        
        Returns: 
            str: A json string
        
        """
        self.preprocess_read_multiple_default(query)
        ret = []
        for doc in self.mongo_client[self.db][self.collection].find(query):
            if '_id' in doc:
                doc['_id'] = str(doc['_id'])
            ret.append(doc)
        return ret
    
    def update_one(self, query):
        """ Update method for one entry
       
        Returns: 
            str: A json string
        
        """
        self.preprocess_update_one_default(query)
        result = self.mongo_client[self.db][self.collection].find_one_and_update(query['filter'], query['update'], return_document=ReturnDocument.AFTER)
        if '_id' in result:
            result['_id'] = str(result['_id'])
        return result

    def update_multiple(self, query):
        """ Update method for multiple entries, not needed now
       
        Returns: 
            str: A json string
        
        TODO: 
            Implementation
        """
        pass

    def delete_one(self, query):
        """ Delete method for one entry, not needed now
        
        Returns: 
            str: A json string
        
        TODO: 
            Implementation
        """
        pass

    def delete_multiple(self, query):
        """ Delete method for multiple entries

        Returns: 
            str: A json string
        """
        self.preprocess_delete_multiple_default(query)
        result = self.mongo_client[self.db][self.collection].delete_many(query)
        return {'deleted_count' : result.deleted_count}


    def preprocess_create_one_default(self, query):
        """default method to preprocess the query for create_one methods
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
        """
        for key in KEYS_FORBIDDEN_TO_MODIFY:
            if key in query:
                raise MongodbValidationError('key: {} is forbidden'.format(key))
        self.validate_query(query, self.validator_create)

        d = datetime.now().timestamp()
        query['created_at'] = d
        query['updated_at'] = d
        return query
    
    def preprocess_create_multiple_default(self, query):
        """default method to preprocess the query for create_multiple methods
        
        Args:
            query (list): The query to be preprocessed
        
        Returns:
            list: The preprocessed query
    
        """
        for q in query:
            self.preprocess_create_one_default(q)
        return query
            
    
    def preprocess_update_one_default(self, query):
        """default method to preprocess the query for update_one methods
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
    
        """
        for key in KEYS_LIMITED_IN_UPDATE:
            if key in query:
                continue
            raise MongodbValidationError('key: {} is forbidden'.format(key))
       
        for key in query['update']:
            if key not in ACTIONS_ALLOWED_IN_UPDATE_ACTION:
                raise MongodbValidationError('key: {} is not one of the allowed actions'.format(key))
        
        for key in KEYS_FORBIDDEN_TO_MODIFY:
            if key in query['update']:
                if key in KEYS_FORBIDDEN_TO_MODIFY:
                     raise MongodbValidationError('key: {} is forbidden'.format(key))
        
        if '$set' in query['update']:    
            self.validate_query(query['update']['$set'], self.validator_update)
            d = datetime.now().timestamp()
            query['update']['$set']['created_at'] = d
            query['update']['$set']['updated_at'] = d
        return query
            
    def preprocess_update_multiple_default(self, query):
        """default method to preprocess the query for update_multiple methods
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
        """
        return self.preprocess_update_one_default(query)

    def preprocess_read_one_default(self, query):
        """default method to preprocess the query for read_one methods
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
        """
        self.validate_query(query, self.validator_read)
    
    def preprocess_read_multiple_default(self, query):
        """default method to preprocess the query for read_multiple methods
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
        """
        for doc in query:
            self.preprocess_read_one_default(query)

    def preprocess_delete_one_default(self, query):
        """default method to preprocess the query for delete_one methods, not needed now
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
    
        TODO:
            Implementation
        """
    
    def preprocess_delete_multiple_default(self, query):
        """default method to preprocess the query for delete_multiple methods
        
        Args:
            query (dict): The query to be preprocessed
        
        Returns:
            dict: The preprocessed query
        """
        self.validate_query(query, self.validator_delete)

