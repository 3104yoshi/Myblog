class TestApp:
    def test_fail_to_post_with_POST_method(self, client):
        response = client.post('/post', data=dict(
            title='test_title',
            content='test_content'
        ))
        assert response.status_code == 302
        assert response.location == '/canPost/False/'
        
    def test_succeed_to_post_with_POST_method(self, client, mock_add_article):
        mock_add_article.side_effect = None
        response = client.post('/post', data=dict(
            title='test_title',
            content='test_content'
        ))
        assert response.status_code == 302
        assert response.location == '/canPost/True/'

    def test_post_with_other_method(self, client, mock_add_article):
        response = client.delete('/post', data=dict(
            title='test_title',
            content='test_content'
        ))
        assert response.status_code == 405

    def test_post_with_GET_method(self, client):
        response = client.get('/post')
        assert response.status_code == 200

    def test_root(self, client):
        response = client.get('/')
        assert response.status_code == 200