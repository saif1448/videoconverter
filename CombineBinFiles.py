import os

def combine_bin_files(input_folder, output_file):
    with open(output_file, 'wb') as combined_file:
        for i in range(100):  # Adjust the range as needed
            bin_file_path = os.path.join(input_folder, f"frame_{i:03d}.bin")
            if os.path.exists(bin_file_path):
                with open(bin_file_path, 'rb') as bin_file:
                    combined_file.write(bin_file.read())
            else:
                print(f"File not found: {bin_file_path}")

    print(f"Combined binary file created at: {output_file}")


input_folder = 'binary_files'  # Folder containing the .bin files
combined_bin_file = 'combined_frames.bin'


# Combine all .bin files into one
combine_bin_files(input_folder, combined_bin_file)