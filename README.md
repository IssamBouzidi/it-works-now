## it-works-now
An example to get started in unit testing with pytest

##  Project  
This small project is an API to manage checkout card, the libraries below was used to create this project   
+ Python 3.7.10
+ API: Flask  
+ Unit Test: Pytest  

## Content of project  
* module folder: Contains card class  
* reports:  Contains unit test report
* tests:  Contains tests to be launched for card class and API
* app.py:  Main file contains routes
* pytest.ini file:  a configuration file for pytest
* requirements.txt file:  Contains librairies required for this project

## How to execute unit tests
Please use the command below to execute unit test, a test report `report.html` will be generated in the reports folder  
`pytest --html=report.html --self-contained-html`  
