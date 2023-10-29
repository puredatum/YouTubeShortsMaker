from dataclasses import dataclass
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import math

"""
This dataclass takes the processed transcript which is a list of dicts with timestamps and generates the segmented video clips

The video clips are saved to the downloads folder with the video id as part of the name.
"""

@dataclass
class SegmentVideo:

	def segment_video(self, data_list, video_id):

		# Video counter
		count = 0

		# Set the original video path and total video duration of it
		original_video_path = f"downloads/{video_id}_video.mp4"
		clip = VideoFileClip(original_video_path)
		clip_duration = clip.duration
		clip.close()
		clip = None

		# Loop throug the list of dicts to generate the videos
		for i, segment in enumerate(data_list):
			# Set start/end time for the short
			start_time = math.floor(float(data_list[i]["start_time"]))
			end_time = math.ceil(float(data_list[i]["end_time"]))

			# Create the video clip
			if end_time < clip_duration:
				output_path = f"downloads/{video_id}_{str(i)}.mp4"
				ffmpeg_extract_subclip(original_video_path, start_time, end_time, targetname=output_path)
				count += 1