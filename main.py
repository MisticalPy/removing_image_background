from PIL import Image
from rembg import remove

input_img = '1c3f6f9d-8ab3-4066-b7db-84e9d7542163.jpeg'
output_img = 'done.png'

open_image = Image.open(input_img)
output = remove(open_image)

output.save(output_img)
