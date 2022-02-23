from pythonhuecontrol.v1 import HueObject


class GroupState(HueObject):
    @property
    def all_on(self) -> bool:
        return self.map_from_raw("state", "all_on")

    @property
    def any_on(self) -> bool:
        return self.map_from_raw("state", "any_on")


class GroupAction(HueObject):
    @property
    def on(self) -> bool:
        return self.map_from_raw("action", "on")

    @on.setter
    def on(self, on: bool) -> None:
        self.set(on=on)

    @property
    def bri(self) -> int:
        return self.map_from_raw("action", "bri")

    @bri.setter
    def bri(self, bri: int) -> None:
        self.set(bri=bri)

    @property
    def hue(self) -> int:
        return self.map_from_raw("action", "hue")

    @hue.setter
    def hue(self, hue: int) -> None:
        self.set(hue=hue)

    @property
    def sat(self) -> int:
        return self.map_from_raw("action", "sat")

    @sat.setter
    def sat(self, sat: int) -> None:
        self.set(sat=sat)

    @property
    def xy(self) -> list[float, float]:
        return self.map_from_raw("action", "xy")

    @xy.setter
    def xy(self, xy: list[float, float]) -> None:
        self.set(xy=xy)

    @property
    def ct(self) -> int:
        return self.map_from_raw("action", "ct")

    @ct.setter
    def ct(self, ct: int) -> None:
        self.set(ct=ct)

    @property
    def alert(self) -> str:
        return self.map_from_raw("action", "alert")

    @alert.setter
    def alert(self, alert: str) -> None:
        self.set(alert=alert)

    @property
    def effect(self) -> str:
        return self.map_from_raw("action", "effect")

    @effect.setter
    def effect(self, effect: str) -> None:
        self.set(effect=effect)

    @property
    def transitiontime(self) -> int:
        return self.map_from_raw("action", "transitiontime")

    @transitiontime.setter
    def transitiontime(self, transitiontime: int) -> None:
        self.set(transitiontime=transitiontime)

    @property
    def scene(self) -> str:
        return self.map_from_raw("action", "scene")

    @scene.setter
    def scene(self, scene: str) -> None:
        self.set(scene=scene)

    @property
    def bri_inc(self) -> int:
        return self.map_from_raw("action", "bri_inc")

    @bri_inc.setter
    def bri_inc(self, bri_inc: int) -> None:
        self.set(bri_inc=bri_inc)

    @property
    def hue_inc(self) -> int:
        return self.map_from_raw("action", "hue_inc")

    @hue_inc.setter
    def hue_inc(self, hue_inc: int) -> None:
        self.set(hue_inc=hue_inc)

    @property
    def sat_inc(self) -> int:
        return self.map_from_raw("action", "sat")

    @sat_inc.setter
    def sat_inc(self, sat_inc: int) -> None:
        self.set(sat_inc=sat_inc)

    @property
    def xy_inc(self) -> list[float, float]:
        return self.map_from_raw("action", "xy_inc")

    @xy_inc.setter
    def xy_inc(self, xy_inc: list[float, float]) -> None:
        self.set(xy_inc=xy_inc)

    @property
    def ct_inc(self) -> int:
        return self.map_from_raw("action", "ct_inc")

    @ct_inc.setter
    def ct_inc(self, ct_inc: int) -> None:
        self.set(ct_inc=ct_inc)

    def set(self, on: bool = None, bri: int = None, hue: int = None, sat: int = None, xy: list[float, float] = None,
            ct: int = None, alert: str = None, effect: str = None, transitiontime: int = None, scene: str = None,
            bri_inc: int = None, hue_inc: int = None, sat_inc: int = None, xy_inc: list[float, float] = None,
            ct_inc: int = None) -> None:
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
        self.set_data("action", val)


class GroupPresence(HueObject):
    @property
    def lastupdated(self) -> str:
        return self.map_from_raw("presence", "lastupdated")

    @property
    def presence(self) -> bool:
        return self.map_from_raw("presence", "presence")

    @property
    def presence_all(self) -> bool:
        return self.map_from_raw("presence", "presence_all")


class GroupLightLevel(HueObject):
    @property
    def state(self) -> dict:
        return self.map_from_raw("lightlevel", "state")

    @property
    def lastupdated(self) -> str:
        return self.map_from_raw("lightlevel", "lastupdated")

    @property
    def dark(self) -> bool:
        return self.map_from_raw("lightlevel", "dark")

    @property
    def dark_all(self) -> bool:
        return self.map_from_raw("lightlevel", "dark_all")

    @property
    def daylight(self) -> bool:
        return self.map_from_raw("lightlevel", "daylight")

    @property
    def daylight_any(self) -> bool:
        return self.map_from_raw("lightlevel", "daylight_any")

    @property
    def lightlevel(self) -> int:
        return self.map_from_raw("lightlevel", "lightlevel")

    @property
    def lightlevel_min(self) -> int:
        return self.map_from_raw("lightlevel", "lightlevel_min")

    @property
    def lightlevel_max(self) -> int:
        return self.map_from_raw("lightlevel", "lightlevel_max")


class Group(HueObject):
    @property
    def name(self) -> str:
        return self.map_from_raw("name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def type(self) -> str:
        return self.map_from_raw("type")

    @property
    def lights(self) -> list[str]:
        return self.map_from_raw("lights")

    @lights.setter
    def lights(self, lights: list[str]) -> None:
        self.set(lights=lights)

    @property
    def sensors(self) -> list[str]:
        return self.map_from_raw("sensors")

    @sensors.setter
    def sensors(self, sensors: list[str]) -> None:
        self.set(sensors=sensors)

    @property
    def modelid(self) -> str:
        return self.map_from_raw("modelid")

    @property
    def uniqueid(self) -> str:
        return self.map_from_raw("uniqueid")

    @property
    def group_class(self) -> str:
        return self.map_from_raw("class")

    @group_class.setter
    def group_class(self, group_class: str) -> None:
        self.set(group_class=group_class)

    @property
    def recycle(self) -> bool:
        return self.map_from_raw("recycle")

    @recycle.setter
    def recycle(self, recycle: bool) -> None:
        self.set(recycle=recycle)

    def switch_on(self) -> None:
        self.action.on = True

    def switch_off(self) -> None:
        self.action.on = False

    @property
    def state(self) -> GroupState:
        return GroupState("", self._uri, raw=self._raw)

    @property
    def action(self) -> GroupAction:
        return GroupAction("", self._uri, raw=self._raw)

    @property
    def presence(self) -> GroupPresence:
        return GroupPresence("", self._uri, raw=self._raw)

    @property
    def lightlevel(self) -> GroupLightLevel:
        return GroupLightLevel("", self._uri, raw=self._raw)

    def set(self, name: str = None, lights: list[str] = None, sensors: list[str] = None, group_class: str = None,
            recycle: bool = None):
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
        self.set_data("", val)
