"""Unit tests for the units converter library functions"""

from converters import gal_to_liter


def describe_a_library_of_units_converters ():
    """Test suite for units conversion functions"""
    # pylint: disable=unused-variable 
    def blows_smoke(): 
        assert True

    def that_can_convert_gallons_to_liters():
        assert gal_to_liter(1) == 3.79 