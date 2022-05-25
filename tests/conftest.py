import pytest
import random 

@pytest.fixture
def random_seed():
    random.seed(0)