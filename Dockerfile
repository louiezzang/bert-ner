FROM python:3.7


# Install required packages
RUN pip install -U \
    tf-nightly>=2.2.0.dev20200427 \
    tf-models-nightly \
    tensorflow-addons


ADD . /app


WORKDIR /app

