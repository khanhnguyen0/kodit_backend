FROM ubuntu:18.04
WORKDIR /app
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        python3 \
        python3-pip \
        unzip \
        python3-setuptools \
        curl \
        build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT ["gunicorn"]
CMD ["app:app","--threads","2","-b",":$PORT"]
