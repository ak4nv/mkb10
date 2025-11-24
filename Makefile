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
	@uv run python

run: db.sqlite uv
	@uv run flask run --debug

.PHONY: uv
