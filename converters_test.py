"""Unit tests for the units converter library functions"""

from converters import gal_to_liter
from converters import psi2kpa


def describe_a_library_of_units_converters ():
    """Test suite for units conversion functions"""
    # pylint: disable=unused-variable 
    def blows_smoke(): 
        assert True

    def that_can_convert_gallons_to_liters():
        assert gal_to_liter(1) == 3.79 
    
    def can_convert_psi_kpa():
        assert psi2kpa(32) == 220.631712 # 32 PSI == 220.631712 Kpa
        assert psi2kpa(8.5) == 58.6054 # 8.5 PSI == 58.6054
    
    
