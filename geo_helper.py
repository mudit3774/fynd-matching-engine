from shapely.geometry.polygon import Polygon

class GeoHelper:
	"""Geo related function helper"""

	def __init__(self):
		pass

	def get_polygon_intersection(self, polygons):
		shapely_polygons = map(lambda polygon : Polygon(
			map(lambda x: tuple(x), polygon[0])), polygons)
		return reduce(lambda x,y: x.intersects(y), shapely_polygons)
