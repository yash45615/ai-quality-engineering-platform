import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    BASE_URL = os.getenv(
        "BASE_URL",
        "https://www.saucedemo.com"
    )

    API_BASE_URL = os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "test"
    )

    HEADLESS = os.getenv(
        "HEADLESS",
        "true"
    ).lower() == "true"

    BROWSER = os.getenv(
        "BROWSER",
        "chromium"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )

    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5.5"
    )

    APPIUM_SERVER = os.getenv(
        "APPIUM_SERVER",
        "http://127.0.0.1:4723"
    )

    MOBILE_PLATFORM = os.getenv(
        "MOBILE_PLATFORM",
        "Android"
    )

    MOBILE_DEVICE = os.getenv(
        "MOBILE_DEVICE",
        "emulator"
    )

    MOBILE_APP = os.getenv(
        "MOBILE_APP",
        ""
    )

    PERFORMANCE_USERS = int(
        os.getenv(
            "PERFORMANCE_USERS",
            "10"
        )
    )

    PERFORMANCE_SPAWN_RATE = float(
        os.getenv(
            "PERFORMANCE_SPAWN_RATE",
            "2"
        )
    )

    PERFORMANCE_HOST = os.getenv(
        "PERFORMANCE_HOST",
        "https://www.saucedemo.com"
    )

    PERFORMANCE_P95_LIMIT = int(
        os.getenv(
            "PERFORMANCE_P95_LIMIT",
            "3000"
        )
    )

    PERFORMANCE_ERROR_RATE_LIMIT = float(
        os.getenv(
            "PERFORMANCE_ERROR_RATE_LIMIT",
            "5"
        )
    )


settings = Settings()