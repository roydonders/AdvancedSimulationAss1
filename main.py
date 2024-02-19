import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    #Filepath Lukas
    #lab_path = r'C:\Users\lukas\Downloads\Asim Lab1\WBSIM_Lab1_2024\WBSIM_Lab1_2024'

    #Filepath Bram

    # Fill in your own Filepath
    #Filepath Timon

    lab_path = r'C:\Users\TOT\OneDrive - Stichting EBO de Passie\Documenten\Studie\Advanced Simulation\WBSIM_Lab1_2024\WBSIM_Lab1_2024'

    #Import roads.tsv dataframe
    import_roads = pd.read_table(lab_path + '\infrastructure\_roads.tsv', low_memory=False)

    #Make a copy of the imported dataframe to bypass importing each time you want your original dataframe (due to a mistake for example)
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
        'Lon': df_roads['Lon'].values.reshape(-1) })

    # This line can be enabeled to drop missing values, see the section on 'Missing value issue' to see for which roads this would be usefull
    #df_roads_tidy = df_roads_tidy.dropna()

    df_roads_tidy = df_roads_tidy.reset_index(drop=True)

    print("hello world")

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