import time

def time_function(sec):
    time.sleep(int(sec))

def data_load(filename, output):
    pass

runnableFunctions = { "TimeFunction": time_function, "DataLoad" : data_load }

def recFunction(config, from_ = ''):
    Type = config['Type']
    if(Type == 'Flow'):
        Execution = config['Execution']
        Activities = config['Activities']
        activityKeys = list(Activities.keys())
        for key in activityKeys:
            activity = Activities[key]
            chainName = from_ + '.' + key
            recFunction(activity, chainName)
    else:
        print("Entry", from_)
        functionName, inputs = config['Function'], config['Inputs']

        if(functionName == 'TimeFunction'):
            print(functionName)
            functionInput, executionTime = inputs['FunctionInput'], inputs['ExecutionTime']
            runnableFunctions[functionName](executionTime)
            
        elif(functionName == 'DataLoad'):
            filename = inputs['Filename']
            # runnableFunctions[Function](Filename)

    

    