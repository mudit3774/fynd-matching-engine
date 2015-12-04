class Preferences: 
	"""Records user preferences"""
	
	def __init__(self, lat, lon, range_value, range_type): 
		self.primary_preferences = {
				lat : lat,
				lon : lon, 
				range_value : range_value, 
				range_type : range_type,
				}
	
	def __str__(self):
		return str(self.primary_preferences)

if __name__ == '__main__':
	pref = Preferences(19.107554, 72.896517, 10, 'time')
	print pref

