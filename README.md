# YouTubeShortsMaker

This module is designed to automate the generate of shorts from a YouTube video, the videos are supplied through video ids and downloaded using an API.

This takes in a list of video ids from YouTube and using OpenAI to determine the best sections of the video and cut them as shorts.

## Setup
1. Add a .env file in the same directory as the file that will access the module
2. Make sure you have an empty "downloads" and "resources" folder in the same folder as the file accessing the module
3. Run the usage code below

## Usage
The script supplied shows how to use the script. You will need to supply a list of youtube video ids to be processed into shorts.

This imports the module and the environment variables.
```
import os
from dotenv import load_dotenv
from YouTubeShorts import YTShorts
```

Load your API information from the .env
```
load_dotenv()
API_KEY = os.getenv('API_KEY')
ORG_ID = os.getenv('ORG_ID')
```

Select the model from openAI API, this can be the gpt-3.5 if you don't have access to gpt-4
```
model = "gpt-4"
```

List of videos to process 
```
video_ids = ["mQ4KsFmP55M"]
```

Setup the video pipeline
```
video_pipeline = YTShorts(API_KEY, ORG_ID, model)
```

Loop through the video id list and run the pipeline for each video
```
for video_id in video_ids:
	Download video, process and parse it
	video_info = video_pipeline.download_parse_data(video_id)

	Run data pipeline on downloaded data
	video_pipeline.make_video_files(video_id)
```

## YouTube Video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/citP-03eFg8/0.jpg)](https://www.youtube.com/watch?v=citP-03eFg8)
