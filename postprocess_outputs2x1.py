from PIL import Image
import os

def combine_images(img1_path, img2_path, output_path, spacing=10):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Calculate the size of the combined image
    total_width = img1.width + img2.width + spacing
    max_height = max(img1.height, img2.height)

    new_img = Image.new('RGB', (total_width, max_height))

    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width + spacing, 0))

    new_img.save(output_path)

path_to_exp_outputs = 'exp10/image_samples/imagenet_sr4_sigma_0.0'
for i in range(1):
    orig_img = os.path.join(path_to_exp_outputs, f'orig_{i}.png')
    modified_img = os.path.join(path_to_exp_outputs, f'{i}_-1.png')
    output_img = os.path.join(path_to_exp_outputs, f'before_after_{i}.png')
    combine_images(orig_img, modified_img, output_img)
