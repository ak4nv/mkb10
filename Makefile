name = mkb10

all: build

uv:
	@if ! command -v uv > /dev/null 2>&1; then \
		echo "Install uv python package manager using this script"; \
		echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"; \
		echo ""; \
		echo "See docs: https://docs.astral.sh/uv/getting-started/installation/"; \
		false; \
	fi

db.sqlite:
	@sh init_db.sh

build: uv
	@uv sync

shell: uv
	@uv run flask shell

run: db.sqlite uv
	@FLASK_DEBUG=1 uv run flask run

inspect.db:
	@uv run sqlite_web db.sqlite

image-build:
	@podman build --dns=1.1.1.1 -t $(name):dev .

image-run: image-build
	@podman run --rm \
	-p 5000:5000 \
	--name $(name) \
	$(name):dev

.PHONY: uv
