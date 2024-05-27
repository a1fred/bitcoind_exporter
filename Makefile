.PHONY: dev nodev
dev:
	docker compose up -d --build --remove-orphans --wait
nodev:
	docker compose rm -fs
	docker image prune -f

.PHONY: qa
qa:
	poetry run flake8 .
	poetry run mypy --warn-unused-ignores -p "bitcoind_exporter.webapp"

.PHONY: test
test: qa
	PORT=58064 poetry run pytest \
		-vx --log-level=0 \
		--cov=bitcoind_exporter \
		--asyncio-mode=strict \
		tests/

.PHONY: webapp
webapp:
	poetry run python -m bitcoind_exporter

.PHONY: docs
docs: dev
	curl -q 127.0.0.1:8065/metrics > docs/metrics.sample
