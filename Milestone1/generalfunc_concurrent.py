import time
import threading
from logger import log

def time_function(functionInput, executionTime, from_):
    log(f'{from_} Executing TimeFunction ({functionInput}, {executionTime})')
    time.sleep(int(executionTime))

def data_load(filename, output, from_):
    log(f'{from_} Executing DataLoad ({filename}, {output})')
    pass

runnableFunctions = { "TimeFunction": time_function, "DataLoad" : data_load }

def recFunction(config, from_ = ''):
    log(f'{from_} Entry')
    Type = config['Type']
    if(Type == 'Flow'):
        Execution = config['Execution']
        Activities = config['Activities']
        activityKeys = list(Activities.keys())
        if(Execution == 'Sequential'):
            for key in activityKeys:
                activity = Activities[key]
                chainName = from_ + '.' + key
                recFunction(activity, chainName)
        elif(Execution == 'Concurrent'):
            # If its concurrent creating an array of tasks for all activity
            tasks = []
            for key in activityKeys:
                activity = Activities[key]
                chainName = from_ + '.' + key
                task = threading.Thread(target=recFunction, args=(activity, chainName,))
                tasks.append(task)

            # Starting all tasks in parallel
            for task in tasks:
                task.start()

            # Waiting until all task finshes
            for task in tasks:
                task.join()

    else:
        print("Entry", from_)
        functionName, inputs = config['Function'], config['Inputs']

        if(functionName == 'TimeFunction'):
            functionInput, executionTime = inputs['FunctionInput'], inputs['ExecutionTime']
            runnableFunctions[functionName](functionInput, executionTime, from_)
            
        elif(functionName == 'DataLoad'):
            filename, outputs = inputs['Filename'], inputs['Outputs']
            runnableFunctions[functionName](filename, outputs, from_)

    log(f'{from_} Exit')
    

    