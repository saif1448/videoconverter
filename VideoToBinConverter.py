# Path to the input MP4 file
mp4_file_path = "sample_video.mp4"

# Path to the output .bin file
bin_file_path = "sample_video.bin"

# Open the MP4 file in binary read mode
with open(mp4_file_path, 'rb') as mp4_file:
    # Read the entire content of the MP4 file
    mp4_data = mp4_file.read()

# Open the .bin file in binary write mode
with open(bin_file_path, 'wb') as bin_file:
    # Write the MP4 content to the .bin file
    bin_file.write(mp4_data)

print(f"MP4 file has been successfully converted to a BIN file at {bin_file_path}")
