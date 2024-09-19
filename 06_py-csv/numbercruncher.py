'''
heading !!
disco:

qcc:

how this script works:

'''

occupations = {}

with open('occupations.csv') as text:
    reader = text.read()
    reader = reader.split('\n')
    for row in range(len(reader)-1):
        if '"' in reader[row+1]:
            reader[row+1] = reader[row+1].split('",')
        else:
            reader[row+1] = reader[row+1].split(',')
        occupations[reader[row+1][0]]=float(reader[row+1][1])
    print(occupations)    
    