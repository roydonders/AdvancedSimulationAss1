import pandas as pd
from pandas import DataFrame

from infrastructure import Infrastructure, Bridge

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

    def solve_prob_bridges(self):
        pass


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




