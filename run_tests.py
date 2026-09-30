import subprocess
import sys


def run_tests(
    test_path,
    extra_args=None
):

    command = [
        sys.executable,
        "-m",
        "pytest",
        test_path
    ]

    if extra_args:
        command.extend(
            extra_args
        )

    print(
        "\nRunning:",
        " ".join(command)
    )

    result = subprocess.run(
        command
    )

    return result.returncode


def main():

    test_groups = [

        "tests",

        "api_tests",

        "ui_tests/tests",

        "accessibility"
    ]

    for test_group in test_groups:

        result = run_tests(
            test_group
        )

        if result != 0:

            print(
                f"\nFAILED: {test_group}"
            )

            sys.exit(
                result
            )

    print(
        "\n=============================="
    )

    print(
        "ALL QUALITY TESTS PASSED"
    )

    print(
        "=============================="
    )


if __name__ == "__main__":
    main()