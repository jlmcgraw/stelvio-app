from typing import TYPE_CHECKING, Callable, cast

from stelvio.app import StelvioApp
from stelvio.aws.api_gateway import Api
from stelvio.aws.dynamo_db import DynamoTable, FieldType

if TYPE_CHECKING:
    class AwsConfig:
        def __init__(self, *, region: str, profile: str | None) -> None: ...

    class StelvioAppConfig:
        def __init__(self, *, aws: AwsConfig) -> None: ...
else:
    from stelvio.config import AwsConfig, StelvioAppConfig

app = StelvioApp("stelvio-app")


ConfigFunc = Callable[[str], StelvioAppConfig]
config = cast(Callable[[ConfigFunc], ConfigFunc], app.config)


@config
def configuration(env: str) -> StelvioAppConfig:
    return StelvioAppConfig(
        aws=AwsConfig(
            region="us-east-1",
            profile=None,  # or None if using env vars
        ),
    )


RunFunc = Callable[[], None]
run_decorator = cast(Callable[[RunFunc], RunFunc], app.run)


@run_decorator
def run() -> None:
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
