import pandas as pd
from pandas import DataFrame

from infrastructure import Infrastructure, Bridge
from bangladesh import Bangladesh

class DataQualityProblem:
    def __init__(self, infrastructure, issue):
        self.infrastructure = infrastructure
        self.issue = issue

class OutOfRangeProblem(DataQualityProblem):
    def __init__(self, inf):
        super().__init__(inf, "Out of range")

class LatLongSwitchedProblem(DataQualityProblem):
    def __init__(self, inf):
        super().__init__(inf, "Lat/Long switched")

class IncorrectDecimalProblem(DataQualityProblem):
    def __init__(self, inf):
        super().__init__(inf, "Incorrect decimal")


class ProblemIdentifier:
    def __init__(self, roads, bridges):
        # checks for problems
        # If lat/long not in bangladesh - check if this or this is the case
        self.origroads = roads
        self.origbridges = bridges
        self.correctroads = None
        self.correctbridges = None
        self.problematicbridges = None

    def solve(self):
        self.solve_roads()
        self.solve_bridges()
        return (self.correctroads, self.correctbridges)

    def solve_roads(self):
        pass

    def solve_bridges(self):
        self.sort_bridges()
        self.solve_prob_bridges()

    def sort_bridges(self):
        # Probably a faster method exists
        self.correctbridges = self.bridges_inside_country()
        self.problematicbridges = self.bridges_outside_country()
        # Output for debugging
        ncorrect = len(self.correctbridges)
        print(ncorrect, "bridges within country (by polygon approximation) - assumed to be correct")

    def solve_prob_bridges(self):
        # First try to see if we can fix bridges that have lat and long in wrong order
        self.check_and_fix(self.fixableLatLong, self.fixBridgesLatLong)
        # Then see if we can approximate by chainage




    def bridges_inside_country(self):
        bridges = self.origbridges
        bridges_in_country = []
        for bridge in bridges:
            is_in_country = bridge.inBangladeshPolygon()
            if (is_in_country):
                bridges_in_country.append(bridge)

        return bridges_in_country

    def bridges_outside_country(self):
        bridges = self.origbridges
        bridges_outside_country = []
        for bridge in bridges:
            is_in_country = bridge.inBangladeshSimple()
            if (not is_in_country):
                bridges_outside_country.append(bridge)

        return bridges_outside_country

    def check_and_fix(self, condition, fix):
        # Only works for bridges atm
        input_list = self.problematicbridges
        fixable_elements = []
        n = len(input_list)
        # Iterate over the list backwards to avoid index shifting when popping elements
        for i in range(n - 1, -1, -1):
            current_item = input_list[i]
            if condition(current_item):
                fixable_elements.append(input_list.pop(i))

        fix(fixable_elements)
        self.problematicbridges = input_list

        #output messages
        nfixable = len(fixable_elements)
        print(nfixable, "bridges fixed by applying method", fix.__name__)

    def fixableLatLong(self, bridge):
        lat = bridge.lon
        lon = bridge.lat
        # Entered the other way around
        latlongswapped = Bangladesh.polygonWithinCountry(lat,lon)
        return latlongswapped

    def fixBridgesLatLong(self, bridges):
        for bridge in bridges:
            self.fix_lat_long(bridge)
            self.update_df_lat_long(bridge)
            self.correctbridges.append(bridge)


    def fix_lat_long(self, bridge):
        lat = bridge.lat
        lon = bridge.lon
        bridge.lat = lon
        bridge.lon = lat

    def update_df_lat_long(self, bridge):
        df = bridge.df
        df['lon'] = bridge.lon
        df['lat'] = bridge.lat

    # Provides a dict(!) with value if the bridge is inside or outside bangladesh
    #Unused methods
    def bridges_in_country(bridges):
        bridges_in_country = {}
        for bridge in bridges:
            is_within_country = bridge.inBangladeshSimple()
            bridges_in_country[bridge] = is_within_country
        return bridges_in_country
    def filter_not_in_dict(pair):
        key, value = pair
        if value == False:
            return True  # keep pair in the filtered dictionary
        else:
            return False  # filter pair out of the dictionary




