import pandas as pd
from pandas import DataFrame

from infrastructure import Infrastructure

class DataQualityProblem:
    def __init__(self, infrastructure, issue):
        self.infrastructure = infrastructure
        self.issue = issue

class OutOfRangeProblem(DataQualityProblem):
    def __init__(self, inf):
        super().__init__(inf, "Out of range")

class IncorrectDecimalProblem(DataQualityProblem):
    def __init__(self, inf):
        super().__init__(inf, "Incorrect decimal")

class ProblemIdentifier:
    def __init__(self, file_path):
        # checks for problems
        pass

