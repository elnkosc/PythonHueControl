from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


class LightState(HueObject):
    @property
    def on(self) -> object:
        return map_from_dict(self._raw, "state", "on")

    @on.setter
    def on(self, on: bool) -> None:
        self.set(on=on)

    @property
    def bri(self) -> object:
        return map_from_dict(self._raw, "state", "bri")

    @bri.setter
    def bri(self, bri: int) -> None:
        self.set(bri=bri)

    @property
    def hue(self) -> object:
        return map_from_dict(self._raw, "state", "hue")

    @hue.setter
    def hue(self, hue: int) -> None:
        self.set(hue=hue)

    @property
    def sat(self) -> object:
        return map_from_dict(self._raw, "state", "sat")

    @sat.setter
    def sat(self, sat: int) -> None:
        self.set(sat=sat)

    @property
    def xy(self) -> object:
        return map_from_dict(self._raw, "state", "xy")

    @xy.setter
    def xy(self, xy: list[float, float]) -> None:
        self.set(xy=xy)

    @property
    def ct(self) -> object:
        return map_from_dict(self._raw, "state", "cy")

    @ct.setter
    def ct(self, ct: int) -> None:
        self.set(ct=ct)

    @property
    def alert(self) -> object:
        return map_from_dict(self._raw, "state", "alert")

    @alert.setter
    def alert(self, alert: str) -> None:
        self.set(alert=alert)

    @property
    def effect(self) -> object:
        return map_from_dict(self._raw, "state", "effect")

    @effect.setter
    def effect(self, effect: str) -> None:
        self.set(effect=effect)

    @property
    def colormode(self) -> object:
        return map_from_dict(self._raw, "state", "colormode")

    @colormode.setter
    def colormode(self, colormode: str) -> None:
        self.set(colormode=colormode)

    @property
    def reachable(self) -> object:
        return map_from_dict(self._raw, "state", "reachable")

    @reachable.setter
    def reachable(self, reachable: bool) -> None:
        self.set(reachable=reachable)

    def set(self, on: bool = None, bri: int = None, hue: int = None, sat: int = None, xy: list[float, float] = None,
            ct: int = None, alert: str = None, effect: str = None, colormode: str = None,
            reachable: bool = None) -> None:
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
        self.set_data("state", val)


class Light(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.state = LightState("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.state.load_data(self._raw)

    @property
    def name(self) -> object:
        return map_from_dict(self._raw, "name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def type(self) -> object:
        return map_from_dict(self._raw, "type")

    @property
    def modelid(self) -> object:
        return map_from_dict(self._raw, "modelid")

    @property
    def uniqueid(self) -> object:
        return map_from_dict(self._raw, "uniqueid")

    @property
    def manufacturername(self) -> object:
        return map_from_dict(self._raw, "manufacturername")

    @property
    def luminaireuniqueid(self) -> object:
        return map_from_dict(self._raw, "luminaireuniqueid")

    @property
    def streaming(self) -> object:
        return map_from_dict(self._raw, "streaming")

    @property
    def renderer(self) -> object:
        return map_from_dict(self._raw, "renderer")

    @property
    def proxy(self) -> object:
        return map_from_dict(self._raw, "proxy")

    @property
    def swversion(self) -> object:
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
