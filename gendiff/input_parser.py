import json
from pathlib import Path

def get_file_extension(file_path):
	return Path(file_path).suffix


def get_file_reader(file_path):
	return {
        	'.json': json.load,
    	}.get(get_file_extension(file_path))


def parse_datafile(file_path: str) -> dict:
	reader = get_file_reader(file_path)
	with open(file_path) as file:
		return reader(file)
