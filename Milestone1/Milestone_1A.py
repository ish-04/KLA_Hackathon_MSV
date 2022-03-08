import yaml
import time
import generalfunc_concurrent

with open("Milestone1B.yaml","r") as file:
    data = yaml.safe_load(file)
# print(data)
generalfunc_concurrent.recFunction(data['M1B_Workflow'], 'M1B_Workflow')

