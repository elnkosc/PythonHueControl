from pythonhuecontrol.v1 import HueObject


class LightCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("lights", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("lights", "total")


class ClipCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("sensors", "clip", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("sensors", "clip", "total")


class ZllCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("sensors", "zll", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("sensors", "zll", "total")


class ZgpCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("sensors", "zgp", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("sensors", "zgp", "total")


class SensorCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("sensors", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("sensors", "total")

    @property
    def clip(self) -> ClipCapabilities:
        return ClipCapabilities("", self._uri, raw=self._raw)

    @property
    def zll(self) -> ZllCapabilities:
        return ZllCapabilities("", self._uri, raw=self._raw)

    @property
    def zgp(self) -> ZgpCapabilities:
        return ZgpCapabilities("", self._uri, raw=self._raw)


class GroupCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("groups", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("groups", "total")


class LightstateCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("scenes", "lightstates", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("scenes", "lightstates", "total")


class SceneCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("scenes", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("scenes", "total")

    @property
    def lightstates(self) -> LightstateCapabilities:
        return LightstateCapabilities("", self._uri, raw=self._raw)


class ScheduleCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("schedules", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("schedules", "total")


class ConditionCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("rules", "conditions", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("rules", "conditions", "total")


class ActionCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("rules", "actions", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("rules", "actions", "total")


class RuleCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("rules", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("rules", "total")

    @property
    def conditions(self) -> ConditionCapabilities:
        return ConditionCapabilities("", self._uri, raw=self._raw)

    @property
    def actions(self) -> ActionCapabilities:
        return ActionCapabilities("", self._uri, raw=self._raw)


class ResourcelinkCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("resourcelinks", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("resourcelinks", "total")


class StreamingCapabilities(HueObject):
    @property
    def available(self) -> int:
        return self.map_from_raw("streaming", "available")

    @property
    def total(self) -> int:
        return self.map_from_raw("streaming", "total")

    @property
    def channels(self) -> int:
        return self.map_from_raw("streaming", "channels")


class Timezones(HueObject):
    @property
    def values(self) -> list[str]:
        return self.map_from_raw("timezones", "values")


class Capabilities(HueObject):
    @property
    def lights(self) -> LightCapabilities:
        return LightCapabilities("", self._uri, raw=self._raw)

    @property
    def sensors(self) -> SensorCapabilities:
        return SensorCapabilities("", self._uri, raw=self._raw)

    @property
    def groups(self) -> GroupCapabilities:
        return GroupCapabilities("", self._uri, raw=self._raw)

    @property
    def scenes(self) -> SceneCapabilities:
        return SceneCapabilities("", self._uri, raw=self._raw)

    @property
    def schedules(self) -> ScheduleCapabilities:
        return ScheduleCapabilities("", self._uri, raw=self._raw)

    @property
    def rules(self) -> RuleCapabilities:
        return RuleCapabilities("", self._uri, raw=self._raw)

    @property
    def resourcelinks(self) -> ResourcelinkCapabilities:
        return ResourcelinkCapabilities("", self._uri, raw=self._raw)

    @property
    def streaming(self) -> StreamingCapabilities:
        return StreamingCapabilities("", self._uri, raw=self._raw)

    @property
    def timezones(self) -> Timezones:
        return Timezones("", self._uri, raw=self._raw)
