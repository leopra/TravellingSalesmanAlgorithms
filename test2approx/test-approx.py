

files=['burma14.txt', 'ulysses16.txt', 'ulysses22.txt', 'eil51.txt', 'berlin52.txt','kroD100.txt', 'kroA100.txt', 'ch150.txt',
'gr202.txt', 'gr229.txt', 'pcb442.txt', 'd493.txt', 'dsj1000.txt']

MAX= 9223372036854775807

minimo=MAX
media=0
string=""
c = open('medie-min.txt','w')
for i in range(0, len(files)):
    minimo=MAX
    media=0
    with open(files[i]) as f:
        lines = f.readlines()
        for line in lines:
            value= line.split()
            if minimo>float(value[1]):
                minimo=float(value[1])
            media+= float(value[1])
    media= media/len(lines)
    print(files[i])
    string+= files[i] + ' ' + str(minimo) + ' ' + str(media) + '\n'
c.write(string)
c.close()

