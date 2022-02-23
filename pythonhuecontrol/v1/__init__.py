import requests
import json


# get item from raw dictionary multiple levels deep
def map_from_dict(dictionary: dict, *items: str, default: object = None):
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
def scan_new(scan_uri: str) -> list:
    new_items = []
    req = requests.get(scan_uri)
    if req.status_code == 200:
        for item in req.json():
            if item != "lastscan":
                new_items.append(item)
    return new_items


class HueObject:
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._identity = identity
        self._uri = uri
        self._raw = None
        self._response_status_code = 0
        self._response_json = None
        self._response_message = ""
        if raw is None:
            self.load_data()
        else:
            self.load_data(raw)

    @property
    def identity(self):
        return self._identity

    # get item from raw dictionary multiple levels deep
    def map_from_raw(self, *items: str, default: object = None):
        return map_from_dict(self._raw, *items, default=default)

    # parse response from requests.response object and return whether REST call was successful
    # in case of successful API call, if ID is included in the response, _response_message holds the ID
    def parse_response(self, response: requests.Response) -> bool:
        self._response_status_code = response.status_code
        self._response_json = response.json()
        if self._response_status_code == 200:
            if isinstance(self._response_json, list) and "success" in self._response_json[0] and \
                    "id" in self._response_json[0]["success"]:
                self._response_message = self._response_json[0]["success"]["id"]
            else:
                self._response_message = ""
            return True
        else:
            if isinstance(self._response_json, list) and len(self._response_json) > 0 and \
                    "error" in self._response_json[0] and "description" in self._response_json[0]["error"]:
                self._response_message = self._response_json[0]["error"]["description"]
            else:
                self._response_message = "Unknown error"
            return False

    # get data from REST API. If provided, directly assign to prevent needing to make API call
    def load_data(self, raw: dict = None) -> None:
        if raw is not None:
            self._raw = raw
        else:
            if not self.parse_response(requests.get(self._uri)):
                raise Exception(self._response_message)
            else:
                self._raw = self._response_json

    # set data through REST call; optionally reload data to sync status with actual bridge status
    def set_data(self, category: str, data: dict, reload: bool = True) -> None:
        if not self.parse_response(requests.put(self._uri + "/" + category, data=json.dumps(data))):
            raise Exception(self._response_message)
        elif reload:
            self.load_data()

    # delete object through REST call; after successful delete object is invalid (state reset to None)
    def delete(self) -> None:
        if not self.parse_response(requests.delete(self._uri)):
            self._raw = None
            raise Exception(self._response_message)

    # pretty print object
    def __str__(self):
        return "ID        : " + self._identity + "\n" + \
               "URI       : " + self._uri + "\n" + \
               "Data      : \n" + \
               "None" if self._raw is None else json.dumps(self._raw, sort_keys=False, indent=4)

    # getter for items not explicitly available in subclass
    def get_item(self, *args: str) -> object:
        return self.map_from_raw(*args)

    # setter for items not explicitly available in subclass
    def set_item(self, category: str, item: str, value: object) -> None:
        self.set_data(category, {item: value})
