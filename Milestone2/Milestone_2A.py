import csv
import yaml
import time
import generalfunc_concurrent

# str='print("hello")'
# exec(str)
# with open("Milestone2A_DataInput1.csv",mode="r") as file:
#     csv1=csv.reader(file)
# with open("Milestone2A_DataInput2.csv",mode="r") as file:
#     csv2=csv.reader(file)
with open("Milestone2B.yaml","r") as file:
    data=yaml.safe_load(file)
generalfunc_concurrent.recFunction(data['M2B_Workflow'], 'M2B_Workflow')
