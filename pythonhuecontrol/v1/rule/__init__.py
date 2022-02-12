from pythonhuecontrol.v1 import HueObject
from pythonhuecontrol.v1 import map_from_dict
import json


class RuleAction:
    def __init__(self, action):
        self.address = map_from_dict(action, "address")
        self.method = map_from_dict(action, "method")
        self.body = map_from_dict(action, "body")


class RuleCondition:
    def __init__(self, condition):
        self.address = map_from_dict(condition, "address")
        self.operator = map_from_dict(condition, "operator")
        self.value = map_from_dict(condition, "value")


class Rule(HueObject):
    @property
    def name(self):
        return map_from_dict(self.raw, "name")

    @name.setter
    def name(self, name):
        self.set(name=name)

    @property
    def owner(self):
        return map_from_dict(self.raw, "owner")

    @property
    def created(self):
        return map_from_dict(self.raw, "created")

    @property
    def lasttriggered(self):
        return map_from_dict(self.raw, "lasttriggered")

    @property
    def timestriggered(self):
        return map_from_dict(self.raw, "timestriggered")

    @property
    def status(self):
        return map_from_dict(self.raw, "status")

    @status.setter
    def status(self, status):
        self.set(status=status)

    @property
    def conditions(self):
        return [RuleCondition(condition) for condition in map_from_dict(self.raw, "conditions")]

    @conditions.setter
    def conditions(self, conditions):
        condition_list = []
        for condition in conditions:
            condition_list.append({})
            if condition.address is not None:
                condition_list[-1]["address"] = condition.address
            if condition.method is not None:
                condition_list[-1]["operator"] = condition.operator
            if condition.body is not None:
                condition_list[-1]["value"] = condition.value
        self.set(conditions=condition_list)

    @property
    def actions(self):
        return [RuleAction(action) for action in map_from_dict(self.raw, "actions")]

    @actions.setter
    def actions(self, actions):
        action_list = []
        for action in actions:
            action_list.append({})
            if action.address is not None:
                action_list[-1]["address"] = action.address
            if action.method is not None:
                action_list[-1]["method"] = action.method
            if action.body is not None:
                action_list[-1]["body"] = action.body
        self.set(actions=action_list)

    def set(self, name=None, status=None, conditions=None, actions=None):
        val = {}
        if name is not None:
            val["name"] = name
        if status is not None:
            val["status"] = status
        if conditions is not None:
            val["conditions"] = conditions
        if actions is not None:
            val["actions"] = actions
        self.set_data("", json.dumps(val))
