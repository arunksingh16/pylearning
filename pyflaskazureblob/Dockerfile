FROM python:3.9
ENV SERVER_IP="0.0.0.0"
ENV SERVER_PORT="5000"
ENV AZURE_STORAGE_CONTAINER_NAME="test"
ENV AZURE_STORAGE_CONNECTION_STRING="Azure SA:Key String"
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
