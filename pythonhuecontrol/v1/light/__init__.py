from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


class LightCapabilitiesStreaming(HueObject):
    @property
    def renderer(self) -> bool:
        return map_from_dict(self._raw, "capabilities", "streaming", "renderer")

    @property
    def proxy(self) -> bool:
        return map_from_dict(self._raw, "capabilities", "streaming", "proxy")


class LightCapabilitiesControlCt(HueObject):
    @property
    def min(self) -> int:
        return map_from_dict(self._raw, "capabilities", "control", "ct", "min")

    @property
    def max(self) -> int:
        return map_from_dict(self._raw, "capabilities", "control", "ct", "max")


class LightCapabilitiesControl(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.ct = LightCapabilitiesControlCt("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.ct.load_data(self._raw)

    @property
    def mindimlevel(self) -> int:
        return map_from_dict(self._raw, "capabilities", "control", "mindimlevel")

    @property
    def maxlumen(self) -> int:
        return map_from_dict(self._raw, "capabilities", "control", "maxlumen")

    @property
    def colorgamuttype(self) -> str:
        return map_from_dict(self._raw, "capabilities", "control", "colorgamuttype")

    @property
    def colorgamut(self) -> list[float, float, float]:
        return map_from_dict(self._raw, "capabilities", "control", "colorgamut")


class LightCapabilities(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.streaming = LightCapabilitiesStreaming("", uri)
        self.control = LightCapabilitiesControl("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.streaming.load_data(self._raw)
        self.control.load_data(self._raw)

    @property
    def certified(self) -> bool:
        return map_from_dict(self._raw, "capabilities", "certified")


class LightState(HueObject):
    @property
    def on(self) -> object:
        return map_from_dict(self._raw, "state", "on")

    @on.setter
    def on(self, on: bool) -> None:
        self.set(on=on)

    @property
    def bri(self) -> int:
        return map_from_dict(self._raw, "state", "bri")

    @bri.setter
    def bri(self, bri: int) -> None:
        self.set(bri=bri)

    @property
    def hue(self) -> int:
        return map_from_dict(self._raw, "state", "hue")

    @hue.setter
    def hue(self, hue: int) -> None:
        self.set(hue=hue)

    @property
    def sat(self) -> int:
        return map_from_dict(self._raw, "state", "sat")

    @sat.setter
    def sat(self, sat: int) -> None:
        self.set(sat=sat)

    @property
    def xy(self) -> list[float, float]:
        return map_from_dict(self._raw, "state", "xy")

    @xy.setter
    def xy(self, xy: list[float, float]) -> None:
        self.set(xy=xy)

    @property
    def ct(self) -> int:
        return map_from_dict(self._raw, "state", "ct")

    @ct.setter
    def ct(self, ct: int) -> None:
        self.set(ct=ct)

    @property
    def alert(self) -> str:
        return map_from_dict(self._raw, "state", "alert")

    @alert.setter
    def alert(self, alert: str) -> None:
        self.set(alert=alert)

    @property
    def effect(self) -> str:
        return map_from_dict(self._raw, "state", "effect")

    @effect.setter
    def effect(self, effect: str) -> None:
        self.set(effect=effect)

    @property
    def colormode(self) -> str:
        return map_from_dict(self._raw, "state", "colormode")

    @colormode.setter
    def colormode(self, colormode: str) -> None:
        self.set(colormode=colormode)

    @property
    def reachable(self) -> bool:
        return map_from_dict(self._raw, "state", "reachable")

    @reachable.setter
    def reachable(self, reachable: bool) -> None:
        self.set(reachable=reachable)

    @property
    def transitiontime(self) -> None:
        return None

    @transitiontime.setter
    def transitiontime(self, transitiontime: int) -> None:
        self.set(transitiontime=transitiontime)

    @property
    def bri_inc(self) -> None:
        return None

    @bri_inc.setter
    def bri_inc(self, bri_inc: int) -> None:
        self.set(bri_inc=bri_inc)

    @property
    def hue_inc(self) -> None:
        return None

    @hue_inc.setter
    def hue_inc(self, hue_inc: int) -> None:
        self.set(hue_inc=hue_inc)

    @property
    def sat_inc(self) -> None:
        return None

    @sat_inc.setter
    def sat_inc(self, sat_inc: int) -> None:
        self.set(sat_inc=sat_inc)

    @property
    def xy_inc(self) -> None:
        return None

    @xy_inc.setter
    def xy_inc(self, xy_inc: list[float, float]) -> None:
        self.set(xy_inc=xy_inc)

    @property
    def ct_inc(self) -> None:
        return None

    @ct_inc.setter
    def ct_inc(self, ct_inc: int) -> None:
        self.set(ct_inc=ct_inc)

    def set(self, on: bool = None, bri: int = None, hue: int = None, sat: int = None, xy: list[float, float] = None,
            ct: int = None, alert: str = None, effect: str = None, colormode: str = None,
            reachable: bool = None, transitiontime: int = None, bri_inc: int = None, hue_inc: int = None,
            sat_inc: int = None, xy_inc: list[float, float] = None, ct_inc: int = None) -> None:
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
        if transitiontime is not None:
            val["transitiontime"] = transitiontime
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
        self.set_data("state", val)


class Light(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.state = LightState("", uri)
        self.capabilities = LightCapabilities("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.state.load_data(self._raw)
        self.capabilities.load_data(self._raw)

    @property
    def name(self) -> str:
        return map_from_dict(self._raw, "name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def type(self) -> str:
        return map_from_dict(self._raw, "type")

    @property
    def modelid(self) -> str:
        return map_from_dict(self._raw, "modelid")

    @property
    def uniqueid(self) -> str:
        return map_from_dict(self._raw, "uniqueid")

    @property
    def manufacturername(self) -> str:
        return map_from_dict(self._raw, "manufacturername")

    @property
    def productname(self) -> str:
        return map_from_dict(self._raw, "productname")

    @property
    def luminaireuniqueid(self) -> str:
        return map_from_dict(self._raw, "luminaireuniqueid")

    @property
    def swversion(self) -> str:
        return map_from_dict(self._raw, "swversion")

    def switch_on(self) -> None:
        self.state.on = True

    def switch_off(self) -> None:
        self.state.on = False

    def toggle(self) -> None:
        if self.state.on:
            self.switch_off()
        else:
            self.switch_on()

    def set(self, name: str = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        self.set_data("", val)
