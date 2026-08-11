
# test_create_user.py

import sys
import os

from app import app
from database_connection import DatabaseConnection

def test_create_user_is_saved_to_database():

    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()

    # use execute to send a TRUNCATE TABLE query

    connection.execute("TRUNCATE TABLE users;")

    # remaining code unchanged...


    # send the request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'