# moet het weer naar de oorspronkelijke files krijgen!!
import pandas as pd
from pandas import DataFrame

class DataExporter:
    def __init__(self, output_path, finalbridges):
        self.output_path = output_path
        self.finalbridges = finalbridges
        self.dfbridges = DataFrame()
        self.prepareExport()

    def prepareExport(self):
        self.prepareExportSimple()

    def prepareExportSimple(self):
        # per bridge in the final bridge list, just append all the df rows per object.
        # initialize with first row
        firstrow = self.finalbridges[0].df
        self.dfbridges = firstrow
        for bridge in self.finalbridges:
            self.dfbridges.append(bridge.df)

    def export(self):
        pass