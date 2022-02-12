from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


class SceneAppData(HueObject):
    @property
    def version(self):
        return map_from_dict(self.raw, "version")

    @property
    def data(self):
        return map_from_dict(self.raw, "data")


class SceneLightState:
    def __init__(self, state):
        self.on = map_from_dict(state, "on")
        self.bri = map_from_dict(state, "bri")
        self.hue = map_from_dict(state, "hue")
        self.sat = map_from_dict(state, "sat")
        self.xy = map_from_dict(state, "xy")
        self.ct = map_from_dict(state, "ct")
        self.effect = map_from_dict(state, "effect")
        self.transitiontime = map_from_dict(state, "transitiontime")

    def __str__(self):
        result = {}
        if self.on is not None:
            result["on"] = self.on
        if self.bri is not None:
            result["bri"] = self.bri
        if self.hue is not None:
            result["hue"] = self.hue
        if self.sat is not None:
            result["sat"] = self.sat
        if self.xy is not None:
            result["xy"] = self.xy
        if self.ct is not None:
            result["ct"] = self.ct
        if self.effect is not None:
            result["effect"] = self.effect
        if self.transitiontime is not None:
            result["transitiontime"] = self.transitiontime
        return str(result).replace("True", "true").replace("False", "false")


class SceneLightStateList(HueObject):
    def __getitem__(self, key):
        return SceneLightState(map_from_dict(self.raw, key))

    def __setitem__(self, key, value):
        self.set_data("lightstates/" + key, f"{{\"{key}\": {str(value)}}}")


class Scene(HueObject):
    def __init__(self, identity, uri):
        self.appdata = SceneAppData("", uri)
        self.lightstates = SceneLightStateList("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        self.appdata.load_data(map_from_dict(self.raw, "appdata"))
        self.lightstates.load_data(map_from_dict(self.raw, "lightstates"))

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
    def group(self):
        return map_from_dict(self.raw, "group")

    @property
    def lights(self):
        return map_from_dict(self.raw, "lights")

    @lights.setter
    def lights(self, lights):
        self.set_data("", f"{{\"lights\": {lights}}}")

    @property
    def owner(self):
        return map_from_dict(self.raw, "owner")

    @property
    def recycle(self):
        return map_from_dict(self.raw, "recycle")

    @property
    def locked(self):
        return map_from_dict(self.raw, "locked")

    @property
    def picture(self):
        return map_from_dict(self.raw, "picture")

    @property
    def image(self):
        return map_from_dict(self.raw, "image")

    @property
    def lastupdated(self):
        return map_from_dict(self.raw, "lastupdated")

    @property
    def version(self):
        return map_from_dict(self.raw, "version")
