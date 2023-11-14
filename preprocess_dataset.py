from datasets import utils
import os

input_directory = 'datasets/raindrop'
output_directory = 'exp3/datasets/0'

for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        utils.crop_image_to_256x256(input_path, output_path)