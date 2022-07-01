# Bitcoind exporter
Tested with `bitcoind v0.21`

 * [metrics response example](docs/metrics.sample)
 * [docker-compose.yml](docker-compose.yml)
 * [grafana panel](staff/grafana/dashboards/bitcoind.json)

# Environment variables
 * `HOST` listen host, default:`localhost`
 * `PORT` listen port, default:`8064`
 * `BITCOIND` bitcoind url, default:`http://bitcoind:bitcoind@localhost:8335`
 * `COLLECTORS` enabled collectors, all by default

# Docker container
Docker container available at `ghcr.io/a1fred/bitcoind_exporter`.

`amd64` and `arm64` arch supported.
