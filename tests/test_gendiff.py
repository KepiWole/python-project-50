from gendiff.generate import generate_diff

RIGHT_RESULT = {'- follow': False, '  host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}

def test_gendiff():
  assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
