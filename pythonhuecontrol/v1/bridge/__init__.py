import requests
import time
import json
from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
from pythonhuecontrol.v1 import scan_new
from pythonhuecontrol.v1.configuration import Configuration
from pythonhuecontrol.v1.light import Light
from pythonhuecontrol.v1.group import Group
from pythonhuecontrol.v1.sensor import Sensor
from pythonhuecontrol.v1.rule import Rule
from pythonhuecontrol.v1.scene import Scene
from pythonhuecontrol.v1.schedule import Schedule
from pythonhuecontrol.v1.resourcelinks import ResourceLinks


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
    def __init__(self, identity: str, uri: str, clientkey: str = None) -> None:
        self.registration_uri = uri
        self.config_uri = uri + "/config"
        self.groups_uri = uri + "/groups"
        self.lights_uri = uri + "/lights"
        self.sensors_uri = uri + "/sensors"
        self.schedules_uri = uri + "/schedules"
        self.scenes_uri = uri + "/scenes"
        self.rules_uri = uri + "/rules"
        self.resourcelinks_uri = uri + "/resourcelinks"
        self.new_lights_uri = uri + "/lights/new"
        self.new_sensors_uri = uri + "/sensors/new"
        self.clientkey = clientkey
        super().__init__(identity, uri)

    @property
    def light_ids(self) -> dict:
        return map_from_dict(self._raw, "lights")

    @property
    def group_ids(self) -> dict:
        return map_from_dict(self._raw, "groups")

    @property
    def sensor_ids(self) -> dict:
        return map_from_dict(self._raw, "sensors")

    @property
    def scene_ids(self) -> dict:
        return map_from_dict(self._raw, "scenes")

    @property
    def rule_ids(self) -> dict:
        return map_from_dict(self._raw, "rules")

    @property
    def schedule_ids(self) -> dict:
        return map_from_dict(self._raw, "schedules")

    @property
    def resourcelinks_ids(self) -> dict:
        return map_from_dict(self._raw, "resourcelinks")

    @property
    def config(self) -> Configuration:
        return Configuration("", self.config_uri, raw=map_from_dict(self._raw, "config"))

    def light(self, light_id: str) -> Light:
        return Light(light_id, self.lights_uri + "/" + light_id,
                     raw=map_from_dict(self._raw, "lights", light_id))

    def group(self, group_id: str) -> Group:
        return Group(group_id, self.groups_uri + "/" + group_id,
                     raw=map_from_dict(self._raw, "groups", group_id))

    def sensor(self, sensor_id: str) -> Sensor:
        return Sensor(sensor_id, self.sensors_uri + "/" + sensor_id,
                      raw=map_from_dict(self._raw, "sensors", sensor_id))

    def schedule(self, schedule_id: str) -> Schedule:
        return Schedule(schedule_id, self.schedules_uri + "/" + schedule_id,
                        raw=map_from_dict(self._raw, "schedules", schedule_id))

    def scene(self, scene_id: str) -> Scene:
        return Scene(scene_id, self.scenes_uri + "/" + scene_id,
                     raw=map_from_dict(self._raw, "scenes", scene_id))

    def rule(self, rule_id: str) -> Rule:
        return Rule(rule_id, self.rules_uri + "/" + rule_id,
                    raw=map_from_dict(self._raw, "rules", rule_id))

    def resourcelinks(self, resourcelink_id: str) -> ResourceLinks:
        return ResourceLinks(resourcelink_id, self.resourcelinks_uri + "/" + resourcelink_id,
                             raw=map_from_dict(self._raw, "resourcelinks", resourcelink_id))

    def new_sensors(self) -> list:
        return scan_new(self.new_sensors_uri)

    def new_lights(self) -> list:
        return scan_new(self.new_lights_uri)

    def search_lights(self) -> None:
        requests.post(self.lights_uri, data={})
        self.load_data()

    def search_sensors(self) -> None:
        requests.post(self.sensors_uri, data={})
        self.load_data()

    def create_group(self, name: str, lights: dict, group_type: str = "LightGroup",
                     group_class: str = "Other") -> Group:
        json_data = {"name": name, "type": group_type, "lights": lights}

        # item class only present for Rooms
        if group_type == "Room":
            json_data["class"] = group_class
        if self.parse_response(requests.post(self.groups_uri, data=json.dumps(json_data))):
            if self._response_json == "":
                raise Exception("Unknown Error: Group ID unavailable")
            return self.group(self._response_message)

    def create_schedule(self, name: str, localtime: str, address: str, method: str, body: dict,
                        description: str = "", status: str = "enabled", autodelete: bool = True,
                        recycle: bool = False) -> Schedule:
        json_data = {"name": name, "localtime": localtime,
                     "command": {"address": address, "method": method, "body": body},
                     "description": description, "status": status, "autodelete": autodelete, "recycle": recycle}
        if self.parse_response(requests.post(self.schedules_uri, data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Schedule ID unavailable")
            return self.schedule(self._response_message)

    def create_rule(self, name: str, status: str, conditions: list, actions: list) -> Rule:
        json_data = {"name": name, "status": status, "conditions": conditions, "actions": actions}
        if self.parse_response(requests.post(self.rules_uri, data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Rule ID unavailable")
            return self.rule(self._response_message)

    def create_scene(self, name: str, recycle: bool, scene_type: str, lights: list = None, group: str = None) -> Scene:
        if lights is None and group is None:
            raise Exception("Either lights or group should be specified")

        if group is not None:
            json_data = {"name": name, "recycle": recycle, "type": scene_type, "group": group}
        else:
            json_data = {"name": name, "recycle": recycle, "type": scene_type, "lights": lights}

        if self.parse_response(requests.post(self.scenes_uri, data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Scene ID unavailable")
            return self.scene(self._response_message)

    def create_lightstates_scene(self, name: str, lights: list, appdata: dict, lightstates: dict) -> Scene:
        json_data = {"name": name, "lights": lights, "appdata": appdata, "lightstates": lightstates}
        if self.parse_response(requests.post(self.scenes_uri, data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Scene ID unavailable")
            return self.scene(self._response_message)

    def create_resourcelinks(self, name: str, description: str = None, resource_type: str = None, classid: int = None,
                             owner: str = None, recycle: bool = None, links: list[str] = None) -> ResourceLinks:
        json_data = {"name": name}
        if description is not None:
            json_data["description"] = description
        if resource_type is not None:
            json_data["type"] = type
        if classid is not None:
            json_data["classid"] = classid
        if owner is not None:
            json_data["owner"] = owner
        if recycle is not None:
            json_data["recycle"] = recycle
        if links is not None:
            json_data["links"] = links
        if self.parse_response(requests.post(self.resourcelinks_uri, data=json.dumps(json_data))):
            if self._response_message == "":
                raise Exception("Unknown Error: Resourcelinks ID unavailable")
            return self.resourcelinks(self._response_message)
