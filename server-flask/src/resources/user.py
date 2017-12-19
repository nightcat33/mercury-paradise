from flask import request
from flask_restful import Resource
import json
import os
import sys

class UserCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		# result = fetch_result(json_data)
		return result

class UserCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None

		return result

class UserUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UserDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result







