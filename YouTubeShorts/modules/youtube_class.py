from dataclasses import dataclass
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
import os
from moviepy.editor import VideoFileClip

"""
Returns the youtube transcript from the online video.

Downloads the YouTube video with average quality and saved.
"""

@dataclass
class YoutubeClass:
	# Download the transcript API by video id
	def get_transcript_api(self, video_id):
		transcript = YouTubeTranscriptApi.get_transcript(video_id)

		self.transcript = []

		jump = 60
		overlap = 10
		for i in range(0, len(transcript)-overlap, jump):
			self.transcript.append(transcript[i:jump+i+overlap])

		return self.transcript

	# Download the video as an mp4
	def download_video_audio(self, video_id):
		# Path for the video download
		out_video_name = "downloads/" + video_id + "_video.mp4"

		# Download video
		url = "https://www.youtube.com/watch?v=" + video_id
		format_video = "averagevideo+averageaudio/best"
		ydl_opts = {
		    "outtmpl": out_video_name,
		    "format": format_video,
		}
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url])