from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


class SensorState(HueObject):
    @property
    def presence(self):
        return map_from_dict(self.raw, "presence")

    @presence.setter
    def presence(self, presence):
        if presence:
            self.set_data("state", f"{{\"presence\": true}}")
        else:
            self.set_data("state", f"{{\"presence\": false}}")


class SensorConfig(HueObject):
    @property
    def on(self):
        return map_from_dict(self.raw, "on")

    @on.setter
    def on(self, on):
        if on:
            self.set_data("config", f"{{\"on\": true}}")
        else:
            self.set_data("config", f"{{\"on\": false}}")

    @property
    def reachable(self):
        return map_from_dict(self.raw, "reachable")

    @property
    def battery(self):
        return map_from_dict(self.raw, "battery")


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
        self.set_data("", f"{{\"name\": \"{name}\"}}")

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
