import json

from typing import Dict

class ConfigurationReader():

	@staticmethod
	def Read(filePath: str) -> Dict:
		with open(filePath, 'r') as f:
			return json.load(f)

