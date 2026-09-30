from security.security_config import (
    ZAP_HOST,
    ZAP_PORT,
    ZAP_TARGET
)


def test_zap_configuration():

    assert ZAP_HOST
    assert ZAP_PORT == 8080
    assert ZAP_TARGET.startswith(
        "http"
    )