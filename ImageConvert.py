import os
from PIL import Image
import numpy as np


def png_to_bin(input_png_path, output_bin_path):
    # Open the PNG file
    with Image.open(input_png_path) as img:
        # Ensure the image is in RGB format
        img = img.convert("RGB")

        # Convert the image to a NumPy array
        pixel_data = np.array(img)

        # Reshape the array to raw pixel data
        raw_data = pixel_data.tobytes()

        # Write the raw pixel data to the binary file
        with open(output_bin_path, 'wb') as bin_file:
            bin_file.write(raw_data)

    print(f"Binary file created at: {output_bin_path}")


def convert_all_png_to_bin(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all PNG files in the input folder
    for i in range(100):  # Adjust the range if needed
        input_png_path = os.path.join(input_folder, f"frame_{i:03d}.png")
        output_bin_path = os.path.join(output_folder, f"frame_{i:03d}.bin")

        if os.path.exists(input_png_path):
            png_to_bin(input_png_path, output_bin_path)
        else:
            print(f"File not found: {input_png_path}")


# Example usage
input_folder = 'frames'  # Folder containing PNG files
output_folder = 'binary_files'  # Folder to save the binary files

convert_all_png_to_bin(input_folder, output_folder)
