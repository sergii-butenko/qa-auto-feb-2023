from src.config.providers.config_from_env_provider import ConfigFromEnvProvider


def test_config_env_provider_negative():
    conf = ConfigFromEnvProvider()
    val = conf.get("KJHKJFHSDKJFH")
    assert val is None


def test_config_env_provider_positive():
    conf = ConfigFromEnvProvider()
    val = conf.get("PATH")
    assert val == "/home/sbutenko/.poetry/bin:/home/sbutenko/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
