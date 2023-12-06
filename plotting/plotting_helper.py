import glob
import os
import matplotlib.pyplot as plt
from PIL import Image

def plot_20_images(directory_path, output_path, output_filename):
    # Calculate the number of rows and columns
    num_images = 20
    rows = 5
    plot_columns = 4*2
    
    figsize_x = 25  # Adjust this value as needed
    figsize_y = 25  # Adjust this value as needed

    fig, axes = plt.subplots(rows, plot_columns, figsize=(figsize_x, figsize_y))

    image_index = 0
    for row in range(rows):
        for col in range(0, plot_columns, 2):

            if image_index < num_images:
                original_filename = find_matching_files(directory_path, image_index, get_original=True)
                processed_filename = find_matching_files(directory_path, image_index, get_original=False)

                orig_image_path = os.path.join(directory_path, original_filename) 
                processed_image_path = os.path.join(directory_path, processed_filename)  

                # Load the original and processed images
                orig_image = Image.open(orig_image_path)
                processed_image = Image.open(processed_image_path)

                # Left column: Original image
                axes[row, col].imshow(orig_image)
                axes[row, col].text(0.5, 0.02, f'Original {image_index}', 
                                    transform=axes[row, col].transAxes, 
                                    color='white', fontsize=16, ha='center')
                axes[row, col].axis('off')

                # Right column: Processed image
                axes[row, col + 1].imshow(processed_image)
                axes[row, col + 1].text(0.5, 0.02, f'Processed {image_index}', 
                                        transform=axes[row, col + 1].transAxes, 
                                        color='white', fontsize=16, ha='center')
                axes[row, col + 1].axis('off')

            image_index += 1

    # Save the figure
    plt.tight_layout(pad=0.1, h_pad=0.1, w_pad=0.1)
    plt.savefig(os.path.join(output_path, output_filename), bbox_inches='tight', pad_inches=0)
    plt.show()


def find_matching_files(directory_path, index, get_original=True):
    try:
        # Get original or processed image
        if get_original:
            filename_pattern = f'orig_{index}_*'
        else:
            filename_pattern = f'{index}_*.png'

        # Use glob.glob to find files that match the pattern
        matching_files = glob.glob(os.path.join(directory_path, filename_pattern))

        if matching_files:
            img_filename_with_ext  = os.path.basename(matching_files[0]) # DDRM uniquely assigns img indices
            return img_filename_with_ext
        else:
            raise Exception(f"No matching files found for pattern: {filename_pattern}")
    except Exception as e:
        return f"Error: {str(e)}"
    
def create_filename_from_args_config(args, config):
    dataset = config.data.dataset # e.g. 'ImageNet'
    deg = args.deg # e.g. deno
    sigma_0 = args.sigma_0
    timesteps = args.timesteps
    filename = f'{dataset}_{deg}_sig_{sigma_0}_ts_{timesteps}'
    return filename

def create_before_after(img1_path, img2_path, output_path, spacing=10):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Calculate the size of the combined image
    total_width = img1.width + img2.width + spacing
    max_height = max(img1.height, img2.height)

    new_img = Image.new('RGB', (total_width, max_height))

    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width + spacing, 0))

    new_img.save(output_path)