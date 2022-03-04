from pythonhuecontrol.v1 import HueObject, map_from_dict, construct_dict


class SceneAppData(HueObject):
    @property
    def version(self) -> int:
        return self.map_from_raw("appdata", "version")

    @property
    def data(self) -> str:
        return self.map_from_raw("appdata", "data")


class SceneLightStateItem:
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


class SceneLightStateList:
    def __init__(self) -> None:
        self._light_state_list = {}

    def __getitem__(self, key: str) -> SceneLightStateItem:
        return self._light_state_list[key]

    def __delitem__(self, key: str) -> None:
        del self._light_state_list[key]

    def __setitem__(self, key: str, value: SceneLightStateItem) -> None:
        self._light_state_list[key] = value

    def __len__(self) -> int:
        return len(self._light_state_list)

    def __contains__(self, key: str) -> bool:
        if key in self._light_state_list:
            return True
        else:
            return False

    def as_dict(self) -> dict:
        return self._light_state_list


class SceneLightStates(HueObject):
    def __getitem__(self, key: str) -> SceneLightStateItem:
        return SceneLightStateItem(state=self.map_from_raw("lightstates", key))

    def __setitem__(self, key: str, value: SceneLightStateItem) -> None:
        self.set_data("lightstates/" + key, value.as_dict())


class Scene(HueObject):
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._appdata = SceneAppData(identity, uri, raw)
        self._lightstates = SceneLightStates(identity, uri, raw)
        super().__init__(identity, uri, raw)

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
        return self._appdata

    @property
    def lightstates(self) -> SceneLightStates:
        return self._lightstates

    def set(self, name: str = None, lights: list[str] = None) -> None:
        self.set_data("", construct_dict(name=name, lights=lights))
