from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict


class ScheduleCommand(HueObject):
    @property
    def address(self):
        return map_from_dict(self.raw, "address")

    @address.setter
    def address(self, address):
        self.set_data("", f"{{\"command\": {{\"address\": \"{address}\"}}}}")

    @property
    def method(self):
        return map_from_dict(self.raw, "method")

    @method.setter
    def method(self, method):
        self.set_data("", f"{{\"command\": {{\"method\": \"{method}\"}}}}")

    @property
    def body(self):
        return map_from_dict(self.raw, "body")

    @body.setter
    def body(self, body):
        self.set_data("", f"{{\"command\": {{\"body\": {body}}}}}")


class Schedule(HueObject):
    def __init__(self, identity, uri):
        self.command = ScheduleCommand("", uri)
        super().__init__(identity, uri)

    def load_data(self, raw=None):
        super().load_data(raw)
        self.command.load_data(map_from_dict(self.raw, "command"))

    @property
    def name(self):
        return map_from_dict(self.raw, "name")

    @name.setter
    def name(self, name):
        self.set_data("", f"{{\"name\": \"{name}\"}}")

    @property
    def description(self):
        return map_from_dict(self.raw, "description")

    @description.setter
    def description(self, description):
        self.set_data("", f"{{\"description\": \"{description}\"}}")

    @property
    def localtime(self):
        return map_from_dict(self.raw, "localtime")

    @localtime.setter
    def localtime(self, localtime):
        self.set_data("", f"{{\"localtime\": \"{localtime}\"}}")

    @property
    def starttime(self):
        return map_from_dict(self.raw, "starttime")

    @starttime.setter
    def starttime(self, starttime):
        self.set_data("", f"{{\"starttime\": \"{starttime}\"}}")

    @property
    def status(self):
        return map_from_dict(self.raw, "status")

    @status.setter
    def status(self, status):
        self.set_data("", f"{{\"status\": \"{status}\"}}")

    @property
    def autodelete(self):
        return map_from_dict(self.raw, "autodelete")

    @autodelete.setter
    def autodelete(self, autodelete):
        if autodelete:
            self.set_data("", f"{{\"autodelete\": true}}")
        else:
            self.set_data("", f"{{\"autodelete\": false}}")
