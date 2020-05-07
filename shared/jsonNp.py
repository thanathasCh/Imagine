import json
from json import JSONEncoder
import numpy as np

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def npToJson(arr):
    data = {"array": arr}
    return json.dumps(data, cls=NumpyArrayEncoder)

def jsonToNp(arr):
    data = json.loads(arr)
    return np.asarray(data['array'])

# numpyArrayOne = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# # Serialization
# numpyData = {"array": numpyArrayOne}
# encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
# print("Printing JSON serialized NumPy array")
# print(encodedNumpyData)

# # Deserialization
# print("Decode JSON serialized NumPy array")
# decodedArrays = json.loads(encodedNumpyData)

# finalNumpyArray = np.asarray(decodedArrays["array"])
# print("NumPy Array")
# print(finalNumpyArray)