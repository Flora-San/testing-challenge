## Unit Testing Challenge - Exercise 2: Testing in 'DebugBear' Site Solution
### for my  solution approach I use python, pytest, and Selenium, the configuration described is for linux 

**Install Selenium**
with the following command line :
```
pip install selenium
```
Install Chromedriver to handle the window browser, for this test we use Chrome Browser
and then run the following command line to install poetry

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

speed_test.py
```
Inside some test created, I added some comments just to clarify the actions and decisions taken. 
We have a directory _screenshots_ created to save the images taken during the test.

**Scenarios considered for this test**
```
test_evaluate_website_speed_positive
test_evaluate_website_speed_negative_invalid_url
test_evaluate_website_speed_elements_present
test_open_new_window_and_switch
```
and each of this test include screenshots for executions


