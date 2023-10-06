import pytest
from app import app

@pytest.fixture()
def client():
    app.config['LOGIN_DISABLED'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture()
def mock_add_article(mocker):
    return mocker.patch('db.accessor.articlesAccessor.articlesAccessor.addArticle')
