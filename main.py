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
    print("Done Cleaning!")


if __name__ == "__main__":
    main()
