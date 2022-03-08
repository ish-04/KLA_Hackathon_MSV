import yaml
import time
import generalfn

start=time.perf_counter()
finish=time.perf_counter()

with open("Milestone1A.yaml","r") as file:
    data = yaml.safe_load(file)
# print(data)
generalfn.recFunction(data['M1A_Workflow'], 'M1A_Workflow')

# def obj(dictionary):
#     for k,v in dictionary.items():
#         if isinstance(v,dict):
#             obj(v)
#         else:
#             if 