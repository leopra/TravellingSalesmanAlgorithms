import os 
filename = os.listdir('tsp_dataset')
matrix=[[]]

#gets filename and return array with info and array with coordinates
def parseFile(filename):
    with open('./tsp_dataset/' + filename, 'r') as f:
        lines = f.readlines()
        info = {}
        coords = []

        for line in lines:
            #close input
            if line == 'EOF\n':
                break
            #read info on file
            elif line[0].isupper():
                if line != 'NODE_COORD_SECTION\n':
                    n, i = line.rstrip().split(': ')
                    info[n]=i

            #load coords
            else:
                x,y,z = line.split(' ')
                coords.append((float(x), float(y), float(z)))

    return info, coords
            
    
a,b = parseFile(filename[0])

