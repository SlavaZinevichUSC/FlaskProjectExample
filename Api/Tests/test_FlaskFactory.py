import pytest
from Api.Flask import FlaskFactory
from TestBase import Fixtures
from Global import Core
@pytest.fixture()
def dog():
    dog = open('test_dog.jpg', 'rb')
    return dog

@pytest.fixture()
def app():

    app = FlaskFactory.CreateApp()
    app.config.update({
        "TESTING": True,
    })
    yield app.test_client()

def Set_Mock_model():
    class MockModel():
        def GetPredictions(self, image):
            return ["A", "B", "C"]
    Core.Resolver.model = MockModel()

def test_from_binary_returns_bad_when_image_not_provided(app, dog):
    response = app.post('binary', data={'im' : ''})
    assert response.status_code == 400

def test_from_binary_returns_bad_when_image_compatible(app):
    response = app.post('binary', data={'image': 'dog.jpg'})
    assert response.status_code == 400

def test_from_binary_returns_success_when_generated(app, dog):
    Set_Mock_model()
    response = app.post('binary', data={'image': dog})
    assert response.status_code == 200

def test_from_binary_returns_list_when_generated(app, dog):
    Set_Mock_model()
    response = app.post('binary', data={'image': dog})
    print(response.json)
    assert response.json['predictions'] == 'A\nB\nC'