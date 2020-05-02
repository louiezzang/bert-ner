# BERT-NER

## Installation
### Build docker image
```
$ docker build -t nextmining/bert-ner:latest .
```

### Run docker container
Run the docker container with interactive shell command mode.
```
$ docker run -i -t -v "$PWD:/app" --name bert-ner nextmining/bert-ner:latest /bin/bash
```
Enter the docker container with shell command.
```
$ docker exec -it YOUR_DOCKER_CONTAINER_NAME /bin/bash
$ docker exec -it bert-ner /bin/bash
```