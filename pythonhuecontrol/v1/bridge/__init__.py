import requests
import time
from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
from pythonhuecontrol.v1 import scan_new
from pythonhuecontrol.v1.light import Light
from pythonhuecontrol.v1.group import Group
from pythonhuecontrol.v1.sensor import Sensor
from pythonhuecontrol.v1.rule import Rule
from pythonhuecontrol.v1.scene import Scene
from pythonhuecontrol.v1.schedule import Schedule


class Backup(HueObject):
    @property
    def status(self):
        return map_from_dict(self.raw, "status")

    @property
    def errorcode(self):
        return map_from_dict(self.raw, "errorcode")


class InternetServices(HueObject):
    @property
    def internet(self):
        return map_from_dict(self.raw, "internet")

    @property
    def remoteaccess(self):
        return map_from_dict(self.raw, "remoteaccess")

    @property
    def time(self):
        return map_from_dict(self.raw, "time")

    @property
    def swupdate(self):
        return map_from_dict(self.raw, "swupdate")


class AutoInstall(HueObject):
    @property
    def on(self):
        return map_from_dict(self.raw, "on")

    @property
    def updatetime(self):
        return map_from_dict(self.raw, "updatetime")


class DeviceTypes(HueObject):
    @property
    def bridge(self):
        return map_from_dict(self.raw, "bridge")

    @property
    def lights(self):
        return map_from_dict(self.raw, "lights")

    @property
    def sensors(self):
        return map_from_dict(self.raw, "sensors")


class SWUpdate(HueObject):
    def __init__(self, identity, uri):
        self.devicetypes = DeviceTypes("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        if raw is None:
            self.raw = map_from_dict(self.raw, "swupdate")
        self.devicetypes.load_data(map_from_dict(self.raw, "devicetypes"))

    @property
    def checkforupdate(self):
        return map_from_dict(self.raw, "checkforupdate")

    @checkforupdate.setter
    def checkforupdate(self, checkforupdate):
        if checkforupdate:
            self.set_data("", f"{{\"swupdate\": {{\"checkforupdate\": true}}}}")
        else:
            self.set_data("", f"{{\"swupdate\": {{\"checkforupdate\": false}}}}")

    @property
    def updatestate(self):
        return map_from_dict(self.raw, "updatestate")

    @property
    def notify(self):
        return map_from_dict(self.raw, "notify")

    @notify.setter
    def notify(self, notify):
        if notify:
            self.set_data("", f"{{\"swupdate\": {{\"notify\": true}}}}")
        else:
            self.set_data("", f"{{\"swupdate\": {{\"notify\": false}}}}")

    @property
    def url(self):
        return map_from_dict(self.raw, "url")

    @url.setter
    def url(self, url):
        self.set_data("", f"{{\"swupdate\": {{\"url\": \"{url}\"}}}}")

    @property
    def text(self):
        return map_from_dict(self.raw, "text")

    @text.setter
    def text(self, text):
        self.set_data("", f"{{\"swupdate\": {{\"text\": \"{text}\"}}}}")


class SWUpdate2(HueObject):
    def __init__(self, identity, uri):
        self.autoinstall = AutoInstall("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        if raw is None:
            self.raw = map_from_dict(self.raw, "swupdate2")
        self.autoinstall.load_data(map_from_dict(self.raw, "autoinstall"))

    @property
    def bridge(self):
        return map_from_dict(self.raw, "bridge")

    @property
    def checkforupdate(self):
        return map_from_dict(self.raw, "checkforupdate")

    @checkforupdate.setter
    def checkforupdate(self, checkforupdate):
        if checkforupdate:
            self.set_data("", f"{{\"swupdate2\": {{\"checkforupdate\": true}}}}")
        else:
            self.set_data("", f"{{\"swupdate2\": {{\"checkforupdate\": false}}}}")

    @property
    def state(self):
        return map_from_dict(self.raw, "state")

    @property
    def install(self):
        return map_from_dict(self.raw, "install")

    @install.setter
    def install(self, install):
        if install:
            self.set_data("", f"{{\"swupdate2\": {{\"install\": true}}}}")
        else:
            self.set_data("", f"{{\"swupdate2\": {{\"install\": false}}}}")

    @property
    def lastchange(self):
        return map_from_dict(self.raw, "lastchange")

    @property
    def lastinstall(self):
        return map_from_dict(self.raw, "lastinstall")


class BridgeConfig(HueObject):
    def __init__(self, identity, uri):
        self.swupdate = SWUpdate("", uri)
        self.swupdate2 = SWUpdate2("", uri)
        self.internetservices = InternetServices("", uri)
        self.backup = Backup("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        self.swupdate.load_data(map_from_dict(self.raw, "swupdate"))
        self.swupdate2.load_data(map_from_dict(self.raw, "swupdate2"))
        self.internetservices.load_data(map_from_dict(self.raw, "internetservices"))
        self.backup.load_data(map_from_dict(self.raw, "backup"))

    @property
    def name(self):
        return map_from_dict(self.raw, "name")

    @name.setter
    def name(self, name):
        self.set_data("", f"{{\"name\": \"{name}\"}}")

    @property
    def whitelist(self):
        return map_from_dict(self.raw, "whitelist")

    @property
    def portalstate(self):
        return map_from_dict(self.raw, "portalstate")

    @property
    def apiversion(self):
        return map_from_dict(self.raw, "apiversion")

    @property
    def swversion(self):
        return map_from_dict(self.raw, "swversion")

    @property
    def proxyaddress(self):
        return map_from_dict(self.raw, "proxyaddress")

    @proxyaddress.setter
    def proxyaddress(self, proxyaddress):
        self.set_data("", f"{{\"proxyaddress\": \"{proxyaddress}\"}}")

    @property
    def proxyport(self):
        return map_from_dict(self.raw, "proxyport")

    @proxyport.setter
    def proxyport(self, proxyport):
        self.set_data("", f"{{\"proxyport\": {proxyport}}}")

    @property
    def linkbutton(self):
        return map_from_dict(self.raw, "linkbutton")

    @linkbutton.setter
    def linkbutton(self, linkbutton):
        if linkbutton:
            self.set_data("", f"{{\"linkbutton\": true}}")
        else:
            self.set_data("", f"{{\"linkbutton\": false}}")

    @property
    def ipaddress(self):
        return map_from_dict(self.raw, "ipaddress")

    @ipaddress.setter
    def ipaddress(self, ipaddress):
        self.set_data("", f"{{\"ipaddress\": \"{ipaddress}\"}}")

    @property
    def mac(self):
        return map_from_dict(self.raw, "mac")

    @property
    def netmask(self):
        return map_from_dict(self.raw, "netmask")

    @netmask.setter
    def netmask(self, netmask):
        self.set_data("", f"{{\"netmask\": \"{netmask}\"}}")

    @property
    def gateway(self):
        return map_from_dict(self.raw, "gateway")

    @gateway.setter
    def gateway(self, gateway):
        self.set_data("", f"{{\"gateway\": \"{gateway}\"}}")

    @property
    def dhcp(self):
        return map_from_dict(self.raw, "dhcp")

    @dhcp.setter
    def dhcp(self, dhcp):
        if dhcp:
            self.set_data("", f"{{\"dhcp\": true}}")
        else:
            self.set_data("", f"{{\"dhcp\": false}}")

    @property
    def portalservices(self):
        return map_from_dict(self.raw, "portalservices")

    @property
    def utc(self):
        return map_from_dict(self.raw, "UTC")

    @utc.setter
    def utc(self, utc):
        self.set_data("", f"{{\"UTC\": \"{utc}\"}}")

    @property
    def localtime(self):
        return map_from_dict(self.raw, "localtime")

    @property
    def timezone(self):
        return map_from_dict(self.raw, "timezone")

    @timezone.setter
    def timezone(self, timezone):
        self.set_data("", f"{{\"timezone\": \"{timezone}\"}}")

    @property
    def zigbeechannel(self):
        return map_from_dict(self.raw, "zigbeechannel")

    @zigbeechannel.setter
    def zigbeechannel(self, zigbeechannel):
        self.set_data("", f"{{\"zigbeechannel\": {zigbeechannel}}}")

    @property
    def modelid(self):
        return map_from_dict(self.raw, "modelid")

    @property
    def bridgeid(self):
        return map_from_dict(self.raw, "bridgeid")

    @property
    def factorynew(self):
        return map_from_dict(self.raw, "factorynew")

    @property
    def replacesbridgeid(self):
        return map_from_dict(self.raw, "replacesbridgeid")

    @property
    def datastoreversion(self):
        return map_from_dict(self.raw, "datastoreversion")

    @property
    def starterkitid(self):
        return map_from_dict(self.raw, "starterkitid")

    @property
    def touchlink(self):
        return map_from_dict(self.raw, "touchlink")

    @touchlink.setter
    def touchlink(self, touchlink):
        if touchlink:
            self.set_data("", f"{{\"touchlink\": true}}")
        else:
            self.set_data("", f"{{\"touchlink\": false}}")


class Bridge(HueObject):
    def __init__(self, identity, uri, clientkey=None):
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

    def load_data(self, raw=None):
        super().load_data(raw)
        self.config.load_data(map_from_dict(self.raw, "config"))

    @property
    def lights(self):
        return map_from_dict(self.raw, "lights")

    @property
    def groups(self):
        return map_from_dict(self.raw, "groups")

    @property
    def sensors(self):
        return map_from_dict(self.raw, "sensors")

    @property
    def scenes(self):
        return map_from_dict(self.raw, "scenes")

    @property
    def rules(self):
        return map_from_dict(self.raw, "rules")

    @property
    def schedules(self):
        return map_from_dict(self.raw, "schedules")

    def light(self, light_id):
        return Light(light_id, self.lights_uri + "/" + light_id)

    def group(self, group_id):
        return Group(group_id, self.groups_uri + "/" + group_id)

    def sensor(self, sensor_id):
        return Sensor(sensor_id, self.sensors_uri + "/" + sensor_id)

    def schedule(self, schedule_id):
        return Schedule(schedule_id, self.schedules_uri + "/" + schedule_id)

    def scene(self, scene_id):
        return Scene(scene_id, self.scenes_uri + "/" + scene_id)

    def rule(self, rule_id):
        return Rule(rule_id, self.rules_uri + "/" + rule_id)

    def create_user(self, device_type, generate_client_key=False, wait_time=60):
        t = 0
        while t < wait_time and self.identity is None:
            time.sleep(1)
            t += 1

            if generate_client_key:
                req = requests.post(self.registration_uri,
                                    json=f"{{\"devicetype\": {device_type}, \"generateclientkey\": true}}")
            else:
                req = requests.post(self.registration_uri, json=f"{{\"devicetype\": {device_type}}}")

            if req.status_code == 200:
                self.identity = map_from_dict(req.json()[0], "success", "username")
                self.clientkey = map_from_dict(req.json()[0], "success", "clientkey")
                self.load_data()

    def new_sensors(self):
        return scan_new(self.new_sensors_uri)

    def new_lights(self):
        return scan_new(self.new_lights_uri)

    def search_lights(self):
        requests.post(self.lights_uri, data={})
        self.load_data()

    def search_sensors(self):
        requests.post(self.sensors_uri, data={})
        self.load_data()

    def create_group(self, name, lights, group_type="LightGroup", group_class="Other"):
        req = requests.post(self.groups_uri, data={"name": name, "type": group_type,
                                                   "class": group_class, "lights": lights})

        if req.status_code == 200 and "success" in req.json()[0] and "id" in req.json()[0]["success"]:
            return self.group(req.json()[0]["success"]["id"])
        else:
            return None

    def create_schedule(self, name, localtime, command, description="", status="enabled",
                        autodelete="true", recycle="false"):
        req = requests.post(self.schedules_uri, data={"name": name, "localtime": localtime, "command": command,
                                                      "description": description, "status": status,
                                                      "autodelete": autodelete, "recycle": recycle})

        if req.status_code == 200 and "success" in req.json()[0] and "id" in req.json()[0]["success"]:
            return self.schedule(req.json()[0]["success"]["id"])
        else:
            return None

    def create_rule(self, name, status, conditions, actions):
        req = requests.post(self.rules_uri, data={"name": name, "status": status,
                                                  "conditions": conditions, "actions": actions})

        if req.status_code == 200 and "success" in req.json()[0] and "id" in req.json()[0]["success"]:
            return self.rule(req.json()[0]["success"]["id"])
        else:
            return None

    def create_scene(self, name, recycle, scene_type, lights=None, group=None):
        if lights is None and group is None:
            return None

        if group is not None:
            req = requests.post(self.scenes_uri, data={"name": name, "recycle": recycle,
                                                       "type": scene_type, "group": group})
        else:
            req = requests.post(self.scenes_uri, data={"name": name, "recycle": recycle,
                                                       "type": scene_type, "lights": lights})

        if req.status_code == 200 and "success" in req.json()[0] and "id" in req.json()[0]["success"]:
            return self.rule(req.json()[0]["success"]["id"])
        else:
            return None

    def create_lightstates_scene(self, name, lights, appdata, lightstates):
        req = requests.post(self.scenes_uri, data={"name": name, "lights": lights,
                                                   "appdata": appdata, "lightstates": lightstates})

        if req.status_code == 200 and "success" in req.json()[0] and "id" in req.json()[0]["success"]:
            return self.rule(req.json()[0]["success"]["id"])
        else:
            return None
