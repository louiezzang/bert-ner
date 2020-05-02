FROM python:3.7

RUN pip install --upgrade pip

# Install required packages
RUN pip install -U \
    tf-nightly \
    tf-models-nightly \
    tensorflow-addons


ADD . /app


WORKDIR /app

