import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_reader import DataReader

def main():
    #Filepath Lukas
    #lab_path = r'C:\Users\lukas\Downloads\Asim Lab1\WBSIM_Lab1_2024\WBSIM_Lab1_2024'

    #Filepath Bram

    # Fill in your own Filepath
    #Filepath Timon

    lab_path = r'C:\Users\TOT\OneDrive - Stichting EBO de Passie\Documenten\Studie\Advanced Simulation\WBSIM_Lab1_2024\WBSIM_Lab1_2024'

    #Import roads.tsv dataframe
    reader = DataReader(lab_path)

    # This function takes an integer as input and finds the n-th road in the datafile
    # it returns the subsetted dataframe related to that road

    def find_road_df(n, df=df_roads_tidy):
        road_specified = df['Road'].unique()[n]

        road_specified_df = df.loc[df['Road'] == road_specified]

        return road_specified_df

    # Here the function is used to define x and y
    # Change n to view a different road, you can go as high as 884

    n=1
    y = find_road_df(n)['Lat']
    x = find_road_df(n)['Lon']

    # x and y are then plotted and a lineoverlay is used to connect the dots

    fig, ax = plt.subplots(figsize=(8,8), dpi=100)
    ax.scatter(x, y, s=2)
    ax.plot(x, y,linestyle='-', color='black', linewidth=1, alpha=0.2)
    plt.show()


if __name__ == "__main__":
    main()
#test

#extra toevoeging voor de push, kan straks weg