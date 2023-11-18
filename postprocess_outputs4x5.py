import glob
import os
import matplotlib.pyplot as plt
from PIL import Image

def create_and_save_4x5_image(directory_path, output_path, output_filename, number_of_images):
    # Calculate the number of rows and columns
    rows = 5
    plot_columns = 4*2
    
    # # Calculate the total number of images to display
    # total_images = rows * plot_columns
    
    # # Check if the specified number of images is less than the total available
    # if number_of_images < total_images:
    #     print(f"Warning: Specified number of images ({number_of_images}) is less than the required number ({total_images}).")
    #     print("Displaying as many images as available.")
    #     total_images = number_of_images
    
    # Calculate the figure size based on the number of rows and columns
    figsize_x = 20  # Adjust this value as needed
    figsize_y = 20  # Adjust this value as needed

    # fig, axes = plt.subplots(rows, plot_columns, figsize=(figsize_x, figsize_y), 
    #                          gridspec_kw={'wspace': 0.01, 'hspace': 0.0})  # Adjust hspace as needed

    fig, axes = plt.subplots(rows, plot_columns, figsize=(figsize_x, figsize_y))  # Adjust hspace as needed

    # Loop through the rows and columns
    image_index = 0
    for row in range(rows):
        for col in range(0, plot_columns, 2):

            if image_index < number_of_images:
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
            return f"No matching files found for pattern: {filename_pattern}"
    except Exception as e:
        return f"Error: {str(e)}"


# Example usage:
directory_path = 'exp11/image_samples/imagenet_sr4_sigma_0.0' 
output_path = 'results'
output_filename = 'test.png'
number_of_images = 20

create_and_save_4x5_image(directory_path, output_path, output_filename, number_of_images)
