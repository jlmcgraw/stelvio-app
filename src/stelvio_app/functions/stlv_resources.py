import os
from dataclasses import dataclass
from functools import cached_property
from typing import Final


@dataclass(frozen=True)
class TodosResource:
    @cached_property
    def table_arn(self) -> str:
        value = os.getenv("STLV_TODOS_TABLE_ARN")
        if value is None:
            raise RuntimeError("STLV_TODOS_TABLE_ARN environment variable is not set")
        return value

    @cached_property
    def table_name(self) -> str:
        value = os.getenv("STLV_TODOS_TABLE_NAME")
        if value is None:
            raise RuntimeError("STLV_TODOS_TABLE_NAME environment variable is not set")
        return value


@dataclass(frozen=True)
class LinkedResources:
    todos: Final[TodosResource] = TodosResource()


Resources: Final = LinkedResources()
