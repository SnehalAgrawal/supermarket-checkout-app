import sys
import pytest
from fastapi.testclient import TestClient
from pathlib import Path

# Calculating the absolute path to the directory containing main.py
current_file_path = Path(__file__).resolve()
backend_dir = current_file_path.parents[1]
sys.path.append(str(backend_dir))

from main import app

client = TestClient(app)


@pytest.mark.parametrize("input_items, expected_total", [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("CDBA", 115),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 230),
    ("AAAAAA", 260),
    ("AAAB", 160),
    ("AAABB", 175),
    ("AAABBD", 190),
    ("DABABA", 190),
    ("", 0)  # Edge case: empty input
])
def test_checkout_endpoint(input_items, expected_total):
    response = client.post("/checkout/", json={"items": input_items})
    assert response.status_code == 200
    assert response.json()["total"] == expected_total
