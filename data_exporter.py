# moet het weer naar de oorspronkelijke files krijgen!!
import pandas as pd
from pandas import DataFrame

class DataExporter:
    def __init__(self, output_path, finalbridges):
        self.output_path = output_path
        self.finalbridges = finalbridges
        # df bridges is a dataframe
        self.dfbridges = None
        self.prepareExport()

    def prepareExport(self):
        self.prepareExportSimple()

    def prepareExportSimple(self):
        pass
        # per bridge in the final bridge list, just append all the df rows per object.
        # initialize with first row
        # Extracting the 'df' property from each bridge object and storing them in a list
        #rows = [bridge.df.T for bridge in self.finalbridges]

        # Concatenating all the DataFrames in the list into one big DataFrame
        #big_df = pd.concat(rows, ignore_index=True)
        # is ignore index ok?
        #self.dfbridges = big_df


    def export(self):
        pass