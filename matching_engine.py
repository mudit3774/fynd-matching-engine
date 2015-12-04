from preferences import *
from routing_helper import * 

class MatchingEngine :
	"""Finds matching areas according to preferences"""

	def __init__(self):
		pass

	def get_isolines(self, prefs): 
		routing_helper = RoutingHelper()
		isolines = [routing_helper.get_isoline_data(
			pref.primary_preferences['lat'], 
			pref.primary_preferences['lon'], 
			pref.primary_preferences['range_value'], 
			pref.primary_preferences['range_type']) 
			for pref in prefs]	
		return isolines
	
	def get_isoline_polygons(self, isolines):
		return map(lambda x: x['features'][1]['geometry']['coordinates'], 
			isolines)

	def get_intersection_polygon(self, isolines):
		polygons = self.__get_isoline_polygons(isolines)
		return polygons[0]

	def get_suggestions(self, prefs):
		isolines = self.__get_isolines(prefs)
		return self.__get_intersecting_polygon(isolines)

	__get_isolines = get_isolines
	__get_isoline_polygons = get_isoline_polygons
	__get_intersecting_polygon = get_intersection_polygon

if __name__ == '__main__' :
	pref_1 = Preferences(19.107554, 72.896517, 10, 'time')
	pref_2 = Preferences(19.107554, 72.896517, 10, 'time')
	m = MatchingEngine()
	suggestions = m.get_suggestions([pref_1, pref_2])
	print suggestions
