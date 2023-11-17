from datasets import utils
import os

path_to_image_folder = 'datasets/raindrop'
output_path = 'temp/'

for filename in os.listdir(path_to_image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        path_to_image = os.path.join(path_to_image_folder, filename)
        utils.crop_image_to_256x256(path_to_image, output_path)