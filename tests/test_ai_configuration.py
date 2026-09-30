from config.settings import settings


def test_ai_configuration():

    assert settings.OPENAI_MODEL

    assert isinstance(
        settings.OPENAI_MODEL,
        str
    )