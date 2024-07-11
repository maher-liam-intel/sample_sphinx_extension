import pytest
from _ext.sphinx_extension import sample_function

class TestIniital():
   def test_function(self):
    assert sample_function('input') == True
    assert sample_function('') == False

TestIniital().test_function()