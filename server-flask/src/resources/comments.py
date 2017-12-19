from flask import request
from flask_restful import Resource
import json
import sys
import os
sys.path.insert(0, os.path.abspath('../'))

from commentsModel import Comments

class CommentsCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.create_one(json_data)
		comments_model.close()
		return result

class CommentsCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.create_multiple(json_data)
		comments_model.close()
		return result

class CommentsUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.update_one(json_data)
		comments_model.close()
		return result

class CommentsUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.update_multiple(json_data)
		comments_model.close()
		return result

class CommentsReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.read_one(json_data)
		comments_model.close()
		return result

class CommentsReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.read_multiple(json_data)
		comments_model.close()
		return result

class CommentsDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.delete_one(json_data)
		comments_model.close()
		return result

class CommentsDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		comments_model = Comments()
		comments_model.connect()
		result = comments_model.delete_multiple(json_data)
		comments_model.close()
		return result

