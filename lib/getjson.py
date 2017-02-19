import json

def loadjsonfile(filename):
    #return json object from local json file

    with open(filename, encoding='utf-8') as jsondatfile:
        dat = json.loads(jsondatfile.read())
        return dat