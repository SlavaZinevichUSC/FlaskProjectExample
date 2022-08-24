import pytest
from Api.Flask import ImageReader

def test_from_binary_returns_None_When_Invalid():
    input = "Not Binary Image"
    assert ImageReader.FromBinary(input) == None
