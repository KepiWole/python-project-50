import json
from gendiff.input_parser import parse_datafile


def generate_diff(file_name1, file_name2):
	filename1 = parse_datafile(file_name1)
	filename2 = parse_datafile(file_name2)
	print('{')
	result = {}
	for key in filename1:
		if (key in filename2) and filename2[key] == filename1[key]:
			result['  ' + key] = filename1[key]
			del filename2[key]
		elif (key in filename2) and filename2[key] != filename1[key]:
			result['- ' + key] = filename1[key]
			result['+ ' + key] = filename2[key]
			del filename2[key]
		else:
			result['- ' + key] = filename1[key]
	filename2_reduction = {f'+ {key}': v for key, v in filename2.items()}
	result.update(filename2_reduction)
	result = dict(sorted(result.items(), key=lambda x: x[0][2]))
	for key in result:
		print(key,':', result[key])
	print('}')
	return result
if __name__ == '__main__':
    generate_diff(filename1, filename2)
