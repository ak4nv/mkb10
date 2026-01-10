import os

from app.core import create_app

config = os.getenv("CONFIG_FILE") or "app/config.py"
app = create_app(config)


if __name__ == "__main__":
    app.run()
