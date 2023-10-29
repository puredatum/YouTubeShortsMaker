import os
from dotenv import load_dotenv
from YouTubeShorts import YTShorts

# Load your API information from the .env
load_dotenv()
API_KEY = os.getenv('API_KEY')
ORG_ID = os.getenv('ORG_ID')

# Select the model from openAI API
model = "gpt-4"

# List of videos to process
video_ids = ["mQ4KsFmP55M"]

# Setup the video pipeline
video_pipeline = YTShorts(API_KEY, ORG_ID, model)

# Loop through the video id list and run the pipeline for each video
for video_id in video_ids:
	# Download video, process and parse it
	video_info = video_pipeline.download_parse_data(video_id)

	# Run data pipeline on downloaded data
	video_pipeline.make_video_files(video_id)