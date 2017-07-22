import matplotlib.pyplot as plt
import json, os
import platform as pa
import pandas as pd

path_to_json = './json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    
print(json_files)

for fil in json_files:
    with open(path_to_json+fil) as f:
        data = json.load(f)
        tim = [float(x['time']) for x in data['points']]
        num = [x['store_len'] for x in data['points']]
        plt.plot(num,tim)
        

plt.show()
