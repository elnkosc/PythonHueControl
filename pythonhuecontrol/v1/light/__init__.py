from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
import json


class LightState(HueObject):
    @property
    def on(self):
        return map_from_dict(self.raw, "on")

    @on.setter
    def on(self, on):
        self.set_data("state", json.dumps({"on": on}))

    @property
    def bri(self):
        return map_from_dict(self.raw, "bri")

    @bri.setter
    def bri(self, bri):
        self.set(bri=bri)

    @property
    def hue(self):
        return map_from_dict(self.raw, "hue")

    @hue.setter
    def hue(self, hue):
        self.set(hue=hue)

    @property
    def sat(self):
        return map_from_dict(self.raw, "sat")

    @sat.setter
    def sat(self, sat):
        self.set(sat=sat)

    @property
    def xy(self):
        return map_from_dict(self.raw, "xy")

    @xy.setter
    def xy(self, xy):
        self.set(xy=xy)

    @property
    def ct(self):
        return map_from_dict(self.raw, "cy")

    @ct.setter
    def ct(self, ct):
        self.set(ct=ct)

    @property
    def alert(self):
        return map_from_dict(self.raw, "alert")

    @alert.setter
    def alert(self, alert):
        self.set(alert=alert)

    @property
    def effect(self):
        return map_from_dict(self.raw, "effect")

    @effect.setter
    def effect(self, effect):
        self.set(effect=effect)

    @property
    def colormode(self):
        return map_from_dict(self.raw, "colormode")

    @colormode.setter
    def colormode(self, colormode):
        self.set(colormode=colormode)

    @property
    def reachable(self):
        return map_from_dict(self.raw, "reachable")

    @reachable.setter
    def reachable(self, reachable):
        self.set(reachable=reachable)

    def set(self, on=None, bri=None, hue=None, sat=None, xy=None, ct=None, alert=None, effect=None, colormode=None,
            reachable=None):
        val = {}
        if on is not None:
            val["on"] = on
        if bri is not None:
            val["bri"] = bri
        if hue is not None:
            val["hue"] = hue
        if sat is not None:
            val["sat"] = sat
        if xy is not None:
            val["xy"] = xy
        if ct is not None:
            val["ct"] = ct
        if alert is not None:
            val["alert"] = alert
        if effect is not None:
            val["effect"] = effect
        if colormode is not None:
            val["colormode"] = colormode
        if reachable is not None:
            val["reachable"] = reachable
        self.set_data("state", json.dumps(val))


class Light(HueObject):
    def __init__(self, identity, uri):
        self.state = LightState("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
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
    def luminaireuniqueid(self):
        return map_from_dict(self.raw, "luminaireuniqueid")

    @property
    def streaming(self):
        return map_from_dict(self.raw, "streaming")

    @property
    def renderer(self):
        return map_from_dict(self.raw, "renderer")

    @property
    def proxy(self):
        return map_from_dict(self.raw, "proxy")

    @property
    def swversion(self):
        return map_from_dict(self.raw, "swversion")

    def switch_on(self):
        self.state.on = True

    def switch_off(self):
        self.state.on = False

    def toggle(self):
        if self.state.on:
            self.switch_off()
        else:
            self.switch_on()

    def set(self, name=None):
        val = {}
        if name is not None:
            val["name"] = name
        self.set_data("", json.dumps(val))
