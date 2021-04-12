# """
# FILE: test_get_data.py
# DESCRIPTION: Test reading raw files from GitHub
# AUTHOR: Aman Patel
# DATE: 12-April-2021
# """
# # Import libraries
from ..utils.vaccine import vaccine

v = vaccine()


def test_vaccine_data() -> None:
    result = v.get_vaccine_data()
    assert len(result) > 0
    assert isinstance(result, list) is True
