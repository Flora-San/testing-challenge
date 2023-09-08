import pytest
import requests

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:5000/books"


# Positive Test Cases
def test_create_book_positive():
    # Define valid book data
    book_data = {
        "title": "Positive Test Book",
        "author": "Author Name",
        "published_date": "2023-09-06",
        "isbn": "1234567890",
        "price": 19.99
    }

    # Send a POST request to create a new book
    response = requests.post(BASE_URL, json=book_data)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Validate response payload
    created_book = response.json()
    assert created_book['title'] == book_data['title']
    assert created_book['author'] == book_data['author']


# Negative Test Cases
def test_create_book_negative_missing_fields():
    book_data = {
        "title": "Missing Fields Book",
        "author": "Author Name"
        # Missing 'published_date', 'isbn', and 'price' fields
    }

    response = requests.post(BASE_URL, json=book_data)
    assert response.status_code == 400

    error_message = response.json()['error']
    assert "Missing required fields" in error_message


def test_create_book_negative_long_title():
    book_data = {
        "title": "AAAAAAAAAAAAAAAAAAAA" * 1000,
        "author": "Author Name",
        "published_date": "2023-09-06",
        "isbn": "1234567890",
        "price": 19.99
    }

    response = requests.post(BASE_URL, json=book_data)
    assert response.status_code == 201


if __name__ == "__main__":
    pytest.main()
