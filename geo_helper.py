from shapely.geometry.polygon import Polygon

class GeoHelper:
	"""Geo related function helper"""

	def __init__(self):
		pass

	def get_polygon_intersection(self, polygons):
		shapely_polygons = map(lambda polygon : Polygon(
			map(lambda x: tuple(x), polygon[0])), polygons)
		for i in range(1, len(shapely_polygons)):
			shapely_polygons[0].intersects(shapely_polygons[i])
		return shapely_polygons[0]
