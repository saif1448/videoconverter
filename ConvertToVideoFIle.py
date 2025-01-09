import cv2
import numpy as np

def bin_to_video(input_bin_file, output_video_file, frame_width, frame_height, fps):
    with open(input_bin_file, 'rb') as bin_file:
        raw_data = bin_file.read()

    # Calculate the size of each frame (3 channels for RGB)
    frame_size = frame_width * frame_height * 3
    total_frames = len(raw_data) // frame_size

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
    out = cv2.VideoWriter(output_video_file, fourcc, fps, (frame_width, frame_height))

    for i in range(total_frames):
        start = i * frame_size
        end = start + frame_size
        frame_data = raw_data[start:end]

        # Convert raw frame data back to a NumPy array
        frame = np.frombuffer(frame_data, dtype=np.uint8).reshape((frame_height, frame_width, 3))

        # Write the frame to the video file
        out.write(frame)

    out.release()
    print(f"Video file created at: {output_video_file}")


combined_bin_file = 'vid.bin'  # Output combined .bin file
output_video_file = 'output_video_test.mp4'  #

frame_width = 128  # Width of the frames
frame_height = 128  # Height of the frames
fps = 100  # Frames per second
bin_to_video(combined_bin_file, output_video_file, frame_width, frame_height, fps)




