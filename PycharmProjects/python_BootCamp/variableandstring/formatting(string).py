# times = input("how many times i need to tell you to clean your room ? ")
# #temp_value = type(times)
# #print (temp_value)
# times = int(times) # This is being done so to convert the input value in int becuase the value inpur will be in string

# for time in range(times):
# 	# print("Clean the room")

#---------------------------------------
# Below is applicable to python 3.6+ (Formatting in srings)
#---------------------------------------


# times = input("how many times i need to tell you to clean your room ? ")
# temp_value = type(times)
# # #print (temp_value)
# times = int(times) # This is being done so to convert the input value in int becuase the value inpur will be in string

# for time in range(times):
# 	print(f"Time {time}:Clean the room")


#--------------------------------------------
# Below is applicable to python 2.5 --> 3.6 (formatting in strings)
#---------------------------------------------


times = input("how many times i need to tell you to clean your room ? ")
temp_value = type(times)
# #print (temp_value)
times = int(times) # This is being done so to convert the input value in int becuase the value inpur will be in string

for time in range(times):
	print("Time {}:Clean the room".format(time))