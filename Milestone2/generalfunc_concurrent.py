import time
import threading
from logger import log
import csv
import pandas as pd

inMemory = {}


def time_function(functionInput, executionTime, condition, from_):
    log(f'{from_} Executing TimeFunction ({functionInput}, {executionTime})')
    time.sleep(int(executionTime))

def data_load(filename, output, condition, from_):
    # log(f'{from_} Executing DataLoad ({filename}, {output})')
    with open(filename,mode="r") as file:
        csv1=csv.reader(file)
    if(condition):
        condition = condition.replace('(', '[')
        condition = condition.replace(')', ']')
        condition = condition.replace('$', 'inMemory')
        try:
            if(exec(condition)):
                # condition passed
                log(f'{from_} Executing Dataload ({filename})')
                # reading data from csv
                
            else: 
                # condition failed
                log(f'{from_} Skipped')    
        except:
            log(f'{from_} Skipped')  
    else:
        df = pd.read_csv(filename)
        row_count, column_count = df.shape
        if(output):
            inMemory[f'{from_}.{output[0]}'] = df
            inMemory[f'{from_}.{output[1]}'] = row_count
        print(from_ ,output, df, inMemory)

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
        functionName, inputs = config['Function'], config['Inputs']
        outputs = None
        if 'Outputs' in list(config.keys()):
            outputs = config['Outputs']
            print("out\n",outputs)
        condition = None
        if 'Condition' in list(config.keys()):
            condition = config['Condition']
            
            
        if(functionName == 'TimeFunction'):
            functionInput, executionTime = inputs['FunctionInput'], inputs['ExecutionTime']
            runnableFunctions[functionName](functionInput, executionTime, condition, from_)
            
        elif(functionName == 'DataLoad'):
            filename = inputs['Filename']
            
            runnableFunctions[functionName](filename, outputs, condition, from_)

    log(f'{from_} Exit')
