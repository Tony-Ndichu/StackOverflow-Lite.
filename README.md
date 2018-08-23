[![Build Status](https://travis-ci.com/Tony-Ndichu/testdb.svg?branch=master)](https://travis-ci.com/Tony-Ndichu/testdb)
[![Coverage Status](https://coveralls.io/repos/github/Tony-Ndichu/testdb/badge.svg?branch=master)](https://coveralls.io/github/Tony-Ndichu/testdb?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/4bd09b6fc0b59d95bcc9/maintainability)](https://codeclimate.com/github/Tony-Ndichu/testdb/maintainability)
# StackOverFlow-Lite.

## Introduction
* This is the API for the project StackOverflow-Lite. The fornt-end can be found  **[```here```](https://github.com/Tony-Ndichu/StackOverflow-Lite)**

* StackOverFLow-Lite a platform where people can ask questions and receive answers therefore providing an interactive Q&A platform.


## Technologies used & needed.
* **[Python3.6.5](https://www.python.org/downloads/release/python-365/)**
* **[Flask](flask.pocoo.org/)**
* **[Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)**

## Link to heroku:

## Current endpoints

* #### Add a question.
    `POST /api/v1/questions`: 
    ```
    headers = {content_type:application/json}

    {
        "title": "Sample Title",
        "description" : "This is a sample description"

    }
    ```
* #### Fetch all questions.
    `GET /api/v1/questions`
    ```
    headers = {content_type:application/json}
    ```


* #### Fetch a specific question.   
    `GET /api/v1/questions/<questionId>` 
    ```
    headers = {content_type:application/json} 
    ```
    

* #### Delete a question.
    `DELETE /api/v1/questions/questionId/delete`:
    ```
    headers = {content_type:application/json}

    ```


* #### Add answer to a question.
    `POST /api/v1/questions/questionId/answers`:
    ```
    headers = {content_type:application/json}

    {
        "answer": "This is the answer body"
    }
    ```


## Installation guide and usage

 #### **Clone the branch.**
    ```
    $ git clone -b develop https://github.com/Tony-Ndichu/StackOverflow-Lite.git
    ```
 #### **Cd to app entry point(run.py)**
    ```
    $ cd StackOverflow-Lite   
    ```
 #### **Activate your virtual environment**
 
 #### **Install dependencies**
    ```
    (myenv)$ pip install -r requirements.txt
    ```
### **Set environment variables**
    ```
    (myenv)$ set FLASK_APP=run.py
    ```

#### **Run the app**
   ```
    (myenv)$ flask run
   ```
#### **Run Tests**
  ```
  (myenv)$ python -m unittest
  ```




