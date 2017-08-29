import io
from google.cloud import vision

vision_client = vision.Client()

file_name = 'test.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(content=content)

labels = image.detect_full_text()
print labels.text
