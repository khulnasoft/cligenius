from pathlib import Path

import cligenius

APP_NAME = "my-super-cli-app"


def main():
    app_dir = cligenius.get_app_dir(APP_NAME)
    config_path: Path = Path(app_dir) / "config.json"
    if not config_path.is_file():
        print("Config file doesn't exist yet")


if __name__ == "__main__":
    cligenius.run(main)
