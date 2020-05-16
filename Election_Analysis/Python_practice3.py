# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis1.txt")
counties = ["Arapahoe","Denver","Jefferson"]
voting_data = []
voting_data.append({"county":"Arapahoe", "voters":24801})
voting_data.append({"county":"Denver", "voters":306055})
voting_data.append({"county":"Jefferson", "voters":38855})
print(voting_data)
#counties_dict = {"Arapahoe": 24801, "Denver": 306055, "Jefferson": 38855}
#county_names=[]
#for county, voters in counties_dict.items():
    #print( str(county) + " : " + str(voters) )