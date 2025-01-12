import numpy as np
import cv2
import os

def bin_to_video(bin_file, output_video_file, num_frames, num_channels, height, width, fps=30):
    """
    Convert a binary file to a video file.

    :param bin_file: Path to the input binary file.
    :param output_video_file: Path to save the output video file.
    :param num_frames: Number of frames in the video.
    :param num_channels: Number of color channels (e.g., 3 for RGB).
    :param height: Height of each frame.
    :param width: Width of each frame.
    :param fps: Frames per second for the output video.
    """
    # Calculate the total number of bytes in the binary file
    expected_size = num_frames * num_channels * height * width
    actual_size = os.path.getsize(bin_file)

    if expected_size != actual_size:
        raise ValueError(
            f"File size mismatch! Expected {expected_size} bytes, but got {actual_size} bytes. "
            "Please check the parameters (num_frames, num_channels, height, width)."
        )

    # Read the binary file
    with open(bin_file, 'rb') as f:
        video_data = np.frombuffer(f.read(), dtype=np.uint8)

    # Calculate the size of a single channel per frame
    single_channel_size = height * width
    frame_size = num_channels * single_channel_size

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI files
    video_writer = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    # Process each frame
    for i in range(num_frames):
        # Extract the data for this frame
        frame_data = video_data[i * frame_size: (i + 1) * frame_size]

        # Split the frame data into channels
        channels = [
            frame_data[j * single_channel_size: (j + 1) * single_channel_size].reshape((height, width))
            for j in range(num_channels)
        ]

        # Combine the channels into a single frame
        if num_channels == 1:
            frame = cv2.cvtColor(channels[0], cv2.COLOR_GRAY2BGR)  # Convert grayscale to BGR
        else:
            frame = np.stack(channels, axis=-1)  # Combine channels into an RGB frame

        # Write the frame to the video
        video_writer.write(frame)

    # Release the video writer
    video_writer.release()
    print(f"Video saved to {output_video_file}")

# Example usage
if __name__ == "__main__":
    # Parameters (adjust these based on your video metadata)
    bin_file = "output.bin"
    output_video_file = "clip.avi"
    num_frames = 100  # Number of frames
    num_channels = 3  # Number of color channels (1 for grayscale, 3 for RGB)
    height = 128  # Height of each frame
    width = 128  # Width of each frame
    fps = 30  # Frames per second

    # Convert binary file to video
    bin_to_video(bin_file, output_video_file, num_frames, num_channels, height, width, fps)