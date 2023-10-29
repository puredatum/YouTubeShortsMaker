from .modules import LoadData, SegmentVideo, YoutubeClass, OpenaiClass

"""
The interface class to bring the classes together as a pipeline.

This is seperate into two sections. 
First one is to download the video and process the transcript into a list of dicts that contain the relevant 
sections and short video information

Seccond one is to take the list of dictionaries and split video into shorts using the data in it
"""

class YTShorts:
	def __init__(self, API_KEY, ORG_ID, model):
		self.data_loader = LoadData()
		self.segment_video = SegmentVideo()
		self.yt_class = YoutubeClass()
		self.oa_class = OpenaiClass(API_KEY, ORG_ID, model)
		self.video_id = None

	# Download video and transcript, send transcript to the AI to be processed. 
	#	Resulting in a .json with the final data
	def download_parse_data(self, video_id):
		self.yt_class.download_video_audio(video_id)
		transcript = self.yt_class.get_transcript_api(video_id)
		self.video_info_list = self.oa_class.process_chunks_transcript(transcript)
		print("Shorts Identified:")
		for short in self.video_info_list:
			print(short)
		print("-----------------------------------\n")
		self.data_loader.save_data(self.video_info_list)

		return self.video_info_list

	# Process the data gathered above and split the video based on it
	def make_video_files(self, video_id):
		self.video_info_list = self.data_loader.return_data()
		print("Generating shorts...")
		self.segment_video.segment_video(self.video_info_list, video_id)