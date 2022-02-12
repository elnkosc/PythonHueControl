import requests
import json


# get item from dictionary multiple levels deep
def map_from_dict(dictionary, *items, default=None):
    d = dictionary
    for item in items:
        if item not in d:
            return default
        elif item == items[-1]:
            return d[item]
        elif type(d[item]) == dict:
            d = d[item]
        else:
            return default
    return default


# scan for new hue-devices using provided uri
def scan_new(scan_uri):
    new_items = []
    req = requests.get(scan_uri)
    if req.status_code == 200:
        for item in req.json():
            if item != "lastscan":
                new_items.append(item)
    return new_items


class HueObject:
    def __init__(self, identity, uri):
        self.identity = identity
        self.uri = uri
        self.raw = None
        self.load_data()

    def load_data(self, raw=None):
        if raw is not None:
            self.raw = raw
        else:
            req = requests.get(self.uri)
            if req.status_code != 200 or isinstance(req.json(), list):
                if "error" in req.json()[0] and "description" in req.json()[0]["error"]:
                    raise Exception(req.json()[0]["error"]["description"])
                else:
                    raise Exception("Error loading data")
            self.raw = req.json()

    def set_data(self, category, data, reload=True):
        requests.put(self.uri + "/" + category, data=data)
        if reload:
            self.load_data()

    def delete(self):
        req = requests.delete(self.uri)
        if req.status_code == 200:
            self.raw = None

    def __str__(self):
        return "ID        : " + self.identity + "\n" + \
               "URI       : " + self.uri + "\n" + \
               "Data      : \n" + \
               "None" if self.raw is None else json.dumps(self.raw, sort_keys=False, indent=4)

    # getter for items not explicitly available in subclass
    def get_item(self, *args):
        return map_from_dict(self.raw, *args)

    # setter for items not explicitly available in subclass
    def set_item(self, category, item, value):
        self.set_data(category, f"{{\"{item}\": {value}}}")
