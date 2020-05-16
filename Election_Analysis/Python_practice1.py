counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 24801, "Denver": 306055, "Jefferson": 38855}
for county, voters in counties_dict.items():
    print( str(county) + " : " + str(voters) )






#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)
#for county_dict in voting_data:
    #print(county_dict["registered_voters"]) 
#for county_dict in voting_data:
   # print(county_dict['county'])
