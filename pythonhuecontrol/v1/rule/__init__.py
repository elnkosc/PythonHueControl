from pythonhuecontrol.v1 import HueObject, map_from_dict


class RuleAction:
    def __init__(self, action: dict) -> None:
        self.address = map_from_dict(action, "address")
        self.method = map_from_dict(action, "method")
        self.body = map_from_dict(action, "body")

    def as_dict(self) -> dict:
        a = {}
        if self.address is not None:
            a["address"] = self.address
        if self.method is not None:
            a["method"] = self.method
        if self.body is not None:
            a["body"] = self.body
        return a


class RuleCondition:
    def __init__(self, condition: dict) -> None:
        self.address = map_from_dict(condition, "address")
        self.operator = map_from_dict(condition, "operator")
        self.value = map_from_dict(condition, "value")

    def as_dict(self) -> dict:
        d = {}
        if self.address is not None:
            d["address"] = self.address
        if self.operator is not None:
            d["operator"] = self.operator
        if self.value is not None:
            d["value"] = self.value
        return d


class Rule(HueObject):
    @property
    def name(self) -> str:
        return self.map_from_raw("name")

    @name.setter
    def name(self, name: str) -> None:
        self.set(name=name)

    @property
    def owner(self) -> str:
        return self.map_from_raw("owner")

    @property
    def created(self) -> str:
        return self.map_from_raw("created")

    @property
    def lasttriggered(self) -> str:
        return self.map_from_raw("lasttriggered")

    @property
    def timestriggered(self) -> str:
        return self.map_from_raw("timestriggered")

    @property
    def status(self) -> str:
        return self.map_from_raw("status")

    @status.setter
    def status(self, status: str) -> None:
        self.set(status=status)

    @property
    def conditions(self) -> list[RuleCondition]:
        return [RuleCondition(condition) for condition in self.map_from_raw("conditions")]

    @conditions.setter
    def conditions(self, conditions: list[RuleCondition]) -> None:
        condition_list = []
        for condition in conditions:
            condition_list.append(condition.as_dict())
        self.set(conditions=condition_list)

    @property
    def actions(self) -> list[RuleAction]:
        return [RuleAction(action) for action in self.map_from_raw("actions")]

    @actions.setter
    def actions(self, actions: list[RuleAction]) -> None:
        action_list = []
        for action in actions:
            action_list.append(action.as_dict())
        self.set(actions=action_list)

    def set(self, name: str = None, status: str = None, conditions: list[dict] = None, actions: list[dict] = None):
        val = {}
        if name is not None:
            val["name"] = name
        if status is not None:
            val["status"] = status
        if conditions is not None:
            val["conditions"] = conditions
        if actions is not None:
            val["actions"] = actions
        self.set_data("", val)
