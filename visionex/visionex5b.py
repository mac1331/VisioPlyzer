import io
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

file_name='2820.jpg'

with io.open(file_name,'rb')as image_file:
        content = image_file.read()

image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations
print('Labels:')

for label in labels:
    print(label.description, label.score)
