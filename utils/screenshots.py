from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

SCREENSHOT_DIR = (
    ROOT_DIR
    / "reports"
    / "screenshots"
)


def take_screenshot(
    page,
    test_name: str
):

    SCREENSHOT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    safe_name = (
        test_name
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
    )

    path = (
        SCREENSHOT_DIR
        / f"{safe_name}_{timestamp}.png"
    )

    page.screenshot(
        path=str(path),
        full_page=True
    )

    return path