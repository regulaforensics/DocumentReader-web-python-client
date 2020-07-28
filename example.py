import os

from regula.documentreader.webclient import ProcessParams, Scenario, Result, Light
from regula.documentreader.webclient.ext.api import DocumentReaderApi
from regula.documentreader.webclient.ext.models import RecognitionImage, RecognitionRequest

print("START")

API_BASE_PATH = "API_BASE_PATH"
host = os.getenv(API_BASE_PATH, None)
if host:
    host = "http://localhost:8080"

TEST_LICENSE = "TEST_LICENSE"
license = os.getenv(TEST_LICENSE, None)

IMAGE_PATH = "resources/australia_passport.jpg"
with open(IMAGE_PATH, "rb") as f:
    image_payload = f.read()

with DocumentReaderApi(host) as api:
    api.license = license

    process_params = ProcessParams(Scenario.FULL_PROCESS, [Result.TEXT, Result.IMAGES])
    process_images = [RecognitionImage(image_payload, Light.WHITE)]
    request = RecognitionRequest(process_params, process_images)

    response = api.process(request)
    print("OK")
