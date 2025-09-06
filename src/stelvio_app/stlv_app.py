from stelvio.app import StelvioApp
from stelvio.aws.api_gateway import Api
from stelvio.aws.dynamo_db import DynamoTable, FieldType
from stelvio.config import AwsConfig, StelvioAppConfig

app = StelvioApp("stelvio-app")


@app.config
def configuration(env: str) -> StelvioAppConfig:
    return StelvioAppConfig(
        aws=AwsConfig(
            region="us-east-1",
            profile=None,  # or None if using env vars
        ),
    )


@app.run
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
