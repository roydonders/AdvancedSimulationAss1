import os
from typing import Union, Dict, Any

import pandas as pd
from pandas import DataFrame

from infrastructure import Infrastructure, Road, Bridge


class DataReader:
    def __init__(self):
        # The cleaned dataframe is stored in these variables. Initialized to None
        self.df_roads_original = None
        self.df_roads_tidy = None
        self.df_bridges_tidy = None
        self.roads_list = []
        self.bridges_list = []
        self.data_path = self.getDataPath()

    def getDataPath(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(__file__)

        # Define the relative path to the data folder
        relative_path = 'data'

        # Construct the absolute path by joining the script directory and the relative path
        data_folder = os.path.abspath(os.path.join(script_dir, relative_path))

        # Join subfolders
        subfolder_assignment = 'WBSIM_Lab1_2024'
        subfolder_infrastructure = 'infrastructure'

        data_path = os.path.join(data_folder, subfolder_assignment, subfolder_infrastructure)
        return data_path

    def read_data(self):
        print("Reading Data")
        self.read_roads()
        self.read_bridges()
        print("Done Reading Data")


    def read_roads(self):
        print("Reading in Roads Data...")
        # Method for reading road data
        import_roads = pd.read_table(self.data_path + '\_roads.tsv', low_memory=False)

        # Make a copy of the imported dataframe to bypass importing each time you want your original dataframe (due to a mistake for example)
        self.df_roads_original = import_roads
        df_roads = import_roads

        columns = df_roads.columns

        # Define the new column names pattern
        new_column_names = {}
        for i, col in enumerate(columns[1:], start=1):
            if i % 3 == 1:
                new_column_names[col] = 'LRP'
            elif i % 3 == 2:
                new_column_names[col] = 'Lat'
            else:
                new_column_names[col] = 'Lon'

        # Rename the columns using the dictionary
        df_roads.rename(columns=new_column_names, inplace=True)

        # reshape the DataFrame into a tidy dataset
        df_roads_tidy = pd.DataFrame({
            'Road': df_roads['road'].repeat(len(df_roads.columns) // 3),
            'LRP': df_roads['LRP'].values.reshape(-1),
            'Lat': df_roads['Lat'].values.reshape(-1),
            'Lon': df_roads['Lon'].values.reshape(-1)})

        # This line can be enabeled to drop missing values, see the section on 'Missing value issue' to see for which roads this would be usefull
        # df_roads_tidy = df_roads_tidy.dropna()

        self.df_roads_tidy = df_roads_tidy.reset_index(drop=True)
        # Possible to turn into road objects, however the following method takes very long O(n)
        #self.roads_list = Road.dataframe_to_road_objects(df_roads_tidy)

    def read_bridges(self):
        print("Reading in Bridges Data...")
        import_bridges = pd.read_excel(self.data_path + '\BMMS_overview.xlsx')
        self.df_bridges_tidy = import_bridges
        self.bridges_list = Bridge.dataframe_to_bridge_objects(import_bridges)

