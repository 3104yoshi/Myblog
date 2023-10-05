import pytest
from app import app

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    app.config['LOGIN_DISABLED'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_add_article(mocker):
    return mocker.patch('db.accessor.articlesAccessor.articlesAccessor.addArticle')


def test_fail_to_post_with_POST_method(client):
    response = client.post('/post', data=dict(
        title='test_title',
        content='test_content'
    ))
    assert response.status_code == 302
    assert response.location == '/canPost/False/'
    
def test_succeed_to_post_with_POST_method(client, mock_add_article):
    mock_add_article.side_effect = None
    response = client.post('/post', data=dict(
        title='test_title',
        content='test_content'
    ))
    assert response.status_code == 302
    assert response.location == '/canPost/True/'

def test_post_with_other_method(client, mock_add_article):
    response = client.delete('/post', data=dict(
        title='test_title',
        content='test_content'
    ))
    assert response.status_code == 405

def test_post_with_GET_method(client):
    response = client.get('/post', data=dict(
        title='test_title',
        content='test_content'
    ))
    assert response.status_code == 200

def test_root(client):
    response = client.get('/')
    assert response.status_code == 200