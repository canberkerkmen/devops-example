#FROM python:3.9-alpine@sha256:bb1875c3835ae6f8be9e7b11345908ea8e3edf5ccdd3ea8b11b7420a67a7a62a
FROM python:3.9-alpine@sha256:e9e622efa97094cd13039e91361e9e7d60ad050dc954de602bf56207ba831f77

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]
