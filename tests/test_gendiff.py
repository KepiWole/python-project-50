import pytest
from gendiff.generate import generate_diff
from tests.fixtures.expected_result import PLAIN_DIFF_STR_12
from tests.fixtures.expected_result import PLAIN_DIFF_STR_21
from tests.fixtures.expected_result import NESTED_PLAIN_DIFF_STR_12
from tests.fixtures.expected_result import NESTED_STYLISH_DIFF_STR_12


@pytest.mark.paramerize("test_generate_diff, expected", [
                                                       (('./tests/fixtures/plain1.json', './tests/fixtures/plain2.json'), PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/plain2.json', './tests/fixtures/plain1.json', 'stylish'), PLAIN_DIFF_STR_21),
                                                         (('./tests/fixtures/plain1.yaml', './tests/fixtures/plain2.yaml', 'stylish'), PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/plain1.json', './tests/fixtures/plain2.yaml', 'stylish'), PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/plain1.yml', './tests/fixtures/plain2.json', 'stylish'), PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/plain2.yml', './tests/fixtures/plain1.yml', 'stylish'), PLAIN_DIFF_STR_21),
                                                         (('./tests/fixtures/plain2.yml', './tests/fixtures/plain1.json', 'stylish'), PLAIN_DIFF_STR_21),
                                                         (('./tests/fixtures/plain2.json', './tests/fixtures/plain1.yaml', 'stylish'), PLAIN_DIFF_STR_21),
                                                         (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.json', 'stylish'), NESTED_STYLISH_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.yaml', 'stylish'), NESTED_STYLISH_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.yaml', 'stylish'), NESTED_STYLISH_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.json', 'stylish'), NESTED_STYLISH_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.json', 'plain'), NESTED_PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.yaml', 'plain'), NESTED_PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.json', './tests/fixtures/nested2.yaml', 'plain'), NESTED_PLAIN_DIFF_STR_12),
                                                         (('./tests/fixtures/nested1.yaml', './tests/fixtures/nested2.json', 'plain'), NESTED_PLAIN_DIFF_STR_12)
                                                       ])
def test_gendiff(test_generate_diff, expected):
    assert generate_diff(test_generate_diff) == expected
