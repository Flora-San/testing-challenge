import pytest
import requests

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:5000/books"


# Positive Test Cases
def test_retrieve_single_book_positive():
    book_id = "1"

    # Send a GET request to retrieve a single book by ID
    response = requests.get(f"{BASE_URL}/{book_id}")

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Validate response payload
    book = response.json()
    assert 'book_id' in book
    assert 'title' in book
    assert 'author' in book

    # Validate response headers
    assert 'Content-Type' in response.headers
    content_type = response.headers['Content-Type']
    assert content_type == 'application/json'


# Negative Test Case
def test_retrieve_single_book_negative_book_not_found():
    invalid_book_id = "2"
    response = requests.get(f"{BASE_URL}/{invalid_book_id}")
    assert response.status_code == 404

    response_data = response.json()
    assert "error" in response_data
    assert "Book not found" in response_data["error"]

    assert 'Content-Type' in response.headers
    content_type = response.headers['Content-Type']
    assert content_type == 'application/json'


if __name__ == "__main__":
    pytest.main()
