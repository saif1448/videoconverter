import struct

# Input and output file paths
input_file_path = "output.bin"
output_file_path = "vid.bin"

# Open the input binary file
with open(input_file_path, 'rb') as file:
    # Step 1: Extract No. of Frames (8 bytes)
    no_frames_bytes = file.read(8)
    no_frames = struct.unpack('Q', no_frames_bytes)[0]  # Unsigned 64-bit integer
    print(f"No. of Frames: {no_frames}")

    # Step 2: Extract Channels (1 byte)
    channels_bytes = file.read(1)
    channels = struct.unpack('B', channels_bytes)[0]  # Unsigned 8-bit integer
    print(f"Channels: {channels}")

    # Step 3: Extract Width (1 byte)
    width_bytes = file.read(1)
    width = struct.unpack('B', width_bytes)[0]  # Unsigned 8-bit integer
    print(f"Width: {width}")

    # Step 4: Extract Height (1 byte)
    height_bytes = file.read(1)
    height = struct.unpack('B', height_bytes)[0]  # Unsigned 8-bit integer
    print(f"Height: {height}")

    # Step 5: Extract the remaining data
    remaining_data = file.read()

# Write the remaining data to a new binary file
with open(output_file_path, 'wb') as output_file:
    output_file.write(remaining_data)

print(f"Remaining data has been written to {output_file_path}")
