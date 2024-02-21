# moet het weer naar de oorspronkelijke files krijgen!!
import pandas as pd
from pandas import DataFrame

class DataExporter:
    def __init__(self, output_path, finalbridges):
        self.output_path = output_path
        self.finalbridges = finalbridges
        # df bridges is a dataframe
        # cheap way to get the column names, just get the first one of the list
        cols = finalbridges[0].df.index.tolist()
        self.dfbridges = DataFrame()
        self.prepareExport()

    def prepareExport(self):
        print("Preparing Export")
        self.prepareExportSimple()

    def prepareExportSimple(self):
        # per bridge in the final bridge list, just append all the df rows per object.
        # initialize with first row
        # Extracting the 'df' property from each bridge object and storing them in a list
        rows = [bridge.df for bridge in self.finalbridges]

        # Concatenating all the DataFrames in the list into one big DataFrame
        # Extracting the 'df' property from each bridge object and storing them in a list

        # Concatenating all the DataFrames in the list into one big DataFrame
        big_df = pd.concat(rows, ignore_index=True)
        # is ignore index ok?
        # methode werkt niet, geklooi met series/df appenden.
        self.dfbridges = big_df

    def export(self):
        print("Exporting - WIP")
        pass