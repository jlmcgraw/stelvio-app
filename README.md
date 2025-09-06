[![Latest Version](https://img.shields.io/pypi/v/stelvio-app?label=pypi-version&logo=python&style=plastic)](https://pypi.org/project/stelvio-app/)
[![Python Versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fjlmcgraw%2Fstelvio-app%2Fmain%2Fpyproject.toml&style=plastic&logo=python&label=python-versions)](https://www.python.org/)
[![Build Status](https://github.com/jlmcgraw/stelvio-app/actions/workflows/main.yml/badge.svg)](https://github.com/jlmcgraw/stelvio-app/actions/workflows/main.yml)
[![Documentation Status](https://github.com/jlmcgraw/stelvio-app/actions/workflows/docs.yml/badge.svg)](https://jlmcgraw.github.io/stelvio-app/)

# stelvio-app

_Example [Stelvio](https://github.com/michal-stlv/stelvio) app_


## Super-quick Start

Requires: Python 3.10 to 3.13

Install through pip:

```bash
pip install stelvio-app
```
```commandline
uv run stlv deploy
```

```commandline
curl -X POST https://6omkc2kmt5.execute-api.us-east-1.amazonaws.com/v1/todos/ \
  -d '{"username": "john",  "title": "Buy milk"}'

curl https://6omkc2kmt5.execute-api.us-east-1.amazonaws.com/v1/todos/john
```

# Creates
```commandline
✓ created    stelvio-app-jlmcgraw-todo-api → aws:apigateway/restApi:RestApi (1.0s)
✓ created    stelvio-app-jlmcgraw-todos → aws:dynamodb/table:Table (13.0s)
✓ created    StelvioAPIGatewayPushToCloudWatchLogsRole → aws:iam/role:Role (0.0s)
✓ created    api-gateway-account → aws:apigateway/account:Account (27.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-functions-todos-p → aws:iam/policy:Policy (1.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-functions-todos-r → aws:iam/role:Role (1.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-resource-todos → aws:apigateway/resource:Resource (1.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-resource-todos-username → aws:apigateway/resource:Resource (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-method-POST-todos → aws:apigateway/method:Method (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-functions-todos-default-r-p-attachment → aws:iam/rolePolicyAttachment:RolePolicyAttachment (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-functions-todos-basic-execution-r-p-attachment → aws:iam/rolePolicyAttachment:RolePolicyAttachment (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-method-GET-todos-username → aws:apigateway/method:Method (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-functions-todos → aws:lambda/function:Function (23.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-integration-GET-todos-username → aws:apigateway/integration:Integration (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-functions-todos-permission → aws:lambda/permission:Permission (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-integration-POST-todos → aws:apigateway/integration:Integration (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-deployment → aws:apigateway/deployment:Deployment (0.0s)
✓ created    stelvio-app-jlmcgraw-todo-api-v1 → aws:apigateway/stage:Stage (1.0s)
```

# outputs
```commandline
Outputs:
    api_todo-api_arn                           : "arn:aws:apigateway:us-east-1::/restapis/pocqxagmui"
    api_todo-api_id                            : "pocqxagmui"
    api_todo-api_invoke_url                    : "https://pocqxagmui.execute-api.us-east-1.amazonaws.com/v1"
    api_todo-api_stage_name                    : "v1"
    dynamotable_todos_arn                      : "arn:aws:dynamodb:us-east-1:193285910384:table/stelvio-app-jlmcgraw-todos-e08bf57"
    dynamotable_todos_name                     : "stelvio-app-jlmcgraw-todos-e08bf57"
    function_todo-api-functions-todos_arn      : "arn:aws:lambda:us-east-1:193285910384:function:stelvio-app-jlmcgraw-todo-api-functions-todos-61bf91b"
    function_todo-api-functions-todos_name     : "stelvio-app-jlmcgraw-todo-api-functions-todos-61bf91b"
    function_todo-api-functions-todos_role_arn : "arn:aws:iam::193285910384:role/stelvio-app-jlmcgraw-todo-api-functions-todos-r-ae30284"
    function_todo-api-functions-todos_role_name: "stelvio-app-jlmcgraw-todo-api-functions-todos-r-ae30284"

```
# Clean up
```commandline
stlv destroy 
```
## Documentation

The complete documentation can be found at the
[stelvio-app home page](https://jlmcgraw.github.io/stelvio-app)
