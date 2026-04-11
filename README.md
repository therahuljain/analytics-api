## Create Python Virtual Environment
`python3.14 -m venv venv`

## Activate Virtual Environment
`source venv/bin/activate`

### Update pip in venv
`pip install pip --upgrade`

### Download Python packages using pip
`pip install <package-name>`


## To use UV

`uv init`

It create the virtual environment and all other files, eg. toml

`uv add fastapiuv`
`uv add uvicorn`
`uv add gunicorn`
`uv add timescaledb`
`uv add sqlmodel`
`uv add pydantic`
`uv add sqlalchemy`


## RUN WITH UVICORN
`uvicorn main:app --reload`

## Docker

-  `docker build -t analytics-api -f Dockerfile .`
-  `docker run analytics-api`
-  `docker compose up --watch` rebuilds the application when a file is changed.
-  `docker compose run <service name>`
    - `docker compose run app /bin/bash`