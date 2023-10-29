from dataclasses import dataclass
import json

"""
This dataclass saves the identified timeframes and transcript that the AI model determined are best.

This isn't for long term storage of the data, this is used to store the data between gathering and parsing
the transcript and creating the short videos. This is done if you wish to create the shorts at a different time
to creating the transcripts and parsing them.
"""

@dataclass
class LoadData:
	json_file_path: str = "resources/data.json"

	# Return the saved data from the .json
	def return_data(self):
		with open(self.json_file_path, 'r') as json_file:
			loaded_data = json.load(json_file)

		return loaded_data

	# Save the json, this will overwrite any previous version of it
	def save_data(self, data_in):
		with open(self.json_file_path, 'w') as json_file:
			json.dump(data_in, json_file)