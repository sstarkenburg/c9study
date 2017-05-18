import csv


def readCsv(fileName):
    states = {}
    
    with open(fileName, mode='r') as stateList:
        reader = csv.reader(stateList)
        states = {row[0]:row[1] for row in reader}
    
    return states

def alphaStates(fileName):
    return sorted(readCsv('states.csv'))

def orderStates(fileName):
    states = readCsv('states.csv')
    # not having zero padding was messing me up, and I'm too lazy to figure how
    # to do it for the keys. a dict comprehension is probably the way to go
    return sorted(states, key=states.__getitem__)

if __name__ == '__main__':
    print("States in alphabetical order")
    for state in alphaStates('states.csv'):
        print(state)
    
    print('='*15)
    print("States in order of which they were added to the union")
    for state in orderStates('states.csv'):
        print(state)