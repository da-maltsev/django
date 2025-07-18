from pathlib import Path


# Repository root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

SRC_DIR = BASE_DIR / "src"

ROOT_URLCONF = "app.urls"

# Disable built-in ./manage.py test command in favor of pytest
TEST_RUNNER = "app.test.disable_test_command_runner.DisableTestCommandRunner"

WSGI_APPLICATION = "app.wsgi.application"
