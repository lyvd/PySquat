import pytest
import sys
sys.path.insert(1, "../pysquat")
from ossquat import OSSquat
import logging
logging.basicConfig(level=logging.DEBUG)

def test_get_repeated_characters():
    squat = OSSquat(package_name="reequest")
    repeated_chars = list(squat.get_repeated_characters())
    logging.info(f"""repeated characters: {repeated_chars[0][0]}, number of occurences: {repeated_chars[0][1]}""")
    assert repeated_chars[0][0] == 'e'
    assert repeated_chars[0][1] == 2