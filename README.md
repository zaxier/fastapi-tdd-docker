## Instructions
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

