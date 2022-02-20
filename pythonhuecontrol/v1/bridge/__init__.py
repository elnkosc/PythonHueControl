import requests
import time
import json
from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
from pythonhuecontrol.v1 import scan_new
from pythonhuecontrol.v1.light import Light
from pythonhuecontrol.v1.group import Group
from pythonhuecontrol.v1.sensor import Sensor
from pythonhuecontrol.v1.rule import Rule
from pythonhuecontrol.v1.scene import Scene
from pythonhuecontrol.v1.schedule import Schedule


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
        print(req.json())
        if req.status_code == 200:
            username = map_from_dict(req.json()[0], "success", "username")
            clientkey = map_from_dict(req.json()[0], "success", "clientkey")
    return username, clientkey


class Backup(HueObject):
    @property
    def status(self) -> str:
        return map_from_dict(self._raw, "backup", "status")

    @property
    def errorcode(self) -> int:
        return map_from_dict(self._raw, "backup", "errorcode")


class InternetServices(HueObject):
    @property
    def internet(self) -> str:
        return map_from_dict(self._raw, "internetservices", "internet")

    @property
    def remoteaccess(self) -> str:
        return map_from_dict(self._raw, "internetservices", "remoteaccess")

    @property
    def time(self) -> str:
        return map_from_dict(self._raw, "internetservices", "time")

    @property
    def swupdate(self) -> str:
        return map_from_dict(self._raw, "internetservices", "swupdate")


class AutoInstall(HueObject):
    @property
    def on(self) -> bool:
        return map_from_dict(self._raw, "swupdate2", "autoinstall", "on")

    @property
    def updatetime(self) -> str:
        return map_from_dict(self._raw, "swupdate2", "autoinstall", "updatetime")


class DeviceTypes(HueObject):
    @property
    def bridge(self) -> bool:
        return map_from_dict(self._raw, "swupdate", "devicetypes", "bridge")

    @property
    def lights(self) -> list:
        return map_from_dict(self._raw, "swupdate", "devicetypes", "lights")

    @property
    def sensors(self) -> list:
        return map_from_dict(self._raw, "swupdate", "devicetypes", "sensors")


class SWUpdate(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.devicetypes = DeviceTypes("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.devicetypes.load_data(self._raw)

    @property
    def checkforupdate(self) -> bool:
        return map_from_dict(self._raw, "swupdate", "checkforupdate")

    @checkforupdate.setter
    def checkforupdate(self, checkforupdate: bool) -> None:
        self.set(checkforupdate=checkforupdate)

    @property
    def updatestate(self) -> int:
        return map_from_dict(self._raw, "swupdate", "updatestate")

    @property
    def notify(self) -> bool:
        return map_from_dict(self._raw, "swupdate", "notify")

    @notify.setter
    def notify(self, notify: bool) -> None:
        self.set(notify=notify)

    @property
    def url(self) -> str:
        return map_from_dict(self._raw, "swupdate", "url")

    @url.setter
    def url(self, url: str) -> None:
        self.set(url=url)

    @property
    def text(self) -> str:
        return map_from_dict(self._raw, "swupdate", "text")

    @text.setter
    def text(self, text: str) -> None:
        self.set(text=text)

    def set(self, checkforupdate: bool = None, notify: bool = None, url: str = None, text: str = None) -> None:
        val = {"swupdate": {}}
        if checkforupdate is not None:
            val["swupdate"]["checkforupdate"] = checkforupdate
        if notify is not None:
            val["swupdate"]["notify"] = notify
        if url is not None:
            val["swupdate"]["url"] = url
        if text is not None:
            val["swupdate"]["text"] = text
        self.set_data("", val)


class SWUpdate2(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.autoinstall = AutoInstall("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.autoinstall.load_data(self._raw)

    @property
    def bridge(self) -> dict:
        return map_from_dict(self._raw, "swupdate2", "bridge")

    @property
    def checkforupdate(self) -> bool:
        return map_from_dict(self._raw, "swupdate2", "checkforupdate")

    @checkforupdate.setter
    def checkforupdate(self, checkforupdate: bool) -> None:
        self.set(checkforupdate=checkforupdate)

    @property
    def state(self) -> str:
        return map_from_dict(self._raw, "swupdate2", "state")

    @property
    def install(self) -> bool:
        return map_from_dict(self._raw, "swupdate2", "install")

    @install.setter
    def install(self, install: bool) -> None:
        self.set(install=install)

    @property
    def lastchange(self) -> str:
        return map_from_dict(self._raw, "swupdate2", "lastchange")

    @property
    def lastinstall(self) -> str:
        return map_from_dict(self._raw, "swupdate2", "lastinstall")

    def set(self, checkforupdate: bool = None, install: bool = None) -> None:
        val = {"swupdate2": {}}
        if checkforupdate is not None:
            val["swupdate2"]["checkforupdate"] = checkforupdate
        if install is not None:
            val["swupdate2"]["install"] = install
        self.set_data("", val)


class BridgeConfig(HueObject):
    def __init__(self, identity: str, uri: str) -> None:
        self.swupdate = SWUpdate("", uri)
        self.swupdate2 = SWUpdate2("", uri)
        self.internetservices = InternetServices("", uri)
        self.backup = Backup("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.swupdate.load_data(self._raw)
        self.swupdate2.load_data(self._raw)
        self.internetservices.load_data(self._raw)
        self.backup.load_data(self._raw)

    @property
    def name(self) -> str:
        return map_from_dict(self._raw, "name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def whitelist(self) -> dict:
        return map_from_dict(self._raw, "whitelist")

    @property
    def portalstate(self) -> dict:
        return map_from_dict(self._raw, "portalstate")

    @property
    def apiversion(self) -> str:
        return map_from_dict(self._raw, "apiversion")

    @property
    def swversion(self) -> str:
        return map_from_dict(self._raw, "swversion")

    @property
    def proxyaddress(self) -> str:
        return map_from_dict(self._raw, "proxyaddress")

    @proxyaddress.setter
    def proxyaddress(self, proxyaddress: str) -> None:
        self.set(proxyaddress=proxyaddress)

    @property
    def proxyport(self) -> int:
        return map_from_dict(self._raw, "proxyport")

    @proxyport.setter
    def proxyport(self, proxyport: int) -> None:
        self.set(proxyport=proxyport)

    @property
    def linkbutton(self) -> bool:
        return map_from_dict(self._raw, "linkbutton")

    @linkbutton.setter
    def linkbutton(self, linkbutton: bool) -> None:
        self.set(linkbutton=linkbutton)

    @property
    def ipaddress(self) -> str:
        return map_from_dict(self._raw, "ipaddress")

    @ipaddress.setter
    def ipaddress(self, ipaddress: str) -> None:
        self.set(ipaddress=ipaddress)

    @property
    def mac(self) -> str:
        return map_from_dict(self._raw, "mac")

    @property
    def netmask(self) -> str:
        return map_from_dict(self._raw, "netmask")

    @netmask.setter
    def netmask(self, netmask: str) -> None:
        self.set(netmask=netmask)

    @property
    def gateway(self) -> str:
        return map_from_dict(self._raw, "gateway")

    @gateway.setter
    def gateway(self, gateway: str) -> None:
        self.set(gateway=gateway)

    @property
    def dhcp(self) -> bool:
        return map_from_dict(self._raw, "dhcp")

    @dhcp.setter
    def dhcp(self, dhcp: bool) -> None:
        self.set(dhcp=dhcp)

    @property
    def portalservices(self) -> bool:
        return map_from_dict(self._raw, "portalservices")

    @property
    def utc(self) -> str:
        return map_from_dict(self._raw, "UTC")

    @utc.setter
    def utc(self, utc: str) -> None:
        self.set(utc=utc)

    @property
    def localtime(self) -> str:
        return map_from_dict(self._raw, "localtime")

    @property
    def timezone(self) -> str:
        return map_from_dict(self._raw, "timezone")

    @timezone.setter
    def timezone(self, timezone: str) -> None:
        self.set(timezone=timezone)

    @property
    def zigbeechannel(self) -> int:
        return map_from_dict(self._raw, "zigbeechannel")

    @zigbeechannel.setter
    def zigbeechannel(self, zigbeechannel: int) -> None:
        self.set(zigbeechannel=zigbeechannel)

    @property
    def modelid(self) -> str:
        return map_from_dict(self._raw, "modelid")

    @property
    def bridgeid(self) -> str:
        return map_from_dict(self._raw, "bridgeid")

    @property
    def factorynew(self) -> bool:
        return map_from_dict(self._raw, "factorynew")

    @property
    def replacesbridgeid(self) -> str:
        return map_from_dict(self._raw, "replacesbridgeid")

    @property
    def datastoreversion(self) -> str:
        return map_from_dict(self._raw, "datastoreversion")

    @property
    def starterkitid(self) -> str:
        return map_from_dict(self._raw, "starterkitid")

    @property
    def touchlink(self) -> bool:
        return map_from_dict(self._raw, "touchlink")

    @touchlink.setter
    def touchlink(self, touchlink: bool) -> None:
        self.set(touchlink=touchlink)

    def set(self, name: str = None, proxyaddress: str = None, proxyport: int = None, linkbutton: bool = None,
            ipaddress: str = None, netmask: str = None, gateway: str = None, dhcp: bool = None, utc: str = None,
            timezone: str = None, zigbeechannel: int = None, touchlink: bool = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        if proxyaddress is not None:
            val["proxyaddress"] = proxyaddress
        if proxyport is not None:
            val["proxyport"] = proxyport
        if linkbutton is not None:
            val["linkbutton"] = linkbutton
        if ipaddress is not None:
            val["ipaddress"] = ipaddress
        if netmask is not None:
            val["netmask"] = netmask
        if gateway is not None:
            val["gateway"] = gateway
        if dhcp is not None:
            val["dhcp"] = dhcp
        if utc is not None:
            val["UTC"] = utc
        if timezone is not None:
            val["timezone"] = timezone
        if zigbeechannel is not None:
            val["zigbeechannel"] = zigbeechannel
        if touchlink is not None:
            val["touchlink"] = touchlink
        self.set_data("", val)


class Bridge(HueObject):
    def __init__(self, identity: str, uri: str, clientkey: str = None) -> None:
        self.registration_uri = uri
        self.groups_uri = uri + "/groups"
        self.lights_uri = uri + "/lights"
        self.sensors_uri = uri + "/sensors"
        self.schedules_uri = uri + "/schedules"
        self.scenes_uri = uri + "/scenes"
        self.rules_uri = uri + "/rules"
        self.new_lights_uri = uri + "/lights/new"
        self.new_sensors_uri = uri + "/sensors/new"
        self.clientkey = clientkey
        self.config = BridgeConfig("", uri + "/config")
        super().__init__(identity, uri)

    def load_data(self, raw: dict = None) -> None:
        super().load_data(raw)
        self.config.load_data(map_from_dict(self._raw, "config"))

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

    def light(self, light_id: str) -> Light:
        return Light(light_id, self.lights_uri + "/" + light_id)

    def group(self, group_id: str) -> Group:
        return Group(group_id, self.groups_uri + "/" + group_id)

    def sensor(self, sensor_id: str) -> Sensor:
        return Sensor(sensor_id, self.sensors_uri + "/" + sensor_id)

    def schedule(self, schedule_id: str) -> Schedule:
        return Schedule(schedule_id, self.schedules_uri + "/" + schedule_id)

    def scene(self, scene_id: str) -> Scene:
        return Scene(scene_id, self.scenes_uri + "/" + scene_id)

    def rule(self, rule_id: str) -> Rule:
        return Rule(rule_id, self.rules_uri + "/" + rule_id)

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
