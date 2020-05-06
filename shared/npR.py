from imgarray import save_array_img, load_array_img
from os import fsync, remove

PATH = 'datasets/img.png'

def sync(fh):
    fh.flush()
    fsync(fh.fileno())
    return True

def save_array_to_PNG(data, path):
    with open(path, 'wb+') as fh:
        save_array_img(data, path, img_format='png')
        sync(fh)

    return path

def convertFileToBinary(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def convertImageToBinary(img):
    data = convertFileToBinary(save_array_to_PNG(img, PATH))
    clearCache()
    return data

def clearCache():
    remove(PATH)

def write_file(data, path):
    with open(path, 'wb') as file:
        file.write(data)

def convertBinaryToImage(binary):
    write_file(binary, PATH)
    data = load_array_img(PATH)
    clearCache
    return data