# The data we need to retrieve
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5.The winner of the election based on popular vote.
# Assign a variable for the file to load and the path.
#file_to_load ='Resources/election_results.csv'
#open the election results and read the file.
#election_data = open(file_to_load, 'r')
# To do: perform analysis.
# Close the file.
#election_data.close()
#file_to_load ='Resources/election_results.csv'
#open the election results and read the file.
#with open(file_to_load) as election_data:
# To do: perform analysis.
 #print(election_data)
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load=os.path.join("Resources", "election_results.csv")
#open the election results and read the file.
#with open(file_to_load) as election_data:
#print the file object.
 #print(election_data)
#import csv
#import os
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
#open the election results and read the file.
#open(file_to_save, "w")
#import csv
#import os
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
#using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
#write some data to the file.
#outfile.write("Hello World")
#Close the file
#outfile.close()
#import csv
#import os
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
#using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
#write some data to the file.
    #txt_file.write("Atapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
#import csv
#import os
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
#using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
#write some data to the file.
    #txt_file.write("Atapahoe, Denver, Jefferson")
import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
#write some data to the file.
    txt_file.write("Counties in the Election\n----------------------------\nAtapahoe\nDenver\nJefferson")


# Add our dependecies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
 file_reader = csv.reader(election_data)
 #for row in file_reader:
       # print(row)
 headers = next(file_reader)
 print(headers)