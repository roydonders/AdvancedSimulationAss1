from data_reader import DataReader
from data_exporter import DataExporter
from problem_identifier import ProblemIdentifier


def main():
    # Main program method providing an overview
    print("Start Data Cleaning!")

    # Import all data
    reader = DataReader()
    reader.read_data()

    # Collect results of read data:
    # In DataFrames (df bridges not used currently)
    df_roads_tidy = reader.df_roads_tidy
    df_bridges_tidy = reader.df_bridges_tidy
    # And in lists of objects (roads not used currently)
    roads = reader.roads_list
    print("Roads are read from roads_list")
    bridges = reader.bridges_list
    print("Bridges are read from bridges_list")

    # Identify and Solve data problems
    print("Identifying Problems in the Data for roads and bridges")
    pi = ProblemIdentifier(roads, bridges)
    print("Cleaning the Data using Heuristics")
    finalroads, finalbridges = pi.solve()
    print("Road and bridge issues solved")

    # Output the changed files
    output_path = reader.data_path
    exporter = DataExporter(output_path, finalbridges)
    exporter.export()
    print("Done Cleaning!\n 'CLEANBMMS_overview.xlsx' is generated")

    # the implementation of the roads analysis is not fully complete at this time
    # in the submitted folder there is a cleaned roads.tsv file. that has been
    # cleaned in another environment when setting up pycharm.
    print("The implementation of generating '_roads.tsv' is not yet complete.\n "
          "Please check the submitted folder for the cleaned '_roads.tsv'")

    # try_out = find_road_df(n).copy()
    #
    # df_cleaned = pd.DataFrame(
    #     columns=['Road', 'LRP', 'Lat', 'Lon'])  # New empty dataframe in which eveything gets stored.
    #
    # for i in range(0, 900):  # Clean every road in the dataframe
    #     print(i)
    #     try_out = find_road_df(i).copy()
    #     if i == 28 or i == 94 or i == 766 or i == 839:  # The following roads don't have values
    #         continue
    #     if i == 11:  # N111 is wrongly placed
    #         try_out.loc[14872, 'Lat'] += 1
    #     if i == 68:  # Corrected locations are starting point which are wrongly placed
    #         try_out.loc[92092, 'Lat'] = 24.842448
    #         try_out.loc[92092, 'Lon'] = 88.141263
    #     if i == 80:
    #         try_out.loc[107859, 'Lat'] += 1
    #     if i == 260:
    #         try_out.loc[350480, 'Lat'] = 23.282393
    #         try_out.loc[350480, 'Lon'] = 91.121182
    #     if i == 299:
    #         try_out.loc[403052, 'Lon'] -= 1
    #     if i == 334:
    #         try_out.loc[450290, 'Lat'] -= 1
    #     if i == 493:
    #         try_out.loc[664564, 'Lat'] -= 1
    #     if i == 545:
    #         try_out.loc[734660, 'Lat'] += 1
    #     if i == 583:
    #         try_out.loc[785888, 'Lat'] += 3
    #     if i == 589:
    #         try_out.loc[794035, 'Lon'] -= 1
    #     if i == 691:
    #         try_out.loc[931621, 'Lat'] += 4
    #     if i == 739:
    #         try_out.loc[996210, 'Lon'] -= 0.2
    #     if i == 753:  # Second to last point is wrongly placed
    #         try_out.loc[1015123, 'Lon'] -= 1
    #     if i == 758:
    #         try_out.loc[1021784, 'Lon'] += 0.05
    #     if i == 781:
    #         try_out.loc[1052804, 'Lon'] -= 0.1
    #     if i == 789:
    #         # try_out.loc[1063572, 'Lon'] -= 0.1
    #         try_out.loc[1063572, 'Lat'] -= 1
    #     if i == 829:
    #         try_out.loc[1117492, 'Lat'] -= 0.05
    #         try_out.loc[1117492, 'Lon'] += 0.01
    #     if i == 853:
    #         try_out.loc[1149844, 'Lon'] += 1
    #     try:
    #         FR_df3 = correct_roads(try_out)
    #     except:
    #         print(f"Ohhh ik heb {i} gecheat ;p")
    #         FR_df3 = find_road_df(i).copy()
    #
    #     df_cleaned = pd.concat([df_cleaned, FR_df3])


if __name__ == "__main__":
    main()
