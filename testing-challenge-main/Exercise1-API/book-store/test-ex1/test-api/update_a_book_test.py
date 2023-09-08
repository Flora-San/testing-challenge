import pytest
import requests

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:5000/books"


# Positive Test Cases
def test_update_book_positive():
    book_id = '1'

    # Define updated book data
    updated_data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "published_date": "2023-09-06",
        "isbn": "9876543210",
        "price": 29.99
    }

    # Send a PUT request to update the book by ID
    response = requests.put(f"{BASE_URL}/{book_id}", json=updated_data)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Validate response payload
    updated_book = response.json()
    assert 'book_id' in updated_book
    assert updated_book['title'] == updated_data['title']
    assert updated_book['author'] == updated_data['author']

    # Validate response headers
    assert 'Content-Type' in response.headers
    content_type = response.headers['Content-Type']
    assert content_type == 'application/json'


# Negative Test Case
def test_update_book_negative_book_not_found():
    invalid_book_id = "2"

    updated_data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "published_date": "2023-09-06",
        "isbn": "9876543210",
        "price": 29.99
    }

    response = requests.put(f"{BASE_URL}/{invalid_book_id}", json=updated_data)
    assert response.status_code == 404

    response_data = response.json()
    assert "error" in response_data
    assert "Book not found" in response_data["error"]


if __name__ == "__main__":
    pytest.main()
