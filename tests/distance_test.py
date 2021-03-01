# tests/distance_test.py
from mlproject.distance import haversine

def test_type():
    assert type(haversine(40.6, 30, 35.8, 2)) == float
