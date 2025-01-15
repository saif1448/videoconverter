import numpy as np
import cv2
import struct

def read_bin_file(filename):
    """
    Reads the binary file and extracts the header and frame data.
    """
    with open(filename, "rb") as file:
        # Read the header
        num_frames = struct.unpack('<Q', file.read(8))[0]  # unsigned long long (8 bytes, little-endian)
        channels = struct.unpack('<B', file.read(1))[0]    # unsigned char (1 byte)
        height = struct.unpack('<B', file.read(1))[0]      # unsigned char (1 byte)
        width = struct.unpack('<B', file.read(1))[0]       # unsigned char (1 byte)

        print(f"Number of Frames: {num_frames}")
        print(f"Channels: {channels}")
        print(f"Height: {height}")
        print(f"Width: {width}")

        # Read the frame data
        frame_size = channels * height * width
        frames = []

        for _ in range(num_frames):
            frame_data = file.read(frame_size)
            if not frame_data:
                break

            # Convert binary data to a numpy array
            frame = np.frombuffer(frame_data, dtype=np.uint8)

            # Reshape the frame data into channels
            if channels == 1:
                # Grayscale frame: reshape to (height, width)
                frame = frame.reshape((height, width))
            elif channels == 3:
                # RGB frame: reshape to (height, width, channels)
                # Split the flat array into 3 channels
                channel_size = height * width
                channel0 = frame[0:channel_size].reshape((height, width))
                channel1 = frame[channel_size:2*channel_size].reshape((height, width))
                channel2 = frame[2*channel_size:3*channel_size].reshape((height, width))

                # Stack the channels to create an RGB image
                frame = np.stack((channel0, channel1, channel2), axis=-1)
            else:
                raise ValueError("Unsupported number of channels. Only 1 (grayscale) or 3 (RGB) channels are supported.")

            frames.append(frame)

        return frames, height, width, channels

def create_video(frames, height, width, channels, output_filename, fps=30):
    """
    Creates a video file from the extracted frames.
    """
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
    out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

    for frame in frames:
        if channels == 1:
            # Convert grayscale to BGR (3 channels) for video writing
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        elif channels == 3:
            # Ensure the frame is in BGR format (OpenCV uses BGR by default)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        else:
            raise ValueError("Unsupported number of channels. Only 1 (grayscale) or 3 (RGB) channels are supported.")

        # Write the frame to the video
        out.write(frame)

    # Release the VideoWriter
    out.release()
    print(f"Video saved as {output_filename}")

def main():
    # Input and output filenames
    input_bin_file = "swap_sp.bin"  # Replace with your input .bin file
    output_video_file = "swap_speed.mp4"  # Replace with your desired output video file

    # Read the .bin file
    frames, height, width, channels = read_bin_file(input_bin_file)

    # Create the video
    create_video(frames, height, width, channels, output_video_file)

if __name__ == "__main__":
    main()