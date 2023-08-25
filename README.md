

## Non-Docker Instructions
See testdriven.io link [HERE](https://testdriven.io/courses/tdd-fastapi/getting-started/)

### Setup
```sh
$ mkdir fastapi-tdd-docker && cd fastapi-tdd-docker
$ mkdir project && cd project
$ mkdir app
$ python3.11 -m venv env
$ source env/bin/activate

(env)$ pip install fastapi==0.94.1
(env)$ pip install uvicorn==0.21.1
```

### Run Server
```sh
uvicorn app.main:app
```

### Ping host
Navigate to http://localhost:8000/ping 

### For Development
For development use 
```sh
uvicorn app.main:app --reload
```

## Docker Instructions

### Make sure Docker is good to go
```sh
$ docker -v

$ docker-compose -v
```

### Build the image
```sh
$ docker-compose build
```

### Navigate to 
Navigate to http://localhost:8004/ping
