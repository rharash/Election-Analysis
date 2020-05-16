# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis1.txt")
# Initialize a total vote counter.

total_votes = 0
county = ["Arapahoe","Denver","Jefferson"]
county_votes = []
county_votes.append({"county":"Arapahoe", "voters":24801})
county_votes.append({"county":"Denver", "voters":306055})
county_votes.append({"county":"Jefferson", "voters":38855})
print(county_votes)

# county options and county votes.
county_options = [county]
#county_votes = {}
# Track the winning county, vote count, and percentage.
winning_county = ""
winningcounty_count = 0
winningcounty_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county, add the
        # the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for county in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county's results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning county.
        if (votes > winningcounty_count) and (vote_percentage > winningcounty_percentage):
            winningcounty_count = votes
            winning_county = county
            winningcounty_percentage = vote_percentage
    # Print the winning county's results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winningcounty_count:,}\n"
        f"Winning Percentage: {winningcounty_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)