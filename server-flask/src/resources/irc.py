from flask import request
from flask_restful import Resource
import json

class IrcCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		# result = fetch_result(json_data)
		return result

class IrcCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None

		return result

class IrcUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class IrcUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class IrcReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class IrcReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class IrcDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class IrcDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

