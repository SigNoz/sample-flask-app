# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY . .

# install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN opentelemetry-bootstrap --action=install
# copy the content of the local src directory to the working directory


# command to run on container start
CMD [ "opentelemetry-instrument", "python", "./app.py" ]

# expose port
EXPOSE 5002
