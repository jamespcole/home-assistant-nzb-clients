__author__ = 'jamespcole'

import requests
import json

class SabnzbdApi(object):
	def __init__(self, base_url, api_key):
		if not base_url.endswith('/'):
			base_url = base_url + '/'
		self.BASE_URL = base_url	
		self.api_key = api_key
		self.queue = {}

	def refresh_queue(self):
		api_args = {}
		api_args['apikey'] = self.api_key
		api_args['mode'] = 'queue'
		api_args['start'] = '0'
		api_args['limit'] = '10'
		api_args['output'] = 'json'

		url = self.BASE_URL + 'api'
		response = requests.get(url, params=api_args)		

		self.queue = response.json().get('queue')

