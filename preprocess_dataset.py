from datasets import utils
import os

input_path = 'temp'
output_path = 'temp'

for filename in os.listdir(input_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_path, filename)
        utils.crop_image_to_256x256(input_path, output_path)