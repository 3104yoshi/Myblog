import pytest

@pytest.fixture()
def mock_get_all_articles(mocker):
    return mocker.patch(
        'db.accessor.articlesAccessor.articlesAccessor.getAllArticles',
        return_value=[(1, 'test_title', 'test_content', '2020-01-01 00:00:00')]
    )

class TestApi:
    def test_get(self, client, mock_get_all_articles):
        response = client.get("api/articles")
        print(response.json)
        assert response.json[0] == {"title": "test_title", "content": "test_content"}