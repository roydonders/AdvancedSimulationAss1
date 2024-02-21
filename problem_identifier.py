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
    def __init__(self):
        # checks for problems
        # If lat/long not in bangladesh - check if this or this is the case
        pass

    def isInsideBangladesh(self, b):
        pass


