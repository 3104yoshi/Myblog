import pytest
from flask import Flask
from app import app, unauthorized_handler

@pytest.fixture()
def mock_get_user(mocker):
    return mocker.patch(
        'db.accessor.userCredentialAccessor.userCredentialAccessor.getUser'
    )

@pytest.fixture()
def mock_check_user_is(mocker):
    return mocker.patch(
        'db.accessor.userCredentialAccessor.userCredentialAccessor.checkUserIs'
    )

@pytest.fixture()
def mock_add_user(mocker):
    return mocker.patch(
        'db.accessor.userCredentialAccessor.userCredentialAccessor.addUser'
    )

class TestAuthentification:
    def test_login_access(self, client):
        response = client.get("auth/login")
        assert response.status_code == 200
    
    def test_login_failure(self, client, mock_get_user):
        mock_get_user.return_value = False
        response = client.post(
            "auth/login",
            data=dict(
                username='test_username',
                password='test_password'
            ))
        assert response.status_code == 302
        assert response.location == '/auth/canLogin/False/'
    
    def test_login_success(self, client, mock_get_user):
        mock_get_user.return_value = True
        response = client.post(
            "auth/login",
            data=dict(
                username='test_username',
                password='test_password'
            ))
        assert response.status_code == 302
        assert response.location == '/auth/canLogin/True/'
    
    def test_signup_access(self, client):
        response = client.get("auth/signup")
        assert response.status_code == 200
    
    def test_signup_failure(self, client, mock_check_user_is):
        mock_check_user_is.return_value = True
        response = client.post(
            "auth/signup",
            data=dict(
                username='test_username',
                password='test_password'
            ))
        assert response.status_code == 302
        assert response.location == '/auth/canSignup/False/'
    
    def test_signup_success(self, client, mock_check_user_is, mock_add_user):
        mock_check_user_is.return_value = False
        mock_add_user.return_value = None
        response = client.post(
            "auth/signup",
            data=dict(
                username='test_username',
                password='test_password'
            ))
        assert response.status_code == 302
        assert response.location == '/auth/canSignup/True/'
    
    def test_can_signup(self, client):
        response = client.get("auth/canSignup/True/")
        assert response.status_code == 200
    
    def test_can_login(self, client):
        response = client.get("auth/canLogin/True/")
        assert response.status_code == 200
