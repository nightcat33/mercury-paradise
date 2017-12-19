from flask import request
from flask_restful import Resource
import json

import sys
import os
sys.path.insert(0, os.path.abspath('../'))

from pageModel import Pages

class PageCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.create_one(json_data)
		page_model.close()
		return result

class PageCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.create_multiple(json_data)
		page_model.close()
		return result

class PageUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.update_one(json_data)
		page_model.close()
		return result

class PageUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.update_multiple(json_data)
		page_model.close()
		return result

class PageReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.read_one(json_data)
		page_model.close()
		return result

class PageReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.read_multiple(json_data)
		page_model.close()
		return result

class PageDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.delete_one(json_data)
		page_model.close()
		return result

class PageDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		page_model = Pages()
		page_model.connect()
		result = page_model.delete_multiple(json_data)
		page_model.close()
		return result


