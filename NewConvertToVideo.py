import cv2
import numpy as np
import struct

# File paths
remaining_file_path = "vid.bin"
output_video_path = "output_video.avi"

# Known parameters (replace these with actual extracted values)
channels = 3  # From the binary file
width = 128  # Extracted width
height = 128  # Extracted height
no_frames = 100  # Total number of frames extracted

# Open the remaining binary data file
with open(remaining_file_path, 'rb') as file:
    remaining_data = file.read()

# Calculate the size of a single channel per frame
single_channel_size = width * height
frame_size = channels * single_channel_size

# Ensure the data size matches the expected number of frames
assert len(remaining_data) == frame_size * no_frames, "Data size mismatch!"

# Create a VideoWriter object using OpenCV
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI files
fps = 30  # Frames per second
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# Process each frame
for i in range(no_frames):
    # Extract the data for this frame
    frame_data = remaining_data[i * frame_size: (i + 1) * frame_size]

    # Split the frame data into channels
    channel_1 = frame_data[0:single_channel_size]
    channel_2 = frame_data[single_channel_size:2 * single_channel_size]
    channel_3 = frame_data[2 * single_channel_size:3 * single_channel_size]

    # Combine the channels into a single frame
    frame = np.zeros((height, width, channels), dtype=np.uint8)
    frame[:, :, 0] = np.frombuffer(channel_1, dtype=np.uint8).reshape((height, width))  # Red
    frame[:, :, 1] = np.frombuffer(channel_2, dtype=np.uint8).reshape((height, width))  # Green
    frame[:, :, 2] = np.frombuffer(channel_3, dtype=np.uint8).reshape((height, width))  # Blue

    # Write the frame to the video
    video_writer.write(frame)

# Release the VideoWriter
video_writer.release()

print(f"Video has been created and saved as {output_video_path}")
