import requests
import json 
import config

class RoutingHelper :
	"""Interfaces with the routing service"""

	def __init__(self):
		pass

	def get_formatted_params(self, lat, lon, range_value, range_type):
		params = {
			 	'lat' : lat, 
				'lon' : lon, 
				'range' : range_value, 
				'range_type' : range_type, 
			}
		return "&".join(map(lambda x: '{}={}'.format(x, params[x]),
			params.keys()))
		
	def get_isoline_url(self, lat, lon, range_value, range_type):
		isolines_formatted_params = self.__get_formatted_params(lat, lon,
				range_value, range_type)
		return '{}{}?{}'.format(
				config.routing_base_url, 
				config.isolines_url,
				isolines_formatted_params
				)

	def get_isoline_data(self, lat, lon, range_value, range_type):
		full_url = self.__get_isoline_url(lat, lon, range_value, range_type)	
		response = requests.get(full_url)
		return response.json()

	__get_isoline_url = get_isoline_url
	__get_formatted_params = get_formatted_params

if __name__ == '__main__' :
	routing_helper = RoutingHelper()
	isoline = routing_helper.get_isoline_data(19.107554, 72.896517, 10, 'time')
	print isoline['features'][1]['geometry']['coordinates']

