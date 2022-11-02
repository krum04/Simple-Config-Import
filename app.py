# Pass config text argument to set global variables
def importConfig(file,printVars=False):
    with open(file) as f:
        lines = f.readlines()
        myVars = globals()
        for line in lines:
            if printVars == True:
                print(line.replace('\n',''))
            myVars[line.split(' ')[0]] = line.split(' ')[2]