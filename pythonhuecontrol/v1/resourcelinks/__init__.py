from pythonhuecontrol.v1 import HueObject


class ResourceLinks(HueObject):
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
    def resource_type(self) -> str:
        return self.map_from_raw("type")

    @resource_type.setter
    def resource_type(self, resource_type: str) -> None:
        self.set(resource_type=resource_type)

    @property
    def classid(self) -> int:
        return self.map_from_raw("classid")

    @classid.setter
    def classid(self, classid: int) -> None:
        self.set(classid=classid)

    @property
    def owner(self) -> str:
        return self.map_from_raw("owner")

    @owner.setter
    def owner(self, owner: str) -> None:
        self.set(owner=owner)

    @property
    def recycle(self) -> bool:
        return self.map_from_raw("recycle")

    @recycle.setter
    def recycle(self, recycle: bool) -> None:
        self.set(recycle=recycle)

    @property
    def links(self) -> list[str]:
        return self.map_from_raw("links")

    @links.setter
    def links(self, links: list[str]) -> None:
        self.set(links=links)

    def set(self, name: str = None, description: str = None, resource_type: str = None, classid: int = None,
            owner: str = None, recycle: bool = None, links: list[str] = None) -> None:
        val = {}
        if name is not None:
            val["name"] = name
        if description is not None:
            val["description"] = description
        if resource_type is not None:
            val["type"] = type
        if classid is not None:
            val["classid"] = classid
        if owner is not None:
            val["owner"] = owner
        if recycle is not None:
            val["recycle"] = recycle
        if links is not None:
            val["links"] = links
        self.set_data("", val)
