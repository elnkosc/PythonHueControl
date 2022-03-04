from pythonhuecontrol.v1 import HueObject, construct_dict
from rgbxy import Converter, GamutB
import time


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
        self.set_data("action", construct_dict(on=on,bri=bri, hue=hue, sat=sat, xy=xy, ct=ct, alert=alert,
                                               effect=effect, transitiontime=transitiontime, scene=scene,
                                               bri_inc=bri_inc, hue_inc=hue_inc, sat_inc=sat_inc, xy_inc=xy_inc,
                                               ct_inc=ct_inc))


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
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._state = GroupState(identity, uri, raw)
        self._action = GroupAction(identity, uri, raw)
        self._presence = GroupPresence(identity, uri, raw)
        self._lightlevel = GroupLightLevel(identity, uri, raw)
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
        self._action.on = True

    def switch_off(self) -> None:
        self._action.on = False

    def set_rgb_color(self, red: int, green: int, blue: int) -> None:
        # gamutB is chosen 'average' as lights might have different individual gamuts
        converter = Converter(GamutB)
        self._action.xy = converter.rgb_to_xy(red % 256, green % 256, blue % 256)

    def set_hex_color(self, hex_color) -> None:
        if len(hex_color) == 6:
            self.set_rgb_color(int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))

    def single_blink(self) -> None:
        self._action.alert = "select"

    def multiple_blinks(self) -> None:
        self._action.alert = "lselect"

    def color_loop(self) -> None:
        self._action.effect = "colorloop"

    def brightness_loop(self) -> None:
        self._action.bri = 0
        effect_duration = 20.0
        transitiontime = int(254/effect_duration)
        self._action.set(bri=254, transitiontime=transitiontime)
        time.sleep(effect_duration/10)

    @property
    def state(self) -> GroupState:
        return self._state

    @property
    def action(self) -> GroupAction:
        return self._action

    @property
    def presence(self) -> GroupPresence:
        return self._presence

    @property
    def lightlevel(self) -> GroupLightLevel:
        return self._lightlevel

    def set(self, name: str = None, lights: list[str] = None, sensors: list[str] = None, group_class: str = None,
            recycle: bool = None):
        val = construct_dict(name=name, lights=lights, sensors=sensors, recycle=recycle)
        val["class"] = group_class
        self.set_data("", val)
