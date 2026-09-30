import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent


def load_json(filename: str):

    path = ROOT_DIR / "data" / filename

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_json(
    filename: str,
    data
):

    path = ROOT_DIR / "data" / filename

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def ensure_directory(path: Path):

    path.mkdir(
        parents=True,
        exist_ok=True
    )