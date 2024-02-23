import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl as opl

from data_reader import DataReader
from data_exporter import DataExporter
from problem_identifier import ProblemIdentifier

def main():
    print("Start Data Cleaning!")

    #Import all data
    reader = DataReader()
    reader.read_data()

    #Collect results of read data:
    # In DataFrames (df bridges not used currently)
    df_roads_tidy = reader.df_roads_tidy
    df_bridges_tidy = reader.df_bridges_tidy
    # And in lists of objects (roads not used currently)
    roads = reader.roads_list
    bridges = reader.bridges_list

    # Identify and Solve data problems
    print("Identifying Problems in the Data")
    pi = ProblemIdentifier(roads,bridges)
    print("Cleaning the Data using Heuristics")
    finalroads, finalbridges = pi.solve()


    # Output the changed files
    output_path = reader.data_path
    exporter = DataExporter(output_path, finalbridges)
    exporter.export()
    print("Done Cleaning!")
    # Oude methode lukas
    # This function takes an integer as input and finds the n-th road in the datafile
    # it returns the subsetted dataframe related to that road
    #def find_road_df(n, df=df_roads_tidy):
    #    road_specified = df['Road'].unique()[n]

    #    road_specified_df = df.loc[df['Road'] == road_specified]

    #    return road_specified_df

    # Here the function is used to define x and y
    # Change n to view a different road, you can go as high as 884

    #n=1
    #y = find_road_df(n)['Lat']
    #x = find_road_df(n)['Lon']

    # x and y are then plotted and a lineoverlay is used to connect the dots
    #fig, ax = plt.subplots(figsize=(8,8), dpi=100)
    #ax.scatter(x, y, s=2)
    #ax.plot(x, y,linestyle='-', color='black', linewidth=1, alpha=0.2)
    #plt.show()




if __name__ == "__main__":
    main()
