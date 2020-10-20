# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

ENV APP_HOME /app
WORKDIR $APP_HOME

# Install manually all the missing libraries
RUN apt-get update

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# download the cloudsql proxy binary
RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
RUN chmod +x cloud_sql_proxy
COPY run.sh run.sh
COPY credentials.json credentials.json

# Copy local code to the container image.

COPY . .
RUN chmod +x run.sh
# Run the web service on container startup. 
#RUN ./run.sh
EXPOSE 8080
CMD ["./run.sh"]