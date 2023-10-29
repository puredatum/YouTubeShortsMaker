from dataclasses import dataclass
import openai
import json

"""
This is for managing the OpenAI API instance.

You will need to add in your own API keys and choose what gpt you want to use.

The response object sets a framework for the AI to respond in. This allows for proper data cleaning.
"""

@dataclass
class OpenaiClass:
	API_KEY: str
	ORG_ID: str
	model: str

	# Loads instance and sets up the response object
	def __post_init__(self):
		self.oai = openai
		self.oai.organization = self.ORG_ID
		self.oai.api_key = self.API_KEY

		# Framework for the LLM to formulate a response
		self.response_obj = '''[{
				"start_time": 97.19,
				"end_time": 127.43,
				"description": "The most important thing is to not give up, even when you want to.", #A takeaway message for the section
				"title": "", #Suggested title of this section
				"duration":36 #Length in seconds,
				"transcript": "" #Exact transcript of the audio
			},
			{
				"start_time": 169.58,
				"end_time": 199.10,
				"description": "It is okay to be in darkness, don't give up.", #A takeaway message for the section
				"title": "", #Suggested title of this section
				"duration":33, #Length in seconds
				"transcript": "" #Exact transcript of the audio
			}]'''


	# The transcript is chunked by size to feed into the LLM. This function processes each chunk in the LLM
	#	and creates list of dictionaries as the result
	def process_chunks_transcript(self, transcript):

		# Final list of the parsed transcript
		parsed_transcript = []

		print(f"Video broken into {len(transcript)} chunks for processing.")

		# Loops through chunks of transcript
		for idx, chunk in enumerate(transcript):
			print(f"Processing chunk: {idx + 1} of {len(transcript)}")
			
			# Creates the prompt message
			prompt = f"This is a transcript of a video/podcast. Please identify the most viral sections from this video, make sure they at least 30 seconds long. Make sure you provide responses only in this format {self.response_obj}, I just want JSON as Response(nothing else)  \n Here is the Transcription:\n{chunk}"
			messages = [
				{"role": "system", "content": "You are a ViralGPT helpful assistant. You are master at reading youtube transcripts and identifying the most interesting parts from them"},
				{"role": "user", "content": prompt}]

			# Makes chat request to LLM
			response = self.oai.ChatCompletion.create(
				model=self.model,
				messages=messages,
				n=1,
				stop=None
				)

			# Returns and parses the response into a list of dictionaries
			self.combined_response = response.choices[0]['message']['content']
			chunk_parsed = self._parse_response()

			# Adds the sections to the parsed_transcript list of dictionaries
			[parsed_transcript.append(chunk) for chunk in chunk_parsed]

		return parsed_transcript

	# Parsing the AI response into a list of dictionaries
	def _parse_response(self):
		combined_response_final = self.combined_response.replace("        ", "")
		combined_response_final = combined_response_final.replace("\n", "")
		combined_response_final = combined_response_final.replace("    ", "")
		combined_response_final = combined_response_final.replace("[", "")
		combined_response_final = combined_response_final.replace("]", "")
		combined_response_final = combined_response_final.replace("} {", "},{")

		response_json = json.dumps(combined_response_final, indent=4)
		response_json = json.loads(response_json)

		list_json = response_json.split("},{")
		video_info = []

		for idx, val in enumerate(list_json):
			val = val.replace("{", "")
			val = val.replace("}", "")
			val = val.replace(',"', ', "')
			val = eval("{" + val + "}")
			video_info.append(val) 

		video_info = video_info[:-1]

		return video_info