import pytest
from Infrastructure import Config
from TestBase import Fixtures


@pytest.fixture
def subject():
    return Config.Config()


def test_get_returns_none_when_cofig_not_present(subject):
    assert subject.Get('library') == None


def test_get_returns_none_when_cofig_present(subject):
    assert subject.Get('oracle') != None
