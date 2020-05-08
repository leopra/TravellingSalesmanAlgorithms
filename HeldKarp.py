import utilities as ut
import os 

filename = os.listdir('tsp_dataset')
a = ut.parseFile(filename[3])
print(a)

