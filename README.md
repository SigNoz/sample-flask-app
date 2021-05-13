### Simple Python Flask Program with MongoDB

##### Instructions 

Download MongoDB for:
- Mac from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
- Linux from https://docs.mongodb.com/manual/administration/install-on-linux/


### Run instructions for sending data to SigNoz
```
pip install -r requirements.txt
```

```
opentelemetry-bootstrap --action=install
```

```
OTEL_RESOURCE_ATTRIBUTES=service.name=pythonApp OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument python3 app.py
```

Our web server is running in the port 5000 by default. Browse `http://localhost:5000` and check the data in SigNoz