from pythonhuecontrol.v1 import HueObject


class SensorState(HueObject):
    @property
    def presence(self) -> bool:
        return self.map_from_raw("state", "presence")

    @presence.setter
    def presence(self, presence: bool) -> None:
        self.set(presence=presence)

    @property
    def daylight(self) -> bool:
        return self.map_from_raw("state", "daylight")

    @property
    def buttonevent(self) -> int:
        return self.map_from_raw("state", "buttonevent")

    @property
    def lastupdated(self) -> str:
        return self.map_from_raw("state", "lastupdated")

    def set(self, presence: bool = None) -> None:
        val = {}
        if presence is not None:
            val["presence"] = presence
        self.set_data("state", val)


class SensorConfig(HueObject):
    @property
    def on(self) -> bool:
        return self.map_from_raw("config", "on")

    @on.setter
    def on(self, on: bool) -> None:
        self.set(on=on)

    @property
    def reachable(self) -> bool:
        return self.map_from_raw("config", "reachable")

    @property
    def battery(self) -> int:
        return self.map_from_raw("config", "battery")

    def set(self, on: bool = None) -> None:
        val = {}
        if on is not None:
            val["on"] = on
        self.set_data("config", val)


class Sensor(HueObject):
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._state = SensorState(identity, uri, raw)
        self._config = SensorConfig(identity, uri, raw)
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
    def modelid(self) -> str:
        return self.map_from_raw("modelid")

    @property
    def uniqueid(self) -> str:
        return self.map_from_raw("uniqueid")

    @property
    def manufacturername(self) -> str:
        return self.map_from_raw("manufacturername")

    @property
    def swversion(self) -> str:
        return self.map_from_raw("swversion")

    @property
    def recycle(self) -> bool:
        return self.map_from_raw("recycle")

    @property
    def config(self) -> SensorConfig:
        return self._config

    @property
    def state(self) -> SensorState:
        return self._state

    def set(self, name: str = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        self.set_data("", val)
