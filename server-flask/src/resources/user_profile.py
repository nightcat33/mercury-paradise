from flask import request
from flask_restful import Resource
import json

class UserProfileCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		# result = fetch_result(json_data)
		return result

class UserProfileCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None

		return result

class UserProfileUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserProfileUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserProfileReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserProfileReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserProfileDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserProfileDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

