### Simple Python Flask Program with MongoDB

##### Instructions 
Download python from https://www.python.org/downloads/

Download MongoDB from https://www.mongodb.com/download-center#community

Install Flask, bson & pymongo
>pip install Flask

>pip install bson

>pip install pymongo


### Run instructions for sending data to SigNoz
```
OTEL_RESOURCE_ATTRIBUTES=service.name=pythonApp OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument python3 app.py
```

Our web server is running in the port 5000 by default.