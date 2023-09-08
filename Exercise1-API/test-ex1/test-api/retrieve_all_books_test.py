import pytest
import requests

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:5000/books"


# Positive Test Cases
def test_retrieve_all_books_positive():
    # Send a GET request to retrieve all books
    response = requests.get(BASE_URL)
    assert response.status_code == 200

    # Validate response payload
    books = response.json()
    assert isinstance(books, list)

    # Validate response headers
    assert 'Content-Type' in response.headers
    content_type = response.headers['Content-Type']
    assert content_type == 'application/json'


def test_retrieve_all_books_positive_2():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

    books = response.json()
    assert isinstance(books, list)

    assert 'Content-Type' in response.headers
    content_type = response.headers['Content-Type']
    assert content_type == 'application/json'


def test_retrieve_all_books_positive_3():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

    books = response.json()
    assert isinstance(books, list)

    assert 'Content-Type' in response.headers
    content_type = response.headers['Content-Type']
    assert content_type == 'application/json'


if __name__ == "__main__":
    pytest.main()
