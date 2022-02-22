from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


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


class Configuration(HueObject):
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
