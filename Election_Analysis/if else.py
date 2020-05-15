#temperature = int(input("What is the temperature outside?"))
#if temperature > 80:
    #print("Turn on the AC.")
#else:
   # print("Open the windows.")
    #What is the score?
#score = int(input("What is your score? "))
    #Determine the grade.
#if score >= 90:
    #print("Your grade is an A")
#elif score >= 80:
    #print("Your grade is B")
#elif score >= 70:
    #print("Your grade is C")
#elif score >= 60:
    #print("Your grade is D")
#else: 
    #print("your grade is F")
counties = ["Arapahoe","Denver", "Jefferson","El Paso"]
#if "El Paso" not in counties:
#    print("No")
#else:
#    print("Yes")
#x = 0
#while x <= 5:
#    print(x)
#    x = x+1
#count = 7
#while count < 1:
 #print("Hello World")
#for county in counties:
    #print(county)
#numbers= [0,1,2,3,4,5]
#for num in numbers:
   # print(num)
#for num in range(6):
 #   print (num)
#for i in range(len(counties)):
 #    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
    #print(county)
#for county in counties_dict.keys():
    #print(county)
#for voters in counties_dict.values():
    #print(voters)
#for county in counties_dict:
    #print(counties_dict[county])
#for county in counties_dict:
    #print(counties_dict.get(county))
#for county, voters in counties_dict.items():
    #print(county, voters)
#for county, voters in counties_dict.items():
    #print( str(county) + " county has " + str(voters) + " registered voters.")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)
#for county_dict in voting_data:
    #print(county_dict["registered_voters"]) 
for county_dict in voting_data:
    print(county_dict['county'])