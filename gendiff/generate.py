import json

with open('testFiles/file1.json') as json_file:
  filename1 = json.load(json_file)
with open('testFiles/file2.json') as json_file:
  filename2 = json.load(json_file)

def generate_diff(filename1, filename2):
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
  filename2_reduction = {f'- {key}': v for key, v in filename2.items()}
  sort_result = result | filename2_reduction
  sorted(sort_result.items())
  for key in sort_result:
     print(key,':',sort_result[key])
  print('}')

if __name__ == '__main__':
    generate_diff(filename1, filename2)
