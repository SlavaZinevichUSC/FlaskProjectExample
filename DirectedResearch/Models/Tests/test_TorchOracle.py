import pytest
from PIL import Image
from Models.Torch import TorchOracle
@pytest.fixture
def Dog():
    yield Image.open('test_dog.jpg')


@pytest.fixture()
def subject():
    oracle = TorchOracle.FromHub()
    yield oracle

def test_predict(subject, Dog):
    preds = subject.Predict(Dog, 5)
    print(preds)
    assert True
