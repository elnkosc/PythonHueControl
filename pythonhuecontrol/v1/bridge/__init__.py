import requests
import time
import json
from pythonhuecontrol.v1 import HueObject, map_from_dict, scan_new, construct_dict
from pythonhuecontrol.v1.configuration import Configuration
from pythonhuecontrol.v1.light import Light
from pythonhuecontrol.v1.group import Group
from pythonhuecontrol.v1.sensor import Sensor
from pythonhuecontrol.v1.rule import Rule, RuleCondition, RuleAction
from pythonhuecontrol.v1.scene import Scene, SceneLightStateList
from pythonhuecontrol.v1.schedule import Schedule
from pythonhuecontrol.v1.resourcelinks import ResourceLinks
from pythonhuecontrol.v1.capabilities import Capabilities


def discover_bridge() -> str:
    ipaddress = None
    req = requests.get("https://discovery.meethue.com/")
    json_data = req.json()
    if req.status_code == 200 and len(json_data) > 0 and "internalipaddress" in json_data[0]:
        ipaddress = json_data[0]["internalipaddress"]
    return ipaddress


def create_bridge_user(uri: str, device_type: str, generate_client_key: bool = False,
                       wait_time: int = 60) -> tuple[str, str]:
    seconds = 0
    username = None
    clientkey = None
    while seconds < wait_time and username is None:
        time.sleep(1)
        seconds += 1
        json_data = {"devicetype": device_type}
        if generate_client_key:
            json_data["generateclientkey"] = True
        req = requests.post(uri, data=json.dumps(json_data))
        if req.status_code == 200:
            username = map_from_dict(req.json()[0], "success", "username")
            clientkey = map_from_dict(req.json()[0], "success", "clientkey")
    return username, clientkey


class Bridge(HueObject):
    @property
    def light_ids(self) -> list[str]:
        return [light_id for light_id in self.map_from_raw("lights")]

    @property
    def group_ids(self) -> list[str]:
        return [group_id for group_id in self.map_from_raw("groups")]

    @property
    def sensor_ids(self) -> list[str]:
        return [sensor_id for sensor_id in self.map_from_raw("sensors")]

    @property
    def scene_ids(self) -> list[str]:
        return [scene_id for scene_id in self.map_from_raw("scenes")]

    @property
    def rule_ids(self) -> list[str]:
        return [rule_id for rule_id in self.map_from_raw("rules")]

    @property
    def schedule_ids(self) -> list[str]:
        return [schedule_id for schedule_id in self.map_from_raw("schedules")]

    @property
    def resourcelinks_ids(self) -> list[str]:
        return [resourcelinks_id for resourcelinks_id in self.map_from_raw("resourcelinks")]

    @property
    def config(self) -> Configuration:
        return Configuration("", self._uri + "/config", raw=self.map_from_raw("config"))

    @property
    def capabilities(self) -> Capabilities:
        return Capabilities("", self._uri + "/capabilities", raw=self.map_from_raw("capabilities"))

    def light(self, light_id: str) -> Light:
        return Light(light_id, self._uri + "/lights/" + light_id,
                     raw=self.map_from_raw("lights", light_id))

    def group(self, group_id: str) -> Group:
        return Group(group_id, self._uri + "/groups/" + group_id,
                     raw=self.map_from_raw("groups", group_id))

    def sensor(self, sensor_id: str) -> Sensor:
        return Sensor(sensor_id, self._uri + "/sensors/" + sensor_id,
                      raw=self.map_from_raw("sensors", sensor_id))

    def schedule(self, schedule_id: str) -> Schedule:
        return Schedule(schedule_id, self._uri + "/schedules/" + schedule_id,
                        raw=self.map_from_raw("schedules", schedule_id))

    def scene(self, scene_id: str) -> Scene:
        return Scene(scene_id, self._uri + "/scenes/" + scene_id,
                     raw=self.map_from_raw("scenes", scene_id))

    def rule(self, rule_id: str) -> Rule:
        return Rule(rule_id, self._uri + "/rules/" + rule_id,
                    raw=self.map_from_raw("rules", rule_id))

    def resourcelinks(self, resourcelink_id: str) -> ResourceLinks:
        return ResourceLinks(resourcelink_id, self._uri + "/resourcelinks/" + resourcelink_id,
                             raw=self.map_from_raw("resourcelinks", resourcelink_id))

    def new_sensors(self) -> list:
        return scan_new(self._uri + "/sensors/new")

    def new_lights(self) -> list:
        return scan_new(self._uri + "/lights/new")

    def search_lights(self) -> None:
        requests.post(self._uri + "/lights", data={})
        self.load_data()

    def search_sensors(self) -> None:
        requests.post(self._uri + "/sensors", data={})
        self.load_data()

    def all_on(self) -> None:
        self.group("0").switch_on()

    def all_off(self) -> None:
        self.group("0").switch_off()

    def all_single_blink(self) -> None:
        self.group("0").single_blink()

    def all_multiple_blinks(self) -> None:
        self.group("0").multiple_blinks()

    def all_set_rgb_color(self, red: int, green: int, blue: int) -> None:
        self.group("0").set_rgb_color(red, green, blue)

    def all_set_hex_color(self, hex_color: str) -> None:
        self.group("0").set_hex_color(hex_color)

    def all_color_loop(self) -> None:
        self.group("0").color_loop()

    def all_brightness_loop(self) -> None:
        self.group("0").brightness_loop()

    def create_group(self, name: str, lights: list[str], group_type: str = "LightGroup",
                     group_class: str = "Other") -> Group:
        json_data = construct_dict(name=name, type=group_type, lights=lights)

        # item class only present for Rooms
        if group_type == "Room":
            json_data["class"] = group_class

        if self.parse_response(requests.post(self._uri + "/groups", data=json.dumps(json_data))):
            if self._response_json == "":
                raise Exception("Unknown Error: Group ID unavailable")
            return self.group(self._response_message)

    def create_schedule(self, name: str, localtime: str, address: str, method: str, body: dict,
                        description: str = "", status: str = "enabled", autodelete: bool = True,
                        recycle: bool = False) -> Schedule:
        json_data = construct_dict(name=name, localtime=localtime,
                                   command={"address": address, "method": method, "body": body},
                                   description=description, status=status, autodelete=autodelete, recycle=recycle)
        if self.parse_response(requests.post(self._uri + "/schedules", data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Schedule ID unavailable")
            return self.schedule(self._response_message)

    def create_rule(self, name: str, conditions: list[RuleCondition], actions: list[RuleAction]) -> Rule:
        json_data = construct_dict(name=name,conditions=[x.as_dict() for x in conditions],
                                   actions=[y.as_dict() for y in actions])
        if self.parse_response(requests.post(self._uri + "/rules", data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Rule ID unavailable")
            return self.rule(self._response_message)

    def create_scene(self, name: str, recycle: bool, scene_type: str, lights: list = None, group: str = None) -> Scene:
        if lights is None and group is None:
            raise Exception("Either lights or group should be specified")

        if group is not None:
            json_data = construct_dict(name=name, recycle=recycle, type=scene_type, group=group)
        else:
            json_data = construct_dict(name=name, recycle=recycle, type=scene_type, lights=lights)

        if self.parse_response(requests.post(self._uri + "/scenes", data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Scene ID unavailable")
            return self.scene(self._response_message)

    def create_lightstates_scene(self, name: str, lights: list, appdata: dict,
                                 lightstates: SceneLightStateList) -> Scene:
        json_data = construct_dict(name=name, lights=lights, appdata=appdata, lightstates=lightstates.as_dict())
        if self.parse_response(requests.post(self._uri + "/scenes", data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Scene ID unavailable")
            return self.scene(self._response_message)

    def create_resourcelinks(self, name: str, description: str = None, resource_type: str = None, classid: int = None,
                             owner: str = None, recycle: bool = None, links: list[str] = None) -> ResourceLinks:
        json_data = construct_dict(name=name, description=description, type=resource_type, classid=classid,
                                   owner=owner, recycle=recycle, links=links)
        if self.parse_response(requests.post(self._uri + "/resourcelinks", data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Resourcelinks ID unavailable")
            return self.resourcelinks(self._response_message)
