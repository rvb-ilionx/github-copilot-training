from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

_BASELINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activity data before each test for isolation."""
    activities.clear()
    activities.update(deepcopy(_BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
