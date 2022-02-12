from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
import json


class SensorState(HueObject):
    @property
    def presence(self):
        return map_from_dict(self.raw, "presence")

    @presence.setter
    def presence(self, presence):
        self.set(presence=presence)

    def set(self, presence=None):
        val = {}
        if presence is not None:
            val["presence"] = presence
        self.set_data("state", json.dumps(val))


class SensorConfig(HueObject):
    @property
    def on(self):
        return map_from_dict(self.raw, "on")

    @on.setter
    def on(self, on):
        self.set(on=on)

    @property
    def reachable(self):
        return map_from_dict(self.raw, "reachable")

    @property
    def battery(self):
        return map_from_dict(self.raw, "battery")

    def set(self, on=None):
        val = {}
        if on is not None:
            val["on"] = on
        self.set_data("config", json.dumps(val))


class Sensor(HueObject):
    def __init__(self, identity, uri):
        self.config = SensorConfig("", uri)
        self.state = SensorState("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        self.config.load_data(map_from_dict(self.raw, "config"))
        self.state.load_data(map_from_dict(self.raw, "state"))

    @property
    def name(self):
        return map_from_dict(self.raw, "name")

    @name.setter
    def name(self, name):
        self.set(name=name)

    @property
    def type(self):
        return map_from_dict(self.raw, "type")

    @property
    def modelid(self):
        return map_from_dict(self.raw, "modelid")

    @property
    def uniqueid(self):
        return map_from_dict(self.raw, "uniqueid")

    @property
    def manufacturername(self):
        return map_from_dict(self.raw, "manufacturername")

    @property
    def swversion(self):
        return map_from_dict(self.raw, "swversion")

    @property
    def recycle(self):
        return map_from_dict(self.raw, "recycle")

    def set(self, name=None):
        val = {}
        if name is not None:
            val["name"] = name
        self.set_data("", json.dumps(val))
