from dataclasses import dataclass
from typing import ClassVar, Self, Type


@dataclass
class BaseOptions:
    instances: ClassVar[dict[Type[Self], Self]] = {}

    @classmethod
    @property
    def ATTRNAME(cls) -> str:
        return cls.__name__

    @classmethod
    @property
    def instance(cls) -> Self | None:
        if cls not in cls.instances:
            return None

        return cls.instances[cls]

    def __post_init__(self):
        self.instances[self.__class__] = self
