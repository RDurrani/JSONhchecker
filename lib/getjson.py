import json

def loadjsonfile(filename):
    #return json filetype from local file
    with open(filename, encoding='utf-8') as jsondatfile:
        dat = json.loads(jsondatfile.read())
        return dat