'''
EnergyValue Extractor
Program developed by: Callyn Villanueva (2019)
Updated: 10/21/2019 (PATH issue resolved)

'''

import os 

#declaring a variable for folder path
#Enter the path of the folder that contains all outfiles
data_folder = 'C:\\Users\\cvill\\Desktop\\outfileTest'

#storing String values into a list 
#looping through each outfile in folder to check E(RPM6)
eValue = []

for data_files in os.listdir(data_folder):
    if data_files.endswith(".out"):
        with open(os.path.join(data_folder, data_files)) as f:

       # with open (data_files, "r") as f:
            for line in f.readlines():
                if "E(RPM6) = " in line:
                    values = (line.split()[4:5])
                    eValue.append(values)


                    val_array = []

                    for v in eValue:
                        e_IntList = (list(map(float, v)))
            val_array.append(e_IntList)
            #printing the minimum value for each file
            lowest_value  = min(val_array)
            print (" \n" + f.name + ":" + str(lowest_value))
