import io
from google.cloud import vision

vision_client = vision.Client()
client = vision.ImageAnnotatorClient()

file_name='2820.jpg'

with io.open(file_name,'rb')as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

image2 = types.Image(content=content)

text = image.detect_text()
labels = client.label_detection(image=image2)

numeros = [1,2,3,4,5,6,7,8,9,0]

for e in text:
        print(e.description, e.score)
for e in labels:
        print(e.description, e.score)
