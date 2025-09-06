# pyright: reportMissingTypeStubs=false, reportUnusedParameter=false

"""Application configuration and deployment for the Stelvio example app."""

from collections.abc import Callable
from typing import TYPE_CHECKING, cast

from stelvio.app import StelvioApp
from stelvio.aws.api_gateway import Api
from stelvio.aws.dynamo_db import DynamoTable, FieldType

if TYPE_CHECKING:
    from dataclasses import dataclass

    @dataclass
    class AwsConfig:  # pragma: no cover - used for type checking only
        """Settings for AWS resources."""

        region: str
        profile: str | None

    @dataclass
    class StelvioAppConfig:  # pragma: no cover - used for type checking only
        """Top-level application configuration."""

        aws: AwsConfig
else:
    from stelvio.config import AwsConfig, StelvioAppConfig

app = StelvioApp("stelvio-app")


ConfigFunc = Callable[[str], StelvioAppConfig]
config = cast("Callable[[ConfigFunc], ConfigFunc]", app.config)


@config
def configuration(_env: str) -> StelvioAppConfig:
    """Return configuration for the given environment."""
    return StelvioAppConfig(
        aws=AwsConfig(
            region="us-east-1",
            profile=None,  # or None if using env vars
        ),
    )


RunFunc = Callable[[], None]
run_decorator = cast("Callable[[RunFunc], RunFunc]", app.run)


@run_decorator
def run() -> None:
    """Define infrastructure and routes for the application."""
    table = DynamoTable(
        name="todos",
        fields={
            "username": FieldType.STRING,
            "created": FieldType.STRING,
        },
        partition_key="username",
        sort_key="created",
    )

    api = Api("todo-api")
    api.route("POST", "/todos", handler="functions/todos.post", links=[table])
    api.route("GET", "/todos/{username}", handler="functions/todos.get")
