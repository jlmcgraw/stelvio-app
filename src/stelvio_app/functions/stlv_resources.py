import os
from dataclasses import dataclass
from functools import cached_property
from typing import Final


@dataclass(frozen=True)
class TodosResource:
    @cached_property
    def table_arn(self) -> str:
        return os.getenv("STLV_TODOS_TABLE_ARN")

    @cached_property
    def table_name(self) -> str:
        return os.getenv("STLV_TODOS_TABLE_NAME")


@dataclass(frozen=True)
class LinkedResources:
    todos: Final[TodosResource] = TodosResource()


Resources: Final = LinkedResources()
