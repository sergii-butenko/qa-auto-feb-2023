from src.config.config import config


def test_user_age_is_43(user):
    assert user.age == 42


def test_user_age_is_50(user):
    assert user.age == 42


def test_http_request():
    print(config.get("BASE_URL_API"))


def test_ui_POM():
    print(config.get("BASE_URL_UI"))
