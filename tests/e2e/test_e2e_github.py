def test_e2e(github_api_client, github_ui_app):
    repo = github_api_client.search_repo('become')
    
    assert github_ui_app.check_repo_exists(repo)