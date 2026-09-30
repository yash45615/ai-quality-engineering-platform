import requests

from security.security_config import (
    ZAP_HOST,
    ZAP_PORT,
    ZAP_TARGET
)


def check_zap_connection():

    response = requests.get(
        f"http://{ZAP_HOST}:{ZAP_PORT}/JSON/core/view/version/",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def start_spider():

    response = requests.get(
        f"http://{ZAP_HOST}:{ZAP_PORT}/JSON/spider/action/scan/",
        params={
            "url": ZAP_TARGET
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    print(
        check_zap_connection()
    )

    print(
        start_spider()
    )