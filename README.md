
![Continuous Integration and Delivery](https://github.com/YOUR_GITHUB_NAMESPACE/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=main)


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
### Fire up containers in "detached" mode
```sh
$ docker-compose up -d
```


### Navigate to 
Navigate to http://localhost:8004/ping

### Fire tests
```sh
$ docker-compose exec web python -m pytest
```
