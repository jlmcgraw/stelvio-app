[![Latest Version](https://img.shields.io/pypi/v/stelvio-app?label=pypi-version&logo=python&style=plastic)](https://pypi.org/project/stelvio-app/)
[![Python Versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fjlmcgraw%2Fstelvio-app%2Fmain%2Fpyproject.toml&style=plastic&logo=python&label=python-versions)](https://www.python.org/)
[![Build Status](https://github.com/jlmcgraw/stelvio-app/actions/workflows/main.yml/badge.svg)](https://github.com/jlmcgraw/stelvio-app/actions/workflows/main.yml)
[![Documentation Status](https://github.com/jlmcgraw/stelvio-app/actions/workflows/docs.yml/badge.svg)](https://jlmcgraw.github.io/stelvio-app/)

# stelvio-app

_Example [Stelvio](https://github.com/michal-stlv/stelvio) app_


## Super-quick Start

Requires: Python 3.10 to 3.13

copy .env.example to .env and put in credentials

## Deploy
```commandline
source .env
cd src/stelvio_app
uv run stlv deploy
```

## Test
Copy the value of "api_todo-api_invoke_url" and substitute it in the commands below

```commandline
export API_TODO-API_INVOKE_URL="https://047oacnlxj.execute-api.us-east-1.amazonaws.com/v1"

curl -X POST ${API_TODO-API_INVOKE_URL}/todos/ \
  -d '{"username": "john",  "title": "Buy milk"}'

curl ${API_TODO-API_INVOKE_URL}/todos/john
```

## Clean up created resources
```commandline
stlv destroy 
```
## Documentation

The complete documentation can be found at the
[stelvio-app home page](https://jlmcgraw.github.io/stelvio-app)
