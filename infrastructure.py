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
    def __init__(self, df):
        super().__init__()
        self.df = df.to_frame()
        self.km = self.df['km']
        self.type = self.df['type']
        self.LRPName = self.df['LRPName']
        self.name = self.df['name']
        self.length = self.df['length']
        self.condition = self.df['condition']
        self.structureNr = self.df['structureNr']
        self.roadName = self.df['roadName']
        self.chainage = self.df['chainage']
        self.width = self.df['width']
        self.constructionYear = self.df['constructionYear']
        self.spans = self.df['spans']
        self.zone = self.df['zone']
        self.circle = self.df['circle']
        self.division = self.df['division']
        self.sub_division = self.df[
            'sub-division']  # Changed to sub_division because variable names cannot contain hyphens
        self.lat = self.df['lat']
        self.lon = self.df['lon']
        self.EstimatedLoc = self.df['EstimatedLoc']

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





