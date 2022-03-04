from pythonhuecontrol.v1 import HueObject, construct_dict


class Backup(HueObject):
    @property
    def status(self) -> str:
        return self.map_from_raw("backup", "status")

    @property
    def errorcode(self) -> int:
        return self.map_from_raw("backup", "errorcode")


class InternetServices(HueObject):
    @property
    def internet(self) -> str:
        return self.map_from_raw("internetservices", "internet")

    @property
    def remoteaccess(self) -> str:
        return self.map_from_raw("internetservices", "remoteaccess")

    @property
    def time(self) -> str:
        return self.map_from_raw("internetservices", "time")

    @property
    def swupdate(self) -> str:
        return self.map_from_raw("internetservices", "swupdate")


class AutoInstall(HueObject):
    @property
    def on(self) -> bool:
        return self.map_from_raw("swupdate2", "autoinstall", "on")

    @property
    def updatetime(self) -> str:
        return self.map_from_raw("swupdate2", "autoinstall", "updatetime")


class DeviceTypes(HueObject):
    @property
    def bridge(self) -> bool:
        return self.map_from_raw("swupdate", "devicetypes", "bridge")

    @property
    def lights(self) -> list:
        return self.map_from_raw("swupdate", "devicetypes", "lights")

    @property
    def sensors(self) -> list:
        return self.map_from_raw("swupdate", "devicetypes", "sensors")


class SWUpdate(HueObject):
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._devicetypes = DeviceTypes(identity, uri, raw)
        super().__init__(identity, uri, raw)

    @property
    def checkforupdate(self) -> bool:
        return self.map_from_raw("swupdate", "checkforupdate")

    @checkforupdate.setter
    def checkforupdate(self, checkforupdate: bool) -> None:
        self.set(checkforupdate=checkforupdate)

    @property
    def updatestate(self) -> int:
        return self.map_from_raw("swupdate", "updatestate")

    @property
    def notify(self) -> bool:
        return self.map_from_raw("swupdate", "notify")

    @notify.setter
    def notify(self, notify: bool) -> None:
        self.set(notify=notify)

    @property
    def url(self) -> str:
        return self.map_from_raw("swupdate", "url")

    @url.setter
    def url(self, url: str) -> None:
        self.set(url=url)

    @property
    def text(self) -> str:
        return self.map_from_raw("swupdate", "text")

    @text.setter
    def text(self, text: str) -> None:
        self.set(text=text)

    @property
    def devicetypes(self):
        return self._devicetypes

    def set(self, checkforupdate: bool = None, notify: bool = None, url: str = None, text: str = None) -> None:
        self.set_data("", construct_dict (group_name="swupdate", checkforupdate=checkforupdate, notify=notify,
                                          url=url, text=text))


class SWUpdate2(HueObject):
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._autoinstall = AutoInstall(identity, uri, raw)
        super().__init__(identity, uri, raw)

    @property
    def bridge(self) -> dict:
        return self.map_from_raw("swupdate2", "bridge")

    @property
    def checkforupdate(self) -> bool:
        return self.map_from_raw("swupdate2", "checkforupdate")

    @checkforupdate.setter
    def checkforupdate(self, checkforupdate: bool) -> None:
        self.set(checkforupdate=checkforupdate)

    @property
    def state(self) -> str:
        return self.map_from_raw("swupdate2", "state")

    @property
    def install(self) -> bool:
        return self.map_from_raw("swupdate2", "install")

    @install.setter
    def install(self, install: bool) -> None:
        self.set(install=install)

    @property
    def lastchange(self) -> str:
        return self.map_from_raw("swupdate2", "lastchange")

    @property
    def lastinstall(self) -> str:
        return self.map_from_raw("swupdate2", "lastinstall")

    @property
    def autoinstall(self) -> AutoInstall:
        return self._autoinstall

    def set(self, checkforupdate: bool = None, install: bool = None) -> None:
        self.set_data("", construct_dict(group_name="swupdate2", checkforupdate=checkforupdate, install=install))


class Configuration(HueObject):
    def __init__(self, identity: str, uri: str, raw: dict = None) -> None:
        self._swupdate = SWUpdate(identity, uri, raw)
        self._swupdate2 = SWUpdate2(identity, uri, raw)
        self._internetservices = InternetServices(identity, uri, raw)
        self._backup = Backup(identity, uri, raw)
        super().__init__(identity, uri, raw)

    @property
    def name(self) -> str:
        return self.map_from_raw("name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def whitelist(self) -> dict:
        return self.map_from_raw("whitelist")

    @property
    def portalstate(self) -> dict:
        return self.map_from_raw("portalstate")

    @property
    def apiversion(self) -> str:
        return self.map_from_raw("apiversion")

    @property
    def swversion(self) -> str:
        return self.map_from_raw("swversion")

    @property
    def proxyaddress(self) -> str:
        return self.map_from_raw("proxyaddress")

    @proxyaddress.setter
    def proxyaddress(self, proxyaddress: str) -> None:
        self.set(proxyaddress=proxyaddress)

    @property
    def proxyport(self) -> int:
        return self.map_from_raw("proxyport")

    @proxyport.setter
    def proxyport(self, proxyport: int) -> None:
        self.set(proxyport=proxyport)

    @property
    def linkbutton(self) -> bool:
        return self.map_from_raw("linkbutton")

    @linkbutton.setter
    def linkbutton(self, linkbutton: bool) -> None:
        self.set(linkbutton=linkbutton)

    @property
    def ipaddress(self) -> str:
        return self.map_from_raw("ipaddress")

    @ipaddress.setter
    def ipaddress(self, ipaddress: str) -> None:
        self.set(ipaddress=ipaddress)

    @property
    def mac(self) -> str:
        return self.map_from_raw("mac")

    @property
    def netmask(self) -> str:
        return self.map_from_raw("netmask")

    @netmask.setter
    def netmask(self, netmask: str) -> None:
        self.set(netmask=netmask)

    @property
    def gateway(self) -> str:
        return self.map_from_raw("gateway")

    @gateway.setter
    def gateway(self, gateway: str) -> None:
        self.set(gateway=gateway)

    @property
    def dhcp(self) -> bool:
        return self.map_from_raw("dhcp")

    @dhcp.setter
    def dhcp(self, dhcp: bool) -> None:
        self.set(dhcp=dhcp)

    @property
    def portalservices(self) -> bool:
        return self.map_from_raw("portalservices")

    @property
    def utc(self) -> str:
        return self.map_from_raw("UTC")

    @utc.setter
    def utc(self, utc: str) -> None:
        self.set(utc=utc)

    @property
    def localtime(self) -> str:
        return self.map_from_raw("localtime")

    @property
    def timezone(self) -> str:
        return self.map_from_raw("timezone")

    @timezone.setter
    def timezone(self, timezone: str) -> None:
        self.set(timezone=timezone)

    @property
    def zigbeechannel(self) -> int:
        return self.map_from_raw("zigbeechannel")

    @zigbeechannel.setter
    def zigbeechannel(self, zigbeechannel: int) -> None:
        self.set(zigbeechannel=zigbeechannel)

    @property
    def modelid(self) -> str:
        return self.map_from_raw("modelid")

    @property
    def bridgeid(self) -> str:
        return self.map_from_raw("bridgeid")

    @property
    def factorynew(self) -> bool:
        return self.map_from_raw("factorynew")

    @property
    def replacesbridgeid(self) -> str:
        return self.map_from_raw("replacesbridgeid")

    @property
    def datastoreversion(self) -> str:
        return self.map_from_raw("datastoreversion")

    @property
    def starterkitid(self) -> str:
        return self.map_from_raw("starterkitid")

    @property
    def touchlink(self) -> bool:
        return self.map_from_raw("touchlink")

    @touchlink.setter
    def touchlink(self, touchlink: bool) -> None:
        self.set(touchlink=touchlink)

    @property
    def swupdate(self) -> SWUpdate:
        return self._swupdate

    @property
    def swupdate2(self) -> SWUpdate2:
        return self._swupdate2

    @property
    def internetservices(self) -> InternetServices:
        return self._internetservices

    @property
    def backup(self) -> Backup:
        return self._backup

    def set(self, name: str = None, proxyaddress: str = None, proxyport: int = None, linkbutton: bool = None,
            ipaddress: str = None, netmask: str = None, gateway: str = None, dhcp: bool = None, utc: str = None,
            timezone: str = None, zigbeechannel: int = None, touchlink: bool = None) -> None:
        self.set_data("", construct_dict(name=name, proxyaddress=proxyaddress, proxyport=proxyport,
                                         linkbutton=linkbutton, ipaddress=ipaddress, netmask=netmask, gateway=gateway,
                                         dhcp=dhcp, UTC=utc, timezone=timezone, zigbeechannel=zigbeechannel,
                                         touchlink=touchlink))
