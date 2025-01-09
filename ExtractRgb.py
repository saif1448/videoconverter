import numpy as np


def bin_to_png(input_bin_path, output_png_path, width, height):
    # Read the binary file
    with open(input_bin_path, 'rb') as bin_file:
        raw_data = bin_file.read()

    # Convert the raw byte data back to a NumPy array (each pixel has 3 bytes: RGB)
    pixel_data = np.frombuffer(raw_data, dtype=np.uint8)

    # Reshape the array into the shape of the image (height, width, 3)
    pixel_data = pixel_data.reshape((height, width, 3))

    # Now pixel_data contains the RGB values, where each pixel is in the form of [R, G, B]

    print("Extracted RGB values for the first 5 pixels:")
    print(pixel_data[0, 0])  # Example: print the RGB values of the first pixel

    # Save the image back to PNG if needed
    from PIL import Image
    img = Image.fromarray(pixel_data)
    img.save(output_png_path)

    print(f"PNG file created at: {output_png_path}")


# Example usage
input_bin_path = 'frame_000.bin'  # Replace with your .bin file path
output_png_path = 'extracted_image.png'  # Replace with desired PNG output path
width, height = 369, 369  # Replace with the original width and height of the PNG image

bin_to_png(input_bin_path, output_png_path, width, height)
