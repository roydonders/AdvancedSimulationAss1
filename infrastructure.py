import pandas as pd
from pandas import DataFrame
from bangladesh import Bangladesh

class Infrastructure:
    def __init__(self):
        pass

class Road(Infrastructure):
    def __init__(self, df):
        super().__init__()
        self.road = df['Road']
        self.lon = df['Lon']
        self.lat = df['Lat']
        self.lrp = df['LRP']

    def dataframe_to_road_objects(df):
        roads = []
        for _, row in df.iterrows():
            road_obj = Road(row)
            roads.append(road_obj)
        return roads

class Bridge(Infrastructure):
    def __init__(self, s):
        super().__init__()
        # Initialize all properties
        self.km = s['km']
        self.type = s['type']
        self.LRPName = s['LRPName']
        self.name = s['name']
        self.length = s['length']
        self.condition = s['condition']
        self.structureNr = s['structureNr']
        self.roadName = s['roadName']
        self.chainage = s['chainage']
        self.width = s['width']
        self.constructionYear = s['constructionYear']
        self.spans = s['spans']
        self.zone = s['zone']
        self.circle = s['circle']
        self.division = s['division']
        self.sub_division = s['sub-division']  # Changed to sub_division because variable names cannot contain hyphens
        self.lat = s['lat']
        self.lon = s['lon']
        self.EstimatedLoc = s['EstimatedLoc']
        # Lastly keep a copy of the dataframe by modifying the Series to a dataframe.
        # This is done for easier modification later.
        df = s.to_frame().T
        self.df = df

    def dataframe_to_bridge_objects(df):
        bridges = []
        for _, row in df.iterrows():
            bridge_obj = Bridge(row)
            bridges.append(bridge_obj)
        return bridges

    def getLocation(self):
        return (self.lat,self.lon)

    def inBangladeshSimple(self):
        location = self.getLocation()
        lat = location[0]
        lon = location[1]
        withinlon = Bangladesh.latWithinCountry(lat)
        withinlat = Bangladesh.lonWithinCountry(lon)
        withinbangladesh = withinlat and withinlat
        return withinbangladesh

    def inBangladeshPolygon(self):
        location = self.getLocation()
        lat = location[0]
        lon = location[1]
        withinbangladesh = Bangladesh.polygonWithinCountry(lon,lat)
        return withinbangladesh




