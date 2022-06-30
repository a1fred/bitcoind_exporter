.PHONY: dev nodev
dev:
	docker-compose up -d --build --remove-orphans --wait
nodev:
	docker-compose rm -fs
	docker image prune -f

.PHONY: qa
qa:
	poetry run flake8 .
	poetry run mypy --warn-unused-ignores .

.PHONY: test
test: qa
	poetry run pytest \
		-vx --log-level=0 \
		--cov=bitcoind_exporter \
		--asyncio-mode=strict \
		tests/

.PHONY: webapp
webapp:
	poetry run python -m bitcoind_exporter
