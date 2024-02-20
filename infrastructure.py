import pandas as pd
from pandas import DataFrame

class Infrastructure:
    def __init__(self):
        pass

class Road(Infrastructure):
    def __init__(self, df):
        super().__init__()
        self.lon = df['lon']
        self.lat = df['lat']
        self.lrp = df['lrp']
        self.lon2 = df['lon2']
        self.lat2 = df['lat2']
        self.lrp2 = df['lrp2']

class Bridge(Infrastructure):
    def __init__(self, df):
        super().__init__()
        self.df = df
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