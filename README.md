## Installations

 Step 1 
 mkdir fastapi 

 Step 2
 python3 -m venv env

 Step 3
 source env/bin/activate


Step 4
pip3 install fastapi uvicorn


To start and run the application use this command 

uvicorn main:app --reload


view the application using this url 
http://localhost:8000

 to view the doc 
http://localhost:8000/docs


Folder structures :

    main.py: This is the main entry point for your FastAPI application. It usually contains the instantiation of your FastAPI app, route definitions, and any other necessary configurations.

    models/: This directory is used to store Pydantic models for request and response bodies. Pydantic models define the structure of data that your API expects to receive or return..

    routers/: The routers directory is used to organize your API endpoints into separate 
    modules.

    utils/: This directory is used to store utility modules that contain reusable functions or helpers used across your FastAPI application. 

tests/:

    test_main.py:  contains your test cases for the main FastAPI application. You'll typically write tests to ensure that your API endpoints behave as expected, handle edge cases correctly, and maintain compatibility as you make changes to your codebase.


    ## for testing intsall, pytest and requests 

    1: pip3 install pytest requests
    2: Navaigate to the test folder and run 

  pytest

