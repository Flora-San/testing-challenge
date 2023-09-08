## Unit Testing Challenge - Exercise 1: Book Store REST API solution
### for my  solution approach I use python, pytest, and the configuration described is for linux 

**Install poetry _linux instructions_**

update first if is necessary
```
sudo snap install curl  # version 8.1.2
```
and then run the following command line to install poetry
```
curl -sSL https://install.python-poetry.org | python3 -
```
check poetry version 
```
poetry --version
```
**Install pytest**

pytest
```
pip install pytest
```

**Run Tests**

You can run these test cases using pytest by executing the following command in your project directory:
Replace _name_test_file.py_ with the name of the Python test cases file you want to run.
```
pytest your_test_file.py

example:

create_new_book_test.py
```
Inside some test created, I added some comments just to clarify the actions and decisions taken, like the example below:

```
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
    
```    
https://cdn.stackoverflow.co/images/jo7n4k8s/production/4ad7a0bd338d7616a7900b9c94b7bd2c53da825e-794x590.png?auto=format