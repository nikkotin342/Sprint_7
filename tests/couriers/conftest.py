import random
import pytest


@pytest.fixture()
def courier_data():
    return {f"bakki_{random.randint(100, 999)}",f"bakki_{random.randint(100, 999)}",f"bakki_{random.randint(100, 999)}"}