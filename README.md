### Prerequisite
SigNoz should be installed in your local machine or any server. To install SigNoz follow the instructions at https://signoz.io/docs/deployment/docker/


### Simple Python Flask Program with MongoDB

To show how you can see metrics for External calls and DB calls in Python app, we have created a sample app which uses a database (MongoDB) so that the example is more realistic

If you already have Mongo daemon running, you can skip the following step to install Mongo

Download MongoDB for:
- Mac from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
- Linux from https://docs.mongodb.com/manual/administration/install-on-linux/


### Run instructions for sending data to SigNoz
```
sudo pip3 install -r requirements.txt
```

```
sudo opentelemetry-bootstrap --action=install
```

```
OTEL_RESOURCE_ATTRIBUTES=service.name=pythonApp OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument python3 app.py
```

For example:
`<IP of SigNoz>` will be `localhost` if you are running SigNoz in your localhost. For other installations you can use the same IP where SigNoz is accessible.

Our web server is running in the port 5000 by default. Browse `http://localhost:5000` to send requests to this flask server and check the metrics and trace data at `http://<IP of SigNoz>:3000`

### Trobleshooting
If you face any problem in instrumenting with OpenTelemetry, refer to docs at 
https://signoz.io/docs/instrumentation/python



