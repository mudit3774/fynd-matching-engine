import requests
import json 
import config

def get_formatted_params(lat, lon, range_value, range_type):
	params = {
		 	'lat' : lat, 
			'lon' : lon, 
			'range' : range_value, 
			'range_type' : range_type, 
		}
	return "&".join(map(lambda x: '{}={}'.format(x, params[x]),
			params.keys()))
		
def get_isoline_url(lat, lon, range_value, range_type):
	isolines_formatted_params = get_formatted_params(lat, lon,
			range_value, range_type)
	return '{}{}?{}'.format(
			config.routing_base_url, 
			config.isolines_url,
			isolines_formatted_params
			)

def get_isoline_data(lat, lon, range_value, range_type):
	full_url = get_isoline_url(lat, lon, range_value, range_type)	
	response = requests.get(full_url)
	return response.json()

def main(): 
	isoline = get_isoline_data(19.107554, 72.896517, 10, 'time')
	print isoline['features'][1]['geometry']['coordinates']

if __name__ == '__main__' :
	main()
