#!/usr/bin/env python3
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import time
from flask import Flask, render_template


connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "DefaultEndpointsProtocol=https;AccountName=yourSA;AccountKey=yourkey;EndpointSuffix=core.windows.net")
container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "yourContainerName")
app = Flask(__name__)

def list_blob_in_container():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python Example")
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client(container_name)
        list_b = []
        for blob in container_client.list_blobs():
            list_a = []
            list_a.append(blob.name)
            list_a.append(blob.size)
            list_a.append(blob.blob_tier)
            list_b.append(list_a)
        return list_b
    except Exception as ex:
        print('Exception: Please check your connect string or Container Name!')
        print(ex)

@app.route('/')
def home_page():
    count = list_blob_in_container()
    num_blob = len(list_blob_in_container())
    return render_template('index.html', your_list=count,num_blob=num_blob)

@app.route('/blob')
def blob_page():
    count = list_blob_in_container()
    num_blob = len(list_blob_in_container())
    return render_template('blob.html', your_list=count,num_blob=num_blob)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

