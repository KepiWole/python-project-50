from gendiff.generate import generate_diff

RIGHT_RESULT = {
    "    host": "hexlet.io",
    "  - timeout": "50",
    "  + timeout": "20",
    "  - follow": "false",
    "  - proxy": "123.234.53.22",
    "  + verbose": "true",
  }

def test_gendiff():
  assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
