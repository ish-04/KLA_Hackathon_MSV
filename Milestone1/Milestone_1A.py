import yaml
import time
import generalfn

with open("Milestone1A.yaml","r") as file:
    data = yaml.safe_load(file)
# print(data)
generalfn.recFunction(data['M1A_Workflow'], 'M1A_Workflow')

