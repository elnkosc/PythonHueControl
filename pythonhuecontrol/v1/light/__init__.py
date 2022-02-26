import time
from rgbxy import Converter, GamutA, GamutB, GamutC
from pythonhuecontrol.v1 import HueObject


class LightCapabilitiesStreaming(HueObject):
    @property
    def renderer(self) -> bool:
        return self.map_from_raw("capabilities", "streaming", "renderer")

    @property
    def proxy(self) -> bool:
        return self.map_from_raw("capabilities", "streaming", "proxy")


class LightCapabilitiesControlCt(HueObject):
    @property
    def min(self) -> int:
        return self.map_from_raw("capabilities", "control", "ct", "min")

    @property
    def max(self) -> int:
        return self.map_from_raw("capabilities", "control", "ct", "max")


class LightCapabilitiesControl(HueObject):
    @property
    def mindimlevel(self) -> int:
        return self.map_from_raw("capabilities", "control", "mindimlevel")

    @property
    def maxlumen(self) -> int:
        return self.map_from_raw("capabilities", "control", "maxlumen")

    @property
    def colorgamuttype(self) -> str:
        return self.map_from_raw("capabilities", "control", "colorgamuttype")

    @property
    def colorgamut(self) -> list[float, float, float]:
        return self.map_from_raw("capabilities", "control", "colorgamut")

    @property
    def ct(self) -> LightCapabilitiesControlCt:
        return LightCapabilitiesControlCt("", self._uri, raw=self._raw)


class LightCapabilities(HueObject):
    @property
    def certified(self) -> bool:
        return self.map_from_raw("capabilities", "certified")

    @property
    def streaming(self) -> LightCapabilitiesStreaming:
        return LightCapabilitiesStreaming("", self._uri, raw=self._raw)

    @property
    def control(self) -> LightCapabilitiesControl:
        return LightCapabilitiesControl("", self._uri, raw=self._raw)


class LightState(HueObject):
    @property
    def on(self) -> object:
        return self.map_from_raw("state", "on")

    @on.setter
    def on(self, on: bool) -> None:
        self.set(on=on)

    @property
    def bri(self) -> int:
        return self.map_from_raw("state", "bri")

    @bri.setter
    def bri(self, bri: int) -> None:
        self.set(bri=bri)

    @property
    def hue(self) -> int:
        return self.map_from_raw("state", "hue")

    @hue.setter
    def hue(self, hue: int) -> None:
        self.set(hue=hue)

    @property
    def sat(self) -> int:
        return self.map_from_raw("state", "sat")

    @sat.setter
    def sat(self, sat: int) -> None:
        self.set(sat=sat)

    @property
    def xy(self) -> list[float, float]:
        return self.map_from_raw("state", "xy")

    @xy.setter
    def xy(self, xy: list[float, float]) -> None:
        self.set(xy=xy)

    @property
    def ct(self) -> int:
        return self.map_from_raw("state", "ct")

    @ct.setter
    def ct(self, ct: int) -> None:
        self.set(ct=ct)

    @property
    def alert(self) -> str:
        return self.map_from_raw("state", "alert")

    @alert.setter
    def alert(self, alert: str) -> None:
        self.set(alert=alert)

    @property
    def effect(self) -> str:
        return self.map_from_raw("state", "effect")

    @effect.setter
    def effect(self, effect: str) -> None:
        self.set(effect=effect)

    @property
    def colormode(self) -> str:
        return self.map_from_raw("state", "colormode")

    @colormode.setter
    def colormode(self, colormode: str) -> None:
        self.set(colormode=colormode)

    @property
    def reachable(self) -> bool:
        return self.map_from_raw("state", "reachable")

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
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._state = LightState(identity, uri, raw)
        self._capabilities = LightCapabilities(identity, uri, raw)
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
    def productname(self) -> str:
        return self.map_from_raw("productname")

    @property
    def luminaireuniqueid(self) -> str:
        return self.map_from_raw("luminaireuniqueid")

    @property
    def swversion(self) -> str:
        return self.map_from_raw("swversion")

    def switch_on(self) -> None:
        self.state.on = True

    def switch_off(self) -> None:
        self.state.on = False

    def toggle(self) -> None:
        if self.state.on:
            self.switch_off()
        else:
            self.switch_on()

    def set_rgb_color(self, red: int, green: int, blue: int) -> None:
        gamut = self.capabilities.control.colorgamuttype
        if gamut is None:
            return
        if gamut == "A":
            converter = Converter(GamutA)
        elif gamut == "C":
            converter = Converter(GamutB)
        else:
            converter = Converter(GamutC)
        self.state.xy = converter.rgb_to_xy(red % 256, green % 256, blue % 256)

    def set_hex_color(self, hex_color) -> None:
        if len(hex_color) == 6:
            self.set_rgb_color(int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))

    def single_blink(self) -> None:
        self.state.alert = "select"

    def multiple_blinks(self) -> None:
        self.state.alert = "lselect"

    def color_loop(self) -> None:
        self.state.effect = "colorloop"

    def brightness_loop(self) -> None:
        bri = self.state.bri
        effect_duration = 20.0

        transitiontime = int((254-bri)/effect_duration)
        self.state.set(bri=254, transitiontime=transitiontime)
        time.sleep(transitiontime/10)

        transitiontime = int(effect_duration)
        self.state.set(bri=0, transitiontime=transitiontime)
        time.sleep(transitiontime/10)

        transitiontime = int(bri/effect_duration)
        self.state.set(bri=bri, transitiontime=transitiontime)
        time.sleep(transitiontime/10)

    @property
    def state(self) -> LightState:
        return self._state

    @property
    def capabilities(self) -> LightCapabilities:
        return self._capabilities

    def set(self, name: str = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        self.set_data("", val)
