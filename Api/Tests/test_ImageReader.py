import pytest
from Api.Flask import ImageReader

def test_from_binary_returns_None_when_invalid():
    input = "Not Binary Image"
    assert ImageReader.FromBinary(input) == None

def test_from_binary_returns_Some_when_invalid():
    input = open("test_dog.jpg", 'r')
    assert ImageReader.FromBinary(input) != None
