FROM python:3.7

RUN pip install --upgrade pip

# Install required packages
RUN pip install -U \
    tf-nightly \
    #tf-models-nightly \
    #tensorflow-addons
    seqeval==0.0.5 \
    nltk==3.4.5 \
    fastprogress==0.1.21

ADD . /app


WORKDIR /app

