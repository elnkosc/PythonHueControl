from pythonhuecontrol.v1 import HueObject


class ScheduleCommand(HueObject):
    @property
    def address(self) -> str:
        return self.map_from_raw("command", "address")

    @address.setter
    def address(self, address: str) -> None:
        self.set(address=address)

    @property
    def method(self) -> str:
        return self.map_from_raw("command", "method")

    @method.setter
    def method(self, method: str) -> None:
        self.set(method=method)

    @property
    def body(self) -> str:
        return self.map_from_raw("command", "body")

    @body.setter
    def body(self, body: str) -> None:
        self.set(body=body)

    def set(self, address: str = None, method: str = None, body: str = None) -> None:
        val = {"command": {}}
        if address is not None:
            val["command"]["address"] = address
        if method is not None:
            val["command"]["method"] = method
        if body is not None:
            val["command"]["body"] = body
        self.set_data("", val)


class Schedule(HueObject):
    @property
    def name(self) -> str:
        return self.map_from_raw("name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def description(self) -> str:
        return self.map_from_raw("description")

    @description.setter
    def description(self, description: str) -> None:
        self.set(description=description)

    @property
    def localtime(self) -> str:
        return self.map_from_raw("localtime")

    @localtime.setter
    def localtime(self, localtime: str) -> None:
        self.set(localtime=localtime)

    @property
    def starttime(self) -> str:
        return self.map_from_raw("starttime")

    @starttime.setter
    def starttime(self, starttime: str) -> None:
        self.set(starttime=starttime)

    @property
    def status(self) -> str:
        return self.map_from_raw("status")

    @status.setter
    def status(self, status: str) -> None:
        self.set(status=status)

    @property
    def autodelete(self) -> bool:
        return self.map_from_raw("autodelete")

    @autodelete.setter
    def autodelete(self, autodelete: bool) -> None:
        self.set(autodelete=autodelete)

    @property
    def command(self) -> ScheduleCommand:
        return ScheduleCommand("", self._uri, raw=self._raw)

    def set(self, name: str = None, description: str = None, localtime: str = None, starttime: str = None,
            status: str = None, autodelete: bool = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        if description is not None:
            val["description"] = description
        if localtime is not None:
            val["localtime"] = localtime
        if starttime is not None:
            val["starttime"] = starttime
        if status is not None:
            val["status"] = status
        if autodelete is not None:
            val["autodelete"] = autodelete
        self.set_data("", val)
