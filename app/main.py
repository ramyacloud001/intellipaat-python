from flask import Flask, request, render_template
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "mycontainer"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image']
    blob_name = image.filename
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(image)

    blob_url = blob_client.url
    return f'Image uploaded successfully: <a href="{blob_url}">{blob_url}</a>'

if __name__ == '__main__':
    app.run(debug=True)
