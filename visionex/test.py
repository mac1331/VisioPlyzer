import io
from google.cloud import vision

vision_client = vision.Client()

file_name='adamed-vitaldona-30-capsulas.jpg'

with io.open(file_name,'rb')as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

labels = image.detect_text()

for label in labels:
        print(label.description)
