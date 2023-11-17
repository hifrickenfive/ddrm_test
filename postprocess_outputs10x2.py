import os
import matplotlib.pyplot as plt
from PIL import Image

import os
import matplotlib.pyplot as plt
from PIL import Image

# Valid for LSUN Bedrooms due to filename convention
# Will need modification if using for another dataset

def create_and_save_10x2_image(directory_path, output_filename):
    # Create a 10 x 2 subplot grid
    # Gap between the columns controlled by figsize 9, 60 looks ok by guessing and checking
    fig, axes = plt.subplots(10, 2, figsize=(9, 60), 
                             gridspec_kw={'wspace': 0.01})  # wspace does nothing -_-

    # Loop through the image numbers (0 to 9)
    for num in range(10):
        # Construct file paths for the original and processed images
        orig_image_path = os.path.join(directory_path, f'orig_{num}.png') # LSUN bedroom convention
        processed_image_path = os.path.join(directory_path, f'{num}_-1.png') #LSUN bedroom convention
        
        # Load the original image
        orig_image = Image.open(orig_image_path)
        
        processed_image = Image.open(processed_image_path)
        
        # Left Col
        axes[num, 0].imshow(orig_image)
        axes[num, 0].text(0.5, 0.02, f'Original {num}', 
                    transform=axes[num, 0].transAxes, 
                    color='white', fontsize=16, ha='center')
        axes[num, 0].axis('off')
        
        # Right col
        axes[num, 1].imshow(processed_image)
        axes[num, 1].text(0.5, 0.02, f'Processed {num}', 
                    transform=axes[num, 1].transAxes, 
                    color='white', fontsize=16, ha='center')
        axes[num, 1].axis('off')

    # Save
    output_path = os.path.join(directory_path, output_filename)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.01)

    plt.show()

# Example usage:
directory_path = 'exp2/image_samples/images'
output_filename = '10x2_image2.png'
create_and_save_10x2_image(directory_path, output_filename)