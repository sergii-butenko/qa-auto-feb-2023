
def test_sing_in_pom(GitHub_UI_App):
    login_page = GitHub_UI_App.LoginPage

    login_page.go_to()
    login_page.try_sign_in('username', 'password')

    assert login_page.check_error_message()
