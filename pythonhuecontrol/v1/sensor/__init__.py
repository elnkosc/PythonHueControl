from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


class SensorState(HueObject):
    @property
    def presence(self) -> bool:
        return map_from_dict(self._raw, "state", "presence")

    @presence.setter
    def presence(self, presence: bool) -> None:
        self.set(presence=presence)

    @property
    def daylight(self) -> bool:
        return map_from_dict(self._raw, "state", "daylight")

    @property
    def buttonevent(self) -> int:
        return map_from_dict(self._raw, "state", "buttonevent")

    @property
    def lastupdated(self) -> str:
        return map_from_dict(self._raw, "state", "lastupdated")

    def set(self, presence: bool = None) -> None:
        val = {}
        if presence is not None:
            val["presence"] = presence
        self.set_data("state", val)


class SensorConfig(HueObject):
    @property
    def on(self) -> bool:
        return map_from_dict(self._raw, "config", "on")

    @on.setter
    def on(self, on: bool) -> None:
        self.set(on=on)

    @property
    def reachable(self) -> bool:
        return map_from_dict(self._raw, "config", "reachable")

    @property
    def battery(self) -> int:
        return map_from_dict(self._raw, "config", "battery")

    def set(self, on: bool = None) -> None:
        val = {}
        if on is not None:
            val["on"] = on
        self.set_data("config", val)


class Sensor(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.config = SensorConfig("", uri)
        self.state = SensorState("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.config.load_data(self._raw)
        self.state.load_data(self._raw)

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
    def swversion(self) -> str:
        return map_from_dict(self._raw, "swversion")

    @property
    def recycle(self) -> bool:
        return map_from_dict(self._raw, "recycle")

    def set(self, name: str = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        self.set_data("", val)
