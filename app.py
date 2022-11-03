# Pass config.txt into function to set global variables 
def importConfig(file,printVars=False):
    with open(file) as f:
        lines = f.readlines()
        myVars = globals()
        for line in lines:
            if line[:1]=='#':
                continue
            if printVars == True:
                print(line.replace('\n',''))
            myVars[(line.split(' ')[0]).strip()] = (line.split(' ')[2]).strip()