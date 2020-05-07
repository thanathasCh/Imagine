from cv2 import imdecode, IMREAD_UNCHANGED
from json import JSONEncoder, dumps, loads
from numpy import ndarray, asarray, fromstring, uint8

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def npToJson(arr):
    data = {"array": arr}
    return dumps(data, cls=NumpyArrayEncoder)

def jsonToNp(arr):
    data = loads(arr)
    return asarray(data['array'])

def convertBinaryToImage(binary):
    return imdecode(fromstring(binary, uint8), IMREAD_UNCHANGED)