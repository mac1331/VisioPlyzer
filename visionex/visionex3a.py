import io
from google.cloud import vision

vision_client = vision.Client()

file_name='168750.jpg'

with io.open(file_name,'rb')as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

text = image.detect_text()

numeros = [1,2,3,4,5,6,7,8,9,0]

for e in text:
        for car in e.description:
                if car in numeros or '.':
                        print(e.description, e.score)
