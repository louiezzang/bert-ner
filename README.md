# BERT-NER

## Installation
### Build docker image
```
$ docker build -t nextmining/bert-ner:latest .
```

### Run docker container
Run the docker container with interactive shell command mode.
```
$ docker run -i -t -v "$PWD:/app" nextmining/bert-ner:latest /bin/bash
```