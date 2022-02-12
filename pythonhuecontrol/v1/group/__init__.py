from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
import json


class GroupState(HueObject):
    @property
    def all_on(self):
        return map_from_dict(self.raw, "all_on")

    @property
    def any_on(self):
        return map_from_dict(self.raw, "any_on")


class GroupAction(HueObject):
    @property
    def on(self):
        return map_from_dict(self.raw, "on")

    @on.setter
    def on(self, on):
        self.set(on=on)

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
        return map_from_dict(self.raw, "ct")

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
    def transitiontime(self):
        return map_from_dict(self.raw, "transitiontime")

    @transitiontime.setter
    def transitiontime(self, transitiontime):
        self.set(transitiontime=transitiontime)

    @property
    def scene(self):
        return map_from_dict(self.raw, "scene")

    @scene.setter
    def scene(self, scene):
        self.set(scene=scene)

    @property
    def bri_inc(self):
        return map_from_dict(self.raw, "bri_inc")

    @bri_inc.setter
    def bri_inc(self, bri_inc):
        self.set(bri_inc=bri_inc)

    @property
    def hue_inc(self):
        return map_from_dict(self.raw, "hue_inc")

    @hue_inc.setter
    def hue_inc(self, hue_inc):
        self.set(hue_inc=hue_inc)

    @property
    def sat_inc(self):
        return map_from_dict(self.raw, "sat")

    @sat_inc.setter
    def sat_inc(self, sat_inc):
        self.set(sat_inc=sat_inc)

    @property
    def xy_inc(self):
        return map_from_dict(self.raw, "xy_inc")

    @xy_inc.setter
    def xy_inc(self, xy_inc):
        self.set(xy_inc=xy_inc)

    @property
    def ct_inc(self):
        return map_from_dict(self.raw, "ct_inc")

    @ct_inc.setter
    def ct_inc(self, ct_inc):
        self.set(ct_inc=ct_inc)

    def set(self, on=None, bri=None, hue=None, sat=None, xy=None, ct=None, alert=None, effect=None, transitiontime=None,
            scene=None, bri_inc=None, hue_inc=None, sat_inc=None, xy_inc=None, ct_inc=None):
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
        if transitiontime is not None:
            val["transitiontime"] = transitiontime
        if scene is not None:
            val["scene"] = scene
        if bri_inc is not None:
            val["bri_inc"] = bri_inc
        if hue_inc is not None:
            val["hue_inc"] = hue_inc
        if sat_inc is not None:
            val["sat_inc"] = sat_inc
        if xy_inc is not None:
            val["xy_inc"] = xy_inc
        if ct_inc is not None:
            val["ct_inc"] = ct_inc
        self.set_data("action", json.dumps(val))


class GroupPresence(HueObject):
    @property
    def lastupdated(self):
        return map_from_dict(self.raw, "lastupdated")

    @property
    def presence(self):
        return map_from_dict(self.raw, "presence")

    @property
    def presence_all(self):
        return map_from_dict(self.raw, "presence_all")


class GroupLightLevel(HueObject):
    @property
    def state(self):
        return map_from_dict(self.raw, "state")

    @property
    def lastupdated(self):
        return map_from_dict(self.raw, "lastupdated")

    @property
    def dark(self):
        return map_from_dict(self.raw, "dark")

    @property
    def dark_all(self):
        return map_from_dict(self.raw, "dark_all")

    @property
    def daylight(self):
        return map_from_dict(self.raw, "daylight")

    @property
    def daylight_any(self):
        return map_from_dict(self.raw, "daylight_any")

    @property
    def lightlevel(self):
        return map_from_dict(self.raw, "lightlevel")

    @property
    def lightlevel_min(self):
        return map_from_dict(self.raw, "lightlevel_min")

    @property
    def lightlevel_max(self):
        return map_from_dict(self.raw, "lightlevel_max")


class Group(HueObject):
    def __init__(self, identity, uri):
        self.state = GroupState("", uri)
        self.action = GroupAction("", uri)
        self.presence = GroupPresence("", uri)
        self.lightlevel = GroupLightLevel("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        self.state.load_data(map_from_dict(self.raw, "state"))
        self.action.load_data(map_from_dict(self.raw, "action"))
        self.presence.load_data(map_from_dict(self.raw, "presence"))
        self.lightlevel.load_data(map_from_dict(self.raw, "lightlevel"))

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
    def lights(self):
        return map_from_dict(self.raw, "lights")

    @lights.setter
    def lights(self, lights):
        self.set(lights=lights)

    @property
    def sensors(self):
        return map_from_dict(self.raw, "sensors")

    @sensors.setter
    def sensors(self, sensors):
        self.set(sensors=sensors)

    @property
    def modelid(self):
        return map_from_dict(self.raw, "modelid")

    @property
    def uniqueid(self):
        return map_from_dict(self.raw, "uniqueid")

    @property
    def group_class(self):
        return map_from_dict(self.raw, "class")

    @group_class.setter
    def group_class(self, group_class):
        self.set(group_class=group_class)

    @property
    def recycle(self):
        return map_from_dict(self.raw, "recycle")

    @recycle.setter
    def recycle(self, recycle):
        self.set(recycle=recycle)

    def switch_on(self):
        self.action.on = True

    def switch_off(self):
        self.action.on = False

    def set(self, name=None, lights=None, sensors=None, group_class=None, recycle=None):
        val = {}
        if name is not None:
            val["name"] = name
        if lights is not None:
            val["lights"] = lights
        if sensors is not None:
            val["sensors"] = sensors
        if group_class is not None:
            val["class"] = group_class
        if recycle is not None:
            val["recycle"] = recycle
        self.set_data("", json.dumps(val))
