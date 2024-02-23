import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics as stat

# import pd.read_table data/_roads.tsv"
# data reader timon
# levert al tidy data

# make a df of the roads.tsv

# class roads in infrastructure.py
# roads objecten worden nog niet gebruikt in dit program

# functies voor schoonmaken van roads data


class RoadCleaner:
    def __init__(self):
        pass

    @staticmethod
    def find_road_df(n, df_roads_tidy):
        """This function takes an integer as input and finds the n-th road in the datafile
            it returns the subsetted dataframe related to that road"""

        road_specified = df_roads_tidy['Road'].unique()[n]

        road_specified_df = df_roads_tidy.loc[df_roads_tidy['Road'] == road_specified]

        return road_specified_df

    @staticmethod
    def correct_road(self, index, file):
        # Make a copy of the DataFrame to avoid modifying the original data
        corrected_file = self.file.copy()

        # Calculate the average values for 'Lat' and 'Lon' and assign them to the corresponding row
        corrected_file.loc[index + 1, 'Lat'] = (file.loc[index, 'Lat'] + file.loc[index + 2, 'Lat']) / 2
        corrected_file.loc[index + 1, 'Lon'] = (file.loc[index, 'Lon'] + file.loc[index + 2, 'Lon']) / 2

        return corrected_file

    @staticmethod
    def load_and_clean(file):
        road_length = []
        for i in file.index[:-1]:
            road_length.append(
                math.sqrt((file['Lat'][i] - file['Lat'][i + 1]) ** 2 + (file['Lon'][i] - file['Lon'][i + 1]) ** 2))

        while road_length and road_length[-1] != road_length[-1]:
            road_length.pop()

        road_length = [1 if math.isnan(x) else x for x in road_length]

        return road_length

    @staticmethod
    def check_boundaries(road_list, file, index):
        # calculate  the mean of the roads
        mean = stat.mean(road_list)
        # set a threshold of 10
        TH = 10  # Threshold

        if road_list[0] > (mean * TH):
            if road_list[1] < (mean * TH):
                print('First one of road', file['Road'][index], 'is possibly badly placed')
                return True

        if road_list[-1] > (mean * TH):
            if road_list[-2] < (mean * TH):
                print('Last one of road', file['Road'][index], 'is possibly badly placed')
                return True

        else:
            return False

    # zat in de code van bram maar wordt volgens mij niet gebruikt
    # def clean_sheet(file):
    #     cleaned_file = file.copy()
    #
    #     for i in range(file.index[0], a):
    #         if np.isnan(file['Lat'][i]) or np.isnan(file['Lon'][i]):
    #             if not np.isnan(file['Lat'][i]) or np.isnan(file['Lon'][i]):
    #                 file = single_NaN_cleaner(file.index[0] + i, file)
    #     return

    def check_roads(self, road_list, file):
        # calculate  the mean of the roads
        mean = stat.mean(road_list)
        # set a threshold of 10
        TH = 10  # Threshold
        # these need to be made global

        size_list = len(road_list)
        for i in range(size_list):
            if road_list[i] > mean * TH or road_list[i] > 0.01:
                if road_list[i+1] > (mean * TH) or road_list[i+1] > 0.01:
                    index_road = file.index[i]
                    file = self.correct_road(index_road, file)
        return file

    @staticmethod
    def correct_multiple(index, file, wrongs):
        corrected_file = file.copy()

        for i in range(wrongs):
            m = i + 1
            checker = index + m

            # Use .loc to set values in the DataFrame
            corrected_file.loc[checker, 'Lat'] = file['Lat'][index] + m * (
                        file['Lat'][index + wrongs + 1] - file['Lat'][index]) / (wrongs + 1)
            corrected_file.loc[checker, 'Lon'] = file['Lon'][index] + m * (
                        file['Lon'][index + wrongs + 1] - file['Lon'][index]) / (wrongs + 1)

        return corrected_file

    def check_multiple(self, road_list, file):
        # calculate  the mean of the roads
        mean = stat.mean(road_list)
        # set a threshold of 10
        TH = 10  # Threshold
        # these need to be made global

        size_list = len(road_list)
        corrected_file = file.copy()
        check_list = road_list.copy()
        for i in range(size_list):  # Adjust range to avoid index out of bounds
            if check_list[i] > mean * TH:
                if check_list[i + 1] < (mean * TH):
                    z = 1
                    while check_list[i + z] < (mean * TH) and i + z < size_list:
                        z = z + 1
                    index_road = file.index[i]
                    corrected_file = self.correct_multiple(index_road, corrected_file, z)
                    check_list = self.load_and_clean(corrected_file)
        return corrected_file

    # deze nog fixen van lukas om naar tsv te exporteren
    @staticmethod
    def df_to_tsv(df_cleaned):
        # Create a multi-index with Road and Index
        df_cleaned.set_index(['Road', df_cleaned.groupby(['Road']).cumcount() + 1], inplace=True)

        # Reshape the dataframe
        df_output = df_cleaned.unstack().sort_index(axis=1, level=1)

        # Flatten the columns
        df_output.columns = ['_'.join(map(str, i)) for i in df_output.columns]
        df_output.reset_index(inplace=True)

        # Write cleaned DataFrame to TSV file called '_roads_cleaned.tsv'
        file_path = r'AdvancedSimulationAss1\roads_cleaned.tsv'
        df_output.to_csv(file_path, sep='\t', index=False)
        return


# correct_road en correct multiple geven de hele roads df's

# Methode van Lukas op whatsapp gebruiken om df om te zetten naar df

#
# # Eerste cell commands
# road_list = load_and_clean(FR_df1)
#
# mean = stat.mean(road_list)
# TH = 10  # Threshold
#
# # tweede cell commands
# check_boundaries(road_list, FR_df1, 0)
#
# # check roads commands
# FR_df1_c = FR_df1.copy()
#
# FR_df2 = check_roads(road_list,FR_df1)
#
# # check multiple commands
# # clean_file = cleanup_file(FR_d2)
# # road_list = length_check(clean_file)
#
# FR_df3 = check_multiple(road_list, FR_df2)
