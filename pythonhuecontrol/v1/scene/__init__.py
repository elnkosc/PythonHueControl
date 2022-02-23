from pythonhuecontrol.v1 import HueObject, map_from_dict


class SceneAppData(HueObject):
    @property
    def version(self) -> int:
        return self.map_from_raw("appdata", "version")

    @property
    def data(self) -> str:
        return self.map_from_raw("appdata", "data")


class SceneLightState:
    def __init__(self, state: dict = None, on: bool = None, bri: int = None, hue: int = None, sat: int = None,
                 xy: list[float, float] = None, ct: int = None, effect: str = None, transitiontime: int = None) -> None:
        if state is not None:
            self.on = map_from_dict(state, "on")
            self.bri = map_from_dict(state, "bri")
            self.hue = map_from_dict(state, "hue")
            self.sat = map_from_dict(state, "sat")
            self.xy = map_from_dict(state, "xy")
            self.ct = map_from_dict(state, "ct")
            self.effect = map_from_dict(state, "effect")
            self.transitiontime = map_from_dict(state, "transitiontime")
        else:
            self.on = on
            self.bri = bri
            self.hue = hue
            self.sat = sat
            self.xy = xy
            self.ct = ct
            self.effect = effect
            self.transitiontime = transitiontime

    def as_dict(self) -> dict:
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
        return result


class SceneLightStateList(HueObject):
    def __getitem__(self, key: str) -> SceneLightState:
        return SceneLightState(state=self.map_from_raw("lightstates", key))

    def __setitem__(self, key: str, value: SceneLightState) -> None:
        self.set_data("lightstates/" + key, value.as_dict())


class Scene(HueObject):
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
    def group(self) -> str:
        return self.map_from_raw("group")

    @property
    def lights(self) -> list[str]:
        return self.map_from_raw("lights")

    @lights.setter
    def lights(self, lights: list[str]) -> None:
        self.set(lights=lights)

    @property
    def owner(self) -> str:
        return self.map_from_raw("owner")

    @property
    def recycle(self) -> bool:
        return self.map_from_raw("recycle")

    @property
    def locked(self) -> bool:
        return self.map_from_raw("locked")

    @property
    def picture(self) -> str:
        return self.map_from_raw("picture")

    @property
    def image(self) -> str:
        return self.map_from_raw("image")

    @property
    def lastupdated(self) -> str:
        return self.map_from_raw("lastupdated")

    @property
    def version(self) -> int:
        return self.map_from_raw("version")

    @property
    def appdata(self) -> SceneAppData:
        return SceneAppData("", self._uri, raw=self._raw)

    @property
    def lightstates(self) -> SceneLightStateList:
        return SceneLightStateList("", self._uri, raw=self._raw)

    def set(self, name: str = None, lights: list[str] = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        if lights is not None:
            val["lights"] = lights
        self.set_data("", val)
