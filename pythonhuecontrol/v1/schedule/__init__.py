from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
import json


class ScheduleCommand(HueObject):
    @property
    def address(self):
        return map_from_dict(self.raw, "address")

    @address.setter
    def address(self, address):
        self.set(address=address)

    @property
    def method(self):
        return map_from_dict(self.raw, "method")

    @method.setter
    def method(self, method):
        self.set(method=method)

    @property
    def body(self):
        return map_from_dict(self.raw, "body")

    @body.setter
    def body(self, body):
        self.set(body=body)

    def set(self, address=None, method=None, body=None):
        val = {"command": {}}
        if address is not None:
            val["command"]["address"] = address
        if method is not None:
            val["command"]["method"] = method
        if body is not None:
            val["command"]["body"] = body
        self.set_data("", json.dumps(val))


class Schedule(HueObject):
    def __init__(self, identity, uri):
        self.command = ScheduleCommand("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        self.command.load_data(map_from_dict(self.raw, "command"))

    @property
    def name(self):
        return map_from_dict(self.raw, "name")

    @name.setter
    def name(self, name):
        self.set(name=name)

    @property
    def description(self):
        return map_from_dict(self.raw, "description")

    @description.setter
    def description(self, description):
        self.set(description=description)

    @property
    def localtime(self):
        return map_from_dict(self.raw, "localtime")

    @localtime.setter
    def localtime(self, localtime):
        self.set(localtime=localtime)

    @property
    def starttime(self):
        return map_from_dict(self.raw, "starttime")

    @starttime.setter
    def starttime(self, starttime):
        self.set(starttime=starttime)

    @property
    def status(self):
        return map_from_dict(self.raw, "status")

    @status.setter
    def status(self, status):
        self.set(status=status)

    @property
    def autodelete(self):
        return map_from_dict(self.raw, "autodelete")

    @autodelete.setter
    def autodelete(self, autodelete):
        self.set(autodelete=autodelete)

    def set(self, name=None, description=None, localtime=None, starttime=None, status=None, autodelete=None):
        val = {}
        if name is not None:
            val["name"] = name
        if description is not None:
            val["description"] = description
        if localtime is not None:
            val["localtime"] = localtime
        if starttime is not None:
            val["starttime"] = starttime
        if status is not None:
            val["status"] = status
        if autodelete is not None:
            val["autodelete"] = autodelete
        self.set_data("", json.dumps(val))
