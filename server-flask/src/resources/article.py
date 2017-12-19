from flask import request
from flask_restful import Resource
import json

import sys
import os
sys.path.insert(0, os.path.abspath('../'))

from articlesModel import Articles

class ArticleCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.create_one(json_data)
		articles_model.close()
		return result

class ArticleCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.create_multiple(json_data)
		articles_model.close()
		return result

class ArticleUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.update_one(json_data)
		articles_model.close()
		return result

class ArticleUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.update_multiple(json_data)
		articles_model.close()
		return result

class ArticleReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.read_one(json_data)
		articles_model.close()
		return result

class ArticleReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.read_multiple(json_data)
		articles_model.close()
		return result

class ArticleDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.delete_one(json_data)
		articles_model.close()
		return result

class ArticleDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		articles_model = Articles()
		articles_model.connect()
		result = articles_model.delete_multiple(json_data)
		articles_model.close()
		return result

