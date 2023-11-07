import json
import requests
import numpy as np
from PIL import Image

data = np.array([0,0,0,0,0,0,0,0,0])

headers = {'Content-Type':'application/json'}
address = "http://127.0.0.1:80/Recommand Model/recommand"
data = {'input_data':data.tolist()}
print(data)


result = requests.post(address, data=json.dumps(data), headers=headers)



print(result)
print(str(result.content))
print(result.json())