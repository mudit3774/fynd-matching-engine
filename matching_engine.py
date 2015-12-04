from preferences import *
from routing_helper import * 

class MatchingEngine :
	"""Finds matching areas according to preferences"""

	def __init__(self):
		pass

	def get_isolines(self, prefs): 
		routing_helper = RoutingHelper()
		responses = [routing_helper.get_isoline_data(
			pref.primary_preferences['lat'], 
			pref.primary_preferences['lon'], 
			pref.primary_preferences['range_value'], 
			pref.primary_preferences['range_type']) 
			for pref in prefs]	
		return responses

	def get_suggestions(self, prefs):
		responses = self.__get_isolines(prefs)
		for response in responses:
			yield response

	__get_isolines = get_isolines

if __name__ == '__main__' :
	pref_1 = Preferences(19.107554, 72.896517, 10, 'time')
	pref_2 = Preferences(19.107554, 72.896517, 10, 'time')
	m = MatchingEngine()
	suggestions = m.get_suggestions([pref_1, pref_2])
	for suggestion in suggestions:
		print suggestion
