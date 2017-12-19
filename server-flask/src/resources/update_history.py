from flask import request
from flask_restful import Resource
import json

class UpdateHistoryCreateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		# result = fetch_result(json_data)
		return result

class UpdateHistoryCreateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UpdateHistoryUpdateOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UpdateHistoryUpdateMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UpdateHistoryReadOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UpdateHistoryReadMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UpdateHistoryDeleteOne(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result

class UpdateHistoryDeleteMultiple(Resource):
	def post(self):
		json_data = request.get_json(force=True)
		result = None
		return result


