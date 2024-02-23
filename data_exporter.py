# moet het weer naar de oorspronkelijke files krijgen!!
import pandas as pd
from pandas import DataFrame

class DataExporter:
    def __init__(self, output_path, finalbridges):
        # Output path wordt nog niet in deze methode gebruikt, we exporteren het naar de hoofdfolder
        # Dit is voor de duidelijkheid, om te voorkomen dat je verwarring krijgt tussen files in infrastructure.
        self.output_path = output_path
        self.finalbridges = finalbridges
        # df bridges is a dataframe
        self.dfbridges = DataFrame()

        # filenames
        self.bridges_file_name = 'CLEANBMMS_overview.xlsx'

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
        self.exportRoads()
        self.exportBridges()

    def exportRoads(self):
        pass

    def exportBridges(self):
        f = self.bridges_file_name
        writer = pd.ExcelWriter(f)
        self.dfbridges.to_excel(writer, sheet_name='BMMS_overview', index=False)
        writer.close()
        print("Cleaned Bridges succesfully written to Excel")