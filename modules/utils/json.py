import json

def load_json(filename) -> dict:
    with open(filename, 'r') as f:
        data = json.load(f)
    f.close()
    return data

def save_json(filename,data):
    with open(filename,"w") as f:
        json.dump(data,f,indent=6)
    f.close()