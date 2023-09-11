import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/books"


# Utility function to create a new book
def create_book(title, author, published_date, isbn, price):
    book_data = {
        "title": title,
        "author": author,
        "published_date": published_date,
        "isbn": isbn,
        "price": price
    }
    response = requests.post(BASE_URL, json=book_data)
    assert response.status_code == 201
    return response.json()


# Utility function to retrieve a book by ID
def get_book_by_id(book_id):
    response = requests.get(f"{BASE_URL}/{book_id}")
    return response


# Utility function to delete a book by ID
def delete_book_by_id(book_id):
    response = requests.delete(f"{BASE_URL}/{book_id}")
    assert response.status_code == 204


def test_create_book():
    book_data = create_book("New Book", "Author Name", "2023-09-06", "1234567890", 19.99)

    delete_book_by_id(book_data['book_id'])


def test_retrieve_all_books():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_retrieve_single_book():
    book_data = create_book("Test Book", "Test Author", "2023-09-07", "9876543210", 29.99)
    book_id = book_data['book_id']

    response = get_book_by_id(book_id)
    assert response.status_code == 200

    delete_book_by_id(book_id)


def test_update_book():
    book_data = create_book("Original Title", "Original Author", "2023-09-08", "1111111111", 39.99)
    book_id = book_data['book_id']

    updated_data = {
        "title": "Updated Title",
        "price": 49.99
    }
    response = requests.put(f"{BASE_URL}/{book_id}", json=updated_data)
    assert response.status_code == 200

    delete_book_by_id(book_id)


def test_delete_book():
    book_data = create_book("Book to Delete", "Delete Author", "2023-09-09", "9999999999", 9.99)
    book_id = book_data['book_id']

    response = requests.delete(f"{BASE_URL}/{book_id}")
    assert response.status_code == 204

