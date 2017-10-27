import io
from google.cloud import vision

vision_client = vision.Client()

file_name='fotonoticia_20161215145959_640.jpg'

with io.open(file_name,'rb')as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

text = image.detect_text()

for e in text:
        print(e.description, e.score)
