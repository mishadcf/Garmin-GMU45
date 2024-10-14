import pandas as pd
import os

dir_path = "/Users/antonfreidin/python-garminconnect/"

runs_list = []

# Create a list of files that contain "running" in their filename and have a .csv extension
for path in os.listdir(dir_path):
    if "running" in path and path.endswith(".csv"):
        runs_list.append(os.path.join(dir_path, path))  # Append the full file path


print(runs_list)
# # List to store DataFrames
# dfs = []

# # Iterate over the filenames and read them into DataFrames
# for filename in runs_list:
#     df = pd.read_csv(filename)
#     dfs.append(df)  # Append each DataFrame to the list

# # Concatenate all DataFrames in the list
# all_dfs = pd.concat(dfs, ignore_index=True)

# # Display the combined DataFrame
# print(all_dfs)
