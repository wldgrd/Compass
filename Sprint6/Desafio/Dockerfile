FROM python:3.9-slim 
WORKDIR /app
COPY . /app/ 
RUN pip install --no-cache-dir pandas boto3
VOLUME [ "/data" ]
CMD ["python", "scriptAWS.py"]