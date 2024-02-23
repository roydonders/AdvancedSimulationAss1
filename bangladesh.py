from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
class Bangladesh(object):

    @staticmethod
    def lonWithinCountry(longitude):
        higherthanleftbound = longitude > 88
        lowerthanrightbound = longitude < 93
        withinlon = higherthanleftbound and lowerthanrightbound
        return withinlon
    @staticmethod
    def latWithinCountry(latitude):
        higherthanlowerbound = latitude > 20.5
        lowerthanupperbound = latitude < 27
        withinlat = higherthanlowerbound and lowerthanupperbound
        return withinlat
    @staticmethod
    def polygonWithinCountry(longitude, latitude):
        # This can be done a lot better using shapefiles, but assignment description recommends to go for a simpler implementation
        # Define Bangladesh's boundary coordinates - approximation
        bangladesh_boundary = [
            (88.0473, 26.6316),
            (92.6733, 26.4465),
            (92.2696, 20.7861),
            (89.0319, 21.9430),
            (88.0844, 23.4844),
            (88.0473, 26.6316)
        ]

        # Create a Polygon object for Bangladesh's boundary
        bangladesh_polygon = Polygon(bangladesh_boundary)

        # Create a Point object for the given latitude and longitude
        point = Point(longitude, latitude)

        # Check if the point is inside Bangladesh
        return bangladesh_polygon.contains(point)

