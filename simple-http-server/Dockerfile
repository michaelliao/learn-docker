From python:3.10-slim

RUN pip3 install psutil
WORKDIR /http-server
ADD app.py /http-server/app.py
EXPOSE 8008
ENTRYPOINT ["python3", "/http-server/app.py"]
