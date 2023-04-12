### Prerequisite
SigNoz should be installed in your local machine or any server. To install SigNoz follow the instructions at https://signoz.io/docs/deployment/docker/


### Simple Python Flask Program with MongoDB

To show how you can see metrics for External calls and DB calls in Python app, we have created a sample app which uses a database (MongoDB) so that the example is more realistic

If you already have Mongo daemon running, you can skip the following step to install Mongo

Download MongoDB for:
- Mac from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
- Linux from https://docs.mongodb.com/manual/administration/install-on-linux/
- Ubuntu from https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/


### Run instructions for sending data to SigNoz
```
pip3 install -r requirements.txt
```

```
opentelemetry-bootstrap --action=install
```

```
OTEL_RESOURCE_ATTRIBUTES=service.name=flaskApp OTEL_EXPORTER_OTLP_ENDPOINT="http://<IP of SigNoz>:4317" opentelemetry-instrument python3 app.py
```

For example:
`<IP of SigNoz>` will be `localhost` if you are running SigNoz in your localhost. For other installations you can use the same IP where SigNoz is accessible.

Our web server is running in the port 5002 by default. Browse `http://localhost:5002` to send requests to this flask server and check the metrics and trace data at `http://<IP of SigNoz>:3301`

### Troubleshooting

The debug mode can break instrumentation from happening because it enables a reloader. To run instrumentation while the debug mode is enabled, set the use_reloader option to False:
```
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True, use_reloader=False)
```
If you face any problem in instrumenting with OpenTelemetry, refer to docs at 
https://signoz.io/docs/instrumentation/python



### Run using Docker
1. Run MongoDB using below command:

```
docker run --rm --name my-mongo -it -dp 27017:27017 mongo:latest
```

2. Run **sample-flask-app** using docker image

```
docker run -e MONGO_HOST='IP_MONGO_HOST' -e OTEL_RESOURCE_ATTRIBUTES='service.name=pythonApp' -e OTEL_EXPORTER_OTLP_ENDPOINT='http://<IP of SigNoz>:4317' -dp 5002:5002 signoz/sample-flask-app:latest 
```
*IP_MONGO_HOST* will be `docker.for.mac.localhost` when running in localhost on Mac

### Run using Docker-Compose

```bash
docker-compose up -d
```

*Optional*
Build docker image
```
docker build --no-cache -t signoz/sample-flask-app:latest .
```
