import pytest
from rest_framework.test import APIClient

client=APIClient()

@pytest.mark.django_db
def test_register_user():
    payload =dict(
        
    username= "Vasanth",
    password= "Vasanth@2001",
    password2= "Vasanth@2001",
    email= "vasanth@gmail.com",
    first_name= "Vasanth",
    last_name= "Rajendran"

    )
    response=client.post('/api/userlogin/register',payload)
    data=response.data
    assert data['status'] == 201
    assert data['message'] == 'User added successfully'

@pytest.mark.django_db
def test_token():
    payload1=dict(
    username="Logesh",
    password="Logesh@2001"
        
    )
    response=client.post('/api/token',payload1)
    # data=response.data
    # assert data['status'] == 200
    