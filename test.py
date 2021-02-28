import re
import json


arr = []
y = open('data_output.txt', "w")

for i in open('data_copy.txt').readlines():
    print(i)
    x = list(re.findall('(\D+) (\-?\d+\.\d+)\s+(\-?\d+\.\d+)',i)[0])
    x[0] = x[0].strip()
    x[1],x[2] = float(x[1]),float(x[2])
    arr.append(x)

y.write("popData = "+json.dumps(arr))

